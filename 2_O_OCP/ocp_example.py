# O - Principio Aberto/Fechado (Open/Closed Principle - OCP)
# Um artefato de software deve estar aberto para extensão, mas fechado para modificação.
# Em outras palavras, o comportamento de um artefato de software deve ser extensivel, sem ter que modificar esse artefato.

# Exemplo de classe sem o conceito
# class Company:
#     def do_work(self, worker: int) -> None:
#         if worker == 1:
#             print("Programador esta criando codigo...")
#         elif worker == 2:
#             print("O Vendedor esta vendendo produto...")
#         elif worker == 3:
#             print("O RH esta contratando novos devs...")
#         else:
#             print("Erro, nenhum trabalhador encontrado...")
            
# Exemplo de classe com o conceito
class Programmer:
    def make(self):
        print("Programador esta criando codigo...")
        
class Seller:
    def make(self):
        print("O Vendedor esta vendendo produto...")

class RH:
    def make(self):
        print("O RH esta contratando novos devs...")

class Company:
    def do_work(self, worker: any) -> None:
        worker.make()

programmer = Programmer()
seller = Seller()
rh = RH()
company = Company()

company.do_work(programmer)
company.do_work(seller)
company.do_work(rh)