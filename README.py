# ---------------------------------------------------
# CLASIFICADOR BÁSICO DE RAZAS DE PERROS
# Autor: Tu Nombre
# Descripción:
# Este programa identifica una posible raza de perro
# según características ingresadas por el usuario.
# ---------------------------------------------------

# Solicitar información al usuario
tamano = input("Ingrese el tamaño del perro (pequeño, mediano, grande): ").lower()
pelo = input("Ingrese el tipo de pelo (corto o largo): ").lower()
color = input("Ingrese el color principal del perro: ").lower()

# Procesamiento de datos
if tamano == "pequeño" and pelo == "largo":
    raza = "Pomeranian"

elif tamano == "grande" and pelo == "corto" and color == "dorado":
    raza = "Golden Retriever"

elif tamano == "grande" and pelo == "corto" and color == "negro":
    raza = "Labrador Retriever"

elif tamano == "mediano" and pelo == "corto":
    raza = "Bulldog"

elif tamano == "pequeño" and pelo == "corto":
    raza = "Chihuahua"

else:
    raza = "Raza no identificada"

# Mostrar resultado
print("\n--------------------------------")
print("RESULTADO DEL ANÁLISIS")
print("--------------------------------")
print("La posible raza del perro es:", raza)
