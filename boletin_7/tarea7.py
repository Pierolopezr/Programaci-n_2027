# BOLETIN 7 - Cadeas de caracteres
print("-----------------------")
print("---------EJERCICIO 1--------------")
# Mostra a lonxitude do texto: “ Isto é Python!”
def ejercicio1():
    lonxitude = len(" Isto é Python!")
    print(f"La lonxitude es de {lonxitude} carácteres.")
#ejercicio1()
print("-----------------------")
print("-----------------------")
print("---------EJERCICIO 2--------------")
# Desmenuza o String “Python” mostrándoo por pantalla carácter a carácter.
def ejercicio2():
    palabra = "Python"
    for letras in palabra:
        print(letras)
#ejercicio2()
print("-----------------------")
print("-----------------------")
print("---------EJERCICIO 3--------------")
# Invertir o texto: “Python para todos”
def ejercicio3():
    palabra = "Python para todos"
    invertido = palabra[::-1]
    print(invertido)
#ejercicio3()
print("-----------------------")
print("-----------------------")
print("---------EJERCICIO 4--------------")
# Elimina os espazos do texto: “Guido Van Rossum creou Python”
def ejercicio4():
    palabra = "Guido Van Rossum creou Python"
    palabra = palabra.replace(" ", "")  # Creo una nueva cadena y elimino todos los espacios, así que creo una nueva
    print(palabra)
#ejercicio4()
print("-----------------------")
print("-----------------------")
print("---------EJERCICIO 5--------------")
# Conta as vocais e as consoantes do String “Python Python Python”. Ollo cos espazos!
def ejercicio5():
    palabra = "Python Python Python"
    vocales = 0
    consonantes = 0
    for vocal in palabra:
        if vocal in "aeiou": # La letra actual está dentro del grupo de vocales aeiou ¿?
            vocales += 1
        elif vocal.isalpha(): # comprueba si el caracter es una letra
            consonantes += 1
    print(f"Hay un total de {vocales} vocales y {consonantes} consonantes.")
#ejercicio5()
print("-----------------------")
print("-----------------------")
print("---------EJERCICIO 6--------------")
# Divide a cadea de texto “ www. phytonparatodos. com” en duas partes “ www. phyton” e “paratodos. com”.
# Para posteriormente concaténalas e mostralas de novo.
def ejercicio6():
    texto = " www. phytonparatodos. com"
    texto1 = texto[:12]
    print(texto1)
    texto2 = texto[12:]
    print(texto2)
    texto = texto1 + texto2
    print(texto)
#ejercicio6()
print("-----------------------")
print("-----------------------")
print("---------EJERCICIO 7--------------")
# Transforma a cadea de texto “ Phytoneros” a maiúsculas.
# Garda o valor na variable e posteriormente convértea novamente a minúsculas.
def ejercicio7():
    texto = " Phytoneros"
    minusculas = texto.lower()
    print(minusculas)
    mayusculas = minusculas.upper()
    print(mayusculas)
#ejercicio7()
print("-----------------------")
print("-----------------------")
print("---------EJERCICIO 8--------------")
# Compara se o String “Python” é igual que o String “ JavaScript”.
def ejercicio8():
    texto1 = "Python"
    texto2 = " JavaScript"

    if texto1 == texto2:
        print("El texto es igual")
    else:
        print("El texto no es igual")
#ejercicio8()
print("-----------------------")
print("-----------------------")
print("---------EJERCICIO 9--------------")
# Sobre a cadea de texto “ Jeve jeve jeve”,
# substitúe todas as vocais e pola vogal para dando como resultado “java java java”.
def ejercicio9():
    texto = " Jeve jeve jeve"
    texto = texto.replace("e", "a")
    texto = texto.strip()
    print(texto)
#ejercicio9()
print("-----------------------")
print("-----------------------")
print("---------EJERCICIO 10--------------")
# Tenta escribir un metodo, que dado un obxecto da clase str conte diferentes tipos de caracteres. En particular,
# o metodo deberá imprimir o número de letras, díxitos e espazos en branco da cadea.
#  Tenta facer un programa que escriba o cálculo da cadea: «Ola, son alumno de DAM1, e son programador desde o 2025».
def ejercicio10():
    texto = "Ola, son alumno de DAM1, e son programador desde o 2025"
    letras = 0
    dixitos = 0
    espacios = 0
    for caracter in texto:
        if caracter.isalpha():
            letras += 1
        elif caracter.isdigit(): # un dígito es cada símbolo del 0 al 9; un número puede estar formado por uno o varios dígito
            dixitos += 1
        elif caracter.isspace(): # Cuenta los espacios, saltos de linea, tabulaciones. Pero en este caso nos sirve.
            espacios += 1
    print(f"En dicha palabra hay {letras} letras, {dixitos} dixitos y {espacios} espacios ")
