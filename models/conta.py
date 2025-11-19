class Conta:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente.")

    def to_dict(self):
        return {
            "tipo": self.__class__.__name__,
            "titular": self.titular,
            "saldo": self.saldo
        }
    
    def extrato(self):
        print(f"{self.titular}: R${self.saldo}")
