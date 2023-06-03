import timeit
from Algoritmos import Algoritmos_sort
from Vetor import vetor

valores = int(input('Gerar valores de 0 até: '))
tamanho = int(input('Digite o tamanho do vetor: '))
a=Algoritmos_sort()
v=vetor(valores,tamanho)
tempo_total = 0


# Medindo tempo médio de ordenação do bubble sort
for i in range(0,10):
    vetor_aleatorio = v.criar_vetor()
    
    tempo_inicial = timeit.default_timer()
    a.bubble_sort(vetor_aleatorio.copy())
    tempo_final = timeit.default_timer()
    
    tempo_total += tempo_final - tempo_inicial

tempo_medio = tempo_total / 10
print(f'Tempo médio Bubble Sort: {tempo_medio :.2f}')


# Medindo tempo médio de ordenação do selection sort
for i in range(0,10):
    vetor_aleatorio = v.criar_vetor()
    
    tempo_inicial = timeit.default_timer()
    a.selection_sort(vetor_aleatorio.copy())
    tempo_final = timeit.default_timer()
    
    tempo_total += tempo_final - tempo_inicial

tempo_medio = tempo_total / 10
print(f'Tempo médio Selection Sort: {tempo_medio :.2f}')


# Medindo tempo médio de ordenação do insertion sort
for i in range(0,10):
    vetor_aleatorio = v.criar_vetor()
    
    tempo_inicial = timeit.default_timer()
    a.insertion_sort(vetor_aleatorio.copy())
    tempo_final = timeit.default_timer()
    
    tempo_total += tempo_final - tempo_inicial

tempo_medio = tempo_total / 10
print(f'Tempo médio Insertion Sort: {tempo_medio :.2f}')
