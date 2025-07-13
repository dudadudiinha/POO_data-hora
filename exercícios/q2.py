from datetime import datetime
import enum

class Pagamento(enum.Enum):
    EmAberto = 1
    PagoParcial = 2
    Pago = 3

class Boleto:
    def __init__(self, codB, dataE, dataV, dataP, valorB, valorP):
        self.__codBarras = codB
        self.__dataEmissao = dataE
        self.__dataVencimento = dataV
        self.__dataPago = None
        self.__valorBoleto = valorB
        self.__valorPago = 0.0
        self.__situacaoPagamento = Pagamento.EmAberto

    def __str__(self):
        return f"Código de barras: {self.__codBarras}\nData de emissão: {self.__dataEmissao}\nData de vencimento: {self.__dataVencimento}\nData do pagamento: {self.__dataPago}\nValor do boleto: {self.__valorBoleto}\nValor pago: {self.__valorPago}\nSituação do pagamento: {self.__situacaoPagamento}"
    
class BoletoUI:
    @classmethod
    def menu(cls):
        return int(input("1 - "))

    @classmethod
    def main(cls):
        op = 0
        while op != 5:
            op = BoletoUI.menu()
            match op:
                case 1: 
                case 2: 
                case 3:

BoletoUI.main()
