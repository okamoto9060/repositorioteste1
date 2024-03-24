import string

num_input = int(input("Type an integer number (base 10): "))
num = num_input
list_aux = []
quotient = 1

# base 2 - 36 (10 algarisms + 26 letters)
for i in range(2, 36 + 1):
    while quotient != 0:
        quotient = num // i
        remainder = num % i
        if remainder >= 10:
            remainder = string.ascii_lowercase[remainder - 10]
        list_aux.insert(0, remainder)
        num = quotient
    num_output = "".join([str(i) for i in list_aux])
    print(f"Number {num_input} in base {i} = {num_output}")

    # reset the variables
    num = num_input
    list_aux = []
    quotient = 1
