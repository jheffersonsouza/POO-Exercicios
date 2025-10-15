# 10/10/25 - Atividade – Estruturas de Repetição em Python
# Tema: Simulador de Caixa Eletrônico
saldo = 1000
historico_transacoes = []

while True:
    print("""
    === MENU DO CAIXA ELETRÔNICO ===
1 - Depositar
2 - Sacar
3 - Ver saldo
4 - Ver histórico de transações
5 - Sair""")
    opcao = str(input("Escolha a opção:"))
    if opcao == "1":
        while True:
            deposito = float(input("Digite o valor a ser depositado:"))
            if deposito <= 0:
                print('Impossível depositar valores menores que 1 real.')
                continue
            saldo += deposito
            historico_transacoes.append(f'Deposito de R${deposito:.2f}')
            print(f'Deposito de R${deposito:.2f} realizado com sucesso!')
            break
    elif opcao == "2":
        while True:
            saque = float(input("Digite o valor a ser sacado:"))
            if saque > saldo:
                print('Saldo insuficiente.')
                continue
            saldo -= saque
            historico_transacoes.append(f'Saque de R${saque:.2f}')
            print(f'Saque de R${saque:.2f} realizado com sucesso!')
            break
    elif opcao == "3":
        print(f'Seu saldo atual é de R${saldo:.2f}')
    elif opcao == "4":
        print('-'*10,"Histórico de transações",'-'*10,)
        for i, j in enumerate(historico_transacoes):
            print(f'{i+1}. {j}')
        pass
    elif opcao == "5":
        print("Saindo do sistema...")
        break
    else:
        print('Opção inválida.')