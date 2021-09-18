elementos = {}

# Agregar 
elementos['nombre'] = 'Kevin Cuadros'

print( elementos )
print( len(elementos) )

dicc = { 'a': 1, 'b': 2, 'c': 3 }

# Obtener elementos
valor_1 = dicc['a']
valor_2 = dicc.get('v', 'parametro si no existe')

print(valor_1)
print(valor_2)

# keys
print( dicc.keys() )

# values
print( dicc.values() )

# items
print( dicc.items() )

# Eliminar elementos
dicc.pop('b')
del dicc['c']
print( dicc )