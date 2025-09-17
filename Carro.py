class Carro:
    def __innit__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

    def mostrar_info(self):
        print(f"\nCarro: {self.marca} {self.modelo})")
        print(f"Ano: {self.ano} | Cor: {self.cor}")

print("=== Cria o teu carro ===")
marca = input("Marca: ")
modelo = input("Modelo: ")
ano = input("Ano: ")
cor = input("Cor: ")

meu_carro = Carro(marca, modelo, ano, cor)

meu_carro.mostrar_info()

print("\n Carro criado com sucesso!")
    
