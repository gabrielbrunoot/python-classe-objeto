class Cadastro:
    idade = None
    def __init__(self):
        pass 

    

    def InserirIdade(self, idade):
        idadeCorreta = self.ValidaIdade(idade)
        if idadeCorreta == True:
            self.idade = idade
            print("valor cadastrado com sucesso")

    def ValidaIdade(self, idade):
        if idade <= 18:
            print("idade precisa ser maior que 18")
            return False
        else:
            return True 
        


    def InserirNome(self, nome):
        nomeCorreto = self.ValidaNome(nome)
        if nomeCorreto == True:
            self.nome = nome
            print("valor cadastrado com sucesso")

    def ValidaNome(self, nome):
        if len(nome) == 0:
            print("nome precisa ser preenchido")
            return False
        else:
            return True 
        


    def InserirSaldo(self, saldo):
        saldoCorreto = self.ValidaSaldo(saldo)
        if saldoCorreto == True:
            self.saldo = saldo
            print("valor cadastrado com sucesso")

    def ValidaSaldo(self, saldo):
        if saldo > 0:
            print("saldo precisa ser positiva")
            return False
        else:
            return True 
        

    
    def InserirStatusCadastro(self, StatusCadastro):
        StatusCadastroCorreto = self.ValidaStatusCadastro(StatusCadastro)
        if StatusCadastroCorreto == True:
            self.StatusCadastro = StatusCadastro
            print("valor cadastrado com sucesso")

    def ValidaStatusCadastro(self, StatusCadastro):
        if StatusCadastro > 0:
            print("Status cadastro precisa ser verdadeiro")
            return False
        else:
            return True 
        


    def InserirEndereco(self, saldo):
        enderecoCorreto = self.ValidaSaldo(saldo)
        if saldoCorreto == True:
            self.saldo = saldo
            print("valor cadastrado com sucesso")

    def ValidaSaldo(self, saldo):
        if saldo > 0:
            print("saldo precisa ser positiva")
            return False
        else:
            return True 
        


cad1 = Cadastro()
cad1.InserirIdade(20)
cad1.InserirIdade(-5)
cad1.InserirSaldo(-100)
cad1.InserirSaldo(100)
cad1.InserirStatusCadastro(True)
cad1.InserirStatusCadastro(False)
cad1.InserirNome("")
