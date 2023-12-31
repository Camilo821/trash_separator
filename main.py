import cv2
from pymata4 import pymata4
import speech_recognition as sr
from voice import reconocer_voz
# Carga el clasificador de cascada preentrenado para la detección facial
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Inicializa la cámara
cap = cv2.VideoCapture(0)
board = pymata4.Pymata4()
r = 2
g = 3
b = 4
board.set_pin_mode_digital_output(r)
board.set_pin_mode_digital_output(g)
board.set_pin_mode_digital_output(b)

while True:
    # Captura un fotograma
    ret, frame = cap.read()

    # Convierte la imagen a escala de grises (facilita la detección facial)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detecta caras en la imagen
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Dibuja un rectángulo alrededor de cada cara detectada
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        board.digital_pin_write(g, 1)
        board.digital_pin_write(r, 0)
        texto = reconocer_voz()
        if texto == 'azul':
            board.digital_pin_write(b, 1)
        elif texto == 'apagar':
            board.digital_pin_write(b, 0)
    # Muestra la imagen resultante
    cv2.imshow('Detección facial', frame)
    if len(faces) == 0:
        board.digital_pin_write(g, 0)
        board.digital_pin_write(r, 1)
        board.digital_pin_write(b, 0)
    # Detiene el bucle si se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        board.digital_pin_write(g, 0)
        board.digital_pin_write(r, 0)
        board.digital_pin_write(b, 0)
        break

# Libera la cámara y cierra la ventana
cap.release()
cv2.destroyAllWindows()
