class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano


    def imprimir(self):
        print("---------------------")
        print("marca:", self.marca)
        print("modelo:", self.modelo)
        print("ano:", self.ano)


    def ligar(self):
        print("Veiculo ligado")

    def desligar(self):
        print("Veiculo desligado")

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, numeroDePortas):
        super().__init__(marca, modelo, ano)
        self.numeroDePortas = numeroDePortas

    def NumeroDePortas(self):
        print("O carro possui:", self.numeroDePortas)

class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, cilindradas):
        super().__init__(marca, modelo, ano)
        self.cilindradas = cilindradas

    def Cilindradas(self):
        print("A moto possui:", self.cilindradas)


objeto = Veiculo("chevrolet", "corsa", 2017) 
objeto2 =  Carro("chevrolet", "corsa", 2017, "quatro portas")
objeto3 = Moto("honda", "CG 160 titan", 2024, 160)


objeto.ligar()

objeto.imprimir()
objeto2.imprimir()
objeto3.imprimir()

