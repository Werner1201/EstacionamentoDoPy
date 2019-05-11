from EstacionamentoDoPy.modelo.Saida import Saida
import datetime

def removerCar(bilheteEntrada):
    agora = datetime.datetime.now()
    hora = agora.strftime("%H")
    minu = agora.strftime("%M")
    seg = agora.strftime("%S")
    dia = agora.strftime("%d")
    mes = agora.strftime("%m")
    ano = agora.strftime("%Y")
    hrsaida = f"{hora}:{minu}:{seg}.{dia}/{mes}/{ano}"
    s = Saida(bilheteEntrada, hrsaida)
    # aqui chamarei uma função para remover da lista o veic que será implementada em pátio para
    # armazenar quais espaços vagos existem no pátio.
    return s.geraPagamento()
