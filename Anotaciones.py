# STR: Una cadena de caracteres es un conjunto de caracteres (texto).

#palabra = "Python"

#len(palabra)        # Cantidad de caracteres
#palabra[0]          # Primer carácter
#palabra[-1]         # Último carácter
#palabra[0:3]        # Desde posición 0 hasta antes de la 3

#palabra.upper()     # Convierte a mayúsculas
#palabra.lower()     # Convierte a minúsculas
#palabra.strip()	 # Elimina espacios al principio y al final
#palabra = palabra.replace(" ", "") # Elimina todos los espacios existentes
#palabra.isspace()   # Boolean si hay espacios, tabulaciones o saltos en línea

#palabra.count("t")  # Cuenta cuántas veces aparece "t"
# palabra = palabra.replace("G", "P")  #creo una nueva cadena y la guardo
# palabra = "P" + palabra[1:]  # creo una nueva cadena mediante concatenación
# texto1 = texto[::2]   # Creo una nueva cadena y recorro la cadena de 2 en 2
# texto.split(": ", 1) # Indica el split que se parte en dos en el punto ":" donde está en el texto
    # texto[0] y texto[1] # primera mitad y segunda mitad
#"Py" in palabra     # Comprueba si contiene "Py"
# texto.zfill(3) # Rellena los espacios que faltan con 0 -> si tengo 45 -> 045 y así