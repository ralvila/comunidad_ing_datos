"""
BLOQUE 4 — VARIABLES Y TIPOS DE DATOS

En este bloque aprenderás:

- Qué es una variable y cómo se usa
- Tipos de datos básicos en Python (int, float, bool, str)
- Cómo funciona el tipado dinámico
- Conversión de tipos (casting) y sus riesgos
- Sistemas numéricos (binario, octal, hexadecimal)
- Notación científica

Modo de uso:
- Ejecuta el archivo por secciones
- Lee cuidadosamente los comentarios
- Predice qué hará el código antes de ejecutarlo
- Prueba modificar los ejemplos
- Provoca errores intencionalmente y analízalos
"""


# =====================================================
# 1. VARIABLES
# =====================================================

"""
Una variable es un espacio en memoria donde se almacena un valor.
"""

nombre = "Santiago"
edad = 30

print(nombre)
print(edad)

# TIP:
# Piensa en variables como cajas con etiquetas

# BUENAS PRÁCTICAS:
# ✔ nombres descriptivos
# ❌ x = 10
# ✔ edad_usuario = 10


# -------------------- EJERCICIOS ----------------------

# 🟢 Básico:
# Crea variables: ciudad y pais e imprímelas

# 🟡 Medio:
# Crea variables: producto, precio, cantidad

# 🔴 Avanzado:
# Calcula total = precio * cantidad e imprímelo



# =====================================================
# 2. TIPOS DE DATOS BÁSICOS
# =====================================================

"""
Tipos principales:
int, float, bool, str
"""

# -----------------------------------------------------
# Ejemplos
# -----------------------------------------------------

entero = 10
decimal = 3.14
booleano = True
texto = "Hola"

print(type(entero))
print(type(decimal))
print(type(booleano))
print(type(texto))

# TIP:
# Usa type() para inspeccionar

# BUENAS PRÁCTICAS:
# Sé consciente del tipo de dato


# -------------------- EJERCICIOS ----------------------

# 🟢 Básico:
# Crea una variable de cada tipo

# 🟡 Medio:
# Imprime el tipo de cada una

# 🔴 Avanzado:
# Intenta sumar un string con un número y analiza el error



# =====================================================
# 3. TIPADO DINÁMICO
# =====================================================

"""
Python no requiere declarar tipos.
Puede cambiar el tipo en ejecución.
"""

x = 10
print(type(x))

x = "Hola"
print(type(x))

# TIP:
# Flexibilidad alta, pero puede causar errores

# BUENAS PRÁCTICAS:
# Mantener consistencia en tipos


# -------------------- EJERCICIOS ----------------------

# 🟢 Básico:
# Cambia una variable de int a str

# 🟡 Medio:
# Imprime el tipo antes y después

# 🔴 Avanzado:
# Provoca un error mezclando tipos y explica por qué



# =====================================================
# 4. CONVERSIÓN DE TIPOS (CASTING)
# =====================================================

"""
Permite convertir entre tipos
"""

numero = "10"
convertido = int(numero)

print(convertido)
print(type(convertido))

# Otros ejemplos
print(float(10))
print(str(10))
print(bool(1))

# ERROR COMÚN (descomenta):
# int("hola")

# TIP:
# No todas las conversiones son válidas

# BUENAS PRÁCTICAS:
# Validar datos antes de convertir


# -------------------- EJERCICIOS ----------------------

# 🟢 Básico:
# Convierte un string a int

# 🟡 Medio:
# Convierte un número a string y concaténalo

# 🔴 Avanzado:
# Intenta convertir "abc" a int y analiza el error



# =====================================================
# 5. SISTEMAS NUMÉRICOS
# =====================================================

"""
Python soporta múltiples bases numéricas
"""

# -----------------------------------------------------
# Ejemplos
# -----------------------------------------------------

decimal = 10
binario = 0b1010
octal = 0o12
hexadecimal = 0xA

print(decimal, binario, octal, hexadecimal)

# TIP:
# Todos representan el mismo valor

# BUENAS PRÁCTICAS:
# Usar decimal salvo casos específicos


# -------------------- EJERCICIOS ----------------------

# 🟢 Básico:
# Declara un número en binario

# 🟡 Medio:
# Usa bin() para convertir decimal a binario

# 🔴 Avanzado:
# Demuestra que diferentes bases representan el mismo número



# =====================================================
# 6. NOTACIÓN CIENTÍFICA
# =====================================================

"""
Representación compacta de números grandes o pequeños
"""

numero = 1e3
pequeno = 1e-3

print(numero)
print(pequeno)

# TIP:
# Muy usado en ciencia y análisis de datos

# BUENAS PRÁCTICAS:
# Usar cuando mejore la legibilidad


# -------------------- EJERCICIOS ----------------------

# 🟢 Básico:
# Define un número con notación científica

# 🟡 Medio:
# Imprime su valor real

# 🔴 Avanzado:
# Usa notación científica en un cálculo (ej: multiplicación)



# =====================================================
# 🧠 MENSAJES CLAVE
# =====================================================

# 1. Las variables almacenan datos
# 2. Python es dinámico (cuidado con errores)
# 3. El tipo de dato importa
# 4. El casting es poderoso pero peligroso
# 5. Entender números es clave en datos


print("\nFin del bloque 4")