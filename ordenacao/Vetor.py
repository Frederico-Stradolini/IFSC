import numpy as np

class vetor:
    def __init__(self, valores, tamanho):
        self.tamanho = tamanho
        self.valores = valores

    # Cria um vetor aleatório com valores entre 0 e "valores", e de tamanho "tamanho"
    def criar_vetor(self):
        # vetor = np.random.randint(self.valores, size = self.tamanho)
        vetor = [12, 9, 6, 2, 16, 14, 1, 9, 11, 4, 8, 19, 2, 5, 12, 3]
        return vetor