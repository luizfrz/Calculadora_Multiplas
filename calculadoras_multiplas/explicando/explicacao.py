# SISTEMA DE CALCULADORA, ARQUIVO FEITO PARA EXPLICAÇÃO DO CODIGO

"""
Primeira calculadora, juros simples
implementei uma variavel chamada "bem_vindo", serve forma se de fato queira acessar o sistema de calculadora juros simples
foi usado uma condição abaixo
se a resposta for sim, apresentar uma mensagem seguinte "seja bem vindo..."
se a resposta for não, apresentar uma mensagem seguinte "poxa, mas te vejo na proxima"
quando selecionado a opçao "nao" coloquei uma funçao chamada exit que é sair no pt-br

agora após essa pequena verificação, aparece as opções
capital vem junto um input para digitar, ele é um float um numero não inteiro
abaixo existe uma variavel chamda ex com uma mensagem ensinado, logo quando for selecionado a opção será apresentada
pressionado o valor, agora teremos que achar taxa.
taxa é um float, de fato numero não inteiro e sim há quebrado como é dito informal
como havia dito acima, ex (variavel que apresenta como deve ser escrito)
e após tempo (equivalente a meses, usado int representando inteiro)

teremos uma multiplicação dos valores primeiro capital e depois a taxa
após isso, com tempo com resultado da capital e taxa
apresentado abaixo como é feito 
J = c * i * t
j = C * i
 J * T
assim resultado abaixo

implementei uma condição caso queira calcular o montante aparecer a condição "deseja calcular"
caso a resposta seja sim, apresenta valores e assim calcula

há outras variaveis tambem com finalização, mas nada muito complicado
semelhante o primeiro
"""
bem_vindo = str(input("bem vindo a calculadora juros simples, deseja acessar:SIM/NAO"))
if bem_vindo.lower() == "sim":
    print("seja bem vindo, acesse nossa calculadora")
else: 
    print("poxa, mas te vejo na proxima")
    exit()

capital = float(input("Digite aqui seu capital: "))
ex = "digite desse formato na taxa: 0.04 - 4% _ 10 - 0.10"
print(ex)
taxa = float(input("Digite seu taxa: "))
tempo = int(input("Digite seu tempo: "))
resultado_capital_taxa = capital * taxa
resultado_tempo = resultado_capital_taxa * tempo
print(resultado_tempo)
calcular_montante = input("Deseja calcular montante? S ou N")

mensagem_sim = "otimo, vamos calcular..."
mensagem_nao = "obrigado por utilizar calculadora juros simples"
if calcular_montante.lower() == "S":
    print(mensagem_sim)
else: 
    print(mensagem_nao)
    exit()
calculo_montante = capital + resultado_tempo
print("seu montante:", calculo_montante)    