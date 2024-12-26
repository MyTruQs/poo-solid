"""
    I - Principio da Segregação de Interfaces (Interface Segregation Principle - ISP)
    
    Uma classe não deve ser forçada a implementar interfaces que ela não utiliza.
    Em vez disso, as interfaces devem ser segregadas em conjuntos menores e mais especificos de métodos.
"""

from abc import ABC, abstractmethod
#  Exemplo de classe sem o conceito
# class Document(ABC):
    
#     @abstractmethod
#     def load(self): pass

#     @abstractmethod
#     def view(self): pass
   
#     @abstractmethod
#     def format(self): pass

#     @abstractmethod
#     def calculate(self): pass

# class PDF(Document):
#     def load(self):
#         print("Carregando PDF...")
    
#     def view(self):
#         print("Visualizando PDF...")
        
#     def format(self):
#         print("Formatando PDF...")
        
#     def calculate(self):
#         print("Calculando PDF...")


# Exemplo de classe com o conceito
class DocumentPDF(ABC):
    @abstractmethod
    def load(self): pass

    @abstractmethod
    def view(self): pass
    
class DocumentTXT(ABC):
    @abstractmethod
    def load(self): pass

    @abstractmethod
    def format(self): pass

class DocumentExcel(ABC):
    @abstractmethod
    def load(self): pass

    @abstractmethod
    def calculate(self): pass
