nombre = 'kevin'
apellido= 'cuadros'

# Concatenar cadenas
nombre_completo = 'Mr %s %s' %(nombre, apellido)
print(nombre_completo)

nombre_completo = 'Mr {} {}'.format( nombre, apellido )
print(nombre_completo)
