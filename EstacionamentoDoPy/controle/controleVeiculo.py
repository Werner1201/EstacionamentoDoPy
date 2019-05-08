from EstacionamentoDoPy.modelo.veiculo import Veiculo

def addveiculo(placa, dono, nmvei):
    car = Veiculo(placa, dono, nmvei)
    return car