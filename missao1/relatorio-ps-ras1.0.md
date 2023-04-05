Danielly Rayanne Macedo Lima

**Missão 1.0: Primeiro Circuito Eletrônico - Acendendo um LED com Arduino**

Atividade:

- Montar o circuito para acender um LED com Arduino em uma protoboard no TinkerCAD;
- Dimensionar o resistor ideal para a cor do LED escolhida;
- Programar o Arduino para piscar um LED com 3 períodos de tempo diferentes;
- Anexar o link do circuito no TinkerCAD no relatório;
- Escrever um breve relatório sobre a missão;
- (Opcional) Reproduzir o circuito fisicamente no Laboratório eRobótica.

LINK DO CIRCUITO NO TINKERCAD: <https://www.tinkercad.com/things/d5QEwYPBZ92-daring-rottis/editel?sharecode=NJCRJ14RPDUkOFQYKpOt51R0SxmokKO4FlcvHtqCa48>

1 PASSO:

`	`A montagem do circuito foi feita no tinkercad com os seguintes componentes:

1. Microcontrolador arduino;
1. Uma placa de ensaio protoboard;
1. Dois LED’s difusos da cor vermelha;
1. Dois resistores.


2 PASSO:

`	`Cálculo da resistência correta para o led ter seu aproveitamento máximo:

1. A tensão de E/S do Arduino é de 5V. Já os LED’s funcionam com tensões muito baixas. Sendo assim, é necessária a utilização de resistores;
1. Um resistor é um componente eletrônico que serve para limitar o fluxo de cargas elétricas; 
1. Dessa forma, o cálculo para o resistor é dado pela:
   1. Tensão da fonte de alimentação, no caso 5V;
   1. Tensão suportada pelos LED’s, neste caso 3V;
   1. Corrente suportada pelo led em amperes, no caso 20mA

`			`\*\* I = W/V => W = I.V => W = 2.20 => W = 40W

`			`\*\* I = 40/2 => I = 20 mA

`			`\*\* I = W/V => V = W/ I => V = 40/20 => 2 V

1. Convertendo os 20mA para amperes, resultam em 0,02A;
1. Equação para calcular resistores: R = (Valimentacao - Vled)/ I

`		`R = ( 5 - 3 ) / 0,02 => R = 2 / 0,02 => R = 100 ohms;

1. Logo, será necessário um resistor de 100 ohms para cada led encontrado no projeto;
1. Calculando o resistor por meio das cores, temos: 
   1. Marrom = 1;
   1. Preto = 0;
   1. Marrom = 1 (número de 0’s a serem adicionados).
1. Assim, o resistor de 100 ohms possui as cores MARROM - PRETO - MARROM.

`	     `\*\*Obs: Os resistores que possuem apenas 3 faixas tem a tolerância considerada entre mais ou menos 20%.

3 PASSO:

`	`Construção do código com três períodos de tempo diferentes

