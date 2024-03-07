import matplotlib.pyplot as plt
import numpy as np
import math

calculator = """
 _________________
|  _____________  |
| | CALCULADORA | |
| |_____________| |
| |             | |
| | x² √  CE  C | |
| | 7  8  9   / | |
| | 4  5  6   * | |
| | 1  2  3   - | |
| | 0  .  =   + | |
| |_____________| |
|_________________|
    """

print(calculator)

# Definindo funções de operações aritméticas.
def soma(x, y): return x + y
def subtracao(x, y): return x - y
def multiplicacao(x, y): return x * y
def divisao(x, y): return x / y

# Definindo funções de funções matemáticas
def linear(x, a, b): return a * x + b
def quadratica(x, a, b, c): return (a * (x ** 2)) + (b * x) + c
def exponencial(x, a): return a ** x
def fatorial(x):
    resultado = 1
    for i in range(1, x + 1):
        resultado *= i
    return resultado
# def calcular_raizes(a, b, c):
    
def plot_linear(a, b):
    axisX = np.linspace(-math.floor(a)*math.floor(b), math.ceil(a)*math.ceil(b), (math.ceil(a)*math.ceil(b))**(math.ceil(a)*math.ceil(b)))
    axisY = linear(axisX, a, b)
    plt.plot(axisX, axisY)
    plt.title("Gráfico da função linear.")
    plt.xlabel("Eixo x das abscissas.")
    plt.ylabel("Eixo y das ordenadas.")
    plt.grid(True)
    plt.show()

def plot_quadratica(a, b, c):
    axisX = np.linspace(-math.floor(a)*math.floor(b)+math.floor(c), math.ceil(a)*math.ceil(b)+math.ceil(c), (math.ceil(a)*math.ceil(b)+math.ceil(c))**(math.ceil(a)*math.ceil(b)+math.ceil(c)))
    axisY = quadratica(axisX, a, b, c)
    plt.plot(axisX, axisY)
    plt.title("Gráfico da função quadrática.")
    plt.xlabel("Eixo x das abscissas.")
    plt.ylabel("Eixo y das ordenadas.")
    plt.grid(True)
    plt.show()
    
def plot_exponencial(a):
    axisX = np.linspace(-math.floor(a), math.ceil(a), math.ceil(a)**math.ceil(a))
    axisY = exponencial(axisX, a)
    plt.plot(axisX, axisY)
    plt.title("Gráfico da função exponencial.")
    plt.xlabel("Eixo x das abscissas.")
    plt.ylabel("Eixo y das ordenadas.")
    plt.grid(True)
    plt.show()

def plot_fatorial(a):
    axisX = np.linspace(0, a, a - 1)
    axisY = (axisX, a)
    plt.plot(axisX, axisY)
    plt.title("Gráfico da função fatorial.")
    plt.xlabel("Eixo x das abscissas.")
    plt.ylabel("Eixo y das ordenadas.")
    plt.grid(True)
    plt.show()

# Declarando variáveis dos menus do terminal.
calculator_init = """
    MENU INICIAL
    Escolha uma opção      
                                
    1 - Operações aritméticas
    2 - Funções matemáticas
    3 - Sair
    """

calculator_basic = """
    OPERAÇÕES ARITMÉTICAS
    Escolha uma opção      
                                
    1 - Soma
    2 - Subtração
    3 - Multiplicação
    4 - Divisão
    5 - Voltar
    """

calculator_func = """
    FUNÇÕES MATEMÁTICAS
    Escolha uma opção      
                                
    1 - Linear
    2 - Quadrática
    3 - Exponencial
    4 - Fatorial
    5 - Voltar
    """


def init():
    print(calculator_init)

    escolha = int(input("\nEscolha uma opção para iniciar: "))

    while escolha != 3:
        if escolha == 1:
            print(calculator_basic)

            categoria = int(input("\nEscolha uma categoria: "))
            while categoria != 5:

                if categoria == 1:
                    print("\nVocê escolheu SOMA")
                    num1 = float(input("Digite o primeiro número: "))
                    num2 = float(input("Digite o segundo número: "))
                    num3 = soma(num1, num2)
                    print(f"A soma dos números {num1} e {num2} é: {num3}")
                    break

                elif categoria == 2:
                    print("\nVocê escolheu SUBTRAÇÃO")
                    num1 = float(input("Digite o minuendo: "))
                    num2 = float(input("Digite o subtraendo: "))
                    num3 = subtracao(num1, num2)
                    print(f"A diferença dos números {num1} e {num2} é: {num3}")
                    break

                elif categoria == 3:
                    print("\nVocê escolheu MULTIPLICAÇÃO")
                    num1 = float(input("Digite o primeiro número: "))
                    num2 = float(input("Digite o segundo número: "))
                    num3 = multiplicacao(num1, num2)
                    print(f"A diferença dos números {num1} e {num2} é: {num3}")
                    break

                elif categoria == 4:
                    print("\nVocê escolheu DIVISÃO")
                    num1 = float(input("Digite o numerador: "))
                    num2 = float(input("Digite o denominador: "))
                    num3 = divisao(num1, num2)
                    print(f"A diferença dos números {num1} e {num2} é: {num3}")
                    break

                elif categoria == 5:
                    print(calculator_basic)

        elif escolha == 2:
            print(calculator_func)

            funcao = int(input("\nEscolha uma função: "))

            while funcao != 5:

                if funcao == 1:
                    print("\nVocê escolheu a função LINEAR\nf(x) = ax + b")
                    num1 = float(input("Digite o coeficiente da variável: "))
                    num2 = float(input("Digite o termo independente: "))
                    for i in range(100):
                        linear(i, num1, num2)
                    plot_linear(num1, num2)
                    break

                elif funcao == 2:
                    print("\nVocê escolheu a função QUADRÁTICA\nf(x) = ax² + bx + c")
                    num1 = float(input("Digite o primeiro coeficiente: "))
                    num2 = float(input("Digite o segundo coeficiente: "))
                    num3 = float(input("Digite o termo independente: "))
                    for i in range(100):
                        quadratica(i, num1, num2, num3)
                    plot_quadratica(num1, num2, num3)
                    break

                elif funcao == 3:
                    print("\nVocê escolheu a função EXPONENCIAL\nf(x) = aˣ")
                    num1 = float(input("Digite a base do expoente: "))
                    for i in range(100):
                        exponencial(i, num1)
                    plot_exponencial(num1)
                    break

                elif funcao == 4:
                    print("\nVocê escolheu a função FATORIAL\nf(x) = x!")
                    num1 = math.floor(float(input("Digite um número.\n(OBS: Números não-inteiros serão arredondados para baixo.)\n")))
                    fatorial(num1)
                    plot_fatorial(num1)
                    break

                elif funcao == 5:
                    print(calculator_func)

        elif escolha == 3:
            break
        print(calculator_init)

        escolha = int(input("\nEscolha uma opção para iniciar: "))

init()