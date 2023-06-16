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

    def shell_sort(self, vetor):
        n = len(vetor)
        h = 1
        while h < n // 3:
            h = 3 * h + 1
        while h >= 1:
            for i in range(h, n):
                chave = vetor[i]
                j = i
                while j >= h and vetor[j - h] > chave:
                    vetor[j] = vetor[j - h]
                    j -= h
                vetor[j] = chave
            h //= 3
    
    def merge_sort(self, vetor):
        # Caso base: se o vetor tiver tamanho 1, retorna o próprio vetor.
        if len(vetor) <= 1:
            return vetor

        # Divide o vetor ao meio, separando em left e right.
        mid = len(vetor) // 2
        left = vetor[:mid]
        right = vetor[mid:]

        # Chamada recursiva para dividir os subvetores. Cria uma nova instância da função, com suas próprias variáveis e parâmentros, gerando uma pilha de instâncias.
        left = self.merge_sort(left)
        right = self.merge_sort(right)

        # Retorna a combinação dos subvetores ordenados.
        return self.merge(left, right)

    def merge(self, left, right):
        merged = []
        i = j = 0

        # Comparação e mesclagem dos elementos dos subvetores.
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

        # Adiciona os elementos restantes de left, se houver.
        while i < len(left):
            merged.append(left[i])
            i += 1
        # Adiciona os elementos restantes de right, se houver.
        while j < len(right):
            merged.append(right[j])
            j += 1
        # print(merged)
        return merged

    def quick_sort(self, arr):
        if len(arr) <= 1:
            return arr
        
        stack = []
        stack.append((0, len(arr) - 1))
        
        while stack:
            start, end = stack.pop()
            pivot_index = self.partition(arr, start, end)
            
            if pivot_index - 1 > start:
                stack.append((start, pivot_index - 1))
            
            if pivot_index + 1 < end:
                stack.append((pivot_index + 1, end))
        
        return arr

    def partition(self, arr, start, end):
        pivot = arr[start]
        left = start + 1
        right = end
        
        while True:
            while left <= right and arr[left] <= pivot:
                left += 1
            
            while right >= left and arr[right] >= pivot:
                right -= 1
            
            if right < left:
                break
            
            arr[left], arr[right] = arr[right], arr[left]
    
        arr[start], arr[right] = arr[right], arr[start]
        return right
