# Unlocking Potential for Elite Training Programs - Tuwaiq Voice Assistant

## 🔄 Overview

This repository is a complete solution for the Kaggle competition ["Measuring Student Persistence and Completion Rate"](https://www.kaggle.com/competitions/measuring-student-persistence-and-completion-rate), developed as part of the Tuwaiq Academy bootcamp.

We took the original machine learning problem of predicting student persistence and elevated it by wrapping it in a real-time, interactive voice assistant using Python, Whisper, and hardware integration. This transformed a classic ML task into an AI-powered experience.

---
https://github.com/user-attachments/assets/2f07dbc0-aa26-4c9c-905b-62a09075f662

## 📚 Contents

* `Tuwaiq_Academy_Best_Students_predict.ipynb` → Jupyter Notebook with full data analysis, preprocessing, model building, and submission code.
* `train.csv` → Training dataset.
* `tuwaiq_voice_assistant.py` → Python script that integrates the trained model into a real-time voice assistant.
* `README.md` → Project description and implementation documentation (you're reading it).
* `requirements.txt` → All needed libraries.

---

## ✅ Project Objectives

1. **Participate in Kaggle Competition**:

   * Analyze and model persistence data to predict completion rate.

2. **Enhance Model with Voice Assistant**:

   * Transform model into a smart assistant for academic advisors.

3. **Hardware and Voice Interaction**:

   * Implement speech-to-text (STT), text-to-speech (TTS), and microphone handling to create an interactive bot.

---

## 🔹 Competition Breakdown

### 1. Registration

* Team: **Vision Tuwaiq 2030**

### 2. Data Preprocessing

* Categorical encoding using `get_dummies`
* Missing values dropped for `Y` and `University Degree Score`
![target_distribution](https://github.com/user-attachments/assets/eddb1c98-c469-4baa-802b-3a068bf87d8f)
![presentation_method_vs_persistence](https://github.com/user-attachments/assets/20d509e3-3f9a-49c4-9e6f-6e098ea46386)
![gender_vs_persistence](https://github.com/user-attachments/assets/7f5f58fc-aa69-46e7-9b0b-6e696f256862)
![education_vs_persistence](https://github.com/user-attachments/assets/518d076e-0015-4e6c-9792-4a3333d85b06)
![age_distribution](https://github.com/user-attachments/assets/4015ac7e-ae60-4b3d-b6e2-077bd136b99c)
![09_خريطة_الارتباط](https://github.com/user-attachments/assets/079612cb-b208-4311-a614-99fc95def833)
![08_المنطقة_والاستمرارية](https://github.com/user-attachments/assets/591a22ce-bb61-4f3d-b76a-07ca1b8b1c75)
![07_مدة_البرنامج](https://github.com/user-attachments/assets/95144ed8-cbd9-46cf-9b7c-ff0737a9dc7e)
![06_المهارة_والاستمرارية](https://github.com/user-attachments/assets/76523a75-a8af-4d90-a9a7-e7d8a7f95097)
![05_طريقة_التقديم_والاستمرارية](https://github.com/user-attachments/assets/96613bdd-0636-4940-9e85-d72677e10b89)
![04_التعليم_والاستمرارية](https://github.com/user-attachments/assets/4520ce1e-3398-4322-83b5-d6cda2903aad)
![03_الجنس_والاستمرارية](https://github.com/user-attachments/assets/f10aa803-3024-4a34-852f-a7fbc7edb917)
![02_توزيع_الأعمار](https://github.com/user-attachments/assets/4a553cfa-6ac8-4a5f-b3bb-4c91dea10c61)
![01_توزيع_الاستمرارية](https://github.com/user-attachments/assets/462ed66b-424f-45f0-b4ed-3f0a741295e5)



### 3. Model Building

* Used `RandomForestClassifier`
* Features: `Age`, `Gender`, `University Degree Score`
* Target: `Y` (persistence indicator)

### 4. Model Improvement

* Feature engineering (e.g., binary gender, dummy encoding for education/region)
* Fine-tuned with GridSearchCV
* Accuracy > 85%

---

## 🎮 Real-Time Voice Assistant

We built a real-time voice bot that:

* Greets the user
* Understands voice commands using **OpenAI Whisper**
* Answers questions like:

  * Who is the best student?
  * What is your name?
  * Tell me the top performer?
* Speaks the results back using `pyttsx3`

### 🔧 Hardware Implementation
![ChatGPT Image 16 مايو 2025، 02_11_11 ص](https://github.com/user-attachments/assets/6a5f8d67-c9ac-4374-82ec-83f3f069af69)


* **Microphone**: Used for capturing audio via `SpeechRecognition`
* **Speakers**: Used for responding with synthesized voice
* **Laptop (Windows)**: Required for `sapi5` voice driver (for pyttsx3 TTS)

---

## 🎉 Python + AI Integration

* `whisper` for STT: Real-time transcription
* `pyttsx3` for TTS: Speak results clearly
* `speech_recognition` + `Microphone` class
* `RandomForestClassifier` from `sklearn`
* Error handling, re-prompting, and smart confirmation logic

---

## 📅 What We Learned

* Preprocessing large datasets for ML competitions
* Building robust, deployable models
* Integrating AI models into real-time systems
* Voice interface design (asking questions, confirming identity, rephrasing)
* Hardware and Python syncing (audio IO)

---

## 💼 How to Run

```bash
pip install -r requirements.txt
python tuwaiq_voice_assistant.py
```

> Make sure you are using Python 3.10+ and running on Windows (for TTS support).

---

## 🌟 Credits

* Based on Kaggle's "Measuring Student Persistence" competition
* Powered by OpenAI Whisper, scikit-learn, and Python
