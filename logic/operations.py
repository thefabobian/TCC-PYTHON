from voice.speaker import speak
from voice.recognizer import listen  # IMPORTANTE para escuchar la respuesta del usuario
from utils.number_extractor import extraer_numeros, detectar_operador
from num2words import num2words

def calcular(texto):
    numeros = extraer_numeros(texto)
    if len(numeros) < 2:
        speak("Necesito al menos dos números.")
        return

    operador = detectar_operador(texto)

    # 🔁 Si no se detecta operador, preguntar al usuario
    if operador is None:
        speak("No entendí qué operación quieres hacer. ¿Quieres sumar, restar, multiplicar o dividir?")
        respuesta = listen()
        operador = detectar_operador(respuesta)

        if operador is None:
            speak("Lo siento, no entendí la operación. Intenta de nuevo.")
            return

    resultado = None

    if operador == "+":
        resultado = sum(numeros)
        op = "más"
    elif operador == "-":
        resultado = numeros[0]
        for n in numeros[1:]:
            resultado -= n
        op = "menos"
    elif operador == "*":
        resultado = 1
        for n in numeros:
            resultado *= n
        op = "por"
    elif operador == "/":
        if any(n == 0 for n in numeros[1:]):
            speak("No se puede dividir por cero.")
            return
        resultado = numeros[0]
        for n in numeros[1:]:
            resultado /= n
        op = "entre"
    else:
        speak("Operación no reconocida.")
        return

    def limpiar(n): return int(n) if n == int(n) else round(n, 2)
    numeros_texto = f" {op} ".join(str(limpiar(n)) for n in numeros)
    resultado_limpio = limpiar(resultado)
    resultado_palabras = num2words(resultado_limpio, lang="es")

    respuesta = f"{numeros_texto} es {resultado_palabras}"
    print("", respuesta)
    speak(respuesta)
