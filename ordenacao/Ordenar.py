import timeit
from Algoritmos import Algoritmos_sort
from Vetor import vetor

class Ordenar:
    # valores = int(input('Gerar valores de 0 até: '))
    # tamanho = int(input('Digite o tamanho do vetor: '))
    a=Algoritmos_sort()
    v=vetor(20,32)
    
    tempo_total = 0
    tempos_medios = []
    algoritmos = []

    # Medindo tempo médio de ordenação do bubble sort
    for i in range(0,10):
        vetor_aleatorio = v.criar_vetor()
        
        tempo_inicial = timeit.default_timer()
        a.bubble_sort(vetor_aleatorio.copy())
        tempo_final = timeit.default_timer()
        
        tempo_total += tempo_final - tempo_inicial

    tempo_medio = tempo_total / 10
    tempos_medios.append(tempo_medio)
    algoritmos.append('Bubble')
    print(f'Tempo médio Bubble Sort: {tempo_medio :.2f}')

    tempo_total = 0

    # Medindo tempo médio de ordenação do selection sort
    for i in range(0,10):
        vetor_aleatorio = v.criar_vetor()
        
        tempo_inicial = timeit.default_timer()
        a.selection_sort(vetor_aleatorio.copy())
        tempo_final = timeit.default_timer()
        
        tempo_total += tempo_final - tempo_inicial

    tempo_medio = tempo_total / 10
    tempos_medios.append(tempo_medio)
    algoritmos.append('Selection')
    print(f'Tempo médio Selection Sort: {tempo_medio :.2f}')

    tempo_total = 0

    # Medindo tempo médio de ordenação do insertion sort
    for i in range(0,10):
        vetor_aleatorio = v.criar_vetor()
        
        tempo_inicial = timeit.default_timer()
        a.insertion_sort(vetor_aleatorio.copy())
        tempo_final = timeit.default_timer()
        
        tempo_total += tempo_final - tempo_inicial

    tempo_medio = tempo_total / 10
    tempos_medios.append(tempo_medio)
    algoritmos.append('Insertion')
    print(f'Tempo médio Insertion Sort: {tempo_medio :.2f}')

    tempo_total = 0

    # Medindo tempo médio de ordenação do shell sort
    for i in range(0,10):
        vetor_aleatorio = v.criar_vetor()
        
        tempo_inicial = timeit.default_timer()
        a.shell_sort(vetor_aleatorio.copy())
        tempo_final = timeit.default_timer()
        
        tempo_total += tempo_final - tempo_inicial

    tempo_medio = tempo_total / 10
    tempos_medios.append(tempo_medio)
    algoritmos.append('Shell')
    print(f'Tempo médio Shell Sort: {tempo_medio :.2f}')

    tempo_total = 0

    # Medindo tempo médio de ordenação do merge sort
    for i in range(0,10):
        vetor_aleatorio = v.criar_vetor()
        
        tempo_inicial = timeit.default_timer()
        a.merge_sort(vetor_aleatorio.copy())
        tempo_final = timeit.default_timer()
        
        tempo_total += tempo_final - tempo_inicial

    tempo_medio = tempo_total / 10
    tempos_medios.append(tempo_medio)
    algoritmos.append('Merge')
    print(f'Tempo médio Merge Sort: {tempo_medio :.2f}')

    tempo_total = 0
    # Medindo tempo médio de ordenação do quick sort
    for i in range(0,10):
        vetor_aleatorio = v.criar_vetor()
        
        tempo_inicial = timeit.default_timer()
        a.quick_sort(vetor_aleatorio.copy())
        tempo_final = timeit.default_timer()
        
        tempo_total += tempo_final - tempo_inicial

    tempo_medio = tempo_total / 10
    tempos_medios.append(tempo_medio)
    algoritmos.append('Quick')
    print(f'Tempo médio Quick Sort: {tempo_medio :.2f}')