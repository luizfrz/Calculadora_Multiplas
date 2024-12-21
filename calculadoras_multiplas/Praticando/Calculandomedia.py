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
