import speech_recognition as sr

def reconocer_voz():
    # Crear un objeto de reconocimiento
    r = sr.Recognizer()

    # Utilizar el micrófono como fuente de audio
    with sr.Microphone() as source:
        print("Di algo...")
        r.adjust_for_ambient_noise(source)  # Ajustar para el ruido ambiente
        audio = r.listen(source)

    try:
        # Utilizar Google Speech Recognition para convertir el audio en texto
        texto = r.recognize_google(audio, language='en-US')
        print("Has dicho: " + texto)
        return texto
    except sr.UnknownValueError:
        print("No se pudo entender el audio")
    except sr.RequestError as e:
        print("Error al solicitar resultados; {0}".format(e))

if __name__ == "__main__":
    while True:
        texto = reconocer_voz()
        # Aquí puedes agregar lógica adicional basada en el texto reconocido