#ejercicio10()
print("-----------------------")
print("-----------------------")
print("---------EJERCICIO 11--------------")
# Escribir funcións que dada unha cadena de caracteres:
# a. Imprima os dous primeiros caracteres.
# b. Imprima os tres últimos caracteres.
# c. Imprima dita cadea cada dous caracteres. Ex.: recta debería imprimir rca
# d. Imprima a cadea nun sentido e en sentido inverso. Ex: reflexo imprime reflexooxelfer.
def ejercicio11():
    texto = "Perú es clave"
    textoa = texto[0:2]
    textob = texto[-3:]
    textoc = texto[::2] # Cuenta cada dos espacios.
    textod = texto + texto[::-1]

    print(textoa)
    print(textob)
    print(textoc)
    print(textod)

#ejercicio11()
print("-----------------------")
print("-----------------------")
print("---------EJERCICIO 12--------------")
# Escribir funcións que dada unha cadea e un caracter:
#
# a. Reemplace tódolos espazos polo caracter. Ex: ‘meu arquivo de texto.txt’ e ‘\_’ debería devoltar ‘meu\_arquivo\_de\_texto.txt’
# b. Inserte o caracter entre cada letra da cadea. Ex: ‘separar’ e ‘,’ debería devolver s,e,p,a,r,a,r
# c. Reemplace tódolos díxitos na cadea polo caracter. Ex: súa clave é: 1540 e ‘X’ debería devotar súa clave é: XXXX
# d. Inserta o carácter cada 3 díxitos na cadea. Ex. 2552552550 e ‘.’ debería devoltar 255.255.255.0
def ejercicio12():
    texto1 = "meu arquivo de texto.txt"
    textoa = texto1[:texto1.find("t")]
    textoa = textoa.replace(" ", "/_")
    print(textoa + texto1[texto1.find("te"):])

    texto2 = "separar"
    textob = texto2.replace("", ",")[1:]
    print(textob)

    texto = "Su clave es: 1540"
    inicio, clave = texto.split(": ", 1) # inicio se queda con la primera mitad y clave con la segunda que es la condicion
    clave_oculta = ""
    for caracter in clave:
        if caracter.isdigit():
            clave_oculta += "X"
        else:
            clave_oculta += caracter
    textoc = inicio + ": " + clave_oculta
    print(textoc)

    texto4 = "2552552550"
    textod = texto4[:3] + "." + texto4[3:6] + "." + texto4[6:9] + "." + texto4[9:]
    print(textod)
#ejercicio12()
print("-----------------------")
print("-----------------------")
print("---------EJERCICIO 13--------------")
# Modificar las funciones anteriores para que reciban un parámetro que indique la cantidad máxima de sustituciones o inserciones que pueden realizar
def ejercicio13(maximo):


    texto1 = "meu arquivo de texto.txt"
    textoa = texto1[:texto1.find("t")]
    textoa = textoa.replace(" ", "/_", maximo) # sustituyo como "maximo" la cantidad indicada
    print(textoa + texto1[texto1.find("te"):])


    texto2 = "separar"
    textob = texto2.replace("", ",", maximo + 1)[1:] # colocamos +1 porque hago que empiece con 1: y omite el primer , se ,s,e,p...
    print(textob)

    texto = "Su clave es: 1540"
    inicio, clave = texto.split(": ", 1)  # inicio se queda con la primera mitad y clave con la segunda que es la condicion
    clave_oculta = ""
    sustituciones = 0
    for caracter in clave:
        if caracter.isdigit() and sustituciones < maximo:
            clave_oculta += "X"
            sustituciones += 1
        else:
            clave_oculta += caracter
    textoc = inicio + ": " + clave_oculta
    print(textoc)

    texto4 = "2552552550"
    textod = ""
    incersiones = 0
    for i in range(0, len(texto4),3): # calcula longitud 10 y recorre el for cada 3 veces
        if i> 0 and incersiones < maximo: # evita poner un punto antes del primer grupo
            textod +=  "."
            incersiones += 1
        textod += texto4[i:i+3] # en cada vuelta cambia de valor.
    print(textod)
