class Interacao:
    def __init__(self):
        self.inicio = "Menu Inicial" + "\n" + "O que você deseja?"
        self.menu1 = "0 - Sair"
        self.menu2 = "1 - Logar"
        self.menu3 = "2 - Cadastrar"
        self.menu4 = "Menu Principal"
        self.menu5 = "0 - Sair"
        self.menu6 = "1 - Cadastrar Veículos"
        self.menu7 = "2 - Identificar Veículos"
        self.menu8 = "3 - Remover Veículos"
        self.menu9 = "4 - Cadastrar Eventos"
        self.menu10 = "5 - Cadastrar Ocorrencias"
        self.menu11 = "6 - Monitorar Vagas"
        self.menu12 = "7 - Monitorar Eventos"
        self.menu13 = "8 - Monitorar Ocorrencias"


    def getInteracao(self):
        temp = self.inicio + "\n" + self.menu1 + "\n" + self.menu2 + "\n" + self.menu3
        return temp
    def getInteracao2(self):
        temp = self.menu4+"\n" + self.menu5 + "\n" + self.menu6 + "\n" + self.menu7 + "\n" + self.menu8 + \
               "\n" + self.menu9 + "\n" + self.menu10 + "\n" + self.menu11 + "\n" + self.menu12+ "\n" + self.menu13
        return temp