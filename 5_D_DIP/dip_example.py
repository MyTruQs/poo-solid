"""
    D - Principio da Inversão de Dependência (Dependency Inversion Principle - DIP)
    
    Módulos de alto nível não devem depender diretamente dos módulos de baixo nível.
    O Principio da Inversão da Dependência (DIP) nos diz que os sistemas mais flexiveis são aqueles em que as dependências do código-fonte referem-se apenas a abstrações, não a concreções.
"""

# Exemplo de código que não segue o DIP
# from .notificator_email import NotificatorEmail
# class ClientService:
#     def __init__(self, notificator: NotificatorEmail) -> None:
#         self.notificator = notificator
        
#     def send(self, message: str) -> None:
#         self.notificator.send_notification(message)

# Exemplo de código que segue o DIP
from notificator_interface import NotificatorInterface
from notificator_email import NotificatorEmail
from notificator_sms import NotificatorSMS

class ClientService:
    def __init__(self, notificator: NotificatorInterface) -> None:
        self.notificator = notificator
        
    def send(self, message: str) -> None:
        self.notificator.send_notification(message)
        
client = ClientService(NotificatorSMS())
client.send("Hello, World!")