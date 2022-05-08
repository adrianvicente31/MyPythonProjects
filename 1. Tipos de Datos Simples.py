# Ejercicio 1
print('¡Hola, mundo!')

# Ejercicio 2
greet = '¡Hola, mundo!'
print(greet)

# Ejercicio 3
name = str(input('Inserta tu nombre: '))
print(f'¡Hola, {name}!')

# Ejercicio 4
print(((3+2)/(2*5))**2)

# Ejercicio 5
workthours = float(input('Inserte el número de horas trabajadas: '))
costperhour = float(input('Inserte el costo por hora: '))
print(f'Usted recibo el siguiente monto de pago: {costperhour * costperhour}')

# Ejercicio 6
n = int(input('Inserte un número entero positivo'))
print(f'La suma de los {n} primeros números enteros positivos es: {(n*(n+1))/2}')

# Ejercicio 7
peso = float(input('Inserte su peso (en Kg.): '))
estatura = float(input('Inserte su estatura (en Mtrs.): '))
imc = round(peso / (estatura**2), 2)
print(f'Tu índice de masa corporal es: {imc}')

# Ejercicio 8
dividendo = int(input('Inserte un número entero positivo: '))
divisor = int(input('Inserte otro número entero positivo: '))
c = dividendo // divisor
r = dividendo % divisor
print(f'{dividendo} entre {divisor} da un cociente: {c} y un resto: {r}')

# Ejercicio 9
budget = float(input('Inserte la cantidad a invertir: '))
interest_rate = float(input('Inserte la tasa de interes en % (anual): '))/100
year = float(input('Inserte el número de años a invertir: '))
interest = round(budget * (1 - ((1 + interest_rate)**year)), 2)
print(f'El capital obtenido en la inversión es: {interest}')

# Ejercicio 10
payaso = int(input('Inserte el número de payasos: '))
muñeca = int(input('Inserte el número de muñecas: '))
payaso_peso = 112
muñeca_peso = 75
print(f'El peso total del paquete a enviar es {(payaso * payaso_peso + muñeca * muñeca_peso)/100} kg.')

# Ejercicio 11
deposito = float(input('Inserte la cantidad a depositar: '))
for i in range(0, 4):
    print(f'El deposito en el año {i}: {round(deposito * ((1 + 0.04)**(i)), 2)}')

# Ejercicio 12
price = 3.49
discount = 60/100
unfresh = int(input('Inserte el número total de panes no frescos: '))
print(f'El precio unitario de pan freso: {price}')
print(f'El descuento por pan no fresco: {round(discount, 2)*100}%')
print(f'El valor de venta total es: {round(unfresh * price * (1 - discount), 2)}')