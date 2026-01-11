# Car Price Prediction Multiple Linear Regression

Kaggle: https://www.kaggle.com/datasets/hellbuoy/car-price-prediction


# Apresentação da Empresa: Geely Auto

A Geely Auto é uma empresa chinesa líder na fabricação e venda de automóveis. A empresa possui uma vasta experiência na indústria automotiva e tem uma presença significativa no mercado chinês. Com sua visão de expandir sua atuação global, a Geely Auto tem interesse em ingressar no competitivo mercado dos Estados Unidos.

# Problema Específico: Penetração no Mercado dos Estados Unidos

A Geely Auto enfrenta o desafio de entrar no mercado automotivo dos Estados Unidos, que é altamente competitivo e diversificado. Para ter sucesso nesse mercado, a empresa precisa compreender as dinâmicas de preços específicas da região e identificar os principais fatores que influenciam o preço dos carros no mercado americano.

# Perguntas da Pesquisa:

1. Quais são os fatores que afetam significativamente o preço dos carros no mercado automotivo dos Estados Unidos?
2. Quais variáveis independentes estão mais fortemente correlacionadas com o preço dos carros?
3. Como podemos construir um modelo preditivo eficaz para estimar o preço dos carros com base nas variáveis disponíveis?
4. Como essas variáveis explicam a variação nos preços dos carros?
5. Quais insights podemos obter do modelo para ajudar a Geely Auto a tomar decisões estratégicas e atingir seus objetivos de preços no mercado americano?


# Dataset
Disponivel em: https://www.kaggle.com/datasets/hellbuoy/car-price-prediction

## Sobre os dados
Coluna|Descrição
-----|-----
Car_ID	|Sua classificação de risco de seguro atribuída, um valor de +3 indica que o automóvel é arriscado, -3 que provavelmente é bastante seguro. (Categórico)
carCompany |	Nome da empresa de carros (categórica)
fueltype |	Tipo de combustível de carro, ou seja, gás ou diesel (categórico)
aspiration | 	Aspiração usada em um carro (categórico)
doornumber |	Número de portas em um carro (categórico)
carbody |	Corpo de carro (categórico)
drivewheel |	tipo de roda de acionamento (categórica)
enginelocation |	Localização do motor do carro (categórico)
wheelbase |	Weelbase de carro (numérico)
carlength |	Comprimento do carro (numérico)
carwidth |	Largura do carro (numérico)
carheight |	Altura do carro (numérico)
curbweight |	O peso de um carro sem ocupantes ou bagagem. (Numérico)
enginetype |	Tipo de motor. (Categórico)
cylindernumber |	Cilindro colocado no carro (categórico)
enginesize |	Tamanho do carro (numérico)
fuelsystem |	Sistema de combustível de carro (categórico)
boreratio |	Boreratio de carro (numérico)
stroke |	AVC ou volume dentro do motor (numérico)
compressionratio |	Taxa de compressão de carro (numérico)
horsepower |	Potência (numérica)
peakrpm |	RPM de pico de carro (numérico)
citympg |	Milhagem na cidade (numérica)
highwaympg |	Milhagem na rodovia (numérica)
price(Dependent variable) |	Preço do carro (numérico)

* O dataset possui várias colunas, cada uma representando uma característica específica do carro, como a marca do carro, o tipo de combustível (gasolina ou diesel), a aspiração utilizada no carro, o número de portas, o tipo de carroceria, a tração das rodas, a localização do motor, entre outros.
* Algumas colunas são categóricas, ou seja, representam atributos qualitativos, enquanto outras são numéricas, representando atributos quantitativos. Por exemplo, a coluna "carCompany" é categórica, enquanto "horsepower" é numérica.
* A coluna "price" é a variável dependente, que representa o preço do carro, e será nosso alvo para prever com base nas demais variáveis independentes.
* Existem algumas colunas que indicam informações técnicas sobre o motor, como o tamanho do motor ("enginesize"), o número de cilindros ("cylindernumber"), a taxa de compressão ("compressionratio"), entre outras. Essas características do motor podem influenciar significativamente o preço do carro.
* Também temos informações sobre o tamanho físico do carro, como o comprimento ("carlength"), a largura ("carwidth"), a altura ("carheight"), e o peso do carro ("curbweight"). Essas características podem afetar o preço do carro, pois carros maiores ou mais pesados ​​podem ter um preço mais alto.
* Algumas colunas, como "citympg" e "highwaympg", indicam o consumo de combustível na cidade e na estrada, respectivamente. Essas informações podem influenciar o preço do carro, uma vez que carros mais econômicos podem ser mais valorizados.
* O dataset também inclui informações sobre a relação diâmetro do cilindro e curso do pistão ("boreratio"), o curso ou volume dentro do motor ("stroke"), a potência do motor ("horsepower") e o RPM de pico do motor ("peakrpm"), que são fatores importantes a serem considerados na determinação do preço do carro.
* As informações sobre a empresa de carros ("carCompany") também podem ser relevantes, pois diferentes marcas podem ter reputações e posicionamentos de mercado diferentes, o que pode afetar os preços dos carros.






