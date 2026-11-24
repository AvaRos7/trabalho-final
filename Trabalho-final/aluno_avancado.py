from aluno_iniciante import AlunoIniciante
from plano import Plano

class AlunoAvancado(AlunoIniciante):
    def __init__(self, nome, idade, plano):
        super().__init__(idade, nome, plano)

    def exibir_identificacao(self):
        return super().exibir_identificacao()
        