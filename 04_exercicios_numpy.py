# --------------------------------------------
# 04 - Exercícios Práticos com NumPy
# --------------------------------------------
# Este script contém exercícios simples e exemplos para praticar
# os principais conceitos de criação e manipulação de arrays NumPy.

import numpy as np

# --------------------------------------------
# 1. Criar um array de 1 até 10
# --------------------------------------------
arr1 = np.arange(1, 11)
print('Array de 1 até 10:', arr1)

# --------------------------------------------
# 2. Criar arrays de zeros e de uns
# --------------------------------------------
arr_zeros = np.zeros(5)
print("Array de zeros:", arr_zeros)

arr_ones = np.ones(5)
print("Array de uns:", arr_ones)

# --------------------------------------------
# 3. Criar um array com espaçamento linear
# --------------------------------------------
linear_space = np.linspace(0, 50, 10)
print("Espaçamento linear:", linear_space)

# --------------------------------------------
# 4. Criar uma matriz identidade
# --------------------------------------------
identity_matrix = np.identity(3)
print("Matriz identidade:")
print(identity_matrix)

# --------------------------------------------
# 5. Fazer fatiamento (slicing) em arrays
# --------------------------------------------
array = np.array([10, 20, 30, 40, 50])
print("Primeiros 3 elementos:", array[:3])

# --------------------------------------------
# 6. Operações matemáticas com arrays
# --------------------------------------------
array = np.array([1, 2, 3, 4, 5])
squared_array = array ** 2
print("Array ao quadrado:", squared_array)

array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
sum_array = array1 + array2
print("Soma de arrays:", sum_array)

# --------------------------------------------
# 7. Usar reshape para transformar arrays
# --------------------------------------------
array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
reshaped_array = array.reshape(3, 3)
print("Array reshape para 3x3:")
print(reshaped_array)

# --------------------------------------------
# 8. Gerar matriz de valores aleatórios
# --------------------------------------------
random_matrix = np.random.rand(4, 4)
print("Matriz aleatória 4x4:")
print(random_matrix)
