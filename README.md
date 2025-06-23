# 🧮 Calculadora por Voz en Python (Español)

Este es un proyecto de calculadora controlada por voz, desarrollada en Python. Permite realizar operaciones matemáticas simples (suma, resta, multiplicación y división) usando comandos hablados en español.

## 🔧 Requisitos del sistema

- Python 3.8 o superior
- Micrófono funcional
- Conexión a internet (para reconocimiento de voz con Google Speech)

---

## 📦 Instalación de librerías necesarias

Ejecuta este comando en tu terminal o consola:

```bash
pip install SpeechRecognition
pip install pyttsx3
pip install pyaudio
pip install number-parser
pip install num2words

⚠️ Si tienes errores con pyaudio en Windows, ejecuta:

pip install pipwin
pipwin install pyaudio

🚀 ¿Cómo ejecutar la calculadora?
En la terminal, navega hasta la carpeta del proyecto y ejecuta:
python main.py
