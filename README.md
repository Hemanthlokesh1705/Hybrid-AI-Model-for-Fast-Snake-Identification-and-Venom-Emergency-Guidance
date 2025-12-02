<!-- HEADER -->
<h1 align="center">SmartSerpent — Hybrid AI Snake Identification System</h1>
<h3 align="center">Real-Time Snake Recognition • Venom Analysis • Emergency First-Aid Guidance</h3>
<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:0aefff,100:005bff&height=250&section=header&text=SmartSerpent&fontSize=60&fontColor=ffffff&fontAlignY=35"/>
</p>

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


---

## Tech Stack

### Languages  
<p>
  <img src="https://skillicons.dev/icons?i=python" height="50" />
</p>

### Deep Learning & ML  
<p>
  <img src="https://skillicons.dev/icons?i=tensorflow" height="50" />
  <img src="https://skillicons.dev/icons?i=sklearn" height="50" />
</p>
<p>MobileNetV2 • CNNs • Cosine Similarity Embeddings • Data Augmentation</p>

### Backend & Deployment  
<p>
  <img src="https://skillicons.dev/icons?i=flask" height="50" />
</p>

### Frontend  
<p>
  <img src="https://skillicons.dev/icons?i=html,css,js" height="50" />
</p>

### Database / Storage  
<p>
  <img src="https://skillicons.dev/icons?i=mongodb" height="50" />
</p>

---

## Author

<p align="center">
  <a href="https://github.com/Hemanthlokesh1705">
    <img src="https://img.shields.io/badge/GitHub-Hemanthlokesh1705-181717?style=for-the-badge&logo=github&logoColor=white" />
  </a>
</p>

<p align="center">
  <strong>Built by Hemanth L — AI/ML Engineer</strong><br>
  Focused on developing reliable, production-ready AI systems.
</p>

---

<p align="center">
  <b>SmartSerpent — Turning Computer Vision into Life-Saving Intelligence</b>
</p>
