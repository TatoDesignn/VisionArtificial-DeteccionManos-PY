## Detección de manos 🖐️
<p align="center">
  <img style="width: 700px; height: auto;" src="https://github.com/TatoDesign/Repositorios-Imagenes/blob/main/VisionArtifical/DeteccionManos.png">
</p>

Este proyecto creado con python y sus librerias: numpy, cv2 y mediapipe tiene como proposito leer los landmakrs de la mano, pintar los puntos  **0, 4 y 12** y trasar una linea con los puntos **0 y 8** para obtener la direccion en la cual la mano esta apuntando.
## ¿Como funciona?🤷‍♂️
-  Primero debemos importar las librerias `numpy, cv2 y mediapipe`.
-  Creamos los diferentes **frames** con cv2 para mostrar los resultados.
-  En el primer frame mostramos la apertura de la camara esto con `.VideoCapture()`.
-  En el segundo frame pintamos todos los landmakrs de la mano con `.draw_landmarks()`
-  En el tercer frame mostramos unicamente los puntos **0 4 y 12** de esta manera:
  ```python
  for landmark_id in [4, 0, 12]:
    landmark = hand_landmarks[landmark_id]
    height, width, _ = frame.shape

    cx, cy = int(landmark.x * width), int(landmark.y * height)
    cv2.circle(frame2, (cx, cy), 5, (0, 255, 0), -1)
  ```
- En el cuarto frame dibujaremos una linea entre el punto **0 y 8** y con esta obtendremos la direccion a la que a punta la mano:
```python
  landmark_0 = hand_landmarks[0] #almacenar el landmarks 0
  landmark_8 = hand_landmarks[8] #almacenar el landmarks 8

  height, width, _ = frame.shape #Guardar el tamaño de nuestro frame

  cx0, cy0 = int(landmark_0.x * width), int(landmark_0.y * height)
  cx8, cy8 = int(landmark_8.x * width), int(landmark_8.y * height)

  cv2.line(frame3, (cx0, cy0), (cx8, cy8), (0, 255, 0), 2)
  #Como primer argumento el frame donde deseo pintar la linea, 
  #luego las distancias x, y. y el color que tendra esta 

  # Determinar la dirección de la línea
  if landmark_8.x > landmark_0.x:
      direction = "Derecha"
  else:
      direction = "Izquierda"
````
## ¿Como puedo probarlo?👌
Debes tener python instalado en tu equipo y ademas tener las librerias necesarias para que funciones, es bastante sencillo abre el buscador de windows y busca "CMD", en tu terminal escribe estos dos comandos uno por uno:
- `py -m pip install numpy`
- `py -m pip install opencv-python`
- `py -m pip install mediapipe`
