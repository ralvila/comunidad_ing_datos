"""
BLOQUE 3 — SINTAXIS BÁSICA DE PYTHON

Modo de uso:
- Ejecuta por secciones
- Lee los comentarios
- Predice antes de ejecutar
- Rompe el código intencionalmente
"""

# =====================================================
# 1. ESTRUCTURA DE UN PROGRAMA
# =====================================================

"""
Un programa en Python es una secuencia de instrucciones
que se ejecutan de arriba hacia abajo (top-down).

Python es un lenguaje INTERPRETADO:
👉 Ejecuta línea por línea en tiempo real
👉 No compila todo antes (como Java o C)

Esto tiene implicaciones MUY importantes.
"""

# -----------------------------------------------------
# 1. EJECUCIÓN SECUENCIAL
# -----------------------------------------------------

print("Paso 1")

x = 10

print("Paso 2:", x)

print("Paso 3")


# TIP:
# Python ejecuta exactamente en el orden en que está escrito

# EJERCICIO:
# Cambia el orden de los prints y analiza qué pasa


# -----------------------------------------------------
# 2. DEPENDENCIA ENTRE LÍNEAS
# -----------------------------------------------------

# ❌ Error (descomenta)
# print(y)
# y = 10

# 💥 NameError: name 'y' is not defined

# ✔ Correcto
y = 10
print(y)

# TIP:
# No puedes usar algo antes de definirlo


# -----------------------------------------------------
# 3. BLOQUES DE CÓDIGO
# -----------------------------------------------------

# Los bloques se definen por indentación

if True:
    print("Dentro del bloque")

print("Fuera del bloque")

# TIP:
# Todo lo indentado pertenece al bloque


# -----------------------------------------------------
# 4. FLUJO DE EJECUCIÓN
# -----------------------------------------------------

x = 5

if x > 10:
    print("Mayor a 10")
else:
    print("Menor o igual a 10")

print("Fin del programa")

# TIP:
# No todo el código se ejecuta siempre (depende de condiciones)


# -----------------------------------------------------
# 5. DEFINICIÓN vs EJECUCIÓN
# -----------------------------------------------------

def saludar():
    print("Hola")

# Nada se ejecuta aún

saludar()  # Aquí sí se ejecuta

# MENSAJE CLAVE:
# Definir ≠ Ejecutar


# -----------------------------------------------------
# 6. PUNTO DE ENTRADA DEL PROGRAMA
# -----------------------------------------------------

"""
En scripts reales, Python empieza desde la primera línea.

Pero en proyectos grandes se usa un punto de entrada:

if __name__ == "__main__":

Esto permite controlar qué se ejecuta.
"""

def main():
    print("Programa principal")


if __name__ == "__main__":
    main()

# TIP PRO:
# Esto es estándar en código profesional


# -----------------------------------------------------
# 7. ORDEN LÓGICO DEL CÓDIGO (BUENA PRÁCTICA)
# -----------------------------------------------------

"""
Orden recomendado en un script:

1. Imports
2. Constantes
3. Funciones
4. Lógica principal
"""

# EJEMPLO:

# 1. Imports
# import requests

# 2. Constantes
PI = 3.14

# 3. Funciones
def calcular_area(radio):
    return PI * radio ** 2

# 4. Ejecución
print(calcular_area(5))


# TIP:
# Este orden mejora la mantenibilidad


# -----------------------------------------------------
# 8. EFECTOS SECUNDARIOS (IMPORTANTE)
# -----------------------------------------------------

"""
Todo lo que está fuera de funciones se ejecuta automáticamente.

Esto puede generar problemas en proyectos grandes.
"""

print("Esto se ejecuta automáticamente")

# TIP PRO:
# Evita lógica compleja fuera de funciones


# -----------------------------------------------------
# 9. ERRORES POR ORDEN DE EJECUCIÓN
# -----------------------------------------------------

# ❌ Error común
# resultado = calcular(5)

# def calcular(x):
#     return x * 2

# 💥 NameError

# ✔ Correcto
def calcular(x):
    return x * 2

resultado = calcular(5)

# TIP:
# Define antes de usar


# -----------------------------------------------------
# 10. MENTALIDAD CORRECTA
# -----------------------------------------------------

