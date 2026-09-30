# BOLETIN 4 - CONDICIONALES
from pip._internal import self_outdated_check

print("-----------------------")
print("---------EJERCICIO 1--------------")
# Un almacén clasifica os seus produtos segundo a seguinte táboa de vendas anuais:
# Vendas anuais     Artigo de consumo
# < = 100 produtos			baixo
# >100 e < = 500			medio
# > 500 e < = 1000			alto
# > 1000 				primeira necesidade
# Coñecido o nome do artigo e as vendas anuais, que se introducen por teclado, indicar de que tipo é mostrandoo por pantalla

artigoConsumo = input("Introduce el nome o artigo de consumo: ")
vendasAnuais = int(input("Introduce el número de ventas anuales de dicho artigo: "))

if 0 <= vendasAnuais <= 100:
    print(f"El artigo {artigoConsumo} es un tipo de artigo de cosumo baixo.")
elif 100 < vendasAnuais <= 500:
    print(f"El artifo {artigoConsumo} es un tipo de artigo de cosumo medio.")
elif 500 < vendasAnuais <= 1000:
    print(f"El artigo {artigoConsumo} es un tipo de artigo de cosumo alto.")
elif 1000 < vendasAnuais:
    print(f"El artigo {artigoConsumo} es un tipo de artigo de cosumo de primera necesidade.")
else:
    print("Error")

print("-----------------------")

print("-----------------------")
print("---------EJERCICIO 2--------------")
# Codifica un programa que, utilizando un menú de opcións, calcule a superficie de distinto tipo de figuras.
# O usuario seleccionará a opción desexada escribindo a opción. Segundo esta, o programa pediralle os datos necesarios para realizar o cálculo, visualizará o resultado .
# No caso de premer unha opción que non teña o menú visualizar unha mensaxe de “Opción incorrecta “.
# 1…. Cadrado
# 2…. Triangulo
# 3…. Círculo

valor = int(input("Introduce qué opción deseas para calcular su área: 1. Triangulo - 2. Cuadrado - 3. Ciruclo"))

# switch case de python
match valor:
    case 1:
        lado = int(input("Dame el lado en cm: "))
        areaC = (lado*lado)
        print(f"El area del cuadrado es {areaC} cm^2")
    case 2:
        base = int(input("Dame la base en cm: "))
        altura = int(input("Dame la altura en cm: "))
        areaT = (base*altura)/2
        print(f"El area del cuadrado es {areaT} cm^2")
    case 3:
        radio = float(input("Dame el radio en cm: "))
        areaR = (3.14*(radio**2)) # ** es potencia
        print(f"El area del círculo es {areaR:.2f} cm^2") # ".2f" indica cuántos decimales quiero y con la "f" de que es un float
    case _:
        print("Opcion invalida")

print("-----------------------")

print("-----------------------")
print("---------EJERCICIO 3--------------")
# Utiliza o operador ternario(if - else) para calcular o valor absoluto dun número que se solicita o usuario por teclado.
numero = float(input("Introduce un número: "))
# valor_absoluto = abs(numero) # con abs() sirve para sacar el valor absoluto, pero me piden if - else
if numero >= 0:
    valorAbsoluto = numero
    print(f"El valor absoluto de {numero} es: {valorAbsoluto}")
else :
    valorAbsoluto = -numero
    print(f"El valor absoluto es: {valorAbsoluto}")

print("-----------------------")

print("-----------------------")
print("---------EJERCICIO 4--------------")
#  Escribe un programa que solicite o usuario un número comprendido entre 1 y 99.
#  O programa ten que mostrarlo con letras, por exemplo, para o 56, mostrará: “Cincuenta y seis”.

numerito = int(input("Dame un número entero comprendido entre 1 e 99: "))

decenas = int(numerito / 10)
unidades = int(numerito - (decenas * 10))

def f_decena():
    # EL RETURN SIRVE EN FUNCIONES PARA DEVOLVER ALGO PARA UTILIZARLO DESPUÉS

    match decenas:
        case 0:
            return ""
        case 1:
            if unidades == 0:
                return "Diez"
            else:
                return "Dieci"
        case 2:
            if unidades == 0:
                return "Veinte"
            else:
                return "Veinti"
        case 3:
            return "Treinta"
        case 4:
            return "Cuarenta"
        case 5:
            return "Cincuenta"
        case 6:
            return "Sesenta"
        case 7:
            return "Setenta"
        case 8:
            return "Ochenta"
        case 9:
            return "Noventa"
        case _:
            return "Error en las decenas "
