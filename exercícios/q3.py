from datetime import datetime

class Contato:
    def __init__(self, i, n, e, f, b):
        self.__id = i
        self.__nome = n
        self.__email = e
        self.__fone = f
        self.__nasc = b
        self.set_nasc(self.__nasc)
    def set_nasc(self, b):
        if b > datetime.today(): 
            raise ValueError("A data de nascimento é inválida")
        self.__nasc = b
    def get_nasc(self):
        return self.__nasc
    def set_nome(self, nome2):
        self.__nome = nome2
    def get_nome(self):
        return self.__nome
    def get_id(self):
        return self.__id 
    def set_email(self, email2):
        self.__email = email2
    def get_email(self):
        return self.__email
    def set_fone(self, fone2):
        self.__fone = fone2 
    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__email} - {self.__fone} - {self.__nasc.strftime("%d/%m/%Y")}"
        
class ContatoUI:
    __contatos = []

    @classmethod
    def main(cls):
        op = 0
        while op != 7:
            op = ContatoUI.menu()
            if op == 1: ContatoUI.inserir()
            if op == 2: ContatoUI.listar()
            if op == 3: ContatoUI.atualizar()
            if op == 4: ContatoUI.excluir()
            if op == 5: ContatoUI.pesquisar()
            if op == 6: ContatoUI.aniversariantes()

    @classmethod
    def menu(cls):
        print("1-Inserir, 2-Listar, 3-Atualizar, 4-Excluir, 5-Pesquisar, 6-Aniversariantes, 7-Fim")
        return int(input("Informe uma opção: "))
    
    @classmethod
    def inserir(cls):
        nome = input("Informe o nome: ")
        email = input("Informe o e-mail: ")
        fone = input("Informe o fone: ")
        nasc = datetime.strptime(input("Informe a data de nascimento (dd/mm/aaaa): "), "%d/%m/%Y") #strf é pra transformar uma data em str
        for c in cls.__contatos:
            if c.get_email() == email:
                print("Email já cadastrado. Digite novamente")
                return
        id = 1
        for c in cls.__contatos:
            id += 1
        c = Contato(id, nome, email, fone, nasc)
        cls.__contatos.append(c)

    @classmethod
    def listar(cls):
        if len(cls.__contatos) == 0:
            print("Nenhum contato cadastrado")
        for c in cls.__contatos:
            print(c)

    @classmethod
    def listar_id(cls, id):
        for c in cls.__contatos:
            if c.get_id() == id: return c
        return None    

    @classmethod
    def atualizar(cls):
        cls.listar()
        id = int(input("Informe o id do contato a ser atualizado: "))
        c = cls.listar_id(id)
        if c == None: 
            print("Esse contato não existe")
        else:
            nome2 = input("Informe o novo nome: ")
            email2 = input("Informe o novo email: ")
            fone2 = input("Informe o novo fone: ")
            c.set_nome(nome2)
            c.set_email(email2)
            c.set_fone(fone2)
            print("Contato atualizado")

    @classmethod
    def excluir(cls):
        cls.listar()
        id = int(input("Informe o id do contato a ser excluído: "))
        c = cls.listar_id(id)
        if c == None: 
            print("Esse contato não existe")
        else: 
            cls.__contatos.remove(c)

    @classmethod
    def pesquisar(cls):
        nome = input("Informe o nome do contato: ")
        for c in cls.__contatos:
            if c.get_nome().startswith(nome):
                print(c)

    @classmethod
    def aniversariantes(cls):
        mes = int(input("Informe o mês para ver os aniversariantes: "))
        achou = False
        for c in cls.__contatos:
            if c.get_nasc().month == mes:
                print(c)
                achou = True
        if achou == False:
            print("Não há nenhum contato que faz aniversário nesse mês")

ContatoUI.main()