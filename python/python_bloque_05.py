"""
BLOQUE 5 — OPERADORES

En este bloque aprenderás:

- Operadores aritméticos
- Operadores de comparación
- Operadores lógicos
- Precedencia de operadores

Modo de uso:
- Ejecuta por secciones
- Predice el resultado antes de ejecutar
- Prueba cambiar valores
- Analiza los resultados
"""


# =====================================================
# 1. OPERADORES ARITMÉTICOS
# =====================================================

"""
Permiten realizar operaciones matemáticas
"""

# -----------------------------------------------------
# Ejemplos
# -----------------------------------------------------

a = 10
b = 3

print(a + b)   # suma
print(a - b)   # resta
print(a * b)   # multiplicación
print(a / b)   # división (float)
print(a // b)  # división entera
print(a % b)   # módulo (residuo)
print(a ** b)  # potencia

# TIP:
# / siempre devuelve float

# BUENAS PRÁCTICAS:
# Usa nombres claros para variables en cálculos


# -------------------- EJERCICIOS ----------------------

# 🟢 Básico:
# Realiza suma, resta y multiplicación con dos números

# 🟡 Medio:
# Calcula el promedio de 3 números

# 🔴 Avanzado:
# Calcula el total de una compra (precio * cantidad + impuesto)



# =====================================================
# 2. OPERADORES DE COMPARACIÓN
# =====================================================

"""
Comparan valores y devuelven True o False
"""

# -----------------------------------------------------
# Ejemplos
# -----------------------------------------------------

x = 10
y = 5

print(x == y)  # igual
print(x != y)  # diferente
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

# TIP:
# == compara, = asigna

# BUENAS PRÁCTICAS:
# Usa comparaciones claras y simples


# -------------------- EJERCICIOS ----------------------

# 🟢 Básico:
# Compara dos números

# 🟡 Medio:
# Verifica si una persona es mayor de edad (>= 18)

# 🔴 Avanzado:
# Evalúa múltiples condiciones (ej: rango entre 10 y 20)



# =====================================================
# 3. OPERADORES LÓGICOS
# =====================================================

"""
Permiten combinar condiciones
"""

# -----------------------------------------------------
# Ejemplos
# -----------------------------------------------------

edad = 25
tiene_identificacion = True

print(edad > 18 and tiene_identificacion)
print(edad > 18 or False)
print(not tiene_identificacion)

# TIP:
# and → ambas condiciones deben cumplirse
# or → al menos una
# not → invierte el valor

# BUENAS PRÁCTICAS:
# Usa paréntesis para mayor claridad


# -------------------- EJERCICIOS ----------------------

# 🟢 Básico:
# Usa AND con dos condiciones

# 🟡 Medio:
# Evalúa si un número está entre 10 y 50

# 🔴 Avanzado:
# Simula una validación (edad > 18 AND tiene permiso)



# =====================================================
# 4. PRECEDENCIA DE OPERADORES
# =====================================================

"""
Define el orden en que se ejecutan las operaciones
"""

# -----------------------------------------------------
# Ejemplos
# -----------------------------------------------------

resultado = 10 + 2 * 3
print(resultado)  # 16

resultado = (10 + 2) * 3
print(resultado)  # 36

# Orden general:
# 1. ()
# 2. **
# 3. *, /, //, %
# 4. +, -
# 5. Comparaciones
# 6. Lógicos

# TIP:
# Usa paréntesis para evitar confusión

# BUENAS PRÁCTICAS:
# Prioriza claridad sobre memorizar precedencia


# -------------------- EJERCICIOS ----------------------

# 🟢 Básico:
# Evalúa 5 + 3 * 2

# 🟡 Medio:
# Usa paréntesis para cambiar el resultado

# 🔴 Avanzado:
# Combina operaciones aritméticas y lógicas y predice resultado



# =====================================================
# 5. COMBINACIÓN DE OPERADORES (CASOS REALES)
# =====================================================

"""
Aquí se integran todos los operadores
"""

precio = 100
cantidad = 2
descuento = 0.1

total = precio * cantidad * (1 - descuento)

print(total)

# Ejemplo lógico
edad = 20
tiene_permiso = True

puede_entrar = edad >= 18 and tiene_permiso
print(puede_entrar)

# TIP:
# Aquí es donde realmente se usan en la vida real

# BUENAS PRÁCTICAS:
# Divide expresiones complejas en variables


# -------------------- EJERCICIOS ----------------------

# 🟢 Básico:
# Calcula total de compra simple

# 🟡 Medio:
# Agrega descuento y condición

# 🔴 Avanzado:
# Simula un sistema:
# - si compra > 100 aplica descuento
# - si no, no aplica



# =====================================================
# 🧠 MENSAJES CLAVE
# =====================================================

# 1. Los operadores son la base de la lógica
# 2. Comparar no es lo mismo que asignar
# 3. Usa paréntesis para evitar errores
# 4. Divide expresiones complejas
# 5. Pensar antes de ejecutar = nivel profesional


print("\nFin del bloque 5")