import os
from dotenv import load_dotenv
from PIL import Image
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input

class Snake_identification:
    def __init__(self, img, model_path):
        self.image = img
        self.model = load_model(model_path)

    def upscale_image(self, scale_factor=2):
        """
        Automatically upscales the input image using Bicubic interpolation.
        scale_factor: how much to enlarge the image (default = 2x)
        """
        img = Image.open(self.image).convert('RGB')
        width, height = img.size
        new_size = (int(width * scale_factor), int(height * scale_factor))
        upscaled_img = img.resize(new_size, Image.BICUBIC)
        return upscaled_img

    def image_preprocess(self):
        """
        Upscales the image (bicubic), resizes to model input size (356x356),
        converts to array, and preprocesses for MobileNetV2.
        """
        # Step 1: Upscale image
        upscaled_img = self.upscale_image(scale_factor=2)

        # Step 2: Resize to model input dimension
        self.preprocess_img = upscaled_img.resize((356, 356))

        # Step 3: Convert to numpy array
        self.img_array = np.array(self.preprocess_img, dtype=np.float32)

        # Step 4: Expand dimension and preprocess
        self.img_array = np.expand_dims(self.img_array, axis=0)
        self.img_array = preprocess_input(self.img_array)

        return self.img_array

    def prediction(self):
        """
        Runs the model prediction on the preprocessed image and returns
        predicted class and confidence score.
        """
        snake_img_arr = self.image_preprocess()
        identify_snake = self.model.predict(snake_img_arr)
        predicted_class = np.argmax(identify_snake, axis=1)[0]
        confidence = float(np.max(identify_snake))
        return {
            'Predicted class': predicted_class,
            'Model_confidence': round(confidence, 5)
        }


# Example usage
# def main():
#     load_dotenv()
#     image_path = r"C:\Users\LATITUDE\Downloads\russelviper.jpg"
#     model_path = r"C:\Users\LATITUDE\Desktop\python\snake_model\backend\models\model_v3.keras"
#
#     snake_identifier = Snake_identification(image_path, model_path)
#     result = snake_identifier.prediction()
#     print("Prediction Result:", result)
#
# if __name__ == "__main__":
#     main()
