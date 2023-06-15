import numpy as np

class vetor:
    def __init__(self, valores, tamanho):
        self.tamanho = tamanho
        self.valores = valores

    # Cria um vetor aleatório com valores entre 0 e "valores", e de tamanho "tamanho"
    def criar_vetor(self):
        vetor = np.random.randint(self.valores, size = self.tamanho)
        return vetor