from flask import Flask, render_template, request, jsonify
import json
import os
from backend.snake_engine.snake_prediction import Snake_identification
from backend.snake_engine.gemini_model import SnakeInfoService
from backend.snake_engine.similarity_prediction import ImageSimilarity
from PIL import Image
import tempfile

app = Flask(__name__)
snake_info_service = SnakeInfoService()

# Initialize similarity model
similarity_model = ImageSimilarity(
    r'C:\Users\LATITUDE\Desktop\python\snake_model\backend\models\image_embeddings.pkl'
)

# Load class-to-snake mapping
with open(r'C:\Users\LATITUDE\Desktop\python\snake_model\backend\snake_engine\mapping.json') as f:
    class_to_snake = json.load(f)
class_to_snake = {int(k): v for k, v in class_to_snake.items()}

# Basic first-aid info for venomous snakes
VENOMOUS_SNAKES = {"Cobra", "Russell’s viper", "Saw-scaled viper", "Krait"}
FIRST_AID_STEPS = [
    "Keep the person calm and still to slow the spread of venom.",
    "Remove tight clothing or jewelry near the bite area.",
    "Keep the bitten limb below heart level.",
    "Do NOT cut, suck, or apply ice to the wound.",
    "Get emergency medical help immediately."
]

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/prediction', methods=['GET', 'POST'])
def prediction_page():
    if request.method == 'POST':
        if 'image' not in request.files:
            return render_template('prediction.html', error="No image uploaded")

        image_file = request.files['image']
        model_path = r'C:\Users\LATITUDE\Desktop\python\snake_model\backend\models\model_v3.keras'

        # Step 1: Model Prediction
        snake_identifier = Snake_identification(image_file, model_path)
        result = snake_identifier.prediction()
        class_no = result['Predicted class']
        model_conf = result['Model_confidence']
        predicted_snake = class_to_snake[class_no]

        # Step 2: Save temp image for similarity check
        image_file.stream.seek(0)
        with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp:
            temp_path = tmp.name
            img = Image.open(image_file.stream).convert("RGB")
            img.save(temp_path)

        try:
            # Step 3: Similarity prediction (top 1)
            sim_results = similarity_model.find_similar(temp_path)
            similar_snake_name = sim_results[0][0]
            similarity_score = sim_results[0][1]
        finally:
            if os.path.exists(temp_path):
                os.remove(temp_path)

        # Step 4: Weighted fusion (0.5 model + 0.5 similarity)
        final_score = 0.5 * model_conf + 0.5 * similarity_score

        # Step 5: Decision logic
        if model_conf < 0.6 and similarity_score < 0.8:
            message =message = {
        'caution': "❗The snake species might not be in the database. Please upload another clear image.",
        'first_aid': [
            "Keep the person calm and still to slow the spread of venom.",
            "Remove tight clothing or jewelry near the bite area.",
            "Keep the bitten limb below heart level.",
            "Do NOT cut, suck, or apply ice to the wound.",
            "Get emergency medical help immediately."
        ]
    }
            return render_template('prediction.html', confidence=round(final_score * 100, 2),
                similarity=round(similarity_score * 100, 2),
                model_conf=round(model_conf * 100, 2), unknown_snake=True, message=message, image_uploaded=True)
        else:
            snake_name = predicted_snake if model_conf >= similarity_score else similar_snake_name
            venomous = snake_name in VENOMOUS_SNAKES
            first_aid = FIRST_AID_STEPS if venomous else None

            return render_template(
                'prediction.html',
                snake_name=snake_name,
                confidence=round(final_score * 100, 2),
                similarity=round(similarity_score * 100, 2),
                model_conf=round(model_conf * 100, 2),
                first_aid=first_aid,
                image_uploaded=True
            )

    return render_template('prediction.html', image_uploaded=False)

@app.route('/get_details', methods=['POST'])
def get_details():
    data = request.get_json(force=True)
    if not data or 'snake_name' not in data:
        return jsonify({"error": "Missing 'snake_name' in request JSON"}), 400
    snake = data['snake_name']
    snake_info = snake_info_service.get_snake_info(snake)
    return jsonify({'snake_details': snake_info}), 200

if __name__ == '__main__':
    app.run(debug=True)
