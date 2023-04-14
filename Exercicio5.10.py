altura = float(input("Informe sua altura em metros: "))
peso = float(input("Informe seu peso em kg: "))

imc = peso / (altura ** 2)

print("Seu IMC é:", round(imc, 2))

elif imc < 19.9:
    print("Seu IMC é: %.2f" %imc, "Você está abaixo do peso ideal")
elif imc < 24.9:
    print("Seu IMC é: %.2f" %imc, "Você está no peso ideal")
elif imc < 29.9:
    print("Seu IMC é: %.2F" %imc, "Você está no primeiro grau de obesidade")
elif imc <34.9:
    print("Seu IMC é: %.2f" %imc, "Você está no segundo grau de obesidade (severa)")
elif imc > 40:
    print("Seu IMC é: %.2f" %imc, "Você está no teceiro grau de obesidade (môrbida)")