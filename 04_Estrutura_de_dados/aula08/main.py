# Arrays
from array import array

letras = ['A', 'B', 'C', 'D']
numeros_int = [0, 1, 2, 3, 4]
numeros_flt = [1.2, 2.2, 3.3, 4.4]

print(letras)
print(numeros_int)
print(numeros_flt)
print()

array_letras = array('u', letras)
array_numeros_int = array('i', numeros_int)
array_numeros_flt = array('f', numeros_flt)

print(array_letras)
print(array_numeros_int)
print(array_numeros_flt)
