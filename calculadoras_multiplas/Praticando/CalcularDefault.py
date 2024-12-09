# CALCULADORA PADRAO 
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
