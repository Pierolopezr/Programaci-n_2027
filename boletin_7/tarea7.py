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
print("-----------------------")
print("-----------------------")
print("---------EJERCICIO 12--------------")
# Escribir funcións que dada unha cadea e un caracter:
#
# a. Reemplace tódolos espazos polo caracter. Ex: ‘meu arquivo de texto.txt’ e ‘\_’ debería devoltar ‘meu\_arquivo\_de\_texto.txt’
# b. Inserte o caracter entre cada letra da cadea. Ex: ‘separar’ e ‘,’ debería devolver s,e,p,a,r,a,r
# c. Reemplace tódolos díxitos na cadea polo caracter. Ex: súa clave é: 1540 e ‘X’ debería devotar súa clave é: XXXX
# d. Inserta o carácter cada 3 díxitos na cadea. Ex. 2552552550 e ‘.’ debería devoltar 255.255.255.0
print("-----------------------")
print("-----------------------")
print("---------EJERCICIO 13--------------")
# Modificar as funcións anteriores,
# para que reciban un parámetro que indique a cantidade máxima de reemprazos ou insercións a realizar.
print("-----------------------")
print("-----------------------")
print("---------EJERCICIO 14--------------")
# Escribir unha función que reciba unha cadea que conten un número enteiro longo e devolte unha cadea co número e as separacións de miles.
# Por exemplo, se recibe 1234567890, debe devoltar 1.234.567.890
print("-----------------------")
print("-----------------------")
print("---------EJERCICIO 15--------------")
# Escribir unha función que dada unha cadea de caracteres, devolte:
#i. A primeira letra de cada palabra. Por exemplo, se recibe Universal Serial Bus debe devoltar USB.
#ii.  Unha cadea coa primeira letra de cada palabra en maiúsculas. Por exemplo, se recibe república arxentina, debe devoltar, República Arxentina.
#iii. As palabras que comecen coa letra A. Por exemplo, si recibe Antes de abrir, debe devoltar, Antes abrir.
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


