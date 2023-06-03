import numpy as np
from Vetor import vetor

class Algoritmos_sort:
    def bubble_sort(self, vetor):
        ultimo = len(vetor)
        while ultimo != 0:
            for i in range(ultimo-1):
                if vetor[i] > vetor[i+1]:
                    aux = vetor[i]
                    vetor[i] = vetor[i+1]
                    vetor[i+1] = aux
            ultimo-=1

    def selection_sort(self, vetor):
        menor = 0
        while menor < len(vetor):
            for i in range(menor+1, len(vetor)):
                if vetor[i] < vetor[menor]:
                    aux = vetor[menor]
                    vetor[menor] = vetor[i]
                    vetor[i] = aux
            menor += 1

    def insertion_sort(self, vetor):
        for i in range(1, len(vetor)):
            chave = vetor[i]
            j = i - 1
            while j >= 0 and vetor[j] > chave:
                vetor[j + 1] = vetor[j]
                j -= 1
            vetor[j + 1] = chave