import re
from number_parser import parse_number

def detectar_operador(texto):
    operadores = {
        "+": ["+", "más", "suma", "sumar"],
        "-": ["-", "menos", "resta", "restar"],
        "*": ["*", "por", "multiplica", "multiplicado"],
        "/": ["/", "entre", "divide", "dividido", "dividir"]
    }
    for simbolo, palabras in operadores.items():
        for palabra in palabras:
            if palabra in texto:
                return simbolo
    return None

def extraer_numeros(texto):
    texto = texto.lower()
    texto = re.sub(r'(?<=\d),(?=\d{3}\b)', '', texto)
    texto = re.sub(r'(?<=\d)\.(?=\d{3}\b)', '', texto)
    texto = re.sub(r'\s+', ' ', texto)

    palabras = texto.split()
    numeros = []
    buffer = []

    def procesar_buffer(buf):
        frase = " ".join(buf)
        try:
            num = parse_number(frase)
            return float(num) if num is not None else None
        except:
            return None

    i = 0
    while i < len(palabras):
        palabra = palabras[i]

        # Detecta cifras directamente (ej: 1000, 1.5)
        if re.match(r'^\d+(\.\d+)?$', palabra):
            if buffer:
                num = procesar_buffer(buffer)
                if num is not None:
                    numeros.append(num)
                    buffer.clear()
            numeros.append(float(palabra))
        else:
            buffer.append(palabra)
            num = procesar_buffer(buffer)
            if num is not None:
                numeros.append(num)
                buffer.clear()

        i += 1

    # Procesa si queda algo al final
    if buffer:
        num = procesar_buffer(buffer)
        if num is not None:
            numeros.append(num)

    return numeros
