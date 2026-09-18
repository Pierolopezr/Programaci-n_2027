# BOLETIN 2


# 1. Deseña un algoritmo que calcule o área dun triángulo. A saída faise por pantalla. Para codificar este programa inicializa a base ao valor 4, e a altura ao valor 3.
#    Codifica este programa nun script chamado boletin2_1.
print("---------EJERCICIO 1--------------")
base = 4; altura = 3
area = (base * altura)/2
print(f"El area del triangulo es {area}")
print("-----------------------")
print("---------EJERCICIO 2--------------")
# 2. Realiza un ordinograma que permita calcular o área dun cadrado de 3 m de lado.
# De seguido crea un script, co nome boletin2_2, para executalo.

    #         ┌───────────┐
    #         │  INICIO   │
    #         └─────┬─────┘
    #               ↓
    #       ┌────────────────┐
    #       │   lado = 3     │
    #       └───────┬────────┘
    #               ↓
    #       ┌────────────────┐
    #       │ area = lado*lado│
    #       └───────┬────────┘
    #               ↓
    #       ┌──────────────────────┐
    #       │ Mostrar "Área = 9"   │
    #       └──────────┬───────────┘
    #                  ↓
    #         ┌─────────────┐
    #         │     FIN     │
    #         └─────────────┘

lado = 3
area = (lado * lado)
print(f"El area del cuadrado es {area}")
print("-----------------------")
print("---------EJERCICIO 3--------------")

# 3. Crea un algoritmo que cambie euros a dólares (O cambio pídese por teclado).
# Codifica o programa, correspondente, para executar o programa co nome boletin2_3

EU = 0.5
DOL = 0.8
n = input("Qué quieres cambiar euros a dólares o dólares a euros ¿?: ")
if n == "euros":
    moneda = int(input("Cuántos euros quieres cambiar ¿? "))
    cambioEUaDOL= moneda*DOL
    print(f"El cambio de {moneda} euros a dólares es {cambioEUaDOL} dólares.")

elif n == "dolares":
    moneda = int(input("Cuántos dólares quieres cambiar ¿? "))
    cambioDOLaEU= moneda*DOL
    print(f"El cambio de {moneda} dólares a euros {cambioDOLaEU} euros")
else:
    print("Error al escribir lo que desea.")

print("-----------------------")
print("---------EJERCICIO 4--------------")
# 4. Deseña un ordinograma que lea 2 números e calcule a suma, despois a resta, a continuación o produto e por último o cociente.
# Amosa o resultado de cada operación. De seguido codifica o programa correspondente.

a = int(input("Dame el primer número: "))
b = int(input("Dame el segundo numero: "))

# Declaro las funciones:

def sumar(x,y):
    return x+y
def restar(x,y):
    return x-y
def multiplicar(x,y):
    return x*y
def dividir(x,y):
    return x/y

print(f"Suma: {sumar(a,b)}")
print(f"Resta: {restar(a,b)}")
print(f"Multiplicación: {multiplicar(a,b)}")
print(f"Dividisión: {dividir(a,b)}")

print("-----------------------")
print("---------EJERCICIO 5--------------")
# 5. Escribe un programa que lea o valor dunha distancia en millas mariñas e a pase a metros ( 1 milla mariña = 1852 m ).
millas= int(input("Dame la distancia en millas marinas que quieres pasar a metros: "))
metros = millas*1852
print(f"La distancia en metros es: {metros} metros")

print("-----------------------")
print("---------EJERCICIO 6--------------")
# 6. Realiza o ordinograma correspondente a un programa que saque por pantalla a porcentaxe descontada nunha compra.
# Introducindo, por teclado, o prezo da tarifa e o prezo pagado.
tarifa = int(input("Dame el precio de la tarifa: "))
pagado = int(input("Dame el precio pagado: "))

porcentajeDescontado= (100*(tarifa-pagado))/tarifa
print(f"El porcentaje descontado es: {porcentajeDescontado} %")

print("-----------------------")
print("---------EJERCICIO 7--------------")
# 7. Realiza o ordinograma e despois codifica un programa que reciba como dato de entrada o valor dunha temperatura expresada en graos centígrados
# e calcule o seu equivalente en graos Fahrenheit e graos Kelvin.
Centigrados = float(input("Dame la temperatura en Centigrados: "))
Kelvin = Centigrados + 273.15
Fahrenheit = ((9 * Centigrados)/ 5) + 32
print(f"La temperatura de {Centigrados}º centigrados es equivalente a : {Fahrenheit} ºF y {Kelvin} K")

print("-----------------------")
print("---------EJERCICIO 8--------------")
# 8. Deseña un programa para o software dunha máquina, que converta unha cantidade enteira de diñeiro,
# que está presentada en billetes de 100, 20, 5 e moedas de 1 €, no seu equivalente en euros.
# Por exemplo 2 billetes de 100€, 	3 billetes de 20 €, 6 moedas de 1€ visualizaríamos 266 €.

numero = int(input("Dame una cantidad de dinero: "))

centena = int(numero/100)
decena = int( (numero - (centena*100)) / 20 )
moneda5 = int( (numero - (centena*100) - (decena * 20) ) / 5 )
moneda1 = int( (numero - (centena*100) - (decena * 20) - (moneda5 * 5) ) / 1 )

print(f"{numero} euros está representado por: {centena} billetes de 100, {decena} billetes de 20, {moneda5} billetes de 5 y {moneda1} moneda(s) de 1 euro.")

print("-----------------------")
print("---------EJERCICIO 9--------------")

print(" El ejercicio está repetido igual que el ejercicio 9")
print("-----------------------")
print("---------EJERCICIO 10--------------")
# Fai o algoritmo e programa que calcule o soldo bruto e líquido, a percibir por unha persoa. Para iso hai que ter en conta, que o soldo total inclúe os seguintes conceptos:
#
#
# Soldo 	fixo.
#
# Comisión: 	5% sobre importe total de vendas
#
# Quilometraxe: 	2 € por km
#
# Dietas: 	30 € por día de desprazamento.
#
#
# Para calcular o soldo líquido debemos descontarlle ao soldo bruto:
# I.R.P.F. = 18 % do soldo total.
#
# Retención a seguridade social : 36 €.

sueldoFijo = float(input("Dame el sueldo fijo: "))
importeTotalVentas = float(input("Dame el importe total de ventas: "))
kilometraje = float(input("Dame el kilometraje: "))
desplazamiento = int(input("Cuántos días estuviste en desplazamiento: "))

comision = (5/100) * importeTotalVentas
kilometrajeCalculado = 2 * kilometraje
dietas = 30 * desplazamiento
seguridadSocial = 36

SueldoBruto = sueldoFijo + importeTotalVentas + kilometraje + desplazamiento

irpf = SueldoBruto * (18/100)

SueldoLiquido = SueldoBruto - irpf - seguridadSocial

print(f"El sueldo bruto es: {SueldoBruto} euros y el sueldo líquido es: {SueldoLiquido} euros.")



