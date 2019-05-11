class Patio:
    # Adcionar no patio uma estrutura de dados (lista pois nao ha dependencia de entrada e saida) do tipo Vetor para
    # organizar melhor a armazenagem as informacoes e simular as vagas preenchidas ou nao sem necessidade dessa outra
    # Classe Vaga
    def __init__(self, numvagas):
        self.numvagas = numvagas
        self.vagas = []

    def percorrepatio(self, comando):
        for x in self.vagas:
            eval(comando)


    def limitapatio(self, entrada):
        if self.vagas.__len__() >= self.numvagas:
            return -1
        else:
            return self.vagas.append(entrada)
