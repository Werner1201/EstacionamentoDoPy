from EstacionamentoDoPy.modelo.patio import Patio
from EstacionamentoDoPy.modelo.patio import Vaga

def criaPatio(numVagas):
    p = Patio(numVagas)
    return p

def addVaga(idvaga, patio):
    v = Vaga(idvaga, patio)
    if v.idvaga == None:
        return None