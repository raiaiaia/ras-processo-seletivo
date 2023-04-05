# Importação das bibliotecas
import cv2

# Leitura da imagem com a função imread()
path = r'/home/rayanne/ras-processo-seletivo/missao2/entrada.jpg'
imagem = cv2.imread(path)

#percorre as matrizes para mudar os valores na sequência gbr
#retorna o valor do resto da divisao de 256 de x*y para ser o valor de blue


for y in range(0, imagem.shape[0], 1): #percorre as linhas
 for x in range(0, imagem.shape[1], 1): #percorre as colunas
    imagem[y, x] = (0,(x*y)%256,0)

# Mostra a imagem com a função imshow    
cv2.imshow("Imagem modificada", imagem)
cv2.waitKey(0)#espera pressionar qualquer tecla