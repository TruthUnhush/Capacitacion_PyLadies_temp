score = 0

# Funciones sin paramentros que modifican o imprimen algo

def saludo():
    print("Hola a todos")
    

def incrementar_punaje():
    global score
    score += 1

# Funciones sin paramentros que regresan algo

def valor_cero():
    return 0

def forma_de_saludar():
    return "Saludos a todo el mundo"

saludo()
incrementar_punaje()

a = valor_cero()
print(a)
print(forma_de_saludar())

saludo()


# Funciones con argumentos que no tienen return

def saludo_especial(nombre):

    print(f"Hola {nombre} mucho gusto.")

# Funciones con argumentos que devuelven algo

def suma(a, b):
    return a + b


saludo_especial("Maria")

suma_total = suma(21, 7)
print(suma_total)
