class Saida:
    def __init__(self, entrada, hrSaida):
        self.entrada = entrada
        self.hrSaida = hrSaida

    def geraPagamento(self):
        hrEntrada = self.entrada.dataEntrada
        totalhrs = self.hrSaida = hrEntrada
        totalReais = totalhrs * (50 % 24)
        return totalReais
