class Patio:
    # Adcionar no patio uma estrutura de dados (lista pois nao ha dependencia de entrada e saida) do tipo Vetor para
    # organizar melhor a armazenagem as informacoes e simular as vagas preenchidas ou nao sem necessidade dessa outra
    # Classe Vaga
    def __init__(self, numvagas):
        self.numvagas = numvagas
class Vaga:
    def __init__(self, idvaga, patio):
        self.patio = patio
        if idvaga < patio.numvagas:
            self.idvaga = idvaga
        else:
            self.idvaga = None