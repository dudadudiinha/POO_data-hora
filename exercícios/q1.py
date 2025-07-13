from datetime import datetime

class Paciente:
    def __init__(self, id, nome, cpf, tel, nasc):
        self.__id = id
        self.__nome = nome
        self.__cpf = cpf
        self.__tel = tel
        self.__nasc = nasc
        self.set_nasc(self.__nasc)

    def set_nasc(self, nasc):
        if nasc > datetime.today():
            raise ValueError("A data de nascimento é inválida")
        self.__nasc = nasc
    def set_nasc2(self, nasc2):
        self.__nasc = nasc2
    def get_nasc(self):
        return self.__nasc
    def set_nome(self, nome2):
        self.__nome = nome2
    def get_nome(self):
        return self.__nome
    def get_cpf(self):
        return self.__cpf
    def set_tel(self, tel2):
        self.__tel = tel2
    def get_tel(self):
        return self.__tel
    
    def Idade(self): #rever!!!!
        hoje = datetime.today()
        anos = hoje.year - self.__nasc.year
        meses = hoje.month - self.__nasc.month
        return f"{anos} anos e {meses} meses" 
    
    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__cpf} - {self.__tel} - {self.__nasc.strftime('%d/%m/%Y')} - {self.Idade()}"

class PacienteUI:
    __pacientes = []

    @classmethod
    def main(cls):
        op = 0
        while op != 5:
            op = cls.menu()
            match op:
                case 1: cls.inserir()
                case 2: cls.listar()
                case 3: cls.alterar()
                case 4: cls.recuperar()

    @classmethod
    def menu(cls):
        return int(input("1-Inserir, 2-Listar, 3-Alterar, 4-Recuperar, 5-Fim\nInforme uma opção: "))
    
    @classmethod
    def inserir(cls):
        nome = input("Informe o nome: ")
        cpf = input("Informe o CPF: ")
        tel = input("Informe o telefone: ")
        nasc = datetime.strptime(input("Informe a data de nascimento (dd/mm/aaaa): "), '%d/%m/%Y')
        for p in cls.__pacientes:
            if cpf == p.get_cpf():
                return "CPF já cadastrado"
        id = 1
        for p in cls.__pacientes:
            id += 1
        p = Paciente(id, nome, cpf, tel, nasc)
        cls.__pacientes.append(p)

    @classmethod
    def listar(cls):
        if len(cls.__pacientes) == 0:
            print("Nenhum paciente cadastrado.")
        for p in cls.__pacientes:
            print(p)

    @classmethod
    def alterar(cls):
        cls.listar()
        cpf = input("Informe o cpf do paciente que deseja alterar os dados: ")
        for p in cls.__pacientes:
            if cpf == p.get_cpf():
                nome2 = input("Informe o novo nome: ")
                nasc2 = datetime.strptime(input("Informe a nova data de nascimento: "), '%d/%m/%Y')
                tel2 = input("Informe o novo telefone: ")
                p.set_nome(nome2)
                p.set_nasc2(nasc2)
                p.set_tel(tel2)
    @classmethod
    def recuperar(cls):
        cpf = input("Informe o CPF do paciente que deseja buscar: ")
        for p in cls.__pacientes:
            if cpf == p.get_cpf():
                print(p)
                return
        print("CPF não cadastrado.")

PacienteUI.main()