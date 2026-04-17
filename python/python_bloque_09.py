"""
BLOQUE 9 — COLECCIONES BÁSICAS

En este bloque aprenderás:

- Listas (listas dinámicas y mutables)
- Tuplas (inmutables)
- Diccionarios (estructura clave-valor)
- Sets (colecciones sin duplicados)

Modo de uso:
- Ejecuta por secciones
- Predice resultados antes de ejecutar
- Modifica los ejemplos
- Analiza los cambios
"""


# =====================================================
# 1. LISTAS
# =====================================================

"""
Las listas son colecciones ordenadas y mutables.
"""

# -----------------------------------------------------
# 1.1 Creación
# -----------------------------------------------------

numeros = [1, 2, 3, 4]
nombres = ["Ana", "Luis", "Pedro"]

print(numeros)
print(nombres)

# TIP:
# Las listas pueden mezclar tipos (aunque no es buena práctica)

# BUENAS PRÁCTICAS:
# Mantener listas homogéneas


# -------------------- EJERCICIOS ----------------------

# 🟢 Básico:
# Crea una lista de 3 frutas

# 🟡 Medio:
# Crea una lista de precios

# 🔴 Avanzado:
# Crea una lista de productos con nombre y precio (simulado)



# -----------------------------------------------------
# 1.2 Indexing
# -----------------------------------------------------

"""
Indexing es la forma de acceder a un elemento específico
de una secuencia usando su posición (índice).

Sintaxis:
secuencia[indice]

- indice → posición del elemento
"""

numeros = [10, 20, 30, 40]

print(numeros[0])  # 10
print(numeros[1])  # 20

# TIP:
# Índices empiezan en 0

# -------------------- INDEXING NEGATIVO ----------------------

print(numeros[-1])  # 40 (último)
print(numeros[-2])  # 30

# TIP:
# Índices negativos empiezan desde el final

# -------------------- CON STRINGS ----------------------

texto = "Python"

print(texto[0])   # 'P'
print(texto[-1])  # 'n'

# TIP:
# Funciona igual en strings y tuplas

# -------------------- ERRORES COMUNES ----------------------

# ❌ Error
# print(numeros[10])

# 💥 IndexError: list index out of range

# TIP:
# El índice debe existir en la secuencia

# -------------------- BUENAS PRÁCTICAS ----------------------

# ✔ Validar tamaño antes de acceder
if len(numeros) > 2:
    print(numeros[2])

# ✔ Usar índices negativos para últimos elementos

# -------------------- EJERCICIOS ----------------------

# 🟢 Básico:
# Imprime el primer elemento de una lista

# 🟡 Medio:
# Imprime el último elemento usando índice negativo

# 🔴 Avanzado:
# Accede a varios elementos y evita errores usando len()



# -----------------------------------------------------
# 1.3 Slicing
# -----------------------------------------------------

"""
Slicing es una forma de extraer una parte (subconjunto)
de una secuencia (lista, string, tupla, etc.)

Sintaxis general:
secuencia[inicio:fin:paso]

- inicio → índice donde empieza (incluido)
- fin → índice donde termina (excluido)
- paso → salto (opcional)
"""

numeros = [0, 1, 2, 3, 4, 5]

print(numeros[1:4])   # [1, 2, 3]
print(numeros[:3])    # [0, 1, 2]
print(numeros[3:])    # [3, 4, 5]

# TIP:
# slicing no rompe la lista original

# -------------------- SLICING INVERSO ----------------------

print(numeros[::-1])  # [5, 4, 3, 2, 1, 0]

# TIP:
# step negativo invierte la secuencia

# -------------------- CON STRINGS ----------------------

texto = "Python"

print(texto[0:3])   # "Pyt"
print(texto[::-1])  # "nohtyP"

# TIP:
# Funciona igual que con listas

# -------------------- BUENAS PRÁCTICAS ----------------------

# ✔ Usar slicing para copiar listas
copia = numeros[:]

# ✔ Usar slicing para evitar modificar originales

# ❌ Evitar slicing confuso (difícil de leer)

# -------------------- ERRORES COMUNES ----------------------

# ❌ Índices fuera de rango (no rompe, pero puede confundir)
print(numeros[0:100])  # devuelve lo disponible

# ❌ No entender que el final no se incluye


# -------------------- EJERCICIOS ----------------------

# 🟢 Básico:
# Obtén los primeros 2 elementos

