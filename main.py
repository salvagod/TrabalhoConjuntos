#Aluno: Vitor Salvadego

# Enunciado:
# Para obter os pontos relativos a este trabalho, você  deverá criar um programa, utilizando a linguagem Python, C, ou C++.  
# Este programa, quando executado, irá apresentar os resultados de operações que serão realizadas entre dois conjuntos de dados.  
# O programa que você desenvolverá irá receber como entrada um arquivo de texto (.txt) contendo vários conjuntos de dados e várias operações.
# Estas operações e dados estarão representadas em um arquivo de textos contendo apenas os dados referentes as operações que devem ser realizadas 
# segundo a seguinte regra fixa: a primeira linha do arquivo de texto de entrada conterá o número de operações  que  estão  descritas  no  arquivo,
# este número de operações será um inteiro; as linhas seguintes seguirão sempre o mesmo padrão de três linhas: a primeira  linha apresenta o código
# da operação (U para união, I para interseção, D para diferença e C produto cartesiano), a segunda e terceira linhas conterão os elementos dos conjuntos
# separados por virgulas. A seguir está um exemplo das linhas que podem existir em um arquivo de testes para o programa que você irá desenvolver: 
# 4 
# U 
# 3, 5, 67, 7 
# 1, 2, 3, 4  
# I 
# 1, 2, 3, 4, 5 
# 4, 5 
# D 
# 1, A, C, 34 
# A, C, D, 23 
# C 
# 3, 4, 5, 5, A, B, R 
# 1, B, C, D, 1 
# Neste exemplo temos 4 operações uma união (U), uma interseção (I), um diferença (D) e um produto cartesiano (C). A união, definida por U, deverá 
# ser executada sobre os conjuntos {𝟑,𝟓,𝟔𝟕,𝟕} e {𝟏,𝟐,𝟑,𝟒}, cujos elementos estão explicitados nas linhas posteriores a definição da operação (U).  
# A resposta do seu programa deverá conter a operação realizada, descrita por extenso, os dados dos conjuntos identificados, e o resultado da operação.
#  No caso da união a linha de saída deverá conter a informação e a formatação mostrada a seguir:    
# União: conjunto 1 {3,5,67,7}, conjunto 2 {1,2,3,4}. Resultado: {3,5,67,7,1,2,4}   
# Seu programa deverá mostrar a saída no terminal, ou em um arquivo de textos. Em qualquer um dos casos, a saída será composta por uma linha de saída para
# cada operação constante no arquivo de  textos de entrada  formatada segundo o exemplo de saída acima. Observe as letras  maiúsculas e minúsculas, e os 
# pontos utilizados na formatação da linha de saída apresenta acima. No caso do texto de exemplo, teremos 4 linhas, e apenas 4 linhas de saída, formatadas e 
# pontuadas conforme o exemplo de saída acima. O uso de linhas extras na saída, ou erros de formatação, implicam em perda de pontos como pode ser visto na 
# rubrica de avaliação constante neste documento. Para que seu programa possa ser testado você deve criar, no mínimo, três arquivos de entrada contendo um
# número diferente de operações, operações com dados diferentes, e operações em ordem diferentes. Os arquivos de entrada criados para os seus testes
# devem estar disponíveis tanto no ambiente repl.it quanto no ambiente Github. Observe que o professor irá testar seu programa com os arquivos de testes 
# que você criar e com, no mínimo um arquivo de testes criado pelo próprio professor. 

# Referência: Os conhecimentos aqui usados foram adquiridos utilizando o site:
# https://docs.python.org/3/tutorial/index.html

def RemoverNumerosRepetidos(UniaoFinal):    #função para verificar e remover números repetidos na operação de união
    ConjuntoUniaoFinal = []                 #vetor que será populado com a união das 2 listas
    for i in UniaoFinal:
        if i not in ConjuntoUniaoFinal:     #verifica numeros repetidos
            ConjuntoUniaoFinal.append(i)    #somente popula o vetor caso o número não seja repetido
    return ConjuntoUniaoFinal

def CalcularProdutoCartesiano(elementos):   #função para juntar os elementos de cada lista para formar o produto cartesiano
  produtocartesiano = [[]]                  #vetor que será populado com o produto cartesiano
  for elemento in elementos: 
    produtocartesiano = [x+[y] for x in produtocartesiano for y in elemento] #loop de repetição para juntar os elementos de acordo com índice de cada lista
  return produtocartesiano

def Uniao(): #função que realizará a operação de união
    numeros1 = f.readline()              #ler a linha de elementos para a 1ª lista
    numeros1 = numeros1.strip()          #retira espaços desnecessários
    numeros1 = numeros1.split(", ")      #separa a string em elementos separados com base na vírgula e espaço 
    exibicao1 = ', '.join(numeros1)      #junta os elementos separados em uma string para uma melhor exibição e formatação na saída
    exibicao1 = "{" + exibicao1 + "}"    #incorpora chaves para notação correta de um conjunto

    numeros2 = f.readline()
    numeros2 = numeros2.strip()
    numeros2 = numeros2.split(", ")
    exibicao2 = ', '.join(numeros2)
    exibicao2 = "{" + exibicao2 + "}"

    UniaoFinal = numeros1 + numeros2                   #une as 2 listas em uma só
    UniaoFinal = RemoverNumerosRepetidos(UniaoFinal)   #remove possíveis números repetidos
    UniaoFinal = ', '.join(UniaoFinal)                 #une elementos em uma só string com vírgulas e espaços
    UniaoFinal = "{" + UniaoFinal + "}"                #incorpora chaves para notação correta de um conjunto

    print('União: conjunto 1 {}, conjunto 2 {}. Resultado: {}'.format(exibicao1, exibicao2, UniaoFinal)) #Mensagem devidamente formatada com o conjunto 1, 2 e conjunto final de união

