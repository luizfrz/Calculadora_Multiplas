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
if deseja_acessar.lower () == "SIM":
    print("vamos descobrir quanto voce fez de consumo!")
else: 
    print("opa, voce pode voltar quanto quiser!")
    exit()

mensagem_ex = "potencia deve ser digitada sempre primeiro numero após virgula"
mensagem_ex2 = "dessa maneira 5000 = 5,0"
potencia = float(input("digite aqui potencia de energia (w)"))
tempo = input("digite aqui seu tempo")
tempo_li = 60
conversao = tempo / tempo_li

