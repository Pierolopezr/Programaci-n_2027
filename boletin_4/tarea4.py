# BOLETIN 4 - CONDICIONALES

print("-----------------------")
print("---------EJERCICIO 1--------------")

print("-----------------------")

print("-----------------------")
print("---------EJERCICIO 2--------------")
# Codifica un programa que, utilizando un menú de opcións, calcule a superficie de distinto tipo de figuras.
# O usuario seleccionará a opción desexada escribindo a opción. Segundo esta, o programa pediralle os datos necesarios para realizar o cálculo, visualizará o resultado .
# No caso de premer unha opción que non teña o menú visualizar unha mensaxe de “Opción incorrecta “.
# 1…. Cadrado
# 2…. Triangulo
# 3…. Círculo

valor = int(input("Introduce qué opción deseas para calcular su área: "))

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
print("-----------------------")