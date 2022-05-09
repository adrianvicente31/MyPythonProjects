# Ejercicio 1
nombre = input('Inserte el nombre de usuario: ').capitalize()
numero = int(input('Inser un número entero positivo: '))
for i in range(0, numero):
    print(nombre)

# Ejercicio 2
nombre = input('Inserte su nombre completo: ')
print(f'El nombre completo en minuscula: {nombre.lower()}')
print(f'El nombre completo en mayuscula: {nombre.upper()}')
print(f'El nombre completo en titulo: {nombre.title()}')

# Ejercicio 3
nombre = input('Inserte su nombre: ').upper()
n = len(nombre)
print(f'{nombre} tiene {n} letras.')

# Ejercicio 4
telefono = input('Inserte su número de teléfono: ')
print('El número de teléfono es:', telefono[4:-3])

# Ejercicio 5
frase = input('Inserte una frase: ')
print(frase[::-1])

# Ejercicio 6
frase = input('Inserte una frase: ').lower()
vocal = input('Inserte una vocal: ').lower()
print(frase.replace(vocal, vocal.upper()))  

# Ejercicio 7
correo = input('Insertar su correo personal: ')
usuario = correo[:correo.find('@')]
print(f'Su nuevo correo institucional: {usuario}@ceu.es')

# Ejercicio 8
precio = str(round(float(input('Inserte el precio del producto: ')), 2))
print(f'La cantidad de euros: {int(precio[:precio.find(".")])} euros.')
print(f'La cantidad de centavos: {int(precio[precio.find(".")+1:])} centavos.')

# Ejercicio 9
fecha = input('Insertar su fecha de nacimiento (dd/mm/aa): ')
dia = fecha[:fecha.find('/')]
mes = fecha[fecha.find('/')+1:fecha.find('/', 3)]
año = fecha[fecha.find('/', 3)+1:]
print(f'El dia de nacimiento: {int(dia)}')
print(f'El mes de nacimiento: {int(mes)}')
print(f'El año de nacimiento: {int(año)}')

# Ejercicio 10
cesta = input('Escriba su cesta de la compra, separados por comas (,): ')
print(cesta.replace(', ', '\n'))

# Ejercicio 11
product = input('Insertar el nombre del product: ').capitalize()
price =  float(input(f'Insertar el price de {product}: '))
amount = int(input(f'Insertar la amount de {product}: '))
print(f'{product}: {price:9.2f} soles * {amount:3d} unidades = {price * amount: 11.2f} soles.')