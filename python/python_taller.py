# =====================================================
# 💣 TALLER AVANZADO — PYTHON (BLOQUES 1–13)
# =====================================================

# -----------------------------------------------------
# 🔴 EJERCICIO 1 — LIMPIEZA DE DATOS
# -----------------------------------------------------
# ENUNCIADO

# Dada la siguiente lista:

data = ["10", "20", "", "hola", "50", None, "100"]

# Debes:

# Convertir valores válidos a enteros
# Ignorar inválidos
# Mostrar cuáles fallaron
# Retornar:
# lista limpia
# suma total
# promedio

# -----------------------------------------------------
# 🔴 EJERCICIO 2 — INVENTARIO
# -----------------------------------------------------
# ENUNCIADO

# Crear sistema de inventario usando diccionarios.

# Debe permitir:

# agregar producto
# eliminar producto
# actualizar stock
# buscar producto
# lanzar excepción personalizada si stock < 0

# -----------------------------------------------------
# 🔴 EJERCICIO 3 — DETECTOR DE DUPLICADOS
# -----------------------------------------------------
# ENUNCIADO

# Dada una lista:

numeros = [1,2,2,3,4,4,5,6,6]

# Debes:

# Obtener duplicados
# Obtener únicos
# Contar ocurrencias
# Retornar todo en un diccionario

# -----------------------------------------------------
# 🔴 EJERCICIO 4 — LOGIN REALISTA
# -----------------------------------------------------
# ENUNCIADO

# Crear sistema de login:

# validar usuario
# validar contraseña
# máximo 3 intentos
# usar excepciones personalizadas

# -----------------------------------------------------
# 🔴 EJERCICIO 5 — MATRICES
# -----------------------------------------------------
# ENUNCIADO

# Dada una matriz:

matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

# Debes:

# Obtener diagonal principal
# Obtener suma total
# Flatten
# Obtener pares

# -----------------------------------------------------
# 🔴 EJERCICIO 6 — GENERADOR DE PRIMOS
# -----------------------------------------------------
# ENUNCIADO

# Crear un generador que produzca números primos.

# -----------------------------------------------------
# 🔴 EJERCICIO 7 — ANALIZADOR DE TEXTO
# -----------------------------------------------------
# ENUNCIADO

# Dado un texto:

# contar palabras
# contar letras
# encontrar palabras únicas
# encontrar palabra más repetida

# -----------------------------------------------------
# 🔴 EJERCICIO 8 — CAJERO AUTOMÁTICO
# -----------------------------------------------------
# ENUNCIADO

# Simular cajero:

# saldo inicial
# retirar
# depositar
# validar errores
# historial de movimientos

# -----------------------------------------------------
# 🔴 EJERCICIO 9 — TRANSFORMACIÓN TIPO API
# -----------------------------------------------------
# ENUNCIADO

# Dado:

usuarios = [
    {"nombre": "Ana", "edad": 25},
    {"nombre": "Luis", "edad": 30},
    {"nombre": "Pedro", "edad": 35}
]

# Retornar:

{
    "ANA": 50,
    "LUIS": 60,
    "PEDRO": 70
}

# Solo mayores de 28.

# -----------------------------------------------------
# 🔴 EJERCICIO 10 — DEBUGGING
# -----------------------------------------------------
# ENUNCIADO

# Encuentra y corrige TODOS los errores.

def promedio(lista):

    total = sum(lista)

    promedio = total / len(lista)

    return promedio


data = [10,20,"30",40]

print(promedio(data))

# -----------------------------------------------------
# 🔴 EJERCICIO 11 — PREGUNTAS
# -----------------------------------------------------

# 1. ¿Qué diferencia hay entre lista y generador en memoria?

# 2. ¿Cuándo usarías set en vez de lista?

# 3. ¿Por qué except: puede ser peligroso?

# 4. ¿Cuál es la diferencia entre mutabilidad e inmutabilidad?

# 5. ¿Qué hace realmente super()?

# 6. ¿Por qué Python permite tipado dinámico?

# 7. ¿Cuándo usarías comprehension y cuándo NO?