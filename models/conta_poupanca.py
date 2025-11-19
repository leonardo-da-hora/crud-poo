from .conta import Conta

class ContaPoupança(Conta):
    def __init__(self, titular, saldo=0):
        super().__init__(titular, saldo)
        self.cofrinho = 0

    def guardar_no_cofrinho(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            self.cofrinho += valor

    def tirar_do_cofrinho(self, valor):
        if valor <= self.cofrinho:
            self.cofrinho -= valor
            self.saldo += valor

    def ro_dict(self):
        d = super().todict()
        d["cofrinho"] = self.cofrinho
        return d