"""
Antes de ejecutar código, pregúntate:

1. ¿En qué orden se ejecuta?
2. ¿Qué variables existen en cada momento?
3. ¿Qué bloques se ejecutan realmente?
"""

# EJERCICIO AVANZADO:
# ¿Qué imprime este código?

x = 1

if x:
    print("A")

    if x > 0:
        print("B")

print("C")


# -----------------------------------------------------
# 🧠 MENSAJES CLAVE
# -----------------------------------------------------

# 1. Python ejecuta de arriba hacia abajo
# 2. El orden del código IMPORTA
# 3. Definir no es ejecutar
# 4. La indentación controla el flujo
# 5. Pensar en el flujo = nivel profesional


# =====================================================
# 2. INDENTACIÓN (CRÍTICO)
# =====================================================

# La indentación define bloques
if True:
    print("Correcto")

# ERROR COMÚN (descomenta):
# if True:
# print("Error")

# TIP:
# Usa 4 espacios SIEMPRE
# No mezcles tabs y espacios

# MENSAJE CLAVE:
# La indentación en Python ES sintaxis

# EJERCICIO 2:
# Imprime si un número es par o impar


# =====================================================
# 3. COMENTARIOS
# =====================================================

# Comentarios explican el POR QUÉ

# MAL:
# x = 10  # asigna 10

# BIEN:
# x = 10  # valor base para cálculo

# TIP:
# No sobrecomentar

# EJERCICIO 3:
# Escribe un comentario útil para este código
x = 100


# =====================================================
# 4. INSTRUCCIONES
# =====================================================

x = 5
y = 7
print(x + y)

# MAL PRÁCTICA:
# x = 5; y = 7

# TIP:
# Una instrucción por línea mejora la legibilidad

# EJERCICIO 4:
# Haz el código más claro con múltiples prints


# =====================================================
# 5. PALABRAS RESERVADAS
# =====================================================

# No se pueden usar como variables
# if, else, for, while, def, return, True, False

# ERROR (descomenta):
# for = 10

# TIP:
# Usa nombres descriptivos

# EJERCICIO 5:
# Intenta usar una palabra reservada y analiza el error


# =====================================================
# 6. PEP8 (BUENAS PRÁCTICAS)
# =====================================================

"""
PEP8 es la guía oficial de estilo de Python.
No es obligatoria, pero en la práctica profesional ES un estándar.

Objetivo:
- Código legible
- Código consistente
- Código mantenible
"""

# -----------------------------------------------------
# 1. NOMBRES DE VARIABLES (snake_case)
# -----------------------------------------------------

# ✔ Correcto
nombre_usuario = "Santiago"
total_ventas = 1000

# ❌ Incorrecto
NombreUsuario = "Santiago"
totalVentas = 1000

# TIP:
# Usa nombres descriptivos, evita abreviaciones raras


# -----------------------------------------------------
# 2. ESPACIADO
# -----------------------------------------------------

# ✔ Correcto
x = 10
y = x + 5

# ❌ Incorrecto
x=10
y=x+5

# TIP:
# Los espacios mejoran la legibilidad


# -----------------------------------------------------
# 3. UNA INSTRUCCIÓN POR LÍNEA
# -----------------------------------------------------

# ✔ Correcto
x = 10
y = 20

# ❌ Incorrecto
x = 10; y = 20

# TIP:
# Código limpio > código corto


# -----------------------------------------------------
# 4. LONGITUD DE LÍNEA
# -----------------------------------------------------

# ✔ Recomendado: máximo ~79 caracteres
# (no es obligatorio, pero ayuda a leer mejor)

# TIP:
# Evita líneas extremadamente largas


# -----------------------------------------------------
# 5. USO DE MAYÚSCULAS
# -----------------------------------------------------

# Constantes → MAYÚSCULAS
PI = 3.1416
MAX_USERS = 100

# Variables normales → minúsculas
edad = 30


# -----------------------------------------------------
# 6. ESPACIOS EN FUNCIONES
# -----------------------------------------------------

# ✔ Correcto
print("Hola")

# ❌ Incorrecto
print( "Hola" )


# -----------------------------------------------------
# 7. COMENTARIOS
# -----------------------------------------------------

# ✔ Comentarios claros
# Calcula el total de ventas del día

