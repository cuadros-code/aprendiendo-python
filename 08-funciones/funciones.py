# Separar las funciones con dos espacios

def suma ( a, b ):
  return a + b

print(suma(1,2))

# Enviar n cantidad de argumentos
def promedio(*args):
  return sum(args) / len(args)

resultado = promedio( 1, 3, 4)
print(resultado)

# Valores por defecto
def suma ( a, b=3 ):
  return a + b

print(suma(1,2))

# Argumentos como diccionarios
# {'kevin': [10, 20], 'julio': [4, 2, 5]}
def usuarios(**kwargs):
  print(kwargs)

usuarios( kevin=[10, 20], julio=[4, 2, 5] )