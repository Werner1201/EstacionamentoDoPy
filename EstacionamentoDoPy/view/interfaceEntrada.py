def visualizaentrada(entrada):
    hora = entrada.dataEntrada
    v = entrada.veiculo
    placa = v.placa
    nomev = v.veiNome
    print("Novo Veículo entrou: ")
    print(f"Data: {hora}")
    print(f"Nome do Veículo: {nomev}")
    print(f"Placa: {placa}")
    print(f"WIP Vaga: {'pesquisavaga()'}")
    print("E foi adcionado com sucesso")

