# Calculadora de energia
""" 
    FORMULA USADA CODIGO
     E = POT . AT
     SIGLA
     E = ENERGIA CONSUMIDA
     POT = POTENCIA
     AT = INTERVALO TEMPO USO

"""
print("seja bem vindo! sistema para calcular consumo da sua energia")
deseja_acessar = str(input("Deseja acessar o sistema? SIM / NÃO"))
<<<<<<< HEAD
if deseja_acessar.lower () == "sim":
=======
if deseja_acessar.lower () == "SIM":
>>>>>>> a790ef84ec81b66b99d14b54bc1ae5391a509ca5
    print("vamos descobrir quanto voce fez de consumo!")
else: 
    print("opa, voce pode voltar quanto quiser!")
    exit()

<<<<<<< HEAD
mensagem_ex = "potencia deve ser digitada sempre primeiro numero após virgula"
print(mensagem_ex)
print(mensagem_ex2)
mensagem_ex2 = "dessa maneira 5000 = 5,0"
potencia = float(input("digite aqui potencia de energia (w)"))
tempo = int(input("digite aqui seu tempo"))
tempo_li = 60
conversao = tempo / tempo_li
calculo_energa = conversao * potencia
mensagem_abaixo = "aqui esta seu consumo de energia"
print(mensagem_abaixo, calculo_energa)



=======
mensagem_ex = "potencia pode ser utilizada dessa maneira 5000w = 5,0 mas como preferir, voce pode digitar"
POT = input("digite aqui potencia de energia (w)")
mensagem_tempo = "tempo gasto deve ser utilizado dessa maneira 15 = 0,25 h para realizar a hora"
TEMPO = int(input("digite tempo gasto"))
>>>>>>> a790ef84ec81b66b99d14b54bc1ae5391a509ca5
