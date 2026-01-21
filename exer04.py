#Calculo de IMC
#Formula: IMC = peso /(altura x altura)

nome = input("Digite seu nome: ")
peso = float(input("Qual o seu peso atual: "))
altura = float(input("Qual a sua altura atual: "))

calculo = peso / (altura * altura)

if calculo <= 18.5:
    print(f"Você se enquadra no perfil de Magraza! Seu IMC é de: {calculo:.2f}")
elif calculo >= 18.5 and calculo <= 24.9:
    print(f"Você se enquadra no perfil de Normal! Seu IMC é de: {calculo:.2f}")
elif calculo >= 24.9 and calculo <= 30:
    print(f"Você se enquadra no perfil de Sobrepeso! Seu IMC é de: {calculo:.2f}")
elif calculo > 30:
    print(f"Você se enquadra no perfil de Obsidade! Seu IMC é de: {calculo:.2f}")
else:
    print("Verifique os dados digitados se estão corretos.")
    