import cv2
import mediapipe as mp

path = r'quatr0_dedos.png'
img = cv2.imread(path)

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

#convertendo
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
out_results = mp_hands.Hands().process(img)
#convertendo
img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

hand_points = out_results.multi_hand_landmarks
connections = mp_hands.HAND_CONNECTIONS
h,w,_ = img.shape 
pontos = []

#adicionando os 'ligamentos' da mão
if hand_points:
    for points in hand_points:
      mp_drawing.draw_landmarks(img, points, connections)
    
    #contagem dos dedos  
    for id,cord in enumerate(points.landmark): 
            cx,cy = int(cord.x * w),int(cord.y * h)
            pontos.append((cx,cy))
            
    dedos = [8,12,16,20]
    cont = 0
    if pontos: 
      if pontos[4][0] < pontos[3][0]:
        cont += 1
      for x in dedos:
        if pontos[x][1] < pontos[x-2][1]:
          cont +=1

    start_point = (80,10)
    end_point = (200,100)
    color = (0,0,0)
    thickness = -1

    #retangulo que vai aparecer na imagem com o número da contagem
    cv2.rectangle(img, start_point, end_point, color, thickness)

    text = str(cont)
    coordinates = (100, 100)
    font = cv2.FONT_HERSHEY_PLAIN
    font_scale = 8
    color = (255,255,255)

    #colocando a contagem de dedos
    cv2.putText(img,text,coordinates,font,font_scale,color,5) 

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()