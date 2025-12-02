<!-- HEADER -->
<h1 align="center">SmartSerpent — Hybrid AI Snake Identification System</h1>
<h3 align="center">Real-Time Snake Recognition • Venom Analysis • Emergency First-Aid Guidance</h3>

---

## Overview

SmartSerpent is a **hybrid deep-learning system** designed to identify Indian snake species and provide **instant venom information and first-aid recommendations** in real time.

It improves reliability and practical usefulness by combining:

- MobileNetV2 deep-learning classifier  
- Cosine similarity-based embedding verification  
- Bicubic upscaling for texture enhancement  
- Weighted fusion scoring  
- Gemini-powered venom & first-aid intelligence  

This results in a **robust, accurate, and deployable system** suitable for rural healthcare and emergency scenarios.

---

## Core Highlights

### Hybrid Prediction Engine  
The system calculates:

- `model_confidence` → softmax output from MobileNetV2  
- `similarity_score` → cosine similarity of embeddings  

Then fuses them for improved reliability:


final_score = 0.5 × model_confidence + 0.5 × similarity_score

This significantly reduces misclassifications under:
- poor lighting  
- low resolution  
- partial occlusion  
- visually similar species  

---

### Bicubic Upscaling for Clarity
Field images are often blurry or low quality.  
SmartSerpent applies **bicubic interpolation** before resizing to preserve:

- scale texture  
- color gradients  
- pattern details  

This boosts accuracy for species with fine-scale patterns.

---

### Real-Time Venom & First-Aid Guidance
Once identified, SmartSerpent retrieves:

- Venom type (neurotoxic / hemotoxic / cytotoxic / mixed)
- Danger severity
- Immediate first-aid steps
- Habitat & distribution
- Scientific information

This makes the system not just a classifier —  
but a **life-saving emergency assistant**, especially in rural regions.

---

## Supported Species

- Checkered Keelback  
- Green Tree Vine  
- Indian Rock Python  
- King Cobra  
- Russell’s Viper  
- Spectacled Cobra  
- Banded Racer  
- Common Krait  
- Common Sandboa  
- Common Trinket  
- Rat Snake  
- Saw-Scaled Viper  

---

## Model Performance

### Test Metrics
- **Accuracy:** ~79.3%  
- **Weighted F1 Score:** ~0.79  

### Ablation Study
| Model Version | Accuracy |
|--------------|----------|
| MobileNetV2 Only | 74.1% |
| + Bicubic Upscaling | 77.3% |
| + Similarity Fusion | **79.3%** |

Hybrid fusion provides the best stability for real-world images.

---

## How It Works

1. User uploads image  
2. Image undergoes bicubic upscaling  
3. MobileNetV2 extracts features and predicts class  
4. Embedding similarity is computed  
5. Hybrid score decides final prediction  
6. Venom and first-aid guidance is returned  

---

## Installation

### Install Dependencies
pip install -r requirements.txt

### Run Backend
python app.py

### Open UI
http://localhost:5000
---

## Tech Stack

### Core ML
- TensorFlow / Keras  
- MobileNetV2  
- Cosine Similarity Embeddings  

### Backend
- Python Flask  
- NumPy / scikit-learn  

### Frontend
- HTML / CSS / JavaScript  

### Intelligence Layer
- Gemini API for venom & first-aid context  

---

## Usage

1. Launch the app  
2. Upload a snake image  
3. Get:
   - predicted species  
   - confidence score  
   - similarity score  
   - venom information  
   - emergency response steps  

---

## Author

**Hemanth Lokesh**  
AI/ML Engineer | CSE-AI  
GitHub: [Hemanthlokesh1705](https://github.com/Hemanthlokesh1705)

---

<p align="center">
  <b>Building intelligent systems that save lives — one model at a time.</b>
</p>
