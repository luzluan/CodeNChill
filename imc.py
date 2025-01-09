import re

print("Para calcularmos seu IMC, precisarei de algumas informações antes.\n")

def variavel_nome(nome):
    if re.fullmatch(r"^[\w'\-,.][^0-9_!¡?÷?¿/\\+=@#$%ˆ&*(){}|~<>;:[\]]{2,}$", nome):
        return True
    else:
        return False

condicao_nome = True

while condicao_nome:

    nome = input("Insira seu nome\n")

    if variavel_nome(nome):
        condicao_nome = False
    else:
        print("Digite apenas letras, não será aceito números ou caracteres especiais.")

def variavel_altura(altura):
    if re.fullmatch(r"\d+\.\d{2}", altura):
        return True
    else:
        return False

condicao_altura = True

while condicao_altura:

    altura = input("Insira sua altura, em metros\n")

    if variavel_altura(altura):
        condicao_altura = False
    else:
        print("Os dados da altura devem estar em metros, e não em centímeros. Ex: 1.70")

def variavel_peso(peso):
    if re.fullmatch(r"\d{1,3}\.\d{2}", peso):
        return True
    else:
        return False

condicao_peso = True

while condicao_peso:

    peso = input("Insira seu peso, em kilogramas\n")

    if variavel_peso(peso):
        condicao_peso = False
    else:
        print("O valor do peso deve obdecer o formato de duas casas decimais depois do ponto. Ex 75.93")

IMC = (float(peso)/float(altura) ** 2)

print(f"Certo, {nome}. Você tem {altura}m de altura e pesa {peso}kg.\nO valor do seu IMC é: {IMC:.2f} ")

if IMC < 18.5:
    print("Magreza")
elif 18.5 <= IMC >= 24.9:
    print("Saudável")
elif 25.0 <= IMC >= 29.9:
    print("Sobrepeso - Obesidade Grau 1")