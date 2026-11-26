from abc import ABC, abstractmethod

class Historico(ABC):
    def __init__(self, pessoa):
        self.__pessoa = pessoa
        self.__contador_aulas = 0
        self.__aulas_realizadas = 0
    
    @property
    def pessoa(self):
        return self.__pessoa
    
    def gerar_historico(self):
        #Aqui vai ter try/except no main para não dar erro (zero division error)
        return "Frequência: ", self.__contador_aulas / self.__aulas_realizadas
    
    def realizar_aula(self):
        if True: #(aluno avancado ou aluno iniciantes confirmou presença no tatame)
            self.__contador_aulas = self.__contador_aulas + 1
        else:
            #(não sei ainda o que vai ser o else. Acho q vai ser try/except no main)
