# --------------------------------------------
# Introdução ao NumPy: Criação e manipulação de arrays
# --------------------------------------------
# NumPy é uma biblioteca poderosa para computação numérica em Python,
# amplamente usada em análise de dados, ciência de dados e machine learning.

import numpy as np

# --------------------------------------------
# 1. O que é um array do NumPy?
# --------------------------------------------
# Um array (ndarray) é uma estrutura de dados que armazena valores de forma eficiente,
# permitindo operações vetoriais e matriciais rápidas.

minha_lista = [1, 2, 3]                        # Lista padrão do Python
meu_array = np.array(minha_lista)             # Convertendo lista em array NumPy
print("Array 1D criado a partir de uma lista:", meu_array)

# --------------------------------------------
# 2. Criando uma matriz (array 2D)
# --------------------------------------------
minha_matriz = [[1, 2, 3], [4, 5, 6]]          # Lista de listas (matriz 2x3)
meu_array_matriz = np.array(minha_matriz)     # Convertendo para array NumPy
print("Soma de todos os elementos da matriz:", np.sum(meu_array_matriz))

# --------------------------------------------
# 3. Criando arrays com valores em sequência
# --------------------------------------------
array = np.arange(1, 100)                     # Cria array de 1 até 99
print("Array com valores de 1 a 99:", array)

# --------------------------------------------
# 4. Criando array com valores iguais a 1
# --------------------------------------------
array_matriz = np.ones([3, 3, 3])             # Cria array 3x3x3 preenchido com 1.0
print("Matriz 3x3x3 com apenas 1s:", array_matriz)

# --------------------------------------------
# 5. Gerando números aleatórios
# --------------------------------------------
random_ = np.random.rand(2)                   # Gera 2 números aleatórios entre 0.0 e 1.0
print("Array com 2 números aleatórios:", random_)
