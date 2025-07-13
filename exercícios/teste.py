from datetime import datetime
from enum import Enum

class Pagamento(Enum):
    EmAberto = 1
    PagoParcial = 2
    Pago = 3

class Boleto:
    def __init__(self, cod, emissao, venc, valor):
        self.__codBarras = cod
        self.__dataEmissao = emissao
        self.__dataVencimento = venc
        self.__valorBoleto = valor
        self.__dataPago = None
        self.__valorPago = 0.0
        self.__situacaoPagamento = Pagamento.EmAberto

    def pagar(self, valorPago):
        if valorPago <= 0:
            print("Valor inválido")
            return
        self.__valorPago += valorPago
        self.__dataPago = datetime.today()
        self.situacao()  # Atualiza a situação com base no valor pago

    def situacao(self):
        if self.__valorPago == 0:
            self.__situacaoPagamento = Pagamento.EmAberto
        elif self.__valorPago < self.__valorBoleto:
            self.__situacaoPagamento = Pagamento.PagoParcial
        else:
            self.__situacaoPagamento = Pagamento.Pago

    def __str__(self):
        dataPagoStr = self.__dataPago.strftime("%d/%m/%Y") if self.__dataPago else "Não pago ainda"
        return (f"Código de Barras: {self.__codBarras}\n"
                f"Data de Emissão: {self.__dataEmissao.strftime('%d/%m/%Y')}\n"
                f"Data de Vencimento: {self.__dataVencimento.strftime('%d/%m/%Y')}\n"
                f"Data de Pagamento: {dataPagoStr}\n"
                f"Valor do Boleto: R$ {self.__valorBoleto:.2f}\n"
                f"Valor Pago: R$ {self.__valorPago:.2f}\n"
                f"Situação: {self.__situacaoPagamento.name}")

    # Métodos de acesso (getters)
    def get_cod(self): 
        return self.__codBarras
    def get_valorBoleto(self): 
        return self.__valorBoleto
    def get_valorPago(self): 
        return self.__valorPago
    def get_situacao(self): 
        return self.__situacaoPagamento.name

class BoletoUI:
    __boletos = []

    @classmethod
    def menu(cls):
        print("\n1 - Inserir Boleto")
        print("2 - Listar Boletos")
        print("3 - Pagar Boleto")
        print("4 - Recuperar Boleto")
        print("5 - Fim")
        return int(input("Escolha uma opção: "))

    @classmethod
    def main(cls):
        op = 0
        while op != 5:
            op = cls.menu()
            if op == 1: cls.inserir()
            elif op == 2: cls.listar()
            elif op == 3: cls.pagar()
            elif op == 4: cls.recuperar()

    @classmethod
    def inserir(cls):
        cod = input("Informe o código de barras: ")
        emissao = datetime.strptime(input("Data de emissão (dd/mm/aaaa): "), "%d/%m/%Y")
        venc = datetime.strptime(input("Data de vencimento (dd/mm/aaaa): "), "%d/%m/%Y")
        valor = float(input("Valor do boleto: R$ "))
        b = Boleto(cod, emissao, venc, valor)
        cls.__boletos.append(b)
        print("Boleto inserido com sucesso!")

    @classmethod
    def listar(cls):
        if len(cls.__boletos) == 0:
            print("Nenhum boleto cadastrado.")
        else:
            for b in cls.__boletos:
                print("-" * 30)
                print(b)

    @classmethod
    def pagar(cls):
        cod = input("Informe o código de barras do boleto: ")
        for b in cls.__boletos:
            if b.get_cod() == cod:
                valor = float(input("Informe o valor a pagar: R$ "))
                b.pagar(valor)
                print("Pagamento registrado!")
                return
        print("Boleto não encontrado.")

    @classmethod
    def recuperar(cls):
        cod = input("Informe o código de barras: ")
        for b in cls.__boletos:
            if b.get_cod() == cod:
                print(b)
                return
        print("Boleto não encontrado.")

# Iniciar o programa
BoletoUI.main()