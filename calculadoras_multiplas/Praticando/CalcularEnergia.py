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

mensagem_ex = "potencia pode ser utilizada dessa maneira 5000w = 5,0 mas como preferir, voce pode digitar"
POT = input("digite aqui potencia de energia (w)")
mensagem_tempo = "tempo gasto deve ser utilizado dessa maneira 15 = 0,25 h para realizar a hora"
TEMPO = int(input("digite tempo gasto"))
