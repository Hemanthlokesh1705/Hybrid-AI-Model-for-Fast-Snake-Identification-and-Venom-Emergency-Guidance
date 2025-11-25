import os
import numpy as np
import pickle
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input, MobileNetV2
from tensorflow.keras.models import Model
from tensorflow.keras.layers import GlobalAveragePooling2D
from sklearn.metrics.pairwise import cosine_similarity


class ImageSimilarity:
    def __init__(self, embedding_path):
        # Load the saved embeddings and image paths
        with open(embedding_path, 'rb') as f:
            data = pickle.load(f)
        self.image_paths = np.array(data['image_paths'])
        self.embeddings = np.array(data['embeddings'])

        # Load same model used for embedding extraction
        base_model = MobileNetV2(input_shape=(356, 356, 3), include_top=False, weights='imagenet')
        x = GlobalAveragePooling2D()(base_model.output)
        self.embedding_model = Model(inputs=base_model.input, outputs=x)

        print("✅ Model and embeddings loaded successfully!")

    def get_embedding(self, img_path):
        """Generate embedding for a given image"""
        img = image.load_img(img_path, target_size=(356, 356))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = preprocess_input(img_array)
        embedding = self.embedding_model.predict(img_array, verbose=0)
        return embedding.flatten()

    def find_similar(self, img_path, top_k=5):
        """Find top_k most similar images and return (species, similarity)"""
        query_emb = self.get_embedding(img_path)
        sims = cosine_similarity([query_emb], self.embeddings)[0]
        top_indices = np.argsort(sims)[-top_k:][::-1]

        results = []
        for i in top_indices:
            # Extract the folder name as species name
            species_name = os.path.basename(os.path.dirname(self.image_paths[i]))
            similarity_score = float(sims[i])
            results.append((species_name, similarity_score))

        return results

# if __name__ == "__main__":
#     similarity = ImageSimilarity(
#         r"C:\Users\LATITUDE\Desktop\python\snake_model\backend\models\image_embeddings.pkl"
#     )

#     results = similarity.find_similar(
#         r"C:\Users\LATITUDE\Downloads\12_-_The_Mystical_King_Cobra_and_Coffee_Forests.jpg"
#     )

#     print(f'snake_name:{results[0][0]},score:{round(results[0][1],3)}')