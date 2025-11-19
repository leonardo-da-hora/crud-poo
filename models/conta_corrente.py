from .conta import Conta

class ContaCorrente(Conta):
    def __init__(self, titular, saldo=0, limite=500):
        super().__init__(titular, saldo)
        self.limite = limite

    def sacar(self, valor):
        if valor <= self.saldo + self.limite:
            self.saldo -= valor
        else:
            print("Saldo + limite insuficientes.")

    def to_dict(self):
        d = super().to_dict()
        d["limite"] = self.limite
        return d
