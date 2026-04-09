"""
BLOQUE 6 — ENTRADA Y SALIDA DE DATOS

En este bloque aprenderás:

- Qué es la entrada y salida de datos en programación
- Cómo mostrar información en pantalla con print()
- Cómo recibir datos del usuario con input()
- Qué es la concatenación
- Cómo formatear texto correctamente
- f-strings (forma moderna)
- .format() (forma clásica)

Modo de uso:
- Ejecuta el archivo por secciones
- Lee cuidadosamente los comentarios
- Predice qué hará el código antes de ejecutarlo
- Prueba modificar los ejemplos
- Provoca errores intencionalmente y analízalos
"""


# =====================================================
# 1. SALIDA DE DATOS — print()
# =====================================================

"""
CONCEPTO:

La salida de datos es la forma en que un programa
muestra información al usuario.

print() es la función que permite enviar datos a la pantalla.

Es fundamental para:
- Ver resultados
- Depurar código
- Interactuar con el usuario
"""

# Ejemplos básicos
print("Hola mundo")
print("Estoy aprendiendo Python")

# Ejemplo con variables
nombre = "Erika"
edad = 25

print(nombre)
print(edad)

# Ejemplo combinando valores
print("Nombre:", nombre, "Edad:", edad)

# TIP:
# print separa automáticamente con espacios

# -------------------- EJERCICIOS ----------------------

# 🟢 Básico:
# Imprime tu comida favorita

# 🟡 Medio:
# Imprime tu nombre y tu edad

# 🔴 Avanzado:
# Imprime un mensaje como:
# "Hola Erika, tienes 25 años"



# =====================================================
# 2. ENTRADA DE DATOS — input()
# =====================================================

"""
CONCEPTO:

La entrada de datos permite que el usuario
interactúe con el programa.

input():
- Muestra un mensaje
- Espera a que el usuario escriba algo
- Devuelve ese valor como TEXTO (str)

Esto es clave:
👉 TODO lo que entra por input es string
"""

# Ejemplo básico
nombre = input("Ingresa tu nombre: ")
print("Hola", nombre)

# Ejemplo mostrando el tipo
edad = input("Ingresa tu edad: ")
print("Tipo de dato:", type(edad))  # str

# Conversión necesaria
edad = int(edad)
print("Ahora es:", type(edad))  # int

# Ejemplo sencillo
numero1 = input("Número 1: ")
numero2 = input("Número 2: ")

suma = int(numero1) + int(numero2)
print("Resultado:", suma)

# -------------------- EJERCICIOS ----------------------

# 🟢 Básico:
# Pide el nombre del usuario

# 🟡 Medio:
# Pide un número y conviértelo a int

# 🔴 Avanzado:
# Pide dos números y multiplícalos



# =====================================================
# 3. CONCATENACIÓN
# =====================================================

"""
CONCEPTO:

La concatenación es la unión de dos o más textos (strings).

Se hace con el operador +
"""

# Ejemplo básico
texto1 = "Hola"
texto2 = "Mundo"

resultado = texto1 + " " + texto2
print(resultado)

# Ejemplo con variables
nombre = "Erika"
saludo = "Hola " + nombre
print(saludo)

# ERROR COMÚN
# print("Edad: " + 25) ❌

# SOLUCIÓN
print("Edad: " + str(25))

# Ejemplo correcto
edad = 25
mensaje = "Tienes " + str(edad) + " años"
print(mensaje)

# -------------------- EJERCICIOS ----------------------

# 🟢 Básico:
# Une dos palabras

# 🟡 Medio:
# Une nombre y apellido

# 🔴 Avanzado:
# Intenta concatenar texto con número sin convertir



# =====================================================
# 4. FORMATO DE STRINGS
# =====================================================

"""
CONCEPTO:

El formateo de strings permite insertar valores dentro de texto
de forma más clara, ordenada y segura que la concatenación.

Evita errores y mejora la legibilidad.
"""


# -----------------------------------------------------
# 4.1 f-strings (RECOMENDADO)
# -----------------------------------------------------

"""
CONCEPTO:

Los f-strings permiten insertar variables directamente
dentro de un string usando {}.

Son:
✔ Más claros
✔ Más rápidos
✔ Más modernos
"""

nombre = "Erika"
edad = 25

# Ejemplo básico
print(f"Hola {nombre}")

# Ejemplo completo
print(f"Hola {nombre}, tienes {edad} años")

# Ejemplo con operaciones
print(f"En 5 años tendrás {edad + 5}")

# Ejemplo sencillo
precio = 10
cantidad = 3
print(f"Total a pagar: {precio * cantidad}")



# -----------------------------------------------------
# 4.2 .format()
# -----------------------------------------------------

"""
CONCEPTO:

Es una forma más antigua de formatear texto,
pero aún muy usada en código legado.
"""

nombre = "Erika"
edad = 25

# Ejemplo básico
print("Hola {}, tienes {} años".format(nombre, edad))

# Ejemplo con nombres
print("Hola {n}, tienes {e} años".format(n=nombre, e=edad))

# Ejemplo sencillo
precio = 10
print("El precio es {}".format(precio))


# -------------------- EJERCICIOS ----------------------

# 🟢 Básico:
# Usa f-string para mostrar tu nombre

# 🟡 Medio:
# Usa .format() para mostrar edad

# 🔴 Avanzado:
# Muestra una operación dentro de un f-string



# =====================================================
# 🧠 MENSAJES CLAVE
# =====================================================

# 1. print() muestra información al usuario
# 2. input() permite ingresar datos (siempre string)
# 3. Concatenar une textos (cuidado con tipos)
# 4. f-strings son la mejor forma de formatear
# 5. Convertir tipos es clave al trabajar con input


print("\nFin del bloque 6")