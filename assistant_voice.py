import whisper
import pyttsx3
import speech_recognition as sr

# === تحميل الجواب المُجهز مسبقًا ===
with open("discipline_response_ar.txt", encoding="utf-8") as f:
    best_students_reply = f.read()

# === إعداد TTS ===
engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('voice', 'arabic')  # قد تحتاج لضبط الصوت حسب النظام

# === إعداد التعرف على الصوت ===
r = sr.Recognizer()
model = whisper.load_model("small")  # يمكنك استخدام whisper-ar من HuggingFace لو أردت

def recognize_with_whisper():
    with sr.Microphone() as source:
        print("🎙️ اسألني الآن...")
        audio = r.listen(source)
        with open("temp.wav", "wb") as f:
            f.write(audio.get_wav_data())
        result = model.transcribe("temp.wav", language="ar")
        return result["text"]

def respond(text):
    if "أفضل" in text and ("انضباط" in text or "ملتزم" in text):
        print("🤖:", best_students_reply)
        engine.say(best_students_reply)
    else:
        fallback = "عذرًا، لم أفهم سؤالك. حاول مرة أخرى."
        print("🤖:", fallback)
        engine.say(fallback)
    engine.runAndWait()

# === التفاعل ===
while True:
    try:
        question = recognize_with_whisper()
        print("🗣️ قلت:", question)
        respond(question)
    except KeyboardInterrupt:
        print("\nتم الإنهاء.")
        break
    except Exception as e:
        print("حدث خطأ:", e)
        engine.say("حدث خطأ. حاول مرة أخرى.")
        engine.runAndWait()
