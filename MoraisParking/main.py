from usuario import Usuario
from interacao import Interacao
from veiculo import Veiculo
def main():
    usuario = Usuario()
    interacao = Interacao()
    veiculo = Veiculo()
    print(interacao.getInteracao())
    entrada = int(input("Digite: "))
    while entrada <= 3:
        if entrada == 1:
            print("Realizar Login")
            nome = input("Nome: ")
            senha = input("Senha: ")
            validacao = usuario.verificarUsuario(nome,senha)
            if (validacao == True):
                print(interacao.getInteracao2())
                entradaI2 = int(input("Digite: "))
                while entradaI2 < 8:
                    if entradaI2 == 1:
                        matricula = input('Insira um matricula: ')
                        nome = input('Insira um nome: ')
                        placa = input('Insira um placa: ')
                        marca = input('Insira um marca: ')
                        tipo = input('Insira um tipo: ')
                        data = input('Insira um data: ')
                        hora = input('Insira um hora: ')
                        bloco = input('Insira um bloco: ')
                        veiculo.cadastrarVeiculo(matricula,nome,placa,marca,tipo,data,hora,bloco)
                        print("Veículo cadastrado com sucesso!")
                    elif entradaI2 == 2:
                        placa = input('Digite a placa do veiculo: ')
                        veiculo.pesquisarVeiculo(placa)
                        if veiculo.pesquisarVeiculo(placa) == 0:
                            print('Veiculo não encontrado')
                            rs = input("Deseja dacadastrar o Veículo (S/N)?: ")
                            if rs == 'S':
                                matricula = input('Insira um matricula: ')
                                nome = input('Insira um nome: ')
                                placa = input('Insira um placa: ')
                                marca = input('Insira um marca: ')
                                tipo = input('Insira um tipo: ')
                                data = input('Insira um data: ')
                                hora = input('Insira um hora: ')
                                bloco = input('Insira um bloco: ')
                                veiculo.cadastrarVeiculo(matricula,nome,placa,marca,tipo,data,hora,bloco)
                                print("Veículo cadastrado com sucesso!") 
                        else:
                            bloco = input("Digite o bloco para o veículo estacionar: ")
                            print(veiculo.inserirEstaciomanento(bloco,placa))
                            veiculo.pesquisarVeiculo(placa)
                    elif entradaI2 == 6:
                        print(veiculo.getBanco())
                    elif entradaI2 == 3:
                        placa = input('Digite a placa do veiculo: ')
                        veiculo.pesquisarVeiculo(placa)
                        rs = input('Deseja realmente remover o veículo? (S/N): ')
                        if rs == 'S':
                            print(veiculo.removerVeiculo(placa,rs))
                            veiculo.pesquisarVeiculo(placa)
                    elif entradaI2 == 0:
                        print('Volte quando quiser! =)')
                        exit()
                    print(interacao.getInteracao2())
                    entradaI2 = int(input("Digite: "))
            else:
                while validacao == False:
                    print("Usuário ou senha Inválidos!\nTente Novamente.")
                    nome = input("Nome: ")
                    senha = input("Senha: ")
                    validacao = usuario.verificarUsuario(nome, senha)
        elif entrada == 2:
            print("Cadastre um Usuário")
            nome = input("Nome: ")
            senha = input("Senha: ")
            usuario.cadastrar(nome, senha)
            print(usuario.getBanco())
        elif entrada == 0:
            print('Volte quando quiser! =)')
            exit()
        print(interacao.getInteracao())
        entrada = int(input("Digite: "))


main()