# Importação das bibliotecas
import cv2

# Leitura da imagem com a função imread()
path = r'/home/rayanne/ras-processo-seletivo/missao2/entrada.jpg'
imagem = cv2.imread(path)

#percorre as matrizes para mudar os valores na sequência gbr 
#as cores serão de acordo com os restos

for y in range(0, imagem.shape[0]): #percorre linhas
 for x in range(0, imagem.shape[1]): #percorre colunas
    imagem[y, x] = (x%256,y%256,x%256)

# Mostra a imagem com a função imshow
cv2.imshow("Imagem modificada", imagem)
cv2.waitKey(0)#espera pressionar qualquer tecla