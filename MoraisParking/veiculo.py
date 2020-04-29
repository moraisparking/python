class Veiculo:
    def __init__(self):
        self.matricula = ''
        self.nome= ''
        self.placa = ''
        self.marca= ''
        self.tipo= ''
        self.data = ''
        self.hora = ''
        self.status = ''
        self.bloco = ''
        self.banco = [['1212','Yuri','nmk0412','Harley Davyson','Moto','04/12/1993','12:45','ausente','BlocoA'],
                      ['1313','Kruba','mof6616','Gol','Carro','05/04/2020','19:35','presente','BlocoC']]
    def cadastrarVeiculo(self,matricula,nome,placa,marca,tipo,data,hora,bloco):
        veiculo = []
        veiculo.append(matricula)
        veiculo.append(nome)
        veiculo.append(placa)
        veiculo.append(marca)
        veiculo.append(tipo)
        veiculo.append(data)
        veiculo.append(hora)
        veiculo.append('presente')
        veiculo.append(bloco)
        self.banco.append(veiculo)
    def getBanco(self):
        return self.banco
    def pesquisarVeiculo(self,placa):
        temp = ''
        for i in range(len(self.banco)):
            if placa in self.banco[i] and 'ausente' in self.banco[i]:
                temp = self.banco[i]
            else:
                temp = self.banco[i]
        return temp
    def inserirEstaciomanento(self,bloco,placa):
        for i in range(len(self.banco)):
            if placa in self.banco[i]:
                self.banco[i][7] = 'presente'
                self.banco[i][8] = bloco
        return 'Veículo inserido com suceeso!'             
    def removerVeiculo(self, placa, rs):
        if rs == 'S':
            for i in range(len(self.banco)):
                if placa in self.banco[i]:
                    self.banco[i][7] = 'ausente'
        return 'Veículo removido com sucesso!'