# --------------------------------------------
# 03 - Indexação e Comparações Lógicas com NumPy
# --------------------------------------------
# Este script mostra como acessar, modificar e filtrar dados em arrays NumPy
# usando indexação e operações booleanas.

import numpy as np

# --------------------------------------------
# 1. Introdução à Indexação em Arrays NumPy
# --------------------------------------------
# A indexação permite acessar ou modificar elementos específicos de arrays.
# Isso é essencial em análise de dados, onde queremos trabalhar com subconjuntos ou elementos específicos.

arr = np.arange(0, 30, 3)      # Cria array com valores de 0 a 27, pulando de 3 em 3
print("Array original:", arr)

print("Elemento de índice 5:", arr[5])  # Acessa o valor na posição 5 do array

arr[5:] = 100                  # Modifica todos os elementos a partir do índice 5
print("Array após modificação:", arr)

# --------------------------------------------
# 2. Arrays Multidimensionais (2D)
# --------------------------------------------
arr_2d = np.arange(50).reshape([5, 10])  # Cria uma matriz 5x10 com valores de 0 a 49
print("Matriz 2D (5x10):")
print(arr_2d)

# --------------------------------------------
# 3. Comparações Lógicas com Arrays
# --------------------------------------------
# Podemos fazer comparações elemento por elemento.
# O resultado será um array booleano (True/False)

print("Comparação lógica (arr_2d > 20):")
print(arr_2d > 20)

boleano = arr_2d > 20             # Array booleano: True onde arr_2d > 20
print("Valores maiores que 20 na matriz:")
print(arr_2d[boleano])           # Filtra e mostra apenas os valores maiores que 20
