#receba a idade em anos e imprima em meses, dias, horas e minutos.

#Entrada
idade = int(input("Digite a idade: ")) #pega o texto e converte para número inteiro

#Processamento
idadeEmMeses = idade * 12

idadeEmDias = idade * 365

idadeEmHoras = idadeEmDias * 24

idadeEmMinutos = idadeEmHoras * 60 

#Saida
print(f"idade em anos: {idade}")
print("")
print(f"idade em meses: {idadeEmMeses}")
print("")
print(f"idade em dias: {idadeEmDias}")
print("")
print(f"idade em horas: {idadeEmHoras}")
print("")
print(f"idade em minutos: {idadeEmMinutos}")