# 🟡 Medio:
# Obtén los últimos 2 elementos

# 🔴 Avanzado:
# Obtén elementos con salto (step)



# -----------------------------------------------------
# 1.4 Métodos (append, insert, remove, pop)
# -----------------------------------------------------

numeros.append(5)
print(numeros)

numeros.insert(0, 0)
print(numeros)

numeros.remove(3)
print(numeros)

numeros.pop()
print(numeros)

# TIP:
# append → agrega al final
# insert → posición específica
# remove → elimina valor
# pop → elimina por índice

# BUENAS PRÁCTICAS:
# Validar antes de eliminar elementos


# -------------------- EJERCICIOS ----------------------

# 🟢 Básico:
# Agrega un elemento con append

# 🟡 Medio:
# Inserta en una posición específica

# 🔴 Avanzado:
# Elimina elementos de distintas formas y analiza



# =====================================================
# 2. TUPLAS
# =====================================================

"""
Colecciones ordenadas e inmutables
"""

# -----------------------------------------------------
# 2.1 Creación
# -----------------------------------------------------

tupla = (1, 2, 3)
print(tupla)

# TIP:
# No se pueden modificar


# -----------------------------------------------------
# 2.2 Inmutabilidad
# -----------------------------------------------------

# ❌ Error:
# tupla[0] = 10

# BUENAS PRÁCTICAS:
# Usar tuplas para datos que no cambian


# -------------------- EJERCICIOS ----------------------

# 🟢 Básico:
# Crea una tupla

# 🟡 Medio:
# Accede a sus elementos

# 🔴 Avanzado:
# Intenta modificarla y analiza el error



# -----------------------------------------------------
# 2.3 Packing / Unpacking
# -----------------------------------------------------

"""
Packing:
👉 Agrupar múltiples valores en una sola variable o meter varios valores en una sola variable

Unpacking:
👉 Extraer esos valores en múltiples variables o sacar esos valores en variables separadas

Es muy usado en Python para trabajar con datos de forma limpia
"""
# -------------------- PACKING ----------------------


# Sin darte cuenta, ya lo haces:
datos = 1, 2, 3

print(datos)
print(type(datos))  # tuple

"""
¿Qué pasó aquí?

👉 Python tomó múltiples valores y los "empaquetó" en una tupla

Eso es PACKING
"""

# También explícito:
datos = (1, 2, 3)


# 💡 ANALOGÍA
"""
Packing = meter cosas en una caja

caja = (objeto1, objeto2, objeto3)
"""
# -------------------- UNPACKING ----------------------

datos = (1, 2, 3)

a, b, c = datos

print(a)
print(b)
print(c)

"""
👉 Tomaste la caja y sacaste cada elemento

Eso es UNPACKING
"""

# 💡 ANALOGÍA
"""
Unpacking = abrir la caja y repartir su contenido
"""

# -------------------- REGLA IMPORTANTE ----------------------

"""
Debe haber la misma cantidad de variables y valores
"""

# ❌ ERROR
# a, b = (1, 2, 3)

# 💥 ValueError

# ✔ CORRECTO
a, b, c = (1, 2, 3)

# -------------------- UNPACKING CON * (PARTE FLEXIBLE) ----------------------

datos = (1, 2, 3, 4, 5)

a, *resto = datos

print(a)      # 1
print(resto)  # [2, 3, 4, 5]

"""
👉 Aquí Python hace esto:

a = 1
resto = TODO LO DEMÁS

El * permite capturar múltiples valores
"""


# MÁS EJEMPLOS

a, b, *resto = (1, 2, 3, 4, 5)
print(a, b, resto)  # 1 2 [3,4,5]

a, *medio, z = (1, 2, 3, 4, 5)
print(a, medio, z)  # 1 [2,3,4] 5

# -------------------- CASO REAL IMPORTANTE ----------------------

# Intercambio de variables

a = 10
b = 20

a, b = b, a

print(a, b)

"""
👉 Esto es packing + unpacking en una sola línea

Python hace internamente:
(20, 10) → luego lo asigna a (a, b)
"""

# -------------------- UNPACKING EN FUNCIONES ----------------------

def obtener_usuario():
    return "Santiago", 30

nombre, edad = obtener_usuario()

print(nombre, edad)

"""
👉 La función devuelve una tupla
👉 Y tú la desempaquetas directamente
"""

