#calculadora simples

n1 = float(input("Digite o primeiro número da operação: "))
n2 = float(input("Digite o segundo número da operação: "))

operacao = input("Digite uma das operações a seguir: +, -, *. / ")
if (operacao == "+"):
    print(f"Resultado: {n1 + n2}")

elif (operacao == "-"):
    print(f"Resultado: {n1 - n2}")

elif (operacao == "*"):
    print(f"Resultado: {n1 * n2}")

elif (operacao == "/"):
    print(f"Resultado: {n1 / n2}")


#no python, para chamar a operação "resultado" é necessário utilizar o f, onde ativa a f-string
# print(f"o resultado da sua soma é: {resultado}" )