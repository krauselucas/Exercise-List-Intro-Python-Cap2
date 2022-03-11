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

#cap. 04-01

# Analise o Programa 4.1. Responda o que acontece se o primeiro e o segundo valores forem iguais? Explique.

# Se os valores forem iguais, nada será impresso.
# Isso acontece porque a > b e b > a são falsas quando a = b.
# Assim, nem o print de 2, nem o print de 3 serão executados, logo nada será impresso.

#cap. 04-02

# Escreva um programa que pergunte a velocidade do carro de um usuário. Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba o valor da multa, cobrando R$ 5 por km acima de 80 km/h.

velocidade_usuario = int(input("Digite a velocidade do carro: "))

valor_multa = (velocidade_usuario - 80) * 5

if velocidade_usuario > 80:
    print("A velocidade está acima do limite permitido. Você foi multado.")
    print(f"O valor da multa a ser paga é de {valor_multa} reais.")
else:
    print("Você não foi multado.")

#cap. 04-03

# Escreva um programa que leia três números e que imprima o maior e o menor.

num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))
num3 = float(input("Digite mais um número: "))

lista = []

lista.append(num1)
lista.append(num2)
lista.append(num3)

print(f"O valor mais alto dentre os 3 números digitados é {max(lista)} e o menor é {min(lista)}.")

# cap. 04-04

# Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. Para salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, de 15%.

salario = float(input("Digite o valor do seu salário: "))

if salario > 1250:
    aumento = 10
    salario_novo = round(salario*(aumento/100 + 1), 2)
    print(f"Seu salario novo é de {salario_novo}.")
else:
    aumento = 15
    salario_novo = round(salario*(aumento/100 + 1), 2)
    print(f"Seu salario novo é de {salario_novo}.")

# cap. 04-05

# Execute o Programa 4.4 e experimente alguns valores. Verifique se os resultados foram os mesmos do Programa 4.2.

# Sim, os resultados são os mesmos.


# cap. 04-06

# Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km. Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até de 200 km, e R$ 0,45 para viagens mais longas.

distancia = float(input("Qual distância você deseja percorrer? "))

if distancia > 200:
    preco_passagem = distancia * 0.45
    print(f"O preço da sua passagem será R$ {preco_passagem:.2f}.")
else:
    preco_passagem = distancia * 0.5
    print(f"O preço da sua passagem será R$ {preco_passagem:.2f}.")

# cap. 04-07

# O exercício consiste em rastrear o programa da listagem 4.7.
# O resultado deve ser o mesmo do apresentado na tabela 4.2.
# A técnica de rastreamento é apresentada na página 62,
# seção 3.6 Rastreamento.

# cap. 04-08

# Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar. Você deve poder calcular soma (+), subtração (-), multiplicação (*) e divisão (/). Exiba o resultado da operação solicitada.

num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))

operacao = input("Qual operação você deseja realizar? Escreva por extenso: ").upper()

if operacao == "SOMA":
    soma = num1 + num2
    print(soma)
elif operacao == "SUBTRAÇÃO":
    subtracao = num1 - num2
    print(subtracao)
elif operacao == "MULTIPLICAÇÃO":
    multiplicacao = num1 * num2
    print(multiplicacao)
elif  operacao == "DIVISÃO":
    divisao = num1 / num2
    print(divisao)
else:
    print("Algo deu errado.")

# cap. 04-09

# Escreva um programa para aprovar o empréstimo bancário para compra de uma casa. O programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar. O valor da prestação mensal não pode ser superior a 30% do salário. Calcule o valor da prestação como sendo o valor da casa a comprar dividido pelo número de meses a pagar.

valor_casa = float(input("Digite o valor da casa: "))
salario = float(input("Digite o valor do seu salário: "))
anos_a_pagar = int(input("Digite em quantos anos você pretende pagar as prestações: "))
meses_a_pagar = int(anos_a_pagar * 12)
prestacao_mensal = round((valor_casa / meses_a_pagar), 2)

if prestacao_mensal > salario * (30/100):
    print("O empréstimo não pode ser aprovado, pois o valor das prestações supera 30 percentuais do seu salário.")
else:
    print(f"O valor da prestação mensal é de R$ {prestacao_mensal}.")

# cap. 04-10

# Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica. Pergunte a quantidade de kWh consumida e o tipo de instalação: R para residências, I para indústrias e C para comércios. Calcule o preço a pagar de acordo com a tabela a seguir.

# +---------------------------------------+
# |   Preço por tipo e faixa de consumo   |
# +---------------------------------------+
# | Tipo        | Faixa (kWh)   | Preço   |
# +=======================================+
# | Residencial | Até 500       | R$ 0,40 |
# |             | Acima de 500  | R$ 0,65 |
# +---------------------------------------+
# | Comercial   | Até 1000      | R$ 0,55 |
# |             | Acima de 1000 | R$ 0,60 |
# +---------------------------------------+
# | Industrial  | Até 5000      | R$ 0,55 |
# |             | Acima de 5000 | R$ 0,60 |
# +---------------------------------------+

qtd_kwh = float(input("Digite o valor gasto em kWh: "))
tipo_instalacao = input("Digite o tipo de instalação apenas com a inicial: ").upper()

if (tipo_instalacao == "R") and qtd_kwh <= 500:
    preco = qtd_kwh * 0.40
    print(f"O preço a ser pago é de R$ {preco:.2f}.")
elif (tipo_instalacao == "R") and qtd_kwh > 500:
    preco = qtd_kwh * 0.65
    print(f"O preço a ser pago é de R$ {preco:.2f}.")

elif (tipo_instalacao == "C") and qtd_kwh <= 1000:
    preco = qtd_kwh * 0.55
    print(f"O preço a ser pago é de R$ {preco:.2f}.")
elif (tipo_instalacao == "C") and qtd_kwh > 1000:
    preco = qtd_kwh * 0.60
    print(f"O preço a ser pago é de R$ {preco:.2f}.")

elif (tipo_instalacao == "I") and qtd_kwh <= 5000:
    preco = qtd_kwh * 0.55
    print(f"O preço a ser pago é de R$ {preco:.2f}.")
elif (tipo_instalacao == "I") and qtd_kwh > 5000:
    preco = qtd_kwh * 0.60
    print(f"O preço a ser pago é de R$ {preco:.2f}.")

else:
    print("Algo deu errado.")