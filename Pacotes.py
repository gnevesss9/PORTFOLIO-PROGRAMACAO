import random

class Pacotes:
    def __init__(self):
        self.lista_pacotes = [None] * 5
        self.ultimo_numero = None
        self.guardar = None 

    def gerar_pacote(self):
        while None in self.lista_pacotes:
            print("=====================================================================")
            print("Estado atual do pacote: ", self.lista_pacotes)
            print("=====================================================================")
            print("\n")
            pacote = random.randint(-5, 10)
            print("Número aleatório gerado: ", pacote)

            escolha = input("Deseja guardar ou descartar o pacote? (1 para guardar, 0 para descartar): ")

            if escolha == "0":
                print(f"Pacote cujo número é {pacote} foi descartado.\n")
                continue

            elif escolha == "1":
                posicao = int(input("Posição (0 a 4): "))
                if not (0 <= posicao < len(self.lista_pacotes)):
                    print("Posição inválida.")
                    continue
                if self.lista_pacotes[posicao] is not None:
                    print("Esta posição já está ocupada.")
                    continue
                self.lista_pacotes[posicao] = pacote
                print(f"Pacote cujo número é {pacote} foi adicionado na posição {posicao}.")
            else:
                print("Opção inválida.")
                continue

        print("Verificando estrutura...")
        if self.lista_pacotes == sorted(self.lista_pacotes):
            print("A estrutura está correta. Os vídeos irão reproduzir.")
        else:
            print("A estrutura não está correta. Os vídeos NÃO irão reproduzir.")
        
        if self.lista_pacotes == sorted(self.lista_pacotes) and None not in self.lista_pacotes:
            self.ultimo_numero = self.lista_pacotes[-1]
            self.guardar = self.lista_pacotes[:]
            print("Criando uma nova lista de pacotes...")
            self.reiniciar_lista()

    def reiniciar_lista(self):
        self.lista_pacotes = [None] * 5
        print(f"Nova lista criada. Começe a lista pelo número {self.ultimo_numero}.")
        while None in self.lista_pacotes:
            print("=====================================================================\n")
            print("Estado atual do pacote: ", self.lista_pacotes)
            print("\n=====================================================================")
            print("\n")
            pacote = random.randint(-5, 10)
            print("Número aleatório gerado: ", pacote)

            escolha = input("Deseja guardar ou descartar o pacote? (1 para guardar, 0 para descartar): ")

            if escolha == "0":
                print(f"Pacote cujo número é {pacote} foi descartado.\n")
                continue

            elif escolha == "1":
                posicao = int(input("Posição (0 a 4): "))
                if not (0 <= posicao < len(self.lista_pacotes)):
                    print("Posição inválida.")
                    continue
                if self.lista_pacotes[posicao] is not None:
                    print("Esta posição já está ocupada.")
                    continue

                if posicao == 0 and pacote != self.ultimo_numero:
                    print(f"O primeiro número da nova lista deve ser {self.ultimo_numero}.")
                    continue

                self.lista_pacotes[posicao] = pacote
                print(f"Pacote cujo número é {pacote} foi adicionado na posição {posicao}.")

            else:
                print("Opção inválida.")
                continue

        print("Verificando estrutura...")
        if self.lista_pacotes == sorted(self.lista_pacotes):
            print("A estrutura está correta. Os vídeos irão reproduzir.")
        else:
            print("A estrutura não está correta. Os vídeos NÃO irão reproduzir.")

        print("Listas completas.")
        print("Primeira lista: ", self.guardar)
        print("Segunda lista: ", self.lista_pacotes)

p = Pacotes()
p.gerar_pacote()