## Análise da Variável dependente (y)

![All your files and folders are presented as a tree in the file explorer. You can switch from one to another by clicking a file in the tree.](https://cdn-images-1.medium.com/max/800/1*qKqDy7NOPyP6NVZP0f2KqA.png)
![enter image description here](https://cdn-images-1.medium.com/max/800/1*sh1MsMGwMYMvb1nI4dTDzA.png)

O Preço dos automóveis possuem uma assimetria positiva o que pode causar uma maior dispersão entre os valores conforme se distanciam da média, portanto foi aplicado o logaritmo na variável com o objetivo de deixar mais próxima de uma distribuição normal.
![enter image description here](https://cdn-images-1.medium.com/max/800/1*KBRIaSFRlUiEyblULnVreg.png)

## Tratativas das Variáveis dependentes (x)


Foi aplicado a conversão das variáveis alfanuméricas com **LabelEncoder()** com objetivo de ter somente variáveis numéricas, com isso os números foram tratados para não ocorrer erros quando calcula-se o logaritmo.
Com os novos valores analisei quais variáveis possuem mais correlação com o **price**.

![enter image description here](https://cdn-images-1.medium.com/max/800/1*RzMWW5GMrqa5hNxxz3SOiA.png)
![enter image description here](https://cdn-images-1.medium.com/max/800/1*vyHHjG1MB3qFEs988qUuPg.png)
![enter image description here](https://cdn-images-1.medium.com/max/800/1*IVH7FzH7zInOERfq8sZCSQ.png)
![enter image description here](https://cdn-images-1.medium.com/max/800/1*JdNK5ijYbdy6ZeMnGEPI0Q.png)

Utilizando da função **.corr()** do dataframe pandas considerei as variáveis com correlação ≥0.3.

## Estimando qualidade das variaveis

![enter image description here](https://cdn-images-1.medium.com/max/800/1*0QjYv4PI2_RuwXIHnnTAJQ.png)

Após coletar o sumário estatistico considerei as variaveis com **P>|t|** inferior a 0.5.

## Resultado do Modeloenter code here
De posse das variáveis treinei um modelo considerado 80% da base sendo que os outros 20% foram separadas para teste.
Foi possível obter com o modelo um **R² de 0.873**, ou seja, para os dados no treinamento o modelo possui uma boa aderência.

![enter image description here](https://cdn-images-1.medium.com/max/800/1*YvTY_ETpRqL57RAWFNVdIg.png)

Agora considerando a base de teste obtive um **R² de 0.826**.
![enter image description here](https://cdn-images-1.medium.com/max/800/1*0e91tFbZ7qYsXcaBP8P_sA.png)
É possível notar o comportamento gerado devido assimetria positiva na variável **x(price)**.
## Conclusão para o problema
Por fim com esse estudo podemos concluir que as principais variáveis que para precificação de automóveis no mercado americano são:

-   **symboling** → Classificação De segurança de um automóvel.
-   **drivewheel** → Tipo de roda de acionamento.
-   **wheelbase** → Distância entre os eixos do automóvel
-   **carwidth** → Largura do automóvel.
-   **curbweight** → Peso do automóvel (sem ocupantes e bagagem)
-   **enginesize** →Tamanho do motor
-   **boreratio** → relação entre as dimensões do diâmetro do furo do cilindro do motor e o comprimento do curso do pistão.
-   **horsepower** → Cavalos de potência.

Com base nessas variáveis escolhidas por possuírem uma correlação alta com o preço conseguimos entrar um **R² de 0.826**, contudo é importante ressaltar que não obtivemos bons resultado com veículos mais caros (veículos de luxo), é que para esse tipo de veículo o que as variáveis podem ser relevantes para sua precificação podem ser diferentes, assim sendo necessário um novo estudo para esta classe de veículos.