# ❌ Comentarios inútiles
# suma dos números

# TIP:
# Comenta el POR QUÉ, no el QUÉ


# -----------------------------------------------------
# 8. LÍNEAS EN BLANCO
# -----------------------------------------------------

# Usa líneas en blanco para separar bloques lógicos

x = 10
y = 20

print(x + y)


# -----------------------------------------------------
# MENSAJES CLAVE
# -----------------------------------------------------

# 1. Código limpio es más importante que código rápido
# 2. Otros deben poder leer tu código fácilmente
# 3. PEP8 no es solo estética, es comunicación

# -----------------------------------------------------
# EJERCICIO
# -----------------------------------------------------

# Corrige:
# NombreUsuario="Juan";Edad=25


# =====================================================
# 7. ERRORES DE SINTAXIS
# =====================================================

"""
Un error de sintaxis ocurre cuando Python NO puede interpretar el código.

Regla clave:
👉 Si hay SyntaxError, el código ni siquiera empieza a ejecutarse
"""

# -----------------------------------------------------
# 1. PARÉNTESIS SIN CERRAR
# -----------------------------------------------------

# ❌ Error
# print("Hola"

# 💥 Error:
# SyntaxError: '(' was never closed

# TIP:
# Siempre revisa paréntesis, comillas y corchetes


# -----------------------------------------------------
# 2. COMILLAS MAL CERRADAS
# -----------------------------------------------------

# ❌ Error
# print("Hola)

# 💥 Error:
# SyntaxError: unterminated string literal

# TIP:
# Usa siempre pares: "" o ''


# -----------------------------------------------------
# 3. DOS PUNTOS FALTANTES
# -----------------------------------------------------

# ❌ Error
# if True
#     print("Hola")

# 💥 Error:
# SyntaxError: expected ':'

# TIP:
# Siempre usar ':' en:
# if, for, while, def, class


# -----------------------------------------------------
# 4. INDENTACIÓN INCORRECTA
# -----------------------------------------------------

# ❌ Error
# if True:
# print("Hola")

# 💥 Error:
# IndentationError

# TIP:
# Python usa indentación para definir bloques


# -----------------------------------------------------
# 5. MEZCLA DE TABS Y ESPACIOS
# -----------------------------------------------------

# ❌ Error difícil de detectar

# 💥 Error:
# TabError: inconsistent use of tabs and spaces

# TIP:
# Configura tu editor para usar SOLO espacios


# -----------------------------------------------------
# 6. USO INCORRECTO DE OPERADORES
# -----------------------------------------------------

# ❌ Error
# if x = 10:

# 💥 Error:
# SyntaxError: invalid syntax

# ✔ Correcto
# if x == 10:

# TIP:
# = asigna, == compara


# -----------------------------------------------------
# 7. PALABRAS RESERVADAS COMO VARIABLES
# -----------------------------------------------------

# ❌ Error
# for = 10

# 💥 Error:
# SyntaxError

# TIP:
# No usar palabras reservadas como nombres


# -----------------------------------------------------
# 8. FALTA DE PARÉNTESIS EN FUNCIONES
# -----------------------------------------------------

# ❌ Error
# print

# 💥 No ejecuta nada útil

# ✔ Correcto
# print()

# TIP:
# Las funciones SIEMPRE llevan paréntesis


# -----------------------------------------------------
# 9. MAL USO DE COMAS
# -----------------------------------------------------

# ❌ Error
# print("Hola" "Mundo")

# ✔ Puede no fallar, pero es mala práctica
# concatena strings automáticamente

# TIP:
# Usa comas o + de forma explícita


# -----------------------------------------------------
# 10. BLOQUES VACÍOS
# -----------------------------------------------------

# ❌ Error
# if True:

# 💥 Error:
# IndentationError

# ✔ Solución temporal
# if True:
#     pass

# TIP:
# Usa pass cuando aún no tienes código


# -----------------------------------------------------
# 11. ORDEN INCORRECTO EN ELSE / ELIF
# -----------------------------------------------------

# ❌ Error
# else:
#     print("Hola")
# if True:

# 💥 Error:
# SyntaxError

# TIP:
# Orden correcto:
# if → elif → else


