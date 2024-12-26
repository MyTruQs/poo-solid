'''
OPEN CLOSED PRINCIPLE

Imagine que uma clínica veterinária tem seu sistema próprio para aprovação de exames. No primeiro momento, ela tem um método para
verificar exame de sangue. Em outro ela adiciona exame por raio-x. Notamos no código que, conforme a clínica adiciona exames,
deverão adicionar uma validação para o exame. O que aumentaria a complexidade do código e a manutenção do mesmo.

A solução deste caso pode ser feita com o princípio aberto-fechado (Open Closed Principle). 
Utilizando do conceito do OCP, crie uma interface e classes que implementam a mesma para que, caso a clínica necessite de um novo
tipo de exame, uma nova classe seja adicionada, implementando métodos de uma interface padrão para exames.

'''

from abc import ABC, abstractmethod

class Exame(ABC):
    def __init__(self, tipo):
        self.tipo = tipo

    @abstractmethod
    def verifica_condicoes(self):
        pass

class ExameSangue(Exame):
    def __init__(self):
        super().__init__("sangue")

    def verifica_condicoes(self):
        # implemente as condições específicas do exame de sangue
        pass

class ExameRaioX(Exame):
    def __init__(self):
        super().__init__("raio-x")

    def verifica_condicoes(self):
        # implemente as condições específicas do exame de raio-x
        pass

class AprovaExame:
    def aprovar_solicitacao_exame(self, exame: Exame):
        if exame.verifica_condicoes():
            print(f"{exame.tipo.capitalize()} aprovado!")

# Exemplo de uso:
exame_sangue = ExameSangue()
exame_raio_x = ExameRaioX()

aprovador = AprovaExame()
aprovador.aprovar_solicitacao_exame(exame_sangue)
aprovador.aprovar_solicitacao_exame(exame_raio_x)


