import random, time, sys, math
from tqdm import tqdm

def karatsuba(x, y):
    if x < 10 or y < 10: return x * y

    xlist = list(map(int, str(x)))
    ylist = list(map(int, str(y)))
    maxdigit = max(len(xlist), len(ylist))

    # Logaritmo na base 2 da quantidade de dígitos.
    log2_lenx = math.log(len(xlist), 2)
    log2_leny = math.log(len(ylist), 2)
    log2_max = math.log(maxdigit, 2)

    # Adicionar zeros na lista até ela ter uma quantidade de dígitos igual a uma potência de 2
    if log2_lenx != math.ceil(log2_max):                           # log₂(dígitos de x) ≠ ⌈log₂(dígitos do maior número)⌉
        for _ in range(2**(math.ceil(log2_max))-len(xlist)):    # 2^(⌈log₂(dígitos do maior número)⌉) - dígitos de x
            xlist.insert(0, 0)

    if log2_leny != math.ceil(log2_max):
        for _ in range(2**(math.ceil(log2_max))-len(ylist)):
            ylist.insert(0, 0)

    half = len(xlist)//2

    # Dividir a lista em 2 listas menores de n/2 elementos
    xlistleft = xlist[:half]
    xlistright = xlist[half:]
    xleft = int("".join(map(str, xlistleft)))
    xright = int("".join(map(str, xlistright)))

    ylistleft = ylist[:half]
    ylistright = ylist[half:]
    yleft = int("".join(map(str, ylistleft)))
    yright = int("".join(map(str, ylistright)))

    # Chamar recursivamente a função Karatsuba
    z1 = karatsuba(xleft, yleft)
    z2 = karatsuba((xleft + xright), (yleft + yright))
    z3 = karatsuba(xright, yright)

    # Fórmula de Karatsuba (base 10)
    return (z1 * 10**(2*half)) + ((z2 - z3 - z1) * (10**half)) + z3

numDigit = int(input("Digite a quantidade máxima de dígitos dos números aleatórios: "))
if numDigit <= 0:
    print("O número de dígitos deve ser maior que zero.")
    exit()
elif numDigit >= 4300:
    sys.set_int_max_str_digits(numDigit+1)

iteration = int(input("Digite a quantidade de multiplicações: "))
if iteration <= 0:
    print("A quantidade de multiplicações deve ser maior que zero.")
    exit()
numMax = (10 ** numDigit) - 1 # (10ⁿ)-1 (99, 999, 9999 etc.)

# Contadores
listDigitMedio = []
timeTotal = 0
difDoDigitMax = 0

# Algoritmo de multiplicação longa escolar
for i in tqdm(range(iteration)):
    num1 = random.randint(1, numMax)
    num2 = random.randint(1, numMax)
    time1 = time.perf_counter()
    numMult = num1 * num2
    time2 = time.perf_counter()
    timeElapsed = time2 - time1
    timeTotal += timeElapsed
    digitNum1 = len([int(i) for i in str(num1)])
    digitNum2 = len([int(i) for i in str(num2)])
    listDigitMedio.append((digitNum1+digitNum2)/2) # Conta a quantidade de dígitos das vars num1 e num2, faz a média e adiciona à lista.
    if digitNum1 < numDigit:
        difDoDigitMax += 1
    if digitNum2 < numDigit:
        difDoDigitMax += 1

print(f"""
      
      ________________________________________________________________________________________________________________________________________________________
        Algoritmo:                                                                                  ｜Multiplicação longa escolar
        Tempo total de operação:                                                                    ｜{timeTotal} s           
        Tempo médio de operação:                                                                    ｜{timeTotal/iteration} s  
        Quantidade máxima de dígitos dos números aleatórios:                                        ｜{numDigit}                
        Quantidade média de dígitos dos números aleatórios:                                         ｜{sum(listDigitMedio)/len(listDigitMedio)}
        Vezes que a quantidade de dígitos do número é diferente da quantidade máxima de dígitos:    ｜{difDoDigitMax}/{2*iteration}
        Quantidade de multiplicações:                                                               ｜{iteration}             
      ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
    """)

# Resetar os contadores
timeTotal = 0
difDoDigitMax = 0
listDigitMedio = []

# Algoritmo de Karatsuba
for i in tqdm(range(iteration)):
    num1 = random.randint(1, numMax)
    num2 = random.randint(1, numMax)
    time1 = time.perf_counter()
    numMult = karatsuba(num1, num2)
    time2 = time.perf_counter()
    timeElapsed = time2 - time1
    timeTotal += timeElapsed
    digitNum1 = len([int(i) for i in str(num1)])
    digitNum2 = len([int(i) for i in str(num2)])
    listDigitMedio.append((digitNum1+digitNum2)/2) # Conta a quantidade de dígitos das vars num1 e num2, faz a média e adiciona à lista.
    if digitNum1 < numDigit:
        difDoDigitMax += 1
    if digitNum2 < numDigit:
        difDoDigitMax += 1

print(f"""
      
      ________________________________________________________________________________________________________________________________________________________
        Algoritmo:                                                                                  ｜Karatsuba
        Tempo total de operação:                                                                    ｜{timeTotal} s           
        Tempo médio de operação:                                                                    ｜{timeTotal/iteration} s  
        Quantidade máxima de dígitos dos números aleatórios:                                        ｜{numDigit}                
        Quantidade média de dígitos dos números aleatórios:                                         ｜{sum(listDigitMedio)/len(listDigitMedio)}
        Vezes que a quantidade de dígitos do número é diferente da quantidade máxima de dígitos:    ｜{difDoDigitMax}/{2*iteration}
        Quantidade de multiplicações:                                                               ｜{iteration}             
      ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
    """)