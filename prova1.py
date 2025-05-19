from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, id, nome, cpf):
        self.id = id
        self.nome = nome
        self._cpf = cpf

    @abstractmethod
    def marcar_presenca(self):
        pass

    def matricular(self):
        print(f"{self.nome} foi matriculado.")

class Aluno(Pessoa):
    def __init__(self, id, nome, cpf, matricula):
        super().__init__(id, nome, cpf)
        self.__matricula = matricula

    def get_matricula(self):
        return self.__matricula

    def set_matricula(self, nova):
        self.__matricula = nova

    def marcar_presenca(self):
        print(f"Presença marcada para {self.nome}.")

    def matricular(self):
        print(f"{self.nome} com matrícula {self.__matricula} foi matriculado.")

aluno = Aluno(1, "Maria", "xxx.xxx.xxx.xx", "2xx2xx")
aluno.marcar_presenca()
aluno.matricular()
print(aluno.get_matricula())
aluno.set_matricula("3xx3xx")
print(aluno.get_matricula())
aluno.set_matricula("Hello World!")
print(aluno.get_matricula())
aluno.set_matricula("\033[31mGuanabara \033[32mPython \033[34m:)")
print(aluno.get_matricula())
