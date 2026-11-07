#Receba nome, cargo e salário e acrescente 10%.

nome = input("digite seu nome: ")
cargo = input("digite seu cargo: ")
salario = float(input("digite seu salário: "))

acrescimo = salario + (salario*0.1)

print(f"O seu salário atual é de: {acrescimo}")