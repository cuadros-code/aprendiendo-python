# * -> significa que es una LISTA
# _ ignorar elemento
# *_ Ignora y no asigna elementos
# *resto crear una variable y lo asigna como una lista

numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)
uno, dos, tres, cuatro, *resto_de_numeros = numeros

print(uno)
print(dos)
print(tres)
print(cuatro)

print(resto_de_numeros)


