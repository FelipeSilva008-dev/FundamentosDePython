#Receba ano de nascimento e ano atual. Calcule idade e semanas.

#Entrada
anoNascimento = int(input("Digite o ano em que você nasceu: "))
print("")
anoAtual = int(input("Digite o ano atual: "))

#Processamento
idade = anoAtual - anoNascimento
idadeEmSemanas = idade * 4 * 12

#Saida
print(f'a sua idade em anos é {idade}, e sua idade em semanas é {idadeEmSemanas}')