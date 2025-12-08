<h1 align="center">🐍 SmartSerpent: Hybrid AI for Life-Saving Snake Identification</h1>
<h3 align="center">Real-Time Recognition, Venom Analysis, and Emergency Guidance</h3>
<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:0aefff,100:005bff&height=250&section=header&text=SmartSerpent&fontSize=60&fontColor=ffffff&fontAlignY=35"/>
</p>

---

## 💡 Overview & Problem Statement

SmartSerpent is a **robust, hybrid deep-learning system** engineered for fast, highly accurate identification of Indian snake species, coupled with **instant, actionable emergency information**.

This system addresses critical reliability challenges in field deployments (low resolution, poor lighting) by integrating multiple AI techniques:

* **Deep Learning Classifier:** Uses MobileNetV2 for foundational object recognition.
* **Embedding Verification:** Implements Cosine Similarity to verify predictions and prevent misclassification.
* **Texture Enhancement:** Applies Bicubic Upscaling to preserve fine-scale patterns in low-quality images.
* **Weighted Fusion Scoring:** Combines model confidence and similarity scores for superior prediction stability.
* **AI-Powered Guidance:** Leverages Gemini intelligence for context-aware venom analysis and first-aid recommendations.

---

## 🚀 Core Technical Highlights

### 1. Hybrid Prediction Engine (The Fusion)
To ensure reliability against visually similar species and poor image quality, the system fuses two independent scores:

- `model_confidence` → Softmax output from MobileNetV2
- `similarity_score` → Cosine similarity of feature embeddings

The final prediction uses a weighted fusion formula:

final_score= 0.5 model_confidence+ 0.5 similarity_score

**Impact:** This hybrid approach significantly reduces misclassifications under poor lighting, low resolution, and partial occlusion, providing a **+5.2% accuracy boost** over the base model.

### 2. Bicubic Upscaling for Robust Feature Extraction
Field images often suffer from blurriness. SmartSerpent preprocesses images using **bicubic interpolation** to enhance and preserve critical visual features before they are passed to the model, specifically:
* Scale texture and patterns
* Color gradients and subtle markings

### 3. Real-Time Emergency Guidance
SmartSerpent transforms from a classifier into a **life-saving emergency assistant**. Upon identification, it retrieves and presents critical data instantly:
* **Venom Type:** (Neurotoxic / Hemotoxic / Cytotoxic / Mixed)
* **Danger Severity:** A clear risk rating.
* **Immediate First-Aid Steps:** Actionable, localized recommendations.
* **Scientific and Habitat Information.**

---

## 📊 Model Performance & Ablation Study

### Final Test Metrics
* **Accuracy:** **79.3%**
* **Weighted F1 Score:** 0.79

### Ablation Study: Impact of Hybrid Components
| Model Version | Key Feature Added | Accuracy |
| :--- | :--- | :--- |
| **MobileNetV2 Only** | Baseline | 79.3% |
| **+ Bicubic Upscaling** | Image pre-processing | 82.2% |
| **+ Similarity Fusion** | **Final Hybrid Model** | **85.6%** |

---

## 🛠️ System Workflow

The user-facing workflow follows a clear, six-step pipeline:

1.  User uploads snake image via web UI.
2.  Image undergoes bicubic upscaling for texture enhancement.
3.  MobileNetV2 extracts image features and predicts an initial class probability.
4.  Embedding similarity is computed against known training data.
5.  Hybrid score is calculated to determine the robust final prediction.
6.  Venom profile and emergency first-aid guidance are retrieved and displayed.

---

## 📜 Supported Species (12 Total)

| Venomous Species | Non-Venomous Species |
| :--- | :--- |
| King Cobra | Checkered Keelback |
| Russell’s Viper | Green Tree Vine |
| Spectacled Cobra | Indian Rock Python |
| Common Krait | Banded Racer |
| Saw-Scaled Viper | Common Sandboa |
| | Common Trinket |
| | Rat Snake |

---

## 💻 Tech Stack

### Languages & Frameworks
<p>
  <img src="https://skillicons.dev/icons?i=python,flask,tensorflow,sklearn,html,css,js,mongodb" height="50" />
</p>

| Component | Technology | Description |
| :--- | :--- | :--- |
| **Deep Learning** | MobileNetV2, TensorFlow, Keras | Core image classification and feature extraction. |
| **ML Engineering** | Cosine Similarity, scikit-learn | Implemented for embedding verification and robustness. |
| **Backend API** | Python, Flask | RESTful API to handle image uploads and model predictions. |
| **Database** | MongoDB | Stores rich, structured data for venom and first-aid guidance. |

---

## 👤 Author

<p align="center">
  <a href="https://github.com/Hemanthlokesh1705">
    <img src="https://img.shields.io/badge/GitHub-Hemanthlokesh1705-181717?style=for-the-badge&logo=github&logoColor=white" />
  </a>
</p>

**Hemanth L** — AI/ML Engineer
*Focused on developing robust, production-ready AI systems with real-world impact.*
