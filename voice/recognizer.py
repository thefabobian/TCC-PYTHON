import speech_recognition as sr
from voice.speaker import speak

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Escuchando...")
        recognizer.pause_threshold = 1.2   # espera más antes de cortar
        recognizer.energy_threshold = 300  # ajustar si detecta poco sonido
        audio = recognizer.listen(source, timeout=10, phrase_time_limit=10)
    try:
        text = recognizer.recognize_google(audio, language='es-ES')
        print(f"📣 Dijiste: {text}")
        return text.lower()
    except sr.UnknownValueError:
        speak("No entendí. Intenta otra vez.")
        return ""
    except sr.WaitTimeoutError:
        speak("No detecté ninguna voz.")
        return ""
    except sr.RequestError:
        speak("Error con el servicio de reconocimiento.")
        return ""