# -------------------- ERROR COMÚN QUE DEBEN ENTENDER ----------------------

# ❌ ERROR típico
# nombre, edad = "Santiago"

"""
Python intenta hacer esto:

nombre = 'S'
edad = 'a'
...

💥 ERROR: demasiados valores
"""

# -------------------- BUENAS PRÁCTICAS ----------------------

# ✔ Usar unpacking para código limpio
# ✔ Usar * cuando no sabes cuántos valores hay
# ✔ Nombres claros

# ❌ Evitar unpacking confuso
# a, b, c, d, e, f = datos  # difícil de mantener

# -------------------- EJERCICIOS ----------------------

# 🟢 Básico:
# Crea una tupla con 3 valores y desempaquétala

# 🟡 Medio:
# Usa * para capturar valores intermedios

# 🔴 Avanzado:
# Crea una función que retorne 3 valores y desempaquétalos



# =====================================================
# 3. DICCIONARIOS (KEY - VALUE)
# =====================================================

"""
Un diccionario es una estructura de datos que almacena información
en pares clave → valor.

Es similar a un JSON.

Ejemplo mental:
"nombre" → "Santiago"
"edad"   → 30
"""

# -----------------------------------------------------
# 3.1 Creación
# -----------------------------------------------------

persona = {
    "nombre": "Santiago",
    "edad": 30
}

print(persona)

# TIP:
# Ideal para datos tipo JSON
# Las claves (keys) deben ser únicas


# -----------------------------------------------------
# 3.2 Acceso
# -----------------------------------------------------

print(persona["nombre"])

# TIP:
# Si la clave no existe → error


# -------------------- EJERCICIOS ----------------------

# 🟢 Básico:
# Accede a un valor

# 🟡 Medio:
# Agrega una nueva clave

# 🔴 Avanzado:
# Maneja error de clave inexistente

# -----------------------------------------------------
# 3.3 AGREGAR Y MODIFICAR
# -----------------------------------------------------

# Agregar
persona["email"] = "test@email.com"

# Modificar
persona["edad"] = 31

print(persona)

# TIP:
# Si la clave existe → actualiza
# Si no existe → crea


# -----------------------------------------------------
# 3.4 ELIMINAR ELEMENTOS
# -----------------------------------------------------

del persona["email"]

print(persona)

# TIP:
# Validar antes de eliminar



# -----------------------------------------------------
# 3.5 Iteración
# -----------------------------------------------------

# Claves
for clave in persona:
    print(clave)

# Valores
for valor in persona.values():
    print(valor)

# Clave + valor
for clave, valor in persona.items():
    print(clave, valor)

# TIP:
# items() devuelve pares clave-valor

# BUENAS PRÁCTICAS:
# Iterar cuando trabajas con datos reales

# -------------------- EJERCICIOS ----------------------

# 🟢 Básico:
# Itera sobre claves

# 🟡 Medio:
# Itera sobre valores

# 🔴 Avanzado:
# Itera clave-valor y transforma datos

# -----------------------------------------------------
# 3.6 MÉTODOS ÚTILES
# -----------------------------------------------------

# get() evita errores
print(persona.get("nombre"))
print(persona.get("direccion", "No existe"))

# keys()
print(persona.keys())

# values()
print(persona.values())

# items()
print(persona.items())

# -----------------------------------------------------
# 3.7 DICCIONARIOS ANIDADOS (IMPORTANTE)
# -----------------------------------------------------

usuario = {
    "nombre": "Santiago",
    "direccion": {
        "ciudad": "Bogotá",
        "pais": "Colombia"
    }
}

print(usuario["direccion"]["ciudad"])

# TIP:
# Muy común en APIs

# -----------------------------------------------------
# 3.8 BUENAS PRÁCTICAS
# -----------------------------------------------------

# ✔ Usar nombres claros
# ✔ Validar claves con get()
# ✔ No asumir que la clave existe

# ❌ Evitar:
# acceso directo sin validación en datos reales

# -----------------------------------------------------
# 💣 EJERCICIO NIVEL PRO (MUY IMPORTANTE)
# -----------------------------------------------------

# Simula datos tipo API

usuarios = [
    {"nombre": "Ana", "edad": 25},
    {"nombre": "Luis", "edad": 30},
    {"nombre": "Pedro", "edad": 35}
]

# 👉 Imprime solo los nombres

