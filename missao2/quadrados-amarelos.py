# Importação das bibliotecas
import cv2

# Leitura da imagem com a função imread()
path = r'/home/rayanne/ras-processo-seletivo/missao2/entrada.jpg'
imagem = cv2.imread(path)

#percorre as matrizes para mudar os valores na sequência gbr 
# pulando de 5 em 5 no indice e 'adicionando' quadrados amarelos na imagem

for y in range(0, imagem.shape[0], 10): #percorre linhas
    for x in range(0, imagem.shape[1], 10): #percorre colunas
        imagem[y:y+5, x: x+5] = (0,255,255)

# Mostra a imagem com a função imshow       
cv2.imshow("Imagem modificada", imagem)
cv2.waitKey(0)  #espera pressionar qualquer tecla