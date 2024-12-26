"""
    L - Principio de Substituição de Liskov (Liskov Substitution Principle - LSP)
    
    Objetos podem ser substituidos por seus subtipos sem que isso afete a execução correta do programa.
    O LSP pode e deve ser estendido ao nivel da arquitetura. 
    Uma simples violação de substituição,pode fazer com que a arquitetura de um sistema seja poluida com uma quantidade significativa quantidade de mecanismos extras.
"""

#  Exemplo de classe sem o conceito
# class Animal:
#     def comer(self):
#         print("Animal esta comendo...")
    
#     def andar(self):
#         print("Animal esta andando...")
        
# class Felino(Animal):
#     def lamber(self):
#         print("Felino esta lambendo seu pelo")
        
#     def comer(self): # errado
#         print("Felino esta comendo carne")


# Exemplo de classe com o conceito
class Animal:
    def comer(self):
        print("Animal esta comendo...")
    
    def andar(self):
        print("Animal esta andando...")
        
class Felino(Animal):
    def lamber(self):
        print("Felino esta lambendo seu pelo")
        
class Leao(Felino):
    def rugir(self):
        print("Leao esta rugindo...")

class Pessoa:
    def observa(self, animal: Animal):
        animal.comer()
        
animal = Animal()
felino = Felino()
leao = Leao()
pessoa = Pessoa()

pessoa.observa(leao)