"""
BLOQUE 11 — COMPRENSIONES Y ESTRUCTURAS AVANZADAS

Objetivo:
- Transformar datos de forma eficiente
- Escribir código más limpio y expresivo
- Entender cómo trabajan herramientas como pandas y Spark

Modo de uso:
- Lee antes de ejecutar
- Predice resultados
- Modifica ejemplos
- Prioriza legibilidad
"""


# =====================================================
# 1. LIST COMPREHENSION
# =====================================================

"""
¿Qué es?
Es una forma compacta y expresiva de crear listas en Python a partir de otras estructuras.

¿Para qué se usa?
Principalmente para transformar datos, filtrar datos

¿Cuándo usarla?
La lógica es simple o moderada
Estás haciendo transformaciones directas
Quieres código más limpio

NO usarla cuando:
Hay muchas condiciones
Hay múltiples pasos
Pierde legibilidad

Estructura:
[expresión for elemento in iterable if condición]
"""

numeros = [1, 2, 3, 4, 5]

# Tradicional
cuadrados = []
for n in numeros:
    cuadrados.append(n**2)

print(cuadrados)

# Comprehension
cuadrados = [n**2 for n in numeros]
print(cuadrados)


# -----------------------------------------------------
# IF / ELSE
# -----------------------------------------------------

resultado = ["par" if n % 2 == 0 else "impar" for n in numeros]
print(resultado)


# -----------------------------------------------------
# ANIDADO (FLATTEN)
# -----------------------------------------------------

matriz = [[1, 2], [3, 4], [5, 6]]
flatten = [num for fila in matriz for num in fila]
print(flatten)


# -----------------------------------------------------
# DOBLE LOOP
# -----------------------------------------------------

pares = [(x, y) for x in range(3) for y in range(3)]
print(pares)


# -----------------------------------------------------
# CONDICIÓN COMPLEJA
# -----------------------------------------------------

resultado = [n for n in range(20) if n % 2 == 0 and n % 3 == 0]
print(resultado)


# TIP:
# No hacer comprehensions demasiado complejas


# -------------------- EJERCICIOS ----------------------

# -----------------------------------------------------
# 🔴 EJERCICIO 1 — FLATTEN + FILTRO
# -----------------------------------------------------

matriz = [
    [1, 2, 3],
    [4, 5],
    [6, 7, 8]
]

# 👉 obtener lista plana solo con números > 4

# -----------------------------------------------------
# 🔴 EJERCICIO 2 — TRANSFORMACIÓN TIPO API
# -----------------------------------------------------

usuarios = [
    {"nombre": "Ana", "edad": 25},
    {"nombre": "Luis", "edad": 30},
    {"nombre": "Pedro", "edad": 35}
]

# 👉 nombres en mayúscula de usuarios mayores a 28

# -----------------------------------------------------
# 🔴 EJERCICIO 3 — COMBINACIONES
# -----------------------------------------------------

# 👉 generar pares (x,y) donde x != y

# -----------------------------------------------------
# 🔴 EJERCICIO 4 — FILTRADO AVANZADO
# -----------------------------------------------------

numeros = list(range(50))

# 👉 números divisibles por 3 y 5, multiplicados por 10

# -----------------------------------------------------
# 🔴 EJERCICIO 5 — LIMPIEZA DE DATOS
# -----------------------------------------------------

data = ["  Ana", "Luis  ", "  Pedro  ", ""]

# 👉 limpiar espacios y eliminar vacíos

# -----------------------------------------------------
# 🔴 EJERCICIO 6 — DUPLICADOS
# -----------------------------------------------------

numeros = [1,2,2,3,4,4,5]

# 👉 obtener solo los duplicados

# -----------------------------------------------------
# 🔴 EJERCICIO 7 — DIAGONAL MATRIZ
# -----------------------------------------------------

matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

# 👉 diagonal principal

# -----------------------------------------------------
# 🔴 EJERCICIO 8 — APLANAR Y TRANSFORMAR
# -----------------------------------------------------

matriz = [[1,2], [3,4], [5,6]]

# 👉 obtener todos los valores multiplicados por 2

# -----------------------------------------------------
# 🔴 EJERCICIO 9 — FILTRAR STRINGS COMPLEJOS
# -----------------------------------------------------

palabras = ["python", "data", "engineering", "ai", "ml"]

# 👉 palabras con más de 4 letras en mayúscula

# -----------------------------------------------------
# 🔴 EJERCICIO 10 — GENERAR MATRIZ
# -----------------------------------------------------

# 👉 matriz 3x3 con valores i*j

# =====================================================
# 2. DICTIONARY COMPREHENSION
# =====================================================

"""
Un dictionary comprehension permite crear diccionarios
de forma compacta a partir de iterables.

¿Para qué se usa?
Transformar datos
Filtrar datos
Reestructurar datos

¿Cuándo usarla?
Estás creando un diccionario desde otro iterable
La transformación es clara
Estás mapeando datos

¿Cuándo NO usarla?
La lógica es muy compleja
Necesitas múltiples pasos
Pierde legibilidad

Estructura:

{clave: valor for elemento in iterable if condición}
"""

numeros = [1, 2, 3, 4]

cuadrados = {n: n**2 for n in numeros}
print(cuadrados)


# -----------------------------------------------------
# CON FILTRO
# -----------------------------------------------------

pares = {n: n**2 for n in numeros if n % 2 == 0}
print(pares)


# -----------------------------------------------------
# CASO REAL
# -----------------------------------------------------

