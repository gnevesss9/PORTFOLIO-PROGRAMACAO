class Carro:
    #Aqui é o construtor da classe, que inicializa os atributos do carro
    def __innit__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

    def mostrar_info(self):
        #Mostra as informações do carro, como marca, modelo, ano e cor
        print(f"\nCarro: {self.marca} {self.modelo}")
        print(f"Ano: {self.ano} | Cor: {self.cor}")

print("=== Cria o teu carro ===")
# Solicita ao usuário que insira os detalhes do carro, como marca, modelo, ano e cor
marca = input("Marca: ")
modelo = input("Modelo: ")
ano = input("Ano: ")
cor = input("Cor: ")

meu_carro = Carro(marca, modelo, ano, cor)
# Guarda as informações do carro criado na variável meu_carro

meu_carro.mostrar_info()
# Exibe as informações do carro criado

print("\n Carro criado com sucesso!")
