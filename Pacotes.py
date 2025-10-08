class Pacotes:
    def __init__(self):
        self.listas_guardadas = []
        self.lista_em_construcao = [None] * 5

    def iniciar(self):
        while len(self.listas_guardadas) < 2:
            print(f"Lista atual: {self.lista_em_construcao}")
            entrada = input("Insira um número: ")

            if entrada.isdigit():
                numero_inserido = int(entrada)
                posicao = numero_inserido % 5  

                if self.lista_em_construcao[posicao] is None:
                    self.lista_em_construcao[posicao] = numero_inserido
                    print(f"Número {numero_inserido} colocado na posição {posicao}.\n")
                else:
                    print(f"A posição {posicao} já está ocupada pelo número {self.lista_em_construcao[posicao]}.\n")

            else:
                print("Por favor, insira apenas números inteiros.\n")

            if all(v is not None for v in self.lista_em_construcao):
                print(f"Lista final: {self.lista_em_construcao}")
                self.listas_guardadas.append(self.lista_em_construcao[:])
                self.lista_em_construcao = [None] * 5

                if len(self.listas_guardadas) < 2:
                    print("Iniciando nova lista.\n")

        print("\nAs duas listas foram concluídas com sucesso!")
        print("Listas finais:")
        for i, lista in enumerate(self.listas_guardadas, 1):
            print(f"Lista {i}: {lista}")

#CÓDIGO FEITO POR GUILHERME NEVES


p = Pacotes()
p.iniciar()