# 👉 Imprime solo los mayores de 28

# 👉 Cuenta cuántos usuarios hay


# =====================================================
# 4. SETS
# =====================================================

"""
Un set es una colección:

- NO ordenada
- SIN elementos duplicados
- MUTABLE (puedes agregar/quitar elementos)

Es equivalente al concepto matemático de conjunto.
"""

# -----------------------------------------------------
# 4.1 Creación
# -----------------------------------------------------

numeros = {1, 2, 3, 3}
print(numeros)

# TIP:
# Elimina duplicados automáticamente
# No mantiene orden

# --------------------- CREACIÓN DESDE LISTAS ----------------

lista = [1, 2, 2, 3, 4, 4]

sin_duplicados = set(lista)

print(sin_duplicados)

"""
👉 Esto es MUY usado en datos
para limpiar duplicados
"""

# =====================================================
# 4.2 AGREGAR Y ELIMINAR
# =====================================================

numeros = {1, 2, 3}

numeros.add(4)
print(numeros)

numeros.remove(2)
print(numeros)

# ❌ ERROR si no existe
# numeros.remove(10)

# ✔ Alternativa segura
numeros.discard(10)

# TIP:
# remove → error si no existe
# discard → no falla

# -----------------------------------------------------
# 4.3 Operaciones
# -----------------------------------------------------

a = {1, 2, 3}
b = {3, 4, 5}

# Unión (todos)
print(a.union(b))         # {1,2,3,4,5}

# Intersección (comunes)
print(a.intersection(b))  # {3}

# Diferencia
print(a.difference(b))    # {1,2}

# Diferencia simétrica
print(a.symmetric_difference(b))  # {1,2,4,5}

# TIP:
# Estas operaciones son MUY usadas en análisis de datos
# union → combina
# intersection → comunes

# BUENAS PRÁCTICAS:
# Usar sets para eliminar duplicados

# =====================================================
# 4.4 VALIDACIONES
# =====================================================

print(1 in a)  # True
print(5 in a)  # False

# TIP:
# Muy eficiente para búsquedas

# =====================================================
# 4.5 SETS NO PERMITEN INDEXING
# =====================================================

# ❌ ERROR
# print(a[0])

"""
👉 No hay orden → no hay índice
"""

# =====================================================
# 4.6 BUENAS PRÁCTICAS
# =====================================================

# ✔ Usar sets para eliminar duplicados
# ✔ Usar sets para comparaciones rápidas
# ✔ Usar discard en lugar de remove si no estás seguro

# ❌ No usar sets si necesitas orden


# -------------------- EJERCICIOS ----------------------

# 🟢 Básico:
# Crea un set con números duplicados

# 🟡 Medio:
# Convierte una lista con duplicados a set

# 🔴 Avanzado:
# Dadas dos listas, encuentra:
# - elementos comunes
# - elementos únicos

# =====================================================
# 💣 EJERCICIO NIVEL PRO (MUY IMPORTANTE)
# =====================================================

# Simulación real

usuarios_app = {"Ana", "Luis", "Pedro"}
usuarios_web = {"Luis", "Pedro", "Carlos"}

# 👉 Usuarios en ambos sistemas
# 👉 Usuarios solo en app
# 👉 Usuarios solo en web



# =====================================================
# 🧠 MENSAJES CLAVE
# =====================================================

# 1. Listas → ordenadas y mutables
# 2. Tuplas → inmutables
# 3. Diccionarios → clave-valor (muy usados en datos)
# 4. Sets → sin duplicados
# 5. Elegir la estructura correcta es clave


# =====================================================
# MÉTODOS MÁS COMUNES — COLECCIONES
# =====================================================

"""
Aquí verás los métodos más utilizados en:

- Listas
- Tuplas
- Diccionarios
- Sets

Estos métodos son fundamentales en cualquier proyecto real.
"""


# =====================================================
# 1. LISTAS
# =====================================================

numeros = [1, 2, 3]

# -----------------------------------------------------
# Métodos principales
# -----------------------------------------------------

numeros.append(4)       # agrega al final
numeros.insert(0, 0)    # inserta en posición
numeros.remove(2)       # elimina valor
ultimo = numeros.pop()  # elimina último

print(numeros)

# Otros útiles
numeros.sort()          # ordena
numeros.reverse()       # invierte
print(len(numeros))     # tamaño