def Intersecao(): #função que realizará a operação de interseção
    numeros1 = f.readline()
    numeros1 = numeros1.strip()
    numeros1 = numeros1.split(", ")
    exibicao1 = ', '.join(numeros1)
    exibicao1 = "{" + exibicao1 + "}"

    numeros2 = f.readline()
    numeros2 = numeros2.strip()
    numeros2 = numeros2.split(", ")
    exibicao2 = ', '.join(numeros2)
    exibicao2 = "{" + exibicao2 + "}"

    intersecao = []                       #vetor que será populado com os elementos da interseção
    for elemento in numeros1:             #laço de repetição para verificar todos os elementos
        if elemento in numeros2:          #verifica se o elemento da 1ª lista está contido na 2ª
            intersecao.append(elemento)   #caso esteja, o elemento populará o vetor
    intersecao = ', '.join(intersecao)    #une elementos em uma só string com vírgulas e espaços
    intersecao = "{" + intersecao + "}"   #incorpora chaves para notação correta de um conjunto

    print('Interseção: conjunto 1 {}, conjunto 2 {}. Resultado: {}'.format(exibicao1, exibicao2, intersecao))  #Mensagem devidamente formatada com o conjunto 1, 2 e conjunto final de interseção

def Diferenca(): #função que realizará a operação de diferença
    numeros1 = f.readline()
    numeros1 = numeros1.strip()
    numeros1 = numeros1.split(", ")
    exibicao1 = ', '.join(numeros1)
    exibicao1 = "{" + exibicao1 + "}"

    numeros2 = f.readline()
    numeros2 = numeros2.strip()
    numeros2 = numeros2.split(", ")
    exibicao2 = ', '.join(numeros2)
    exibicao2 = "{" + exibicao2 + "}"

    diferenca = []                      #vetor que será populado com os elementos diferentes
    for elemento in numeros1:           #laço de repetição para verificar todos os elementos
        if elemento not in numeros2:    #verifica se elementos na lista 1 estão na lista 2
            diferenca.append(elemento)  #caso não estejam, serão alocados para o vetor
    for elemento in numeros2:           #laço de repetição para verificar todos os elementos
        if elemento not in numeros1:    #verifica se elementos na lista 2 estão na lista 1
            diferenca.append(elemento)  #caso não estejam, serão alocados para o vetor
    diferenca = ', '.join(diferenca)
    diferenca = "{" + diferenca + "}"

    print('Diferença: conjunto 1 {}, conjunto 2 {}. Resultado: {}'.format(exibicao1, exibicao2, diferenca))   #Mensagem devidamente formatada com o conjunto 1, 2 e conjunto final da diferença

def ProdutoCartesiano(): #função que realizará a operação do produto cartesiano
    numeros1 = f.readline()
    numeros1 = numeros1.strip()
    numeros1 = numeros1.split(", ")
    exibicao1 = ', '.join(numeros1)
    exibicao1 = "{" + exibicao1 + "}"

    numeros2 = f.readline()
    numeros2 = numeros2.strip()
    numeros2 = numeros2.split(", ")
    exibicao2 = ', '.join(numeros2)
    exibicao2 = "{" + exibicao2 + "}"

    produtos = [numeros1, numeros2]                                   #variável que conterá as 2 listas de números
    produtocartesiano = CalcularProdutoCartesiano(produtos)           #formar o produto cartesiano
    produtocartesiano = ', '.join(str(i) for i in produtocartesiano)  #unir elementos em uma string para melhor formatação
    produtocartesiano = "{" + produtocartesiano + "}" 

    print('Produto Cartesiano: conjunto 1 {}, conjunto 2 {}. Resultado: {}'.format(exibicao1, exibicao2, produtocartesiano))   #Mensagem devidamente formatada com o conjunto 1, 2 e conjunto final do produto cartesiano

x = 0   #variável utilizada para o laço de repetição do programa
f = open("problema.txt", "r")   #abrir arquivo com problemas que serão lidos (Para trocar de arquivo, utilize os nomes "problema.txt", "problema2.txt", "problema3.txt" ou o de outro criado posteriormente.)
numeroOperacoes = int(f.readline())   #ler o número de operações que serão executadas

operacao = f.readline()           #ler a primeira operação do programa 
operacao = operacao.strip()
operacao = operacao.strip('\n')

while x != numeroOperacoes: #laço de repetição conforme o numero de operações lido anteriormente
    if operacao == "U": #condicional para caso da operação do momento ser União
        Uniao()
        operacao = f.readline() #passar para próxima operação
        operacao = operacao.strip()
        operacao = operacao.strip('\n')
    
    if operacao == "I": #condicional para caso da operação do momento ser Interseção
        Intersecao()
        operacao = f.readline()
        operacao = operacao.strip()
        operacao = operacao.strip('\n')
    
    if operacao == "D": #condicional para caso da operação do momento ser Diferença
        Diferenca()
        operacao = f.readline()
        operacao = operacao.strip()
        operacao = operacao.strip('\n')
    
    if operacao == "C": #condicional para caso da operação do momento ser Produto Cartesiano
        ProdutoCartesiano()
        operacao = f.readline()
        operacao = operacao.strip()
        operacao = operacao.strip('\n')

    x += 1 #continuidade da repetição
f.close()