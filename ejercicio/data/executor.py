# proceso 
#
# acceder al archivo
archivo = open('ejercicio/data/Listado-Instituciones-Educativas-distribuidas-por-zona-distrito-y-circuito.csv', "r")

json = {

}

# obtener las líneas del archivo
lineas = archivo.readlines()

# lineas es ina lista de cadenas
# se imprime las siguientes posiciones
headers = lineas[0].split(('|'))


print(json)
print(lineas[1])

# en línea tomo el valor de lineas[1]
linea = lineas[1]
# a línea que es una cadena, la separo mediante la función
# de Python split
# Recuerdo que el separador de la cadena es un "|"

linea = linea.split("|")

# imprimo la nueva línea; que ahora es una lista
print(linea)

archivo.close()
index = 0
for line in linea[1:]:
    
    data = line.split('|')
 
    pagina = """
        <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
        <b> %s: </b> %s
        <b> %s: </b> %s
        <b> %s: </b> %s
        <b> %s: </b> %s
        <b> %s: </b> %s
        <b> %s: </b> %s
        <b> %s: </b> %s
        <b> %s: </b> %s
        <b> %s: </b> %s
        <b> %s: </b> %s
        <b> %s: </b> %s
        <b> %s: </b> %s
        <b> %s: </b> %s
    </body>
    </html>
    """ % (headers[0], linea[0],
    headers[1], linea[1],
    headers[2], linea[2],
    headers[3], linea[3],
    headers[4], linea[4],
    headers[5], linea[5],
    headers[6], linea[6],
    headers[7], linea[7],
    headers[8], linea[8],
    headers[9], linea[9],
    headers[10], linea[10],
    headers[11], linea[11],
    headers[12], linea[12])
    index +=1
    print(index)
    print (pagina)