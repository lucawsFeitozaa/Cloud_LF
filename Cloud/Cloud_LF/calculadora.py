def soma(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    if y == 0:
        return "Erro! Divisão por zero."
    return x / y

def calculadora():
    print("Selecione a operação:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

    escolha = input("Digite o número da operação desejada: ")

    if escolha in ('1', '2', '3', '4'):
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if escolha == '1':
            print(f"Resultado: {soma(num1, num2)}")
        elif escolha == '2':
            print(f"Resultado: {subtracao(num1, num2)}")
        elif escolha == '3':
            print(f"Resultado: {multiplicacao(num1, num2)}")
        elif escolha == '4':
            print(f"Resultado: {divisao(num1, num2)}")
    else:
        print("Opção inválida!")

calculadora()
