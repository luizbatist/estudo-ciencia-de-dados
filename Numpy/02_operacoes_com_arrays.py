# --------------------------------------------
# 02 - Operações Aritméticas com Arrays NumPy
# --------------------------------------------
# Este script mostra como realizar operações matemáticas entre arrays e com escalares,
# incluindo soma, subtração, multiplicação, divisão, potenciação e raiz quadrada.

import numpy as np

# --------------------------------------------
# 1. Criação dos Arrays
# --------------------------------------------
array1 = np.arange(0, 100, 10)  # Cria array de 0 a 90, de 10 em 10
array2 = np.arange(0, 50, 5)    # Cria array de 0 a 45, de 5 em 5

print("Array 1:", array1)
print("Array 2:", array2)

# --------------------------------------------
# 2. Operações Aritméticas Entre Arrays
# --------------------------------------------
# As operações são feitas elemento por elemento (element-wise)
print("Soma:", array1 + array2)
print("Subtração:", array1 - array2)
print("Multiplicação:", array1 * array2)
print("Divisão:", array1 / array2)  # Cuidado com divisão por zero (gera NaN ou inf)

# 💡 Observação:
# NaN = "Not a Number", aparece quando há operação inválida como divisão por zero

# --------------------------------------------
# 3. Outras Operações Numéricas
# --------------------------------------------
quadrado = array1 ** 2
print("Quadrado dos elementos:", quadrado)

raiz = np.sqrt(array1)
print("Raiz quadrada dos elementos:", raiz)

# --------------------------------------------
# 4. Operações com Escalares
# --------------------------------------------
multiplicacao_escalar = array1 * 100
print("Multiplicação por escalar:", multiplicacao_escalar)

soma_escalar = array1 + 100
print("Soma com escalar:", soma_escalar)
