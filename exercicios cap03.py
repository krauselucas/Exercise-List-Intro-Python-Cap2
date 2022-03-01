##############################################################################
# Parte do livro Introdução à Programação com Python
# Autor: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2020
# Primeira edição - Novembro/2010 - ISBN 978-85-7522-250-8
# Segunda edição - Junho/2014 - ISBN 978-85-7522-408-3
# Terceira Edição - Janeiro/2019 - ISBN 978-85-7522-718-3
#
# Site: https://python.nilo.pro.br/
##############################################################################

#cap. 03-01

#Complete a tabela a seguir, marcando inteiro ou ponto flutuante dependendo do número apresentado.

#5      ○ inteiro
#5.0    ○ ponto flutuante
#4.3    ○ ponto flutuante
#-2     ○ inteiro
#100    ○ inteiro
#1.333  ○ ponto flutuante

#cap. 03-02

#Complete a tabela a seguir, respondendo True ou False. Considere a = 4, b = 10, c = 5.0, d = 1 e f = 5.

#a == c    ○ False   b > a     ○ True
#a < b     ○ True    c >= f    ○ True
#d > b     ○ False   f >= c    ○ True
#c != f    ○ False    c <= c    ○ True
#a == b    ○ False   c <= f    ○ True
#c < d     ○ False

#cap. 03-03

#Complete a tabela a seguir utilizando a = True, b = False e c = True.

#Expressão Resultado         Expressão Resultado
# a and a   ○ True     a or c    ○ True
# b and b   ○ False    b or c    ○ True
# not c     ○ False    c or a    ○ True
# not b     ○ True     c or b    ○ True
# not a     ○ False    c or c    ○ True
# a and b   ○ False    b or b    ○ False
# b and c   ○ False

#cap. 03-04

#salario = 1100
#test1 = salario>1200
#if(test1): print("Paga imposto")
#else: print("Não paga imposto")

#cap. 03-05

#Calcule o resultado da expressão A > B and C or D, utilizando os valores da tabela a seguir.

# A  B C     D      Resultado
# 1  2 True  False  False
# 10 3 False False  False
# 5  1 True  True   True

#cap. 03-06

# Escreva uma expressão que será utilizada para decidir se um aluno foi ou não aprovado. Para ser aprovado, todas as médias do aluno devem ser maiores que 7. Considere que o aluno cursa apenas três matérias, e que a nota de cada uma está armazenada nas seguintes variáveis: matéria1, matéria2 e matéria3.

# aluno = input("Qual o nome do aluno?")

# materia1 = float(input("Qual a nota na matéria1? "))

# materia2 = float(input("Qual a nota na matéria2? "))

# materia3 = float(input("Qual a nota na matéria3? "))

# notas = [materia1, materia2, materia3]

# if notas[0] > 7 and notas[1] > 7 and notas[2] > 7:
#     print(f"O aluno {aluno} foi aprovado!")
# else:
#     print(f"O aluno {aluno} foi reprovado.")


#cap. 03-07

# Faça um programa que peça dois números inteiros. Imprima a soma desses dois números na tela.

# num1 = int(input("Digite um número inteiro: "))

# num2 = int(input("Digite outro número inteiro: "))

# soma = num1 + num2

# print(f"A soma dos valores informados é {soma}.")

#cap. 03-08

# Escreva um programa que leia um valor em metros e o exiba convertido em milímetros.

# valor_metros = float(input("Digite o valor em metros: "))

# valor_milimetros = (valor_metros * 10 ** 3)

# print(f"O valor de {valor_metros} metros corresponde a {valor_milimetros} milímetros.")

#cap. 03-09

# Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos.

# dias = int(input("Digite a quantidade de dias: "))

# horas = int(input("Digite a quantidade de horas: "))

# minutos = int(input("Digite a quantidade de minutos: "))

# segundos = int(input("Digite a quantidade de segundos: "))

# dias_em_seg = dias*86400

# horas_em_seg = horas*3600

# minutos_em_seg = minutos*60

# total = dias_em_seg + horas_em_seg + minutos_em_seg + segundos

# print(f"O valor total em segundos é: {total}")

#cap. 03-10

# Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário.

# salario = float(input("Digite o valor do seu salário: "))

# aumento = float(input("De quanto foi o aumento em % ? "))

# salario_novo = round(salario*(aumento/100 + 1), 2)

# print(f"Seu salario novo é de {salario_novo}")

#cap. 03-11

# Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar.

# preco_sem_desconto = float(input("Qual o valor do produto sem contar o desconto? "))

# desconto = float(input("Digite o valor do desconto: "))

# preco_com_desconto = preco_sem_desconto * (1 - desconto/100)

# print(f"Após aplicar o desconto de {desconto}% o seu produto terá o preço final de {preco_com_desconto} reais")

#cap. 03-12

#Escreva um programa que calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem.

# distancia = float(input("Digite a distancia do percurso da viagem em km: "))

# velo_media = float(input("Digite a velocidade média do percurso da viagem em km/h: "))

# tempo_viagem = distancia / velo_media

# print(f"O tempo de viagem é de {tempo_viagem} horas")

#cap. 03-13

# Escreva um programa que converta uma temperatura digitada em °C em °F. A fórmula para essa conversão é:

#      9 × C
#  F = ----- + 32
#        5

# temp_graus = float(input("Digite a temperatura em graus: "))

# temp_fahrenheit = (9*temp_graus/5) + 32

# print(f"A temperatura de {temp_graus} graus Celsius corresponde a {temp_fahrenheit} graus fahrenheit")

#cap. 03-14

# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado.

# distancia = float(input("Quantos km foram percorridos pelo carro alugado? "))

# dias = float(input("Quantos dias foram passados com o carro alugado? "))

# preco_final = (60*dias) + (0.15*distancia)

# print(f"O valor total a pagar é de {preco_final} reais")

#cap. 03-15

# Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro, e calcule quantos dias de vida um fumante perderá. Exiba o total em dias.

# qtd_cigarros = int(input("Quantos cigarros são fumados por dia? "))

# qtd_anos = int(input("Há quantos anos você fuma? "))

# tempo_perdido = round((qtd_anos*qtd_cigarros*365*10/1440),0)

# print(f"O tempo de vida perdido é de {tempo_perdido} dias, aproximadamente")