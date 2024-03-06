import math

# Definindo funções de operações matemáticas.
def somar(a:float, b: float) -> float: return a + b
def subtrair(a: float, b: float) -> float: return a - b
def multiplicar(a: float, b: float) -> float: return a * b
def dividir(a: float, b: float) -> float: return a / b
def exponenciar(a: float, b: float) -> float: return a ** b
def raizquadrada(a: float) -> float: return a ** (1/2)
def fatorial(a: float) -> int:
    if math.floor(a) != a: print(f"O menor inteiro mais próximo de {a} é {math.floor(a)}")
    a = math.floor(a)
    fatorial = 1
    for i in range(1, a+1): 
        fatorial *= i
    return fatorial

# Declarando variáveis
continuar = "Y"
num = ""
mensagem ="""
======== Calculadora ========
        1. Soma
        2. Subtração
        3. Multiplicação
        4. Divisão
        5. Exponenciação
        6. Raiz quadrada
        7. Fatorial
        8. Sair
"""

# Calculadora
while continuar in ["Y", "y"]:
    
    print(mensagem)
    print(f"        (Número atual: {num})\n=============================\n")
    
    UserInput = int(input("Escolha a opção: "))
    
    # Opção 8 para sair.
    # Outra opção além de 1 até 8 é desconsiderado.
    if UserInput == 8:
        print("Você parou a calculadora.")
        break
    elif UserInput not in [i for i in range(1, 9)]:
        print("Opção inválida.")
        continue
    
    # Condições para pedir um ou dois inputs. 
    # As 5 primeiras operações são binárias e as 2 últimas são unárias. 
    # Após a primeira operação, o resultado é salvo na var num1.
    if UserInput < 6 and num == "":
        num1 = float(input(f"Digite o primeiro número: "))
        num2 = float(input(f"Digite o segundo número: "))
    elif UserInput >= 6 and num == "":
        num1 = float(input(f"Digite um número: "))
    elif UserInput < 6 and num != "":
        num1 = num
        num2 = float(input(f"Digite outro número: "))
    elif UserInput >= 6 and num != "":
        num1 = num
        
    # Casos para cada opção disponível na interface.
    match UserInput:
        case 1:
            num = somar(num1, num2)
            print(f"{num1} + {num2} = {num}")
        case 2:
            num = subtrair(num1, num2)
            print(f"{num1} - {num2} = {num}")
        case 3:
            num = multiplicar(num1, num2)
            print(f"{num1} × {num2} = {num}") 
        case 4:
            num = dividir(num1, num2)
            print(f"{num1} ÷ {num2} = {num}")
        case 5:
            num = exponenciar(num1, num2)
            print(f"{num1} ^ {num2} = {num}")
        case 6:
            num = raizquadrada(num1)
            print(f"Raiz quadrada de {num1} = {num}")
        case 7:
            num = fatorial(num1)
            print(f"O fatorial de {math.floor(num1)} = {num}")
        
    # Continuar ou sair da calculadora.
    continuar = input(f"Continuar? (Y/N) = ")
    if continuar in ["Y", "y"]:
        continue
    else:
        print("Você parou a calculadora.")
        break