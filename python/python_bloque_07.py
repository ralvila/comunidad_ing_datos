"""
BLOQUE 7 — CONDICIONALES
En este bloque aprenderás:
- if, elif, else
- condicionales anidados
- operadores ternarios

Modo de uso:
- Ejecuta por secciones
- Predice el resultado antes de ejecutar
- Prueba cambiar valores
- Analiza los resultados
"""

## =====================================================
## 1. IF, ELIF, ELSE
## =====================================================
"""
Permiten ejecutar código dependiendo de condiciones
"""
## -----------------------------------------------------
## Ejemplos
## -----------------------------------------------------

age = 20

if age >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")

grade = 4.0

if grade >= 4.5:
    print("Excelente")
elif grade >= 3.0:
    print("Aprobado")
else:
    print("Reprobado")

## TIPS (PEP 8):
## Usa indentación de 4 espacios (nunca tabs)
## Coloca espacios alrededor de operadores (>=, ==)
## Usa nombres de variables descriptivos en inglés

## BUENAS PRÁCTICAS (PEP 8):
## El código debe escribirse en inglés
## Evita números mágicos, usa constantes si es necesario

## -------------------- EJERCICIOS ----------------------
## 🟢 Básico:
## Determina si un número es positivo o negativo
## 🟡 Medio:
## Clasifica una nota académica
## 🔴 Avanzado:
## Valida acceso según edad y estado

## =====================================================
## 2. CONDICIONALES ANIDADOS
## =====================================================
"""
Evalúan una condición dentro de otra
"""
## -----------------------------------------------------
## Ejemplos
## -----------------------------------------------------

def validate_access(age, has_id):
    if age >= 18:
        if has_id:
            print("Acceso permitido")
        else:
            print("Necesita identificación")
    else:
        print("Acceso denegado")

validate_access(20, True)
validate_access(20, False)
validate_access(15, True)

## TIPS (PEP 8):
## Usa snake_case para funciones y variables
## Los booleanos deben empezar con is/has/can

## BUENAS PRÁCTICAS (PEP 8):
## El nombre debe reflejar claramente su propósito
## Evita anidaciones profundas (máx. 2 niveles)

## -------------------- EJERCICIOS ----------------------
## 🟢 Básico:
## Verifica si una persona puede ingresar
## 🟡 Medio:
## Evalúa usuario activo y con permisos
## 🔴 Avanzado:
## Simula un proceso de login

## =====================================================
## 3. OPERADOR TERNARIO
## =====================================================
"""
Condicional en una sola línea
"""
## -----------------------------------------------------
## Ejemplos
## -----------------------------------------------------

age = 17
status = "Mayor de edad" if age >= 18 else "Menor de edad"
print(status)

number = 10
parity = "Par" if number % 2 == 0 else "Impar"
print(parity)

## TIPS (PEP 8):
## Usa ternarios solo si la condición es simple

## BUENAS PRÁCTICAS (PEP 8):
## No anides operadores ternarios
## Si pierde legibilidad, usa if tradicional

## -------------------- EJERCICIOS ----------------------
## 🟢 Básico:
## Evalúa si un número es positivo
## 🟡 Medio:
## Asigna estado según saldo
## 🔴 Avanzado:
## Aplica descuento según condiciones

## =====================================================
## 4. CASOS REALES CON CONDICIONALES
## =====================================================
"""
Uso práctico de condicionales
"""

price = 120

MIN_DISCOUNT_AMOUNT = 100
DISCOUNT_RATE = 0.1

discount = DISCOUNT_RATE if price > MIN_DISCOUNT_AMOUNT else 0

total = price * (1 - discount)
print(total)

## TIPS (PEP 8):
## Las constantes se escriben en MAYÚSCULAS

## BUENAS PRÁCTICAS (PEP 8):
## Variables y constantes siempre en inglés
## El código debe leerse como una historia

## -------------------- EJERCICIOS ----------------------
## 🟢 Básico:
## Aplica descuento simple
## 🟡 Medio:
## Determina envío gratis
## 🔴 Avanzado:
## Simula sistema de facturación

## =====================================================
## 🧠 MENSAJES CLAVE
## =====================================================
## 1. Los condicionales controlan el flujo del programa
## 2. PEP 8 recomienda escribir código en inglés
## 3. Código claro > código corto
## 4. Evita anidar cuando no es necesario
## 5. El código también se enseña leyendo

## =====================================================
## 📕 EJERCICIOS ;)
## =====================================================

"""
Reto 1 — Semáforo
Crea una variable que tenga el color de un semáforo:

-  Rojo → "Detener"
-  Amarillo → "Precaución"
-  Verde → "Avanzar"

Imprime el mensaje correcto.
"""


"""
Reto 2 — Mayor de tres números
Crea tres variables.
Imprime cuál es el mayor de los tres.
(Si hay empate, indícalo).
"""


"""
Reto 3 — Validación de contraseña
Crea una variable para la contraseña.

Reglas:
- Si la longitud es menor a 6 → "Muy corta"
- Si tiene 6 o más caracteres → "Aceptable"

Pista: usa len().  # A investigarrr 😋😋
"""


"""
Reto 4 — Horario laboral
Crea una variable (0 a 23).

- 6 a 11  → "Mañana"
- 12 a 17 → "Tarde"
- 18 a 22 → "Noche"
- Otro    → "Fuera de horario"
"""


"""
Reto 5 — Evaluación combinada
Crea las variables para puntaje y puntos extra:


Si la nota es  >= 60 O tiene puntos extra:
→ "Aprobado"
En otro caso:
→ "Reprobado"
"""