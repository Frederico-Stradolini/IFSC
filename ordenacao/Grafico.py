from Ordenar import Ordenar
import matplotlib.pyplot as plt

o=Ordenar()
cores_barras = ['green', '#00FF00', 'yellow', 'orange', '#fc4e03', 'red']
fonte_titulo = {'fontsize': 16, 'fontweight': 'bold'}
fonte = {'fontsize': 12, 'fontweight': 'bold'}

dados_ordenados = sorted(zip(o.algoritmos, o.tempos_medios), key=lambda x: x[1])
algoritmos_ordenados, tempos_medios_ordenados = zip(*dados_ordenados)

plt.figure(figsize=(8,6))
plt.bar(algoritmos_ordenados, tempos_medios_ordenados, color=cores_barras)
plt.xlabel('Algoritmo de Ordenação', fontdict=fonte)
plt.ylabel('Tempo Médio (segundos)', fontdict=fonte)
plt.title('Tempo Médio de Ordenação', fontdict=fonte_titulo)
plt.show()