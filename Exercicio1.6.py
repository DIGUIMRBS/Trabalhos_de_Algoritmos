nun1 = int(input("Digite o primeiro numero"))
nun2 = int(input("Digite o segundo numero"))
nun3 = int(input("Digite o terceiro numero"))

menor = nun1

if nun2 < menor:
    menor = nun2

if nun3 < menor:
    menor = nun3

print("O menor e",menor,)