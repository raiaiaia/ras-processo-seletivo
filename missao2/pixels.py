# Importação das bibliotecas
import cv2

# Leitura da imagem com a função imread()
path = r'/home/rayanne/ras-processo-seletivo/missao2/entrada.jpg'
imagem = cv2.imread(path)

#percorre as matrizes para mudar os valores na sequência gbr 
#deixa a imagem azul

for y in range(0, imagem.shape[0]):
 for x in range(0, imagem.shape[1]):
    imagem[y, x] = (255,0,0)

# Mostra a imagem com a função imshow
cv2.imshow("Imagem modificada", imagem)
cv2.waitKey(0) #espera pressionar qualquer tecla