def f_unidades():
    # EL RETURN SIRVE EN FUNCIONES PARA DEVOLVER ALGO PARA UTILIZARLO DESPUÉS

    match unidades:
        case 0:
            return "cero"
        case 1:
            if decenas == 1:
                return "Once"
            else:
                return "uno"
        case 2:
            if decenas == 1:
                return "Doce"
            else:
                return "dos"
        case 3:
            if decenas == 1:
                return "Trece"
            else:
                return "tres"
        case 4:
            if decenas == 1:
                return "Catorce"
            else:
                return "cuatro"
        case 5:
            if decenas == 1:
                return "Quince"
            else:
                return "cinco"
        case 6:
            return "seis"
        case 7:
            return "siete"
        case 8:
            return "ocho"
        case 9:
            return "nueve"
        case _:
            return "Error en unidades "


adicion = " y "

if decenas == 0: # Para unidades
    print(f_unidades())
elif decenas >= 1: # Para decenas
    if decenas == 1 and unidades >=6: # Del 16 al 19
        print(f_decena() + f_unidades())
    elif decenas == 1 and unidades <6: # Del 10 al 15
        print(f_unidades())
    elif decenas == 2 and unidades >= 1: # Del 21 al 29
        print(f_decena() + f_unidades())
    elif (unidades == 0) and (decenas >= 1): # Decenas
        print(f_decena())
    else:
        print(f_decena() + adicion + f_unidades()) #Del 30 al 99

else :
    print("Error")
print("-----------------------")

print("-----------------------")
print("---------EJERCICIO 5--------------")
# O DNI ten unha parte numérica de i díxitos seguido dunha letra que se obtén a partir do número da seguinte forma:
# letra = número DNI % 23.
# Deseña unha aplicación na que, dado un número de DNI, calcule a letra que lle corresponde.
# Observa que un número de 8 díxitos entra dentro do rango dun tipo int.

dni = input("Bienvenido a la poli, dame tu número de DNI y yo te diré su letra final: ")
if len(dni) == 8 and dni.isdigit():
    calcLetra = int(dni) % 23

    match calcLetra:
        case 0:
            print(f"La letra es: A")
            print(f"DNI: {dni}A")
        case 1:
            print(f"La letra es: B")
            print(f"DNI: {dni}B")
        case 2:
            print(f"La letra es: C")
            print(f"DNI: {dni}C")
        case 3:
            print(f"La letra es: D")
            print(f"DNI: {dni}D")
        case 4:
            print(f"La letra es: E")
            print(f"DNI: {dni}E")
        case 5:
            print(f"La letra es: F")
            print(f"DNI: {dni}F")
        case 6:
            print(f"La letra es: G")
            print(f"DNI: {dni}G")
        case 7:
            print(f"La letra es: H")
            print(f"DNI: {dni}H")
        case 8:
            print(f"La letra es: I")
            print(f"DNI: {dni}I")
        case 9:
            print(f"La letra es: J")
            print(f"DNI: {dni}J")
        case 10:
            print(f"La letra es: K")
            print(f"DNI: {dni}K")
        case 11:
            print(f"La letra es: L")
            print(f"DNI: {dni}L")
        case 12:
            print(f"La letra es: M")
            print(f"DNI: {dni}M")
        case 13:
            print(f"La letra es: N")
            print(f"DNI: {dni}N")
        case 14:
            print(f"La letra es: O")
            print(f"DNI: {dni}O")
        case 15:
            print(f"La letra es: P")
            print(f"DNI: {dni}P")
        case 16:
            print(f"La letra es: Q")
            print(f"DNI: {dni}Q")
        case 17:
            print(f"La letra es: R")
            print(f"DNI: {dni}R")
        case 18:
            print(f"La letra es: S")
            print(f"DNI: {dni}S")
        case 19:
            print(f"La letra es: T")
            print(f"DNI: {dni}T")
        case 20:
            print(f"La letra es: U")
            print(f"DNI: {dni}U")
        case 21:
            print(f"La letra es: V")
            print(f"DNI: {dni}V")
        case 22:
            print(f"La letra es: W")
            print(f"DNI: {dni}W")
        case _:
            print("Error")

else:
    print("Error. El DNI debe tener 8 dígitos")


print("-----------------------")