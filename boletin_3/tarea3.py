# BOLETÍN 3

print("-----------------------")
print("---------EJERCICIO 1--------------")
# Codifica un programa que solicite un número por teclado e que saque un mensaxe que diga “É un número positivo”,
# sempre que cumpra esa condición.

numero= int(input("Introduce el número: "))

if numero>0:
    print("É un número positivo")
else:
    print("É un número negativo")

print("-----------------------")

print("-----------------------")
print("---------EJERCICIO 2--------------")
# Escribe un programa no que se tecleen dous números.
# Se o primeiro é maior ou igual que o segundo,visualizaremos a resta. En calquera caso visualizaremos a suma.
numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))

if numero1>=numero2:
    resta = numero1 - numero2
    print(f"La resta es: {resta}")
else:
    suma = numero1 + numero2
    print(f"La suma es: {suma}")

print("-----------------------")

print("-----------------------")
print("---------EJERCICIO 3--------------")
# Codificar o programa que o teclear un número por teclado,
# mostre por consola o signo “ + “ se o número é positivo, o signo “ –“ se é negativo e “ 0 “ se é cero.
numerito = int(input("Introduce el número: "))
if  numerito>0:
    print(" + ")
elif numerito<0:
    print(" - ")
else :
    print(" 0 ")

print("-----------------------")


print("-----------------------")
print("---------EJERCICIO 4--------------")
# Coñecidos, o nome e o peso de dúas persoas,
# o programa escribirá por consola os datos da persoa que pesa máis e a diferenza de peso entre elas.

nome1 = str(input("Introduce tu nombre: "))
peso1 = float(input("Introduce tu peso: "))
print(f"Persoa 1: {nome1} y peso: {peso1} kg")

nome2 = str(input("Introduce tu nombre: "))
peso2 = float(input("Introduce tu peso: "))
print(f"Persoa 2: {nome2} y peso: {peso2} kg")

if peso1>peso2:
    print(f"La persona que pesa más es {nome1} y la diferencia de peso es {peso1 - peso2} kg")

elif peso1<peso2:
    print(f"La persona que pesa más es {nome2} y la diferencia de peso es {peso2 - peso1} kg")

elif peso1==peso2:
    print(f"Ambas personas pesan lo mismo.")


print("-----------------------")
print("---------EJERCICIO 5--------------")
# Dados 3 números que se supoñen distintos, indicar cal é o maior.
n1 = int(input("Introduce el primer número: "))
n2 = int(input("Introduce el segundo número: "))
n3 = int(input("Introduce el tercer número: "))

if n1!=n2!=n3:
    if n1>n2 and n1>n3:
        print(f"El número mayor es {n1}")
    elif n2>n1 and n2>n3:
        print(f"El número mayor es {n2}")
    else:
        print(f"El número mayor es {n3}")
print("-----------------------")