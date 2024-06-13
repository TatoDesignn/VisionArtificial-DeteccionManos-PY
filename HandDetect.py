import cv2
import mediapipe as mp
import numpy as np

cv2.namedWindow("Seguimiento1", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Seguimiento1", 1280, 720)

mp_mano = mp.solutions.hands
mano = mp_mano.Hands()
mp_drawing = mp.solutions.drawing_utils #Configuraciones de para el funcionamiento de mp_hands

cap = cv2.VideoCapture(0) #apertura de la camara 

while cap.isOpened():
    ret, frame = cap.read() #frame normal

    if not ret:
        continue

    frame2 = frame.copy() #frame2 pintando landmakers 4, 0 y 12
    frame3 = frame.copy() #frame3 pintando la linea entre el 8 y 0 
    frame4 = frame.copy() #frame4 pintando todos los landmakers de la mano

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) #Primero convertir de BGR a RGB

    resultado = mano.process(frame_rgb)

    if resultado.multi_hand_landmarks:
        for landmarks in resultado.multi_hand_landmarks:

            mp_drawing.draw_landmarks(frame4, landmarks, mp_mano.HAND_CONNECTIONS)#Dibujamos todos
            #los landmakers en el frame4

            hand_landmarks = landmarks.landmark

            for landmark_id in [4, 0, 12]:
                landmark = hand_landmarks[landmark_id]
                height, width, _ = frame.shape
                cx, cy = int(landmark.x * width), int(landmark.y * height)
                cv2.circle(frame2, (cx, cy), 5, (0, 255, 0), -1)

            landmark_0 = hand_landmarks[0] #almacenar el landmarks 0
            landmark_8 = hand_landmarks[8] #almacenar el landmarks 8

            height, width, _ = frame.shape #Guardar el tamaño de nuestro frame

            cx0, cy0 = int(landmark_0.x * width), int(landmark_0.y * height)
            cx8, cy8 = int(landmark_8.x * width), int(landmark_8.y * height)

            cv2.line(frame3, (cx0, cy0), (cx8, cy8), (0, 255, 0), 2)#con la funcion line 
            #le paso como primer argumento el frame donde deseo pintar la linea, 
            #luego las distancias x, y. y el color que tendra esta 

            # Determinar la dirección de la línea
            if landmark_8.x > landmark_0.x:
                direction = "Derecha"
            else:
                direction = "Izquierda"

            # Imprimir el texto en la imagen
            cv2.putText(frame3, f'Direccion: {direction}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)


    ventana1 = np.hstack((frame, frame4))
    ventana2 = np.hstack((frame2, frame3))

    ventana_final = np.vstack((ventana1, ventana2))

    cv2.imshow('Seguimiento1', ventana_final)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()