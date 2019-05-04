def escolha():
    choice = int(input("Digite sua Escolha: "))
    return choice

def menu():
    print(f"{30*'-='}")
    print(f"{10*'-='}EstacionamentoDoPy{11*'-='}")
    print(f"{30*'-='}")
    esc = True
    while esc == True:
        print("Opcoes:")
        print("1 - Adcionar Veiculo.")
        print("2 - Retirar Veiculo e Retornar Valor a ser pago.")
        print("3 - Sair")
        choice = escolha()
        if choice == 1:
            # Adciona Veiculo
            print("Adcionando Veiculo...")
        elif choice == 2:
            # Remove veiculo e da o Valor de Pagamento
            print("Removendo Veiculo e o Pagamento eh de R$ 50")
        else:
            # Simplesmente sai
            print("Saindo do Programa")
        res = int(input("Deseja continuar ?<S:1/N:0>"))
        if res == 1:
            esc = True
        else:
            esc = False

# pequeno teste
menu()

