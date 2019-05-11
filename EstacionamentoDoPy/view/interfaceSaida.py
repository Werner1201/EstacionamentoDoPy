# Nessa interface é preciso:
# pegar a placa de qual veículo irá saír
# envia-lo para a funcao responsavel de controle para fazer a query e retornar o bilhete de entrada na lista
# e depois inserir no removerCar no controle inplementar uma remoção da lista na vaga.
# E a segunda parte assim como a entrada deve retornar o que foi removido e a vaga liberada
def quemsai(patio):
    correto = 1
    print(">#>" * 30)
    print(f"{'>#'*17} Remoção de Veículo {'>#'*17}")
    print(">#>" * 30)
    while correto == 1:
        # Aqui tem que implementar ou chamar a funcao de controle para pesquisar o nome que o cliente digitar
        # e Dar uma confirmação caso ele tenha escolhido errado.
        correto = int(input("Deseja remover outro veículo ?<S:1/N:0> "))

