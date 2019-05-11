from EstacionamentoDoPy.modelo.patio import Patio


def criaPatio(numVagas):
    p = Patio(numVagas)
    return p


def addEntrada(patio, entrada):
    if patio.limitapatio(entrada) == -1:
        return "Pátio Lotado"
    else:
        return "Carro Adcionado com Sucesso"
