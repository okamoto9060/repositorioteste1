import random

num1 = random.randint(1000, 9999)
listnum1 = list(map(int, str(num1)))
userGuess = int(input("Digite um número de 4 dígitos distintos: "))
listUserGuess = list(map(int, str(userGuess)))
RdRp = 0 #Right digit, Right position
RdWp = 0 #Right digit, Wrong position

while True:
    if len(listUserGuess) == 4:
        if listUserGuess != listnum1:
            for i in range(0, len(listnum1)):
                for listUserGuess[i] in listnum1:
                    if listUserGuess[i] == listnum1[i]:
                        RdRp += 1
                    else:
                        RdWp += 1
            print(f"Você tem {RdRp} dígito(s) certo(s) no lugar certo e {RdWp} dígito(s) certo(s) no lugar errado.")
            RdRp = 0
            RdWp = 0
            userGuess = int(input("Digite outro número de 4 dígitos distintos: "))
        else:
            print()
            break
    else:
        print("Número inválido.")