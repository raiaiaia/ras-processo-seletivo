import cv2                     #importanto a biblioteca
import mediapipe as mp         #importanto o framework 

path = r'quatr0_dedos.png'     #lendo o caminho da foto
img = cv2.imread(path)         #chamando o metodo imread em uma variável


#soluções do mediapipe para desenho da mão
mp_hands = mp.solutions.hands 
mp_drawing = mp.solutions.drawing_utils

#convertendo de BGR para RGB
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#retorna o processamento da imagem em uma variavel
out_results = mp_hands.Hands().process(img)
#convertendo de RGB para BGR
img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

#pontos da mão
hand_points = out_results.multi_hand_landmarks
#armazena as conexões da mão em uma variável
connections = mp_hands.HAND_CONNECTIONS
#altura e largura da imagem
h,w,_ = img.shape
#cria uma listapara armazenar os pontos 
pontos = []

#adicionando os 'ligamentos' da mão
if hand_points:
    for points in hand_points:
      #desenha os pontos
      mp_drawing.draw_landmarks(img, points, connections)
    
    #contagem dos dedos  
    for id,cord in enumerate(points.landmark): 
            #conta os 21 pontos detectados 
            cx,cy = int(cord.x * w),int(cord.y * h)
            #adiciona os pontos na lista pontos
            pontos.append((cx,cy))

    #posicao dos dedos para contagem        
    dedos = [8,12,16,20]
    #variavel responsavel pela contagem de dedos
    cont = 0
    if pontos: 
      if pontos[4][0] < pontos[3][0]:
        cont += 1
      for x in dedos:
        if pontos[x][1] < pontos[x-2][1]:
          cont +=1

    #ponto de inicio do retangulo
    start_point = (80,10)
    #ponto final do retangulo
    end_point = (200,100)
    #cor do retangulo
    color = (0,0,0)
    #grossuta/espessura do retangulo
    thickness = -1

    #retangulo que vai aparecer na imagem com o número da contagem
    cv2.rectangle(img, start_point, end_point, color, thickness)

    #o texto contendo o numero de dedos contados
    text = str(cont)
    #as coordenadas para o texto
    coordinates = (100, 100)
    #a fonte do texto
    font = cv2.FONT_HERSHEY_PLAIN
    #a 'escala' ou espessura do da fonte
    font_scale = 8
    #a cor, no caso branca
    color = (255,255,255)

    #colocando a contagem de dedos
    cv2.putText(img,text,coordinates,font,font_scale,color,5) 

    '''
    lembrando que os parametros de rectangle e putTex não 
    necessitam vir através de variáveis, fiz isso apenas 
    para métodos de aprendizagem e entendimento do código.
    '''

#carrega a imagem em uma nova janela
cv2.imshow('image', img)

#fecha a janela da imagem quando qualquer tecla for pressionada
cv2.waitKey(0)
cv2.destroyAllWindows()