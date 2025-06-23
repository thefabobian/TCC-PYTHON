from voice.speaker import speak
from voice.recognizer import listen
from logic.operations import calcular

def main():
    speak("Calculadora por voz iniciada. Di tu operación o di 'salir' para terminar.")
    while True:
        texto = listen()
        if not texto:
            continue
        if "salir" in texto or "terminar" in texto:
            speak("Chao, nos vemos.")
            break
        calcular(texto)

if __name__ == "__main__":
    main()
