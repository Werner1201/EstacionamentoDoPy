class Saida:
    def __init__(self, entrada, hrSaida):
        self.entrada = entrada
        self.hrSaida = hrSaida

    def geraPagamento(self):
        hrEntrada = self.entrada.dataEntrada
        totalhrs = self.hrSaida - hrEntrada
        totalReais = 0
        # Modificando como o pagamento funcionando para um metodo de diaria
        if totalhrs > 24:
            totalReais = 50 + 50
        elif totalhrs <= 24:
            totalReais = 50

        return totalReais
