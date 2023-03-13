class Estudante:
    def __init__(self, nome, age, nota):
        self.nome = nome
        self.age = age
        self.nota = nota  # 0 - 100

    def get_nota(self):
        return self.nota


class Curso:
    def __init__(self, nome, max_estudantes):
        self.max_estudantes = max_estudantes
        self.nome = nome
        self.estudantes = []

    def add_estudante(self, estudante):
        if len(self.estudantes) < self.max_estudantes:
            self.estudantes.append(estudante)
            return True
        return False

    def get_mediaNota(self):
        valor = 0
        for estudante in self.estudantes:
            valor += estudante.get_nota()
        return valor/len(self.estudantes)


s1 = Estudante("Kaio", 21, 100)
s2 = Estudante("joao", 20, 75)
s3 = Estudante("pedro", 19, 62)

curso = Curso("matematica", 2)
curso.add_estudante(s1)
curso.add_estudante(s2)

print(curso.get_mediaNota())