#ejercicio13(2)
print("-----------------------")
print("-----------------------")
print("---------EJERCICIO 14--------------")
# Escribir unha función que reciba unha cadea que conten un número enteiro longo e devolte unha cadea co número e as separacións de miles.
# Por exemplo, se recibe 1234567890, debe devoltar 1.234.567.890
def ejercicio14():
    texto = "1234567890"
    textoa = ""

    for i in range(len(texto), 0, -3):

        # Recojo hasta tres cifras desde la derecha
        grupo = texto[max(0, i - 3):i]

        # Si todavía no he guardado nada, añado el primer grupo
        if textoa == "":
            textoa = grupo

        # Si ya tengo algo guardado, pongo el nuevo grupo delante
        else:
            textoa = grupo + "." + textoa

    print(textoa)

    texto2 = "1234567890"
    texto3 = ""

    veces = (len(texto2)-1) // 3 # Hallo la cantidad de miles que tiene el número. En este caso 3.
    for i in range(0, veces):
        texto2 = int(texto2)
        textoR = int(texto2) % 1000  # Hallo el resto de entre 1000 para que me dé las 3 últimas cifras
        texto2 = texto2 // 1000 # Con la división entera //, solo me quedo con el número entero. Con esto, hallo el nuevo número para seguir con la operación de resto en el bucle
        print(textoR)
        print(texto2)

        texto3 = "." + str(textoR).zfill(3)  + texto3 # Voy sumando cada grupo de tres cifras hasta que se cumpla el bucle

    resultado = str(texto2) + texto3 # El número o números restantes menor a 3 cifras le junto en string al grupo texto3 que ya tengo
    resultado = resultado.replace(" ", "") # Quito los espacios.
    print(resultado)
ejercicio14()
print("-----------------------")

print("-----------------------")
print("---------EJERCICIO 15--------------")
# Escribir unha función que dada unha cadea de caracteres, devolte:
#i. A primeira letra de cada palabra. Por exemplo, se recibe Universal Serial Bus debe devoltar USB.
#ii.  Unha cadea coa primeira letra de cada palabra en maiúsculas. Por exemplo, se recibe república arxentina, debe devoltar, República Arxentina.
#iii. As palabras que comecen coa letra A. Por exemplo, si recibe Antes de abrir, debe devoltar, Antes abrir.
def ejercicio15():
    print("hola mundo")
ejercicio15()
print("-----------------------")
print("-----------------------")
print("---------EJERCICIO 16--------------")
# Escribir funcións que dada unha cadea de caracteres:
# a. Devolva soamente as letras consonantes. Por exemplo, se recibe ‘algoritmos’ ou ‘logaritmos’ debe devolver ‘lgrtms’.
# b. Devolva soamente as letras vogais. Por exemplo, se recibe ‘sen 	consoantes’ debe devoltar ‘e ooae’.
# c. Substitúa cada vogal pola súa seguinte vogal. Por exemplo, se recibe ‘vestiario’ debe devoltar ‘vostoerou’.
print("-----------------------")
print("-----------------------")
print("---------EJERCICIO 17--------------")
# Indique si se trata dun palíndromo.
# Por exemplo, ‘anita lava la tina’ é un palíndromo (léese igual de esquerda a dereita que de dereita a esquerda)
print("-----------------------")
print("-----------------------")
print("---------EJERCICIO 18--------------")
# Escribir funcións que dadas dúas cadeas de caracteres:
# a. Indique si a segunda cadea é unha subcadea da primeira. Por exemplo, ‘cadea’ é unha subcadea de ‘subcadea’.
# b. Devolva a que sexa anterior en orden alfabético. Por exemplo, se recibe ‘kde' e ‘gnome’ debe devoltar ‘gnome’.
print("-----------------------")
print("-----------------------")
print("---------EJERCICIO 19--------------")
# Escribir unha función que reciba unha cadea de uns e ceros (é dicir, un número en representación binaria)
# e devolte o valor decimal correspondente
print("-----------------------")
print("-----------------------")
print("---------EJERCICIO 20--------------")
# Escribir as seguintes funcións que fagan o seguinte:
# i. Recibindo unha cadea de caracteres e un carácter, retorne unha nova cadea formada exclusivamente polo novo carácter. Esta nova cadea terá a lonxitude da cadea pasada por parámetro.
# ii. Recibindo unha cadea de caracteres e un carácter, a función terá que comprobar si o carácter está na cadea. A función retornará un String no que aparezan guións e o carácter na posición ou posicións onde coincida na cadea.
print("-----------------------")
print("-----------------------")
print("---------EJERCICIO 21--------------")
# Escribe a función que permita validar un contrasinal, recibindo o contrasinal como parámetro.
# O contrasinal ten que cumprir as condicións de mínimo 8 caracteres, o menos unha maiúscula, unha minúscula e un número.
# A función ten que retornar un booleano especificando si é válida ou non.

print("-----------------------")
print("-----------------------")
print("---------EJERCICIO 22--------------")
# Escribe a función que permita formatear de nomes.
# A función ten que eliminar os espazos en branco e poñer en maiúsculas o primeiro carácter d o nome e apelido pasado como parámetro.
# Finalmente retornará unha cadea co nome e apelidos co formato solicitado.
print("-----------------------")
print("-----------------------")
print("---------EJERCICIO 23--------------")
# Crear a función que permita realizar un análise simple de texto.
# O analizador ten  a función de contar palabras, caracteres e encontrar a palabra mais longa.
# Mostrar os resultados por pantalla.
print("-----------------------")


