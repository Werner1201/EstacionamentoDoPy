from EstacionamentoDoPy.modelo.Entrada import Entrada
import datetime;


def addEntrada(veiculo):
    agora = datetime.datetime.now()
    hora = agora.strftime("%H")
    min = agora.strftime("%M")
    seg = agora.strftime("%S")
    dia = agora.strftime("%d")
    mes = agora.strftime("%m")
    ano = agora.strftime("%Y")
    entra = Entrada(f"{hora}:{min}:{seg}.{dia}/{mes}/{ano}", veiculo)
    return entra