usuarios = [
    {"nombre": "Ana", "edad": 25},
    {"nombre": "Luis", "edad": 30}
]

resultado = {u["nombre"]: u["edad"] for u in usuarios}
print(resultado)


# -----------------------------------------------------
# INVERTIR
# -----------------------------------------------------

data = {"a": 1, "b": 2}
invertido = {v: k for k, v in data.items()}
print(invertido)


# -----------------------------------------------------
# CONDICIÓN EN VALOR
# -----------------------------------------------------

resultado = {n: ("par" if n % 2 == 0 else "impar") for n in numeros}
print(resultado)


# -------------------- EJERCICIOS ----------------------

# Ejercicio 1 — Transformación tipo API
usuarios = [
    {"nombre": "Ana", "edad": 25},
    {"nombre": "Luis", "edad": 30},
    {"nombre": "Pedro", "edad": 35}
]

# 👉 crear dict: nombre → edad

# Ejercicio 2 — Filtrado + transformación
# 👉 solo usuarios mayores de 28

# Ejercicio 3 — Transformación compleja
# 👉 nombre → "adulto" o "joven"

# Ejercicio 9 — Matriz → diccionario
matriz = [[1,2], [3,4], [5,6]]

# 👉 clave: índice
# valor: suma de cada fila



# =====================================================
# 3. SET COMPREHENSION
# =====================================================

"""
Un set comprehension permite crear conjuntos (sets)
de forma compacta.

¿Para qué se usa?
Eliminar duplicados
Transformar + deduplicar
Filtrar datos únicos

Cuándo usarla?
Necesitas eliminar duplicados
No te importa el orden
Estás comparando datos
Estás limpiando información

Cuándo NO usarla?
Necesitas orden → usa lista
Necesitas claves → usa diccionario
Necesitas duplicados → usa lista

Estructura:

{expresion for elemento in iterable if condicion}

Características del set:
- NO tiene orden
- NO permite duplicados
- Es mutable
"""

numeros = [1, 2, 2, 3, 3, 4]

unicos = {n for n in numeros}
print(unicos)

# Transformación
cuadrados = {n**2 for n in numeros}
print(cuadrados)

# Filtro
pares = {n for n in numeros if n % 2 == 0}
print(pares)


# -------------------- EJERCICIOS ----------------------

# Ejercicio 1 — Deduplicación + transformación

numeros = [1,2,2,3,3,4]

# 👉 obtener cuadrados únicos

# Ejercicio 2 — Filtrado complejo

numeros = list(range(50))

# 👉 números únicos divisibles por 3 y 5

# Ejercicio 4 — Comparación de datasets

a = [1,2,3,4]
b = [3,4,5,6]

# 👉 elementos comunes

# Ejercicio 6 — Transformación tipo API

usuarios = [
    {"nombre": "Ana", "edad": 25},
    {"nombre": "Luis", "edad": 30},
    {"nombre": "Ana", "edad": 25}
]

# 👉 nombres únicos en mayúscula


# =====================================================
# 4. GENERADORES
# =====================================================

"""
Un generador es una forma de producir valores uno a uno,
en lugar de crear toda la colección en memoria.

Se define con:
- generator expression → ( ... )
- funciones con yield

¿Para qué se usa?
Procesar grandes volúmenes de datos
Pipelines (tipo streaming)
Evitar usar memoria innecesaria

¿Cuándo usar generadores?
Trabajas con muchos datos
Procesas archivos grandes
Haces pipelines
No necesitas todos los datos al mismo tiempo

NO usarlos cuando:
Necesitas acceder múltiples veces
Necesitas indexación
Necesitas tamaño inmediato

Estructura básica:

(expresion for elemento in iterable if condicion)
"""

gen = (n**2 for n in range(5))

for x in gen:
    print(x)


# -----------------------------------------------------
# DIFERENCIA CON LISTA
# -----------------------------------------------------

lista = [n**2 for n in range(5)]
# El generador NO ejecuta todo de una
# Se ejecuta cada vez que lo recorres
gen = (n**2 for n in range(5))

print(lista)
print(gen)


# -----------------------------------------------------
# ERROR COMÚN
# -----------------------------------------------------

gen = (n for n in range(5))
print(list(gen))
print(list(gen))  # vacío


# TIP:
# Los generadores se consumen


# -------------------- EJERCICIOS ----------------------

# Ejercicio 1 — Generador de pares
# 👉 generar números pares hasta 20

# Ejercicio 3 — Filtro + transformación
numeros = range(50)

# 👉 números > 10 al cuadrado



# =====================================================
# 5. CASOS REALES
# =====================================================

usuarios = [
    {"nombre": "Ana", "edad": 25},
    {"nombre": "Luis", "edad": 30},
    {"nombre": "Pedro", "edad": 35}
]

resultado = [u["nombre"].upper() for u in usuarios if u["edad"] > 28]
print(resultado)



# =====================================================
# 💣 EJERCICIOS NIVEL PRO
# =====================================================

# 1. Flatten + filtro
matriz = [[1,2,3],[4,5],[6]]
# obtener > 3

# 2. Dict:
# nombre → edad * 2

# 3. Detectar duplicados en lista

# 4. Generar combinaciones (x,y) donde x != y

# 5. Filtrar usuarios y transformar datos



# =====================================================
# 🧠 MENSAJES CLAVE
# =====================================================

# 1. Comprehensions = transformación de datos
# 2. No abusar (legibilidad primero)
# 3. Generadores ahorran memoria
# 4. Base de pandas / Spark
# 5. Pensar en datos = nivel pro


print("\nFin del bloque 11")