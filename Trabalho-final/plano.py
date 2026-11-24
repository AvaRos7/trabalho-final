from datetime import date

class Plano:
    def __init__(self, valor_plano, data_assinatura, aluno):
        self.__valor_plano = valor_plano
        self.__data_assinatura = date
        self.__aluno = aluno
        self.__aluno_pagou = True

    @property
    def valor_plano(self):
        return self.__valor_plano

    @property
    def data_assinatura(self):
        return self.__data_assinatura

    @property
    def aluno_pagou(self):
        if self.__data_assinatura + 30 > date.today():
            self.__aluno_pagou = False
        else:
            self.__aluno_pagou = True

    
    def checar_vencimento(self):
        if self.__aluno_pagou == True:
            return f"Plano em dia.\nData do próximo pagamento: {self.__data_assinatura + 30}."
        else:
            return f"Plano venceu no dia {self.__data_assinatura + 30}."

    
    