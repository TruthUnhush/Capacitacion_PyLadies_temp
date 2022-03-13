
archivo = open("copia_ejemplo.txt", "r")

contenido = archivo.read()
print(contenido)


archivo.close()

# with open("nuevo_archivo.txt", "a") as archivo_nuevo:
#     archivo_nuevo.write("\n")
#     archivo_nuevo.write("Esta es mi tercera linea\n")
#     archivo_nuevo.write("Esta es mi cuarta linea\n")

archivo_leer = input("Introduce el nombre del archivo a leer: ")

try: 
    with open(archivo_leer) as archivo:
        contenido = archivo.read()
        print(contenido)
except FileNotFoundError:
    print("No he encontrado el archivo, comprueba el nombre ")
