# Array
lista = [ 'Perro', 'Gato', 'Raton', 'Camello', 'Hormiga', 'Zancudo' ]
lista[ len(lista) - 1 ] = 'Enano'
print( lista )

# Size
print( len(lista) )

# Cortar elementos ( sub lista )
#numero = int( input( 'Ingrese un numero: ' ) )
#nueva_lista = lista[0: numero]
#print(nueva_lista)

# Voltear elementos de lista
print( lista[::-1] )

# Añadir
lista.append('Mysql')
print( lista)

#Eliminar 
lista.remove('Mysql')
print( lista)
