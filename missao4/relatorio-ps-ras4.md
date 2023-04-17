Danielly Rayanne Macedo Lima

**Missão 4.0: Hand Tracking**

**Objetivo:** Criar uma aplicação com OpenCV. Realizar o reconhecimento de números utilizando os dedos da mão.

A missão consistiu no desenvolvimento de um código cujo objetivo foi de contabilizar quantos dedos tinha em uma mão utilizando o framework MediaPipe e a biblioteca OpenCV. 

Como visto na segunda missão da primeira etapa, o OpenCV é uma biblioteca multiplataforma de código aberto utilizada na área de visão computacional a qual permite a criação de softwares utilizando o processamento de imagens e vídeos. Além desta biblioteca, foi utilizado em conjunto o MediaPipe, que é um framework também de código aberto criado pela Google utilizado para detecção de elementos em imagens e em vídeos. 

Dessa forma, com este pequeno projeto de detecção de números com as mãos podemos nos familiarizar com as duas tecnologias utilizadas e entender mais sobre a abrangência de que futuros projetos podem ter. Com poucas linhas de código é possível criar aplicações extremamente funcionais e precisas, como a desta missão.

Aprendizado com essa missão:

- Familiarização com as novas tecnologias;
- Aplicações para tais recursos;
- A prática de conversão de RGB para BGR e vice versa;
- Busca de referências, materiais de estudo e tutoriais.

Conceitos novos aprendidos:

- BGR x RGB: Em resumo, a diferença entre esses dois está em como os pixels estão dispostos e em como as informações de um pixel são armazenadas. Sendo RGB: Red, Green e Blue e BGR: Blue, Green e Red. Assim, imagens BGR possuem arranjo inverso aos de imagens RGB e isso pode impactar em como vemos e tratamos as imagens. Isso se torna importante ao utilizarmos as tecnologias de visão computacional descritas anteriormente. É preciso saber como estamos lidando com a imagem, por exemplo: o OpenCV trabalha com o padrão BGR, já o MediaPipe trabalha com o padrão RGB. Dessa forma, ao longo do código existe a possibilidade de termos que ficar alternando e convertendo essa imagem entre um dos dois, como foi feito no código desta missão.

Dificuldades enfrentadas:

- A princípio, a ideia era de fazer um detector de imagem que utilizasse a webcam e capturasse em vídeo e fizesse a detecção. Entretanto, por motivos de processamento e dificuldades enfrentadas ao longo do desenvolvimento foi decidido a utilização de imagens previamente tiradas.
