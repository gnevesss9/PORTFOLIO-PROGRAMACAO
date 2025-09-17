class Carro:
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.ligado = False
        self.velocidade = 0

    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print("O carro está ligado.")
        else:
            print("O carro já está ligado.")

    def desligar(self):
        if self.ligado:
            self.ligado = False
            self.velocidade = 0
            print("O carro foi desligado.")
        else:
            print("O carro já está desligado.")

    def acelerar(self, incremento=20):
        if self.ligado:
            self.velocidade += incremento
            print(f"O carro acelerou {incremento} km/h. Velocidade atual: {self.velocidade} km/h.")
            if self.velocidade >= 120:
                print("Velocidade máxima atingida! (120km/h)")
        else:
            print("O carro está desligado. Não é possível acelerar.")

    def travar(self, decremento=20):
        if self.ligado and self.velocidade > 0:
            self.velocidade -= decremento
            if self.velocidade < 0:
                self.velocidade = 0
            print(f"O carro travou {decremento} km/h. Velocidade atual: {self.velocidade} km/h.")
        else:
            print("O carro está parado ou desligado.")

    def mostrar_info(self):
        print(f"\nCarro: {self.marca} {self.modelo}")
        print(f"Ano: {self.ano} | Cor: {self.cor}")
        print(f"Estado: {'Ligado' if self.ligado else 'Desligado'} | Velocidade: {self.velocidade} km/h")


# Bloco de teste
if __name__ == "__main__":
    carro = Carro("Toyota", "Corolla", 2020, "Prata")
    carro.mostrar_info()
    carro.ligar()
    carro.acelerar()
    carro.acelerar()
    carro.travar()
    carro.mostrar_info()
    carro.desligar()
    carro.mostrar_info()