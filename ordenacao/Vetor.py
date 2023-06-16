import numpy as np
import random

class vetor:
    def __init__(self, valores, tamanho):
        self.tamanho = tamanho
        self.valores = valores

    # Cria um vetor aleatório com valores entre 0 e "valores", e de tamanho "tamanho"
    def criar_vetor(self):
        vetor = list(range(5000)) # ordenado
        # vetor = list(range(10000, 0, -1)) # reverso
        # vetor = random.sample(range(50000), 50000) # desordenados
        # vetor = [1] * 10000 # valores iguais

        # vetor = np.random.randint(self.valores, size = self.tamanho)
        return vetor