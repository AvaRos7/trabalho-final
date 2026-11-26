from pessoa_abstrato import Pessoa
from plano import Plano

class AlunoIniciante(Pessoa):
    def __init__(self, nome, idade, plano):
        super().__init__(nome, idade)
        self.__plano = plano

    def exibir_identificacao(self):
        return super().exibir_identificacao() + f"Plano: {self.__plano}"