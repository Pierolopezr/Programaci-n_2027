# BOLETÍN 5 - BUCLES
import math


print("-----------------------")
print("---------EJERCICIO 1--------------")

# Escribir un ciclo definido para imprimir por pantalla tódolos números entre	10 e 20.
def ejercicio1():
    for numero in range (10, 20):
        print(numero)
#ejercicio1()
print("-----------------------")

print("-----------------------")
print("---------EJERCICIO 2--------------")

# Escribir un programa que converta un valor dado en grados Fahrenheit a grados Celsius.
# Recordade que a fórmula para a conversión é: F = 9/5 * C + 32.

def ejercicio2():
    while True:
        temperatura = input("Dame la temperatura en ºF y yo te la pasaré a Celsius. (Para salir: 'S'): ")

        if temperatura == "S":
            print("Saliendo ")
            break
        # Uso try except Value Error / para que el programa no se rompa cuando uso una letra diferente a S o a lo especificado
        # y me da un print
        try:
            temperatura = float(temperatura)
            celsius = (float(temperatura) - 32) * 5 / 9
            print(f"La temperatura es: {celsius:.1f} ºC")

        except ValueError:
            print("Introduce una temperatura valida")

#ejercicio2() # No es necesario un print porque dentro de la función ya termina con un print. Si hubiera return SÍ.

print("-----------------------")

print("-----------------------")
print("---------EJERCICIO 3--------------")
# Utiliza o programa anterior para xerar unha táboa de conversión de temperaturas, dende 0º F ata 120º F, de 10 en 10.
def ejercicio3():
    print("Táboa de conversión de temperaturas, dende 0º F ata 120º F, de 10 en 10. ")
    for num in range (0, 130,10): # Va llendo de 1o en 10

        celsius = (float(num) - 32) * 5 / 9
        print(f"La temperatura {num} ºF es: {celsius:.1f} ºC")

#ejercicio3() # No es necesario un print porque dentro de la función ya termina con un print. Si hubiera return SÍ.

print("-----------------------")

print("-----------------------")
print("---------EJERCICIO 4--------------")
# Escribir un programa que imprima tódolos números pares entre dous números que se lle pidan o usuario
def ejercicio4():
    print("Dame dos números y te daré los números pares que hay entre ellos: ")
    numero1= int(input("Dame el primer número: "))
    numero2= int(input("Dame el segundo número: "))
    fila = []

    if numero1 > numero2:
        for x in range (numero2, numero1):
            if x % 2 == 0:
                fila.append(x)
    elif numero2 > numero1:
        for x in range (numero1, numero2):
            if x % 2 == 0:
                fila.append(x)
    else:
        print("Error")

    print(f"Los números son: {fila}")

#ejercicio4()  # No es necesario un print porque dentro de la función ya termina con un print. Si hubiera return SÍ.
print("-----------------------")

print("-----------------------")
print("---------EJERCICIO 5--------------")
# Escribir un programa que reciba un número n por parámetro e imprima os primeiros n números triangulares, xunto co seu índice.
# Os números triangulares obteñense mediante a suma dos números naturales dende 1 ata n.
# É dicir, si se piden os primeros 5 números triangulares, o programa debe imprimir:
# 1 - 1
# 2 - 3
# 3 - 6
# 4 - 10
# 5 - 15
# Nota: facelo usando e sen usar a ecuación n ∗ (n + 1) / 2. Cal realiza máis operacións?
def ejercicio5():
    n = int(input("Dame un número n y te diré sus números triangulares: "))
    for x in range (1, n+1, 1): # equivalente x=1; x<=n; x++
        respuesta = x * ( x + 1) / 2
        print(f"{x} - {int(respuesta)}")

#ejercicio5()  # No es necesario un print porque dentro de la función ya termina con un print. Si hubiera return SÍ.
print("-----------------------")

print("-----------------------")
print("---------EJERCICIO 6--------------")
# Escribir un programa que tome unha cantidade m de valores ingresados polo usuario,
# a cada un lle calcule o factorial e imprima o resultado xunto co número de orden correspondiente.
def ejercicio6():
    valores = int(input("¿Cuántos valores vas a introducir?"))
    lista_no_resueltas = []
    lista_resueltas = []
    for x in range (1, valores+1):
        introduce = int(input(f"Dame el valor {x}: "))
        lista_no_resueltas.append(introduce) # Añade a una lista
        factorial = math.factorial(introduce) # Halla el factorial
        lista_resueltas.append(factorial)
    print(f"El factorial de {lista_no_resueltas} es: {lista_resueltas} respectivamente")

#ejercicio6()  # No es necesario un print porque dentro de la función ya termina con un print. Si hubiera return SÍ.
print("-----------------------")

print("-----------------------")
print("---------EJERCICIO 7--------------")
# Escribir un programa que imprima por pantalla tódalas fichas de dominó, de unha por liña e sen repetir
def ejercicio7():
    for x in range (0, 7):
        for y in range (x, 7): # se ejecutará siempre a partir de la variable x
            print(f"{x}/{y}")
#ejercicio7()
print("-----------------------")

print("-----------------------")
print("---------EJERCICIO 8--------------")
# Modificar o programa anterior para que poida xerar fichas dun xogo que pode ter números de 0 a n.
def ejercicio8():
    n = int(input("Dame un número n para que pueda xerar fichas al estilo dominó: "))
    for x in range (0, n):
        for y in range (x, n): # se ejecutará siempre a partir de la variable x
            print(f"{x}/{y}")
#ejercicio8()
print("-----------------------")

print("-----------------------")
print("---------EJERCICIO 9--------------")
# Calcula a cantidade de números negativos, positivos e ceros que hai nun grupo de 10 números enteiros.
def ejercicio9():

    print("Dame un grupo de 10 números enteros y lo clasificaré")
    numeros_no_clasificados = []
    numeros_clasificados = []

    for x in range(1, 11):

        while True:
            try:
                grupo = int(input(f"Dame el {x}º número: "))
                break
            except ValueError:
                print("Error. Introduce un número entero.")

        numeros_no_clasificados.append(grupo)

        if grupo > 0:
            grupo = "positivo"
            numeros_clasificados.append(grupo)

        elif grupo < 0:
            grupo = "negativo"
            numeros_clasificados.append(grupo)

        elif grupo == 0:
            grupo = "cero"
            numeros_clasificados.append(grupo)

    print(f"El grupo \n{numeros_no_clasificados} es: \n{numeros_clasificados} respectivamente")


#ejercicio9()
print("-----------------------")

print("-----------------------")
print("---------EJERCICIO 10--------------")
# Deseña un programa que calcule o área dun rectángulo cuxa base e altura pides por teclado.
# Asegúrate que estes valores sexan positivos, para eso valida os datos.
def ejercicio10():
    while True:
        try:
            base = int(input("Dame el base: "))
            altura = int(input("Dame el altura: "))
            area = (base * altura)
            print(f"El área del rectángulo es: {area} m2")
            break
        except ValueError:
            print("Error. Introduce una medida válida.")
#ejercicio10()
print("-----------------------")

print("-----------------------")
print("---------EJERCICIO 11--------------")
# Codifica un programa que solicite un número e visualice a táboa de multiplicar dese número.
# O programa seguirá pedindo números ata que o usuario pulse o número cero.
def ejercicio11():
    while True:
        try:
            num = int(input("Dame un número para darte su tabla de multiplicar: "))
            print(f"El tabla de multiplicar de {num} es: ")
            for x in range(0, 13):
                tabla_multi = num * x
                print(f"{num} x {x} = {tabla_multi}")
            if num == 0:
                print("Saliendo de las tablas de multiplicar")
                break
        except ValueError:
            print("Error. Introduce un número entero.")

#ejercicio11()

print("-----------------------")

print("-----------------------")
print("---------EJERCICIO 12--------------")
# Codifica un programa que lea o soldo de cada un dos traballadores dunha empresa e obteña o número deles que ganan entre 1000 e 1750 €,
# ámbolos dous incluídos e, a porcentaxe de traballadores que ganan menos de 1000 €.
# Tendo en conta que non se coñece con antelación o numero de traballadores da empresa e non se admiten os soldos negativos
# (utiliza como condición de fin un soldo 0).
def ejercicio12():
    trabajadores1 = []  # Trabajadores con sueldo entre 1000 y 1750 euros
    trabajadores2 = []  # Trabajadores con sueldo menos de 1000 euros
    total_trabajadores = []  # Todos los trabajadores
    while True:
        try:
            sueldo = float(input("Dame el sueldo de un trabajador: "))
            if sueldo == 0:
                print("Saliendo de sueldos")
                break
            elif sueldo < 0:
                print("Error. Introduce un número positivo: ")
                continue # Salta esta vuelta y vuelve a pedir otro sueldo

            total_trabajadores.append(sueldo)

            if 1000 <= sueldo <= 1750:
                trabajadores1.append(sueldo)
            elif 0 <sueldo < 1000:
                trabajadores2.append(sueldo)

        except ValueError:
            print("Error. Introduce un número válido")
    porcentaje = (len(trabajadores2) / len(total_trabajadores)) * 100
    print(f"Hay {len(trabajadores1)} trabajadores con sueldos entre 1000 y 1750 euros")
    print(f"Hay {len(trabajadores2)} trabajadores con sueldos menores a 1000 euros, que representan el {porcentaje:.1f}% de un total de {len(total_trabajadores)} trabajadores ")


#ejercicio12()

print("-----------------------")

print("-----------------------")
print("---------EJERCICIO 13--------------")
# Solicita o usuario un número n e debuxa un triángulo de base e altura n.
# Si o usuario teclea o número 4 o triángulo sería da seguinte forma:
#    *
#   * *
#  * * *
# * * * *

def ejercicio13():
    n = int(input("Introduce un número n para armar un triángulo de base y altura n: "))

    for x in range(1, n+1):
        for y in range (0, n-x): # si n=4 habrán en la primera habrán 3 espacios
            print (" ", end ="") # end significa que no hara salto de linea
        asterisco = x * "* "
        print(asterisco)
#ejercicio13()

print("-----------------------")

print("-----------------------")
print("---------EJERCICIO 14--------------")
# Codificar o programa que solicite 10 números por consola e calcule a súa suma. Si o usuario introduce en calquera momento o número 999,
# deixa de solicitar máis4 números e presenta o valor da súma acadada ata ese momento.
def ejercicio14():
    veces = 0
    suma = 0
    while veces < 10:
        numeros = int(input("Dame n números hasta 10 de ellos para poder calcula a suma. Introduce o número 999 para terminar en cualquier momento: "))
        if numeros == 999:
            print("Calculando suma...")
            break
        suma += numeros
        veces += 1
    print(f"La suma es: {suma}")
ejercicio14()

print("-----------------------")

print("-----------------------")