# -----------------------------------------------------
# 12. USO INCORRECTO DE PARÉNTESIS EN CONDICIONES
# -----------------------------------------------------

# ❌ Error
# if (x > 5

# 💥 Error:
# SyntaxError

# TIP:
# Siempre cerrar condiciones correctamente


# -----------------------------------------------------
# 13. IDENTIFICADORES INVÁLIDOS
# -----------------------------------------------------

# ❌ Error
# 2variable = 10

# 💥 Error:
# SyntaxError

# ✔ Correcto
# variable2 = 10

# TIP:
# Variables no pueden empezar con números


# -----------------------------------------------------
# 14. USO INCORRECTO DE IMPORT
# -----------------------------------------------------

# ❌ Error
# import requests, 

# 💥 Error:
# SyntaxError

# TIP:
# Cuidado con comas al final


# -----------------------------------------------------
# 15. CONCATENACIÓN INCORRECTA
# -----------------------------------------------------

# ❌ Error
# print("Edad: " + 25)

# 💥 Error:
# TypeError (no es sintaxis, pero es MUY común)

# ✔ Correcto
# print("Edad:", 25)
# print("Edad: " + str(25))


# -----------------------------------------------------
# 🧠 MENSAJES CLAVE
# -----------------------------------------------------

# 1. El error SIEMPRE dice dónde está el problema (línea)
# 2. El mensaje del error es tu mejor amigo
# 3. El 80% de errores son pequeños detalles (paréntesis, :)
# 4. Aprender a leer errores = habilidad clave de programador


# -----------------------------------------------------
# 🧪 EJERCICIO
# -----------------------------------------------------

# Este código tiene múltiples errores.
# Encuéntralos TODOS antes de ejecutar:

# if True
# print("Hola"
# x = 10
# if x = 10:
#     print("Correcto")


# =====================================================
# 8. EJERCICIO FINAL BÁSICO
# =====================================================

# Crear script:
# - nombre
# - edad
# - imprimir mensaje claro


# =====================================================
# 🔥 EJERCICIOS INTERMEDIOS
# =====================================================

# EJERCICIO 9 — Flujo
x = 5
if x > 3:
    print("Mayor a 3")
print("Siempre se ejecuta")

# TIP:
# El scope depende de la indentación

# EJERCICIO 10 — Debugging
# Corrige:
# if True
#     print("Hola")
#  print("Error")

# EJERCICIO 11 — PEP8
# A=10
# B=20
# print(A+B)


# =====================================================
# 🚀 EJERCICIOS AVANZADOS
# =====================================================

# EJERCICIO 12 — Predicción
# ¿Qué imprime?
x = 10
if x > 5:
    print("A")
    if x > 8:
        print("B")
    print("C")
print("D")

# TIP:
# Piensa antes de ejecutar

# EJERCICIO 13 — Debugging real
# x=10
# if x>5:
# print("Mayor")
# else:
#     print("Menor")

# EJERCICIO 14 — Refactorización
# nombre="Juan"
# edad=25
# print("Hola mi nombre es "+nombre+" y tengo "+str(edad)+" años")

# BUENA PRÁCTICA:
# Prioriza claridad sobre rapidez

# EJERCICIO 15 — Caso real
# producto, precio, cantidad
# calcular total
# imprimir limpio


# =====================================================
# 💣 ALTA COMPLEJIDAD
# =====================================================

# EJERCICIO 16 — Lectura de errores
# print("Hola"
# x = 10
# if x > 5
#     print("Mayor")

# EJERCICIO 17 — Tipos
# x = "10"
# print(x + 5)

# EJERCICIO 18 — Booleanos
x = 0
if x:
    print("Verdadero")
else:
    print("Falso")

# TIP:
# 0 en Python es False

# EJERCICIO 19 — Indentación avanzada
# if True:
#     if False:
#         print("A")
#       print("B")

# EJERCICIO 20 — Reto final
# Script limpio con:
# - variables
# - condicional
# - buenas prácticas


# =====================================================
# MENSAJES CLAVE
# =====================================================

# 1. La indentación define todo
# 2. Leer errores es habilidad crítica
# 3. Código limpio = nivel profesional
# 4. Pensar antes de ejecutar = senior


print("\nFin de la guía completa del Bloque 3")
