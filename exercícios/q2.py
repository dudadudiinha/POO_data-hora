from datetime import datetime
import enum

class Pagamento(enum.Enum):
    EmAberto = 1
    PagoParcial = 2
    Pago = 3

class Boleto:
    def __init__(self, cod, emissao, venc, valor):
        self.set_codBarras(cod)
        self.__dataEmissao = emissao
        self.__dataVencimento = venc
        self.__valorBoleto = valor
        self.__dataPago = None
        self.__valorPago = 0
        self.__situacaoPagamento = Pagamento.EmAberto

    def set_codBarras(self, cod):
        if cod < 0:
            raise ValueError("Código inválido")
        self.__codBarras = cod
    def get_codBarras(self):
        return self.__codBarras
    
    def set_dataEmissao(self, emissao):
        if emissao > datetime.today():
            raise ValueError("A data de emissão é inválida")
        self.__dataEmissao = emissao
    def get_dataEmissao(self):
        return self.__dataEmissao
    
    def set_venc(self, venc):
        if venc < datetime.today():
            raise ValueError("A data de emissão é inválida")
        self.__dataVencimento = venc
    
    def set_valorBoleto(self, valor):
        self.__valorBoleto = valor
    def get_valorBoleto(self): 
        return self.__valorBoleto
    
    def get_valorPago(self): 
        return self.__valorPago
    def get_situacao(self): 
        return self.__situacaoPagamento.name
    
    def pagar(self, valorPago):
        if valorPago <= 0:
            raise ValueError("Valor inválido.")
        self.__valorPago = valorPago
        self.__dataPago = datetime.today()
        self.situacao()

    def situacao(self):
        if self.__valorPago < self.__valorBoleto:
            self.__situacaoPagamento = Pagamento.PagoParcial
        if self.__valorPago == self.__valorBoleto:
            self.__situacaoPagamento = Pagamento.Pago

    def __str__(self):
        if self.__dataPago == None:
            data = "Não pago"
        else:
            data = self.__dataPago.strftime('%d/%m/%Y')
        return f"Código de barras: {self.__codBarras}\nData de emissão: {self.__dataEmissao.strftime('%d/%m/%Y')}\nData de vencimento: {self.__dataVencimento.strftime('%d/%m/%Y')}\nData do pagamento: {data}\nValor do boleto: R${self.__valorBoleto}\nValor pago: R${self.__valorPago}\nSituação do pagamento: {self.__situacaoPagamento.name}"
    
class BoletoUI:
    __boletos = []

    @classmethod
    def menu(cls):
        return int(input("1 - Inserir, 2 - Recuperar, 3 - Alterar, 4 - Pagar, 5 - Fim\nInforme uma opção: "))

    @classmethod
    def main(cls):
        op = 0
        while op != 5:
            op = BoletoUI.menu()
            match op:
                case 1: cls.inserir()
                case 2: cls.recuperar()
                case 3: cls.alterar()
                case 4: cls.pagar()

    @classmethod
    def inserir(cls):
        cod = int(input("Informe o código de barras: "))
        emissao = datetime.strptime(input("Informe a data de emissão: "), '%d/%m/%Y')
        venc = datetime.strptime(input("Informe a data de vencimento: "), '%d/%m/%Y')
        valor = int(input("Informe o valor do boleto: R$"))
        b = Boleto(cod, emissao, venc, valor)
        cls.__boletos.append(b)

    @classmethod
    def recuperar(cls):
        cod = int(input("Informe o código de barras do produto: "))
        for b in cls.__boletos:
            if cod == b.get_codBarras():
                return print(b)
        print("Esse produto não está registrado.")

    @classmethod
    def alterar(cls):
        cod = int(input("Informe o código de barras do boleto: "))
        for b in cls.__boletos:
            if cod == b.get_codBarras():
                emissao2 = datetime.strptime(input("Informe a nova data de emissão: "), '%d/%m/%Y')
                venc2 = datetime.strptime(input("Informe a nova data de vencimento: "), '%d/%m/%Y')
                valor2 = int(input("Informe o novo valor do boleto: R$"))
                b.set_dataEmissao(emissao2)
                b.set_venc(venc2)
                b.set_valorBoleto(valor2)

    @classmethod
    def pagar(cls):
        cod = int(input("Informe o código de barras do boleto: "))
        for b in cls.__boletos:
            if b.get_codBarras() == cod:
                valor = int(input("Informe o valor a pagar: R$"))
                b.pagar(valor)
                return
        print("Boleto não encontrado")

BoletoUI.main()