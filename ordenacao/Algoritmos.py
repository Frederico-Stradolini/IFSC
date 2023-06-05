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

    def shell_sort(self, lista):
        n = len(lista)
        h = 1
        while h < n // 3:
            h = 3 * h + 1
        while h >= 1:
            for i in range(h, n):
                chave = lista[i]
                j = i
                while j >= h and lista[j - h] > chave:
                    lista[j] = lista[j - h]
                    j -= h
                lista[j] = chave
            h //= 3
    
    def merge_sort(self, lista, inicio=0, fim=None):
        if fim is None:
            fim = len(lista)
        if(fim - inicio > 1):
            meio = (fim + inicio)//2
            self.merge_sort(lista, inicio, meio)
            self.merge_sort(lista, meio, fim)
            self.merge(lista, inicio, meio, fim)

    def merge(self, lista, inicio, meio, fim):
        left = lista[inicio:meio]
        right = lista[meio:fim]
        top_left, top_right = 0, 0
        for k in range(inicio, fim):
            if top_left >= len(left):
                lista[k] = right[top_right]
                top_right = top_right + 1
            elif top_right >= len(right):
                lista[k] = left[top_left]
                top_left = top_left + 1
            elif left[top_left] < right[top_right]:
                lista[k] = left[top_left]
                top_left = top_left + 1
            else:
                lista[k] = right[top_right]
                top_right = top_right + 1

    def quick_sort(self, lista, inicio=0, fim=None):
        if fim is None:
            fim = len(lista)-1
        if inicio < fim:
            p = self.partition(lista, inicio, fim)
            self.quick_sort(lista, inicio, p-1)
            self.quick_sort(lista, p+1, fim)

    def partition(self, lista, inicio, fim):
        pivot = lista[fim]
        i = inicio
        for j in range(inicio, fim):
            if lista[j] <= pivot:
                lista[j], lista[i] = lista[i], lista[j]
                i = i + 1
        lista[i], lista[fim] = lista[fim], lista[i]
        return i