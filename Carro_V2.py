class Carro:
    def __init__(self, marca, modelo, ano, cor):
        # Aqui é o construtor da classe, que inicializa os atributos do carro, incluindo estado e velocidade
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.ligado = False
        self.velocidade = 0

    def ligar(self):
        # Liga o carro SE ele estiver desligado, se não avisa que já está ligado
        if not self.ligado:
            self.ligado = True
            print("O carro está ligado.")
        else:
            print("O carro já está ligado.")

    def desligar(self):
        # Desliga o carro SE ele estiver ligado, se não avisa que já está desligado
        if self.ligado:
            self.ligado = False
            self.velocidade = 0
            print("O carro foi desligado.")
        else:
            print("O carro já está desligado.")

    def acelerar(self, incremento=20):
        # Acelera o carro SE ele estiver ligado, se não avisa que está desligado.
        if self.ligado:
            self.velocidade += incremento
            print(f"O carro acelerou {incremento} km/h. Velocidade atual: {self.velocidade} km/h.")
            if self.velocidade >= 120:
                # Limite de velocidade
                print("Velocidade máxima atingida! (120km/h)")
        else:
            print("O carro está desligado. Não é possível acelerar.")

    def travar(self, decremento=20):
        # Reduz a velocidade do carro SE ele estiver ligado e em movimento, se não avisa que está parado ou desligado
        if self.ligado and self.velocidade > 0:
            self.velocidade -= decremento
            if self.velocidade < 0:
                self.velocidade = 0
            print(f"O carro travou {decremento} km/h. Velocidade atual: {self.velocidade} km/h.")
        else:
            print("O carro está parado ou desligado.")

    def mostrar_info(self):
        # Mostra as informações do carro, como marca, modelo, ano, cor, estado e velocidade
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
