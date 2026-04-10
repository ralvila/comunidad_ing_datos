"""
BLOQUE 8 — BUCLES (LOOPS)

En este bloque aprenderás:
- while
- loops infinitos
- control de flujo
- for
- range()
- iteración
- control de loops
- break
- continue
- else en loops

Nivel: BÁSICO

Modo de uso:
- Ejecuta por secciones
- Lee primero los comentarios
- Predice el resultado antes de ejecutar
- Cambia valores para experimentar
"""

## =====================================================
## 0. CONCEPTOS CLAVE ANTES DE EMPEZAR
## =====================================================
"""
Un loop repite código automáticamente.
Para evitar errores, es clave entender:
- Cómo cambian las variables
- Cómo se detiene el loop
"""

## ¿Qué significa += ?
## counter += 1  ➜ counter = counter + 1
## Se usa para incrementar valores de forma corta y clara

## =====================================================
## 1. WHILE
## =====================================================
"""
Ejecuta un bloque de código MIENTRAS una condición sea verdadera
"""
## -----------------------------------------------------
## Ejemplos
## -----------------------------------------------------

counter = 1  # contador inicial

while counter <= 5:  # condición
    print(counter)
    counter += 1  # incremento del contador

## ¿Qué pasa aquí paso a paso?
## 1. counter empieza en 1
## 2. Se imprime counter
## 3. counter aumenta en 1
## 4. Se repite hasta que counter > 5

## TIPS (PEP 8):
## Usa nombres como counter, index, total
## Asegura que la condición cambie

## BUENAS PRÁCTICAS (PEP 8):
## Nunca uses while sin entender cómo termina
## Prefiere while cuando no sabes cuántas repeticiones habrá

## -------------------- EJERCICIOS ----------------------
## 🟢 Básico:
## Imprime números del 1 al 10
## 🟡 Medio:
## Imprime solo números pares
## 🔴 Avanzado:
## Cuenta regresiva desde 10

## =====================================================
## 2. LOOPS INFINITOS
## =====================================================
"""
Un loop infinito se ejecuta para siempre a menos que use break
"""
## -----------------------------------------------------
## Ejemplos
## -----------------------------------------------------

attempts = 0

while True:  # True siempre es verdadero
    attempts += 1
    print(f"Intento {attempts}") #f-string deja ingresar variables dentro de texto 

    if attempts == 3:
        break  # rompe el loop

## Explicación:
## while True crea un loop infinito
## break fuerza la salida

## BUENAS PRÁCTICAS:
## Nunca dejes un loop infinito sin break

## -------------------- EJERCICIOS ----------------------
## 🟢 Básico:
## Crea un loop con break
## 🟡 Medio:
## Limita intentos de contraseña
## 🔴 Avanzado:
## Menú interactivo

## =====================================================
## 3. FOR E ITERACIÓN
## =====================================================
"""
for se usa para recorrer elementos uno por uno
"""

names = ["Ana", "Luis", "Pedro"]

for name in names:
    print(name)

## Explicación:
## name toma cada valor de la lista
## Primero Ana, luego Luis, luego Pedro

## BUENAS PRÁCTICAS:
## Usa nombres en singular

## -------------------- EJERCICIOS ----------------------
## 🟢 Básico:
## Recorre una lista de números
## 🟡 Medio:
## Imprime nombres en mayúsculas
## 🔴 Avanzado:
## Suma valores de una lista

## =====================================================
## 4. RANGE()
## =====================================================
"""
range genera números automáticamente
"""

for number in range(5):
    print(number)

## range(5) genera: 0, 1, 2, 3, 4

for number in range(1, 6):
    print(number)

## range(inicio, fin)  ➜ fin no se incluye
## Python empieza a contar desde 0, no desde 1 

## -------------------- EJERCICIOS ----------------------
## 🟢 Básico:
## Imprime 0 a 9
## 🟡 Medio:
## Imprime 1 a 20
## 🔴 Avanzado:
## Imprime números pares

## =====================================================
## 5. BREAK Y CONTINUE
## =====================================================
"""
break detiene el loop
continue salta una iteración
"""

for number in range(1, 6):
    if number == 3:
        continue
    print(number)

## continue salta el 3

for number in range(1, 6):
    if number == 4:
        break
    print(number)

## break detiene en 4

## -------------------- EJERCICIOS ----------------------
## 🟢 Básico:
## Usa break
## 🟡 Medio:
## Usa continue
## 🔴 Avanzado:
## Valida datos

## =====================================================
## 6. ELSE EN LOOPS
## =====================================================
"""
else se ejecuta solo si NO hubo break
"""

for number in range(3):
    if number == 10:
        break
else:
    print("Loop finalizado correctamente")

## =====================================================
## 🧠 MENSAJES CLAVE
## =====================================================
## += 1 → sumar uno (incrementar)
## f"texto {variable}" → meter variables en texto
## {} → lugar donde va la variable
##  while True → loop infinito
## break → rompe el loop
## continue → salta una vuelta
## range() → genera números
## i, number, index → contador automático
## else valida que todo fue correcto

## =====================================================
## 📕 EJERCICIOS ;)
## =====================================================

"""
Reto 6 — Tabla de multiplicar
Crea una variable.
Usa un loop para imprimir su tabla del 1 al 10.
"""


"""
Reto 7 — Contar vocales
Dada una palabra (string),
usa un loop para contar cuántas vocales tiene.
"""


"""
Reto 8 — Lista invertida
Dada una lista de números,
imprime los valores en orden inverso usando un loop.
(No uses reverse()).  ## A investigarrr 😋😋 (de nuevo ;) )
"""


"""
Reto 9 — Primer número divisible
Usa un loop del 1 al 50.
Encuentra el primer número divisible por 7
y detén el loop cuando lo encuentres.
"""


"""
Reto 10 — Validación con else
Dada una lista de nombres y un nombre buscado:

- Usa for para buscarlo
- Si lo encuentras, imprime "Nombre encontrado"
- Si NO, imprime "Nombre no encontrado" usando else
"""
