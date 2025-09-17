class Estudante:
    def __init__(self, nome, idade, curso):
        # Atributos
        self.nome = nome
        self.idade = idade
        self.curso = curso
        self.notas = []
    
    def adicionar_nota(self, nota):
        # Método para adicionar uma nota
        self.notas.append(nota)
        print(f"Nota {nota} adicionada para {self.nome}.")

    def calcular_media(self):
        # Método para calcular a média das notas
        if self.notas:
            return sum(self.notas) / len(self.notas)
        return 0
    
    def apresentar(self):
        # Método para apresentar informações do estudante
        return(f"Olá, meu nome é {self.nome}, tenho {self.idade} anos e estudo {self.curso}.")
    
aluno1 = Estudante("Ana", 17, "Informática")
aluno2 = Estudante("João", 16, "Ciências")

aluno1.adicionar_nota(85) # Adiciona uma nota para Ana
aluno1.adicionar_nota(92) # Adiciona outra nota para Ana
print(aluno1.apresentar())
print(f"Média: {aluno1.calcular_media()}")
