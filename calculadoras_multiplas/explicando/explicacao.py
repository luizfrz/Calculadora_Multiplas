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

# CALCULADORA PADRAO

"""criamos duas variaveis com input escrito com valores numero digite que pode ser primeiro input
e numero digite 2 que é segundo input colocado para ser inserido valor, nesse caso crio 4 variaveis com valores que for digitado
mas como? exemplo, eu faço o calculo de cada um junto a variavel que guarda input 
repito processo nas 4
após isso, crio um print (imprimir) ensinando metodo de chamar uma variavel guardado valor
nesse caso, faço uma variavel input que possa atribuir o qual valor será apresentado
faremos uma condição abaixo utilizando if e elif
caso vá digita +, primeiro dois valores acima nas primeiras variaveis está sendo guardado, nesse caso determinado valor será atribuido de qual eu digitar
seja + vai somar
seja * vai multiplicar
e assim por diante

após uso de condições, utilizo else (se nao) caso nenhum valor acima seja digitado, apresentar então assim seguinte mensagem
(não foi encontrado, tente novamente mais tarde!)
e assim
usei exit() para sair de vez e fazer nova tentativa

"""
numero_digite = int(input("digite aqui seu primeiro numero"))
numero_digite2 = int(input("digite aqui seu primeiro numero"))

Mult = numero_digite * numero_digite2
Soma = numero_digite + numero_digite2
Div = numero_digite / numero_digite2 
Sub = numero_digite - numero_digite2
print("ESCOLHA PARA REALIZAR A SOMA + / * -")
escolha = int(input("escolha para realizar: "))
if escolha == "+":
    print(Soma)
elif escolha == "-":
    print(Sub)
elif escolha == "/":
    print(Div)
elif escolha == "*":
    print(Mult)
else:
    print("não foi encontrado, tente novamente mais tarde!")
    exit()

# CALCULAR ENERGIA CONSUMO
"""

Essa calculadora faz o cálculo do consumo da sua energia, não há implementação de tarifas. Nesse caso, esqueci de implementar.

Crio um print para mostrar uma mensagem de "Bem-vindo ao sistema para calcular etc...". Após isso, abaixo do print, existe uma variável nomeada como "deseja_acessar". Essa variável tem como objetivo ser usada em uma condição para acesso à calculadora, de forma clara e objetiva. Caso a resposta seja 'sim', apresenta uma mensagem; caso contrário, apresenta um print de else.

Depois de seguir esses fatores, a criação da variável "mensagem_ex" é apresentada para guiar o usuário a utilizar de forma correta o sistema da calculadora.

Então, começamos de fato a criação da seguinte forma:
p representa a potência, t o tempo, e limite o tempo limite. Na variável chamada potência, deve ser colocado o valor em watts (W) do aparelho. Após isso, é informado o tempo em que o aparelho ficou ligado na tomada.

Se existir um tempo limite, faremos uma variável chamada "conversao" para converter a energia referente a tempo / limite. Após isso, ajustamos o valor da conversão, utilizando também o tempo e a potência. Multiplicamos a conversão pelo valor da potência.

Por fim, criamos uma variável chamada "consumo_de_energia" para armazenar o valor total do consumo. Um print apresenta a mensagem com o valor convertido.

"""
print("seja bem vindo! sistema para calcular consumo da sua energia")
deseja_acessar = str(input("Deseja acessar o sistema? SIM / NÃO"))
if deseja_acessar.lower () == "sim":
    print("vamos descobrir quanto voce fez de consumo!")
else: 
    print("opa, voce pode voltar quanto quiser!")
    exit()

mensagem_ex = "potencia deve ser digitada sempre primeiro numero após virgula"
mensagem_ex2 = "dessa maneira 5000 = 5,0"
potencia = float(input("digite aqui potencia de energia (w)"))
tempo = int(input("digite aqui seu tempo"))
tempo_li = 60
conversao = tempo / tempo_li
calculo_energa = conversao * potencia
mensagem_abaixo = "aqui esta seu consumo de energia"
print(mensagem_abaixo, calculo_energa)

## CALCULADORA DE MEDIA
media_msg = "seja bem vindo. vamos calcular sua media"
print(media_msg)
b1 = int(input("BIMESTRE 1: "))
b2 = int(input("BIMESTRE 2: "))
b3 = int(input("BIMESTRE 3: "))
b4 = int(input("BIMESTRE 4: "))
calculando = b1 + b2 + b3 + b4
dividir = 4 
dividir_media = calculando / dividir
print("sua média é", dividir_media)
if dividir_media > 7:
    print("foi aprovado")
elif dividir_media  < 7:
    print("reprovado")
elif dividir_media == 10:
    print("aprovado, muito bem voce é 10!")
else:
    print("infelizmente, tente novamente")
 
