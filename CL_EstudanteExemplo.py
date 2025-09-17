class Estudante:
    def __init__(self, nome, idade, curso, genero, turma, ano):
        # Atributos
        self.nome = nome
        self.idade = idade
        self.curso = curso
        self.notas = []
        self.genero = genero
        self.turma = turma
        self.ano = ano

    
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
        return(f"Olá, meu nome é {self.nome}, sou do gênero {self.genero}, tenho {self.idade} anos e estudo {self.curso}. Estou na {self.turma} do {self.ano}º ano.")
    
aluno1 = Estudante("Ana", 17, "Informática", "Feminino", "Turma A", 12)
aluno2 = Estudante("João", 16, "Ciências", "Masculino", "Turma B", 12)

aluno1.adicionar_nota(85) # Adiciona uma nota para Ana
aluno1.adicionar_nota(92) # Adiciona outra nota para Ana
print(aluno1.apresentar())
print(f"Média: {aluno1.calcular_media()}")
