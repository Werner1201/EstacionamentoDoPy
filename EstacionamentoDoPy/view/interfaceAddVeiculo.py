from EstacionamentoDoPy.controle.controleVeiculo import addveiculo


def cadveiculo():
    print(">#"*30)
    print(f"{'>#'*10} Cadastro de Veículos {'>#'*9}")
    print(">#" * 30)
    correto = 0
    while correto == 0:
        nomed = input("Qual o nome do Proprietário: ")
        placa = input("Qual a placa do Veículo: ")
        nomec = input("Qual o nome do Veículo: ")
        print("Revisão dos Dados: ")
        print(f"Nome do Proprietário: {nomed}")
        print(f"Placa do Veículo: {placa}")
        print(f"Nome do Veículo: {nomec}")
        correto = int(input("Estão Corretos os dados ?<S:1/N:0>"))
    return addveiculo(placa, nomed, nomec)
