class Cliente:
    def __init__(self, nome, anoNascimento, sexo, saldo, endereco, ativo):
        self.nome = nome
        self.anoNascimento = anoNascimento
        self.sexo = sexo
        self.saldo = saldo
        self.endereco = endereco
        self.ativo = ativo



    def imprimir(self):
        print("---------------------")
        print("nome:", self.nome)
        print("anoNascimento:", self.anoNascimento)
        print("sexo:", self.sexo)
        print("saldo:", self.saldo)
        print("endereco:", self.endereco)
        print("ativo:", self.ativo)


    def verificaClienteVivo(self):
        if self.ativo:
            print("O cliente", self.nome, "esta ativo")
        else:
            print("O cliente", self.nome, "inativo")


    def calcularIdade(self):
        anoAtual = 2024
        idade = (anoAtual - self.anoNascimento)
        print("A idade do Cliente e", idade)


    def verificarSaldo(self):
        if self.saldo >= 0:
            print("O saldo do cliente", self.nome, "e positivo")
        else:
            print("O saldo do cliente", self.nome, "negativo")


objeto = Cliente("Bruno", 2007, "M", 5000, "Rua 15 novembro", True)
objeto2 = Cliente("Gabriel", 2005, "M", -5000, "Rua teste", True)
objeto3 = Cliente("Guilherme", 2000, "M", 15000, "Rua 7", False)
objeto.imprimir()
objeto2.imprimir()
objeto3.imprimir()
  
objeto.verificaClienteVivo()
objeto2.verificaClienteVivo()
objeto3.verificaClienteVivo()


objeto.calcularIdade()
objeto2.calcularIdade()
objeto3.calcularIdade()


objeto.verificarSaldo()
objeto2.verificarSaldo()
objeto3.verificarSaldo()
