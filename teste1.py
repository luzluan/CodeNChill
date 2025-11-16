#1

user_name = input("Olá!\nQual é o seu nome?\n");

salario_user = input(f"{user_name}, para calcularmos o valor da sua hora, primeiro preciso saber o valor do seu salário. Digite o valor:\n" );

dias_trabalhados = input("Agora, preciso saber seus dias trabalhos por mês.\n");

calculo = float(f"{float(salario_user)/float(dias_trabalhados)}")

print(f"{user_name}, o valor da sua hora de trabalho é de {calculo:.2f} reais");