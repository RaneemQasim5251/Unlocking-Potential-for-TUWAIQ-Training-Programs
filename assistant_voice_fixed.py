import pandas as pd
import whisper
import speech_recognition as sr
import pyttsx3
from sklearn.ensemble import RandomForestClassifier
import soundfile as sf
import tempfile
import os
import difflib

# إعداد محرك الصوت
engine = pyttsx3.init(driverName='sapi5')
engine.setProperty('rate', 145)
engine.setProperty('volume', 1.0)

def speak(text):
    try:
        if engine._inLoop:
            engine.endLoop()
        engine.say(text)
        engine.runAndWait()
    except RuntimeError:
        pass

# تحميل البيانات
df = pd.read_csv("train.csv")
df_cleaned = df.dropna(subset=['Y', 'University Degree Score'])
df_cleaned.loc[:, 'Gender'] = df_cleaned['Gender'].map({'ذكر': 1, 'أنثى': 0})
df_cleaned = pd.get_dummies(df_cleaned, columns=['Home Region', 'Program Presentation Method', 'Completed Degree', 'Level of Education'], drop_first=True)

# تجهيز البيانات
X = df_cleaned[['Age', 'Gender', 'University Degree Score']]
y = df_cleaned['Y']

model = RandomForestClassifier()
model.fit(X, y)

# الطالب الأفضل
best_student = df_cleaned.loc[df_cleaned['Y'].idxmax()]
prob = model.predict_proba([[best_student['Age'], best_student['Gender'], best_student['University Degree Score']]])[0][1] * 100
best_info = f"The most disciplined student is {int(best_student['Age'])} years old, with a university score of {best_student['University Degree Score']}, and a predicted completion probability of {prob:.2f}%."

# تحميل نموذج Whisper
model_whisper = whisper.load_model("small")

def get_voice_input_whisper(prompt=None):
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    if prompt:
        speak(prompt)
    print("🎙️ Listening...")
    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        fd, path = tempfile.mkstemp(suffix=".wav")
        with os.fdopen(fd, 'wb') as f:
            f.write(audio.get_wav_data())
        result = model_whisper.transcribe(path, language="en")
        os.remove(path)
        text = result["text"].strip()
        print("🗣️ You said:", text)
        return text
    except Exception as e:
        print("⚠️ Error:", e)
        return ""

def respond(text):
    lower = text.lower()
    if "best student" in lower or "top student" in lower or "most disciplined" in lower:
        response = best_info
    elif "your name" in lower or "who are you" in lower:
        response = "I'm your loyal academic assistant from Tuwaiq Academy!"
    elif any(word in lower for word in ["thank", "thanks"]):
        response = "You're always welcome! Happy to help."
    elif any(word in lower for word in ["bye", "goodbye", "exit"]):
        response = "Goodbye! See you soon!"
        speak(response)
        exit()
    else:
        response = "Sorry, I didn't get that. Could you try rephrasing?"
    print("🤖:", response)
    speak(response)

# بدء المحادثة مباشرة
speak("Hello! I'm your assistant from Tuwaiq Academy. You can ask me anything about the best student, or say exit to quit.")

while True:
    query = get_voice_input_whisper("What would you like to know?")
    if query:
        respond(query)
