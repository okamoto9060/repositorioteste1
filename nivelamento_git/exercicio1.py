saldo = 0

while True:
    print("\n1. Depósito")
    print("2. Saque")
    print("3. Extrato")
    print("4. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        valor_deposito = float(input("Digite o valor do depósito: "))
        if valor_deposito > 0:
            saldo += valor_deposito
            print(f'Depósito de R${valor_deposito:.2f} realizado com sucesso.')
        else:
            print('O valor do depósito deve ser maior que zero.')

    elif opcao == '2':
        valor_saque = float(input("Digite o valor do saque: "))
        if valor_saque > 0:
            if valor_saque > saldo:
                print("O valor do saque não pode ser maior que o seu saldo.")
            elif valor_saque <= saldo:
                saldo -= valor_saque
                print(f"Saque de R${valor_saque} realizado com sucesso.")
        else:
            print('O valor do saque deve ser maior que zero.')
        
    elif opcao == '3':
        print(f'\nExtrato bancário:\n')
        print(f'Saldo atual: R${saldo:.2f}\n')

    elif opcao == '4':
        print("Saindo...")
        break

    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