numeros.copy()            # copia de la lista
numeros.clear()           # vacía la lista

# ordenar sin modificar original
ordenada = sorted(numeros)
print(ordenada)

# TIP:
# append y pop son los más usados
# sorted() es mejor que sort() si no quieres modificar

# BUENAS PRÁCTICAS:
# Validar antes de usar remove()


# -------------------- EJERCICIOS ----------------------

# 🟢 Básico:
# Agrega elementos a una lista

# 🟡 Medio:
# Ordena una lista

# 🔴 Avanzado:
# Elimina elementos y controla errores



# =====================================================
# 2. TUPLAS
# =====================================================

tupla = (1, 2, 3, 2)

# -----------------------------------------------------
# Métodos principales
# -----------------------------------------------------

print(tupla.count(2))  # cuenta ocurrencias
print(tupla.index(3))  # posición

# TIP:
# Las tuplas tienen pocos métodos porque son inmutables

# BUENAS PRÁCTICAS:
# Usar tuplas para datos constantes


# -------------------- EJERCICIOS ----------------------

# 🟢 Básico:
# Cuenta un valor en la tupla

# 🟡 Medio:
# Encuentra índice de un valor

# 🔴 Avanzado:
# Maneja error si el valor no existe



# =====================================================
# 3. DICCIONARIOS
# =====================================================

persona = {
    "nombre": "Santiago",
    "edad": 30
}

# -----------------------------------------------------
# Métodos principales
# -----------------------------------------------------

print(persona.get("nombre"))         # acceso seguro
print(persona.get("direccion", "N/A"))

print(persona.keys())   # claves
print(persona.values()) # valores
print(persona.items())  # clave-valor

persona.update({"edad": 31})  # actualizar
persona.pop("edad")           # eliminar

# setdefault → crea si no existe
persona.setdefault("pais", "Colombia")

# popitem → elimina último elemento
persona.popitem()

# copy → copia
copia = persona.copy()

# clear → vacía
# persona.clear()

print(persona)

# TIP:
# get() evita errores
# setdefault evita validaciones manuales

# BUENAS PRÁCTICAS:
# No acceder directamente sin validar
# copy() antes de modificar estructuras importantes


# -------------------- EJERCICIOS ----------------------

# 🟢 Básico:
# Usa get()

# 🟡 Medio:
# Itera con items()

# 🔴 Avanzado:
# Actualiza múltiples valores



# =====================================================
# 4. SETS
# =====================================================

a = {1, 2, 3}
b = {3, 4, 5}

# -----------------------------------------------------
# Métodos principales
# -----------------------------------------------------

a.add(4)
a.remove(2)     # error si no existe
a.discard(10)   # no falla

print(a.union(b))
print(a.intersection(b))
print(a.difference(b))

# update → agrega múltiples valores
a.update(b)

# isdisjoint → sin elementos en común
print(a.isdisjoint(b))

# issubset → es subconjunto
print({1, 2}.issubset(a))

# issuperset → contiene a otro
print(a.issuperset({1, 2}))

# copy
copia = a.copy()

# clear
# a.clear()

# TIP:
# discard es más seguro que remove
# update() es como union pero modifica el original

# BUENAS PRÁCTICAS:
# Usar sets para deduplicación y comparación
# Usar operaciones para lógica, no loops innecesarios


# -------------------- EJERCICIOS ----------------------

# 🟢 Básico:
# Agrega elementos a un set

# 🟡 Medio:
# Encuentra intersección

# 🔴 Avanzado:
# Compara dos sets y analiza diferencias

# =====================================================
# 5. FUNCIONES BUILT-IN (MUY IMPORTANTES)
# =====================================================

numeros = [10, 20, 30]

print(len(numeros))   # tamaño
print(max(numeros))   # máximo
print(min(numeros))   # mínimo
print(sum(numeros))   # suma

# TIP:
# Estas funciones se usan TODO el tiempo

# BUENAS PRÁCTICAS:
# Usar built-ins en lugar de loops manuales




# =====================================================
# 🧠 MENSAJES CLAVE
# =====================================================

# 1. Cada estructura tiene sus propios métodos
# 2. Listas → manipulación dinámica
# 3. Diccionarios → acceso seguro con get()
# 4. Sets → operaciones matemáticas
# 5. Conocer estos métodos acelera muchísimo el desarrollo


print("\nFin del bloque 9")