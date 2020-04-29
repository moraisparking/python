class Usuario:
    def __init__(self):
        self.nome = ''
        self.senha = ''
        self.banco = ['yuri','123']
    def cadastrar(self, nome, senha):
        self.banco.append(nome)
        self.banco.append(senha)
    def getBanco(self):
         return self.banco
    def verificarUsuario(self,nome,senha):
        temp = ''
        for i in range(len(self.banco)):
            if self.banco.__contains__(nome) and self.banco.__contains__(senha):
                temp = True   
            else:
                temp = False
        return temp

