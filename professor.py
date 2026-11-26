from pessoa_abstrato import Pessoa

class Professor(Pessoa):
    def __init__(self, nome, idade, aulas_realizadas):
        super().__init__(nome, idade)
        self.__aulas_realizadas = aulas_realizadas

    def exibir_identificacao(self):
       return super().exibir_identificacao() + f"\nAulas realizadas na academia: {self.__aulas_realizadas}"
