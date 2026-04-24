"""
================================================================================
  CAPACITACIÓN: FUNCIONES EN PYTHON
  Duración total: 1 hora 30 minutos
================================================================================

  ESTRUCTURA DE LA SESIÓN:
  ------------------------
  Bloque 1 (15 min) - Introducción y sintaxis básica
  Bloque 2 (15 min) - Parámetros y argumentos
  Bloque 3 (15 min) - Retorno de valores y alcance (scope)
  Bloque 4 (15 min) - Funciones avanzadas (lambda, *args, **kwargs)
  Bloque 5 (10 min) - Ejercicio integrador y cierre

  METODOLOGÍA DE CADA BLOQUE:
  ---------------------------
  PARTE A - EJEMPLOS EXPLICADOS: funciones ya implementadas con comentarios.
            Úsalas para explicar paso a paso y ejecutar en vivo.
  PARTE B - EJERCICIOS (2 por bloque): marcados con "# TODO:" para que los
            participantes los completen.

  CÓMO EJECUTAR:
  --------------
  Al final del archivo hay una "zona de pruebas" con llamadas comentadas.
  Descoméntalas a medida que avanzas en la sesión.

================================================================================
"""


# ==============================================================================
# BLOQUE 1: INTRODUCCIÓN Y SINTAXIS BÁSICA  (15 minutos)
# ==============================================================================
#
# PREGUNTAS PARA ABRIR (2 min):
#   - ¿Qué es una función en matemáticas? ¿Y en programación?
#   - ¿Por qué crees que necesitamos funciones?
#
# CONCEPTOS CLAVE (3 min):
#   Una función es un bloque de código reutilizable que realiza una tarea
#   específica. Sus beneficios principales son:
#     1. Reutilización (principio DRY - Don't Repeat Yourself)
#     2. Legibilidad y mantenimiento
#     3. Abstracción (esconder la complejidad interna)
#     4. Facilita las pruebas
#
#   SINTAXIS GENERAL:
#
#       def function_name(parameters):
#           """Docstring opcional pero recomendado."""
#           # cuerpo de la función
#           return value   # opcional
#
# ==============================================================================

# ------------------------------------------------------------------------------
# PARTE A — EJEMPLOS EXPLICADOS (7 min)
# ------------------------------------------------------------------------------

# EJEMPLO 1.1
# Puntos a explicar: la palabra clave "def", los paréntesis, los dos puntos
# al final, y que el cuerpo va INDENTADO (normalmente 4 espacios).
def greet():
    """La función más simple: no recibe nada y no devuelve nada."""
    print("Hello, welcome to the Python training!")


# EJEMPLO 1.2
# Puntos a explicar: los parámetros son "variables internas" que toman el
# valor que pasemos al llamar la función. Explicar la diferencia entre
# DEFINIR la función (arriba) y LLAMARLA (ejecutarla).
def greet_person(name):
    """Recibe un nombre y lo saluda personalizadamente."""
    print(f"Hello, {name}!")


# EJEMPLO 1.3
# Punto a explicar: una función puede recibir varios parámetros separados
# por comas. Aquí introducimos por primera vez el concepto de operar con
# los valores recibidos.
def add_numbers(a, b):
    """Suma dos números y muestra el resultado."""
    result = a + b
    print(f"{a} + {b} = {result}")


# ------------------------------------------------------------------------------
# PARTE B — EJERCICIOS (6 min)
# ------------------------------------------------------------------------------

# EJERCICIO 1.1
# Crea una función "introduce_yourself" que imprima tu nombre y tu profesión
# en dos líneas diferentes.
# TODO: Implementa la función
def introduce_yourself():
    pass


# EJERCICIO 1.2
# Crea una función "rectangle_area" que reciba "width" y "height"
# e imprima el área del rectángulo.
# TODO: Implementa la función
def rectangle_area(width, height):
    pass


# ==============================================================================
# BLOQUE 2: PARÁMETROS Y ARGUMENTOS  (15 minutos)
# ==============================================================================
#
# DIFERENCIA CLAVE (2 min):
#   - PARÁMETRO: variable declarada en la DEFINICIÓN de la función.
#   - ARGUMENTO: valor real que se pasa cuando se LLAMA a la función.
#
#       def greet(name):    <- "name" es un PARÁMETRO
#           print(f"Hi {name}")
#
#       greet("Ana")        <- "Ana" es un ARGUMENTO
#
# TIPOS DE ARGUMENTOS (a ver en los ejemplos):
#   1. Argumentos posicionales
#   2. Argumentos por palabra clave (keyword arguments)
#   3. Parámetros con valores por defecto
#
# ==============================================================================

# ------------------------------------------------------------------------------
# PARTE A — EJEMPLOS EXPLICADOS (9 min)
# ------------------------------------------------------------------------------

# EJEMPLO 2.1 - Argumentos posicionales
# Punto a explicar: el ORDEN importa. El primer argumento va al primer
# parámetro, el segundo al segundo, etc.
# Llamada típica: describe_pet("dog", "Firulais")
def describe_pet(animal_type, pet_name):
    """Describe una mascota usando argumentos en el orden definido."""
    print(f"I have a {animal_type} named {pet_name}.")


# EJEMPLO 2.2 - Argumentos por palabra clave (keyword arguments)
# Punto a explicar: si usas el nombre del parámetro al llamar la función,
# el orden ya NO importa. Esto hace el código más legible.
# Llamada típica: describe_pet(pet_name="Michi", animal_type="cat")
# (se reutiliza la misma función de arriba, solo cambia la forma de llamarla)


# EJEMPLO 2.3 - Valores por defecto
# Puntos a explicar:
#   - Los parámetros con valor por defecto van SIEMPRE al final.
#   - Si no se pasa el argumento, se usa el valor por defecto.
#   - Si se pasa, se sobreescribe.
def create_profile(name, city="Bogotá", country="Colombia"):
    """Crea un perfil con valores por defecto para city y country."""
    print(f"Name: {name} | City: {city} | Country: {country}")


# EJEMPLO 2.4 - Combinando posicionales y por defecto
# Caso práctico: normalmente calculamos un precio sin descuento y con
# impuesto estándar, pero podemos sobreescribir cuando sea necesario.
def calculate_price(base_price, discount=0, tax=0.19):
    """Calcula el precio final aplicando descuento e impuesto (IVA)."""
    price_after_discount = base_price * (1 - discount)
    final_price = price_after_discount * (1 + tax)
    print(f"Final price: ${final_price:,.2f}")


# ------------------------------------------------------------------------------
# PARTE B — EJERCICIOS (4 min)
# ------------------------------------------------------------------------------

# EJERCICIO 2.1
# Crea una función "formal_greeting" que reciba "first_name" y "last_name",
# y tenga un parámetro "title" con valor por defecto "Mr./Ms."
# Debe imprimir algo como: "Good morning, Mr./Ms. Juan Pérez"
# TODO: Implementa la función
def formal_greeting(first_name, last_name, title="Mr./Ms."):
    pass


# EJERCICIO 2.2
# Crea una función "order_coffee" que reciba "size" (obligatorio)
# y dos parámetros opcionales: "milk_type" con valor por defecto "whole"
# y "sugar" con valor por defecto 1.
# Debe imprimir: "Order: <size> coffee with <milk_type> milk and <sugar> sugar(s)"
# TODO: Implementa la función
def order_coffee(size, milk_type="whole", sugar=1):
    pass


# ==============================================================================
# BLOQUE 3: RETORNO DE VALORES Y ALCANCE (SCOPE)  (15 minutos)
# ==============================================================================
#
# RETURN vs PRINT (3 min):
#   - print() muestra algo en pantalla (efecto visual).
#   - return devuelve un valor que puede ser usado por el código que llama.
#
#   REGLA DE ORO: las funciones "útiles" generalmente RETORNAN valores,
#   no solo los imprimen. Esto las hace componibles y testeables.
#
# ALCANCE (SCOPE):
#   - Variables LOCALES: existen solo dentro de la función.
#   - Variables GLOBALES: existen en todo el programa.
#   - Regla LEGB: Local -> Enclosing -> Global -> Built-in
#
# ==============================================================================

# ------------------------------------------------------------------------------
# PARTE A — EJEMPLOS EXPLICADOS (9 min)
# ------------------------------------------------------------------------------

# EJEMPLO 3.1 - print vs return
# Puntos a explicar:
#   - add_with_print NO devuelve nada (devuelve None implícitamente).
#   - add_with_return devuelve el valor y podemos REUTILIZARLO.
#   - Demostración en vivo: result = add_with_return(2, 3) + 10
def add_with_print(a, b):
    """Imprime la suma pero NO la devuelve."""
    print(a + b)


def add_with_return(a, b):
    """Devuelve la suma para que pueda usarse en otros cálculos."""
    return a + b


# EJEMPLO 3.2 - Retornar múltiples valores
# Punto a explicar: Python "empaqueta" los valores en una tupla
# automáticamente, y al llamar la función podemos "desempaquetarlos".
def get_statistics(numbers):
    """Devuelve el mínimo, máximo y promedio de una lista."""
    minimum = min(numbers)
    maximum = max(numbers)
    average = sum(numbers) / len(numbers)
    return minimum, maximum, average

# Uso: mn, mx, avg = get_statistics([10, 20, 30, 40])


# EJEMPLO 3.3 - Retorno temprano (early return)
# Punto a explicar: return no solo devuelve, también TERMINA la función.
# Muy útil para manejar casos especiales al inicio.
def divide(a, b):
    """Divide dos números manejando la división por cero."""
    if b == 0:
        return None  # Salida temprana si hay error
    return a / b


# EJEMPLO 3.4 - Alcance de variables
# Punto a explicar: "local_message" NO existe fuera de la función.
# Si intentas imprimirla fuera, da NameError.
global_message = "I am a global variable"

def demonstrate_scope():
    """Muestra la diferencia entre variables locales y globales."""
    local_message = "I am a local variable"
    print(global_message)  # Puede leer la global
    print(local_message)   # Puede leer la local


# ------------------------------------------------------------------------------
# PARTE B — EJERCICIOS (3 min)
# ------------------------------------------------------------------------------

# EJERCICIO 3.1
# Crea una función "celsius_to_fahrenheit" que reciba grados Celsius
# y RETORNE (no imprima) los grados Fahrenheit.
# Fórmula: F = C * 9/5 + 32
# TODO: Implementa la función
def celsius_to_fahrenheit(celsius):
    pass


# EJERCICIO 3.2
# Crea una función "analyze_text" que reciba un string y retorne una tupla:
# (character_count, word_count, uppercase_version)
# TODO: Implementa la función
def analyze_text(text):
    pass


# ==============================================================================
# BLOQUE 4: FUNCIONES AVANZADAS  (15 minutos)
# ==============================================================================
#
# TEMAS (3 min de teoría):
#   1. Funciones lambda (funciones anónimas de una sola línea)
#   2. *args   -> cantidad variable de argumentos posicionales
#   3. **kwargs -> cantidad variable de argumentos por palabra clave
#   4. Las funciones son objetos de primera clase (se pueden pasar como
#      argumento, asignar a variables, etc.)
#
# ==============================================================================

# ------------------------------------------------------------------------------
# PARTE A — EJEMPLOS EXPLICADOS (8 min)
# ------------------------------------------------------------------------------

# EJEMPLO 4.1 - Lambda
# Una lambda es una función pequeña y ANÓNIMA.
# Sintaxis:  lambda parameters: expression
# Punto a explicar: son muy útiles cuando necesitas una función "de usar
# y tirar", por ejemplo dentro de map, filter o sorted.
square = lambda x: x ** 2
# square(5) devuelve 25

numbers = [1, 2, 3, 4, 5]
squared_list = list(map(lambda x: x ** 2, numbers))       # [1, 4, 9, 16, 25]
even_list = list(filter(lambda x: x % 2 == 0, numbers))   # [2, 4]


# EJEMPLO 4.2 - *args
# Punto a explicar: el asterisco "empaqueta" todos los argumentos
# posicionales sobrantes en una TUPLA llamada "numbers" (el nombre es
# convencional pero puedes llamarla como quieras).
def sum_all(*numbers):
    """Suma cualquier cantidad de números."""
    total = 0
    for n in numbers:
        total += n
    return total

# Uso: sum_all(1, 2, 3)         -> 6
#      sum_all(1, 2, 3, 4, 5)   -> 15


# EJEMPLO 4.3 - **kwargs
# Punto a explicar: los dos asteriscos empaquetan los argumentos por
# palabra clave sobrantes en un DICCIONARIO.
def create_user(**user_data):
    """Crea un usuario con cualquier cantidad de atributos."""
    print("User data:")
    for key, value in user_data.items():
        print(f"  - {key}: {value}")

# Uso: create_user(name="Ana", age=30, city="Medellín")


# EJEMPLO 4.4 - Funciones como objetos de primera clase
# Punto a explicar: en Python las funciones son objetos. Puedes:
#   - Asignarlas a variables
#   - Pasarlas como argumentos a otras funciones
#   - Retornarlas desde otras funciones
# Esto es la base de los decoradores y la programación funcional.
def apply_operation(x, y, operation):
    """Aplica una función pasada como argumento."""
    return operation(x, y)

def multiply(a, b):
    return a * b

# Uso: apply_operation(4, 5, multiply)                -> 20
#      apply_operation(4, 5, lambda a, b: a - b)      -> -1


# ------------------------------------------------------------------------------
# PARTE B — EJERCICIOS (4 min)
# ------------------------------------------------------------------------------

# EJERCICIO 4.1
# Completa la función para ordenar una lista de tuplas por el SEGUNDO
# elemento (la nota), de mayor a menor, usando lambda + sorted().
# Ejemplo de entrada: [("Ana", 85), ("Luis", 72), ("Carla", 91), ("Pedro", 68)]
# Pista: sorted(lista, key=..., reverse=True)
# TODO: Implementa la función
def sort_students_by_grade(students):
    pass


# EJERCICIO 4.2
# Crea una función "average" con *args que calcule el promedio de todos
# los números que reciba. Debe retornar 0 si no recibe argumentos
# (para evitar divisiones por cero).
# TODO: Implementa la función
def average(*numbers):
    pass

# ==============================================================================
# CIERRE Y RESUMEN
# ==============================================================================
#
# PUNTOS CLAVE PARA RECORDAR:
#   1. Define funciones con "def function_name(parameters):"
#   2. Usa docstrings para documentar qué hace tu función.
#   3. Prefiere "return" sobre "print" — hace tus funciones reutilizables.
#   4. Los parámetros con valor por defecto van al final.
#   5. *args y **kwargs te dan flexibilidad con argumentos variables.
#   7. Las funciones pequeñas y con una sola responsabilidad son las mejores.
#
#
# ==============================================================================


# ==============================================================================
# ZONA DE PRUEBAS
# ==============================================================================
# Descomenta las líneas a medida que avanzas en cada bloque para ejecutar
# los ejemplos en vivo.
# ==============================================================================
if __name__ == "__main__":
    print("=" * 70)
    print("CAPACITACIÓN: FUNCIONES EN PYTHON")
    print("=" * 70)

    # --- BLOQUE 1 ---
    # greet()
    # greet_person("team")
    # add_numbers(5, 3)

    # --- BLOQUE 2 ---
    # describe_pet("dog", "Firulais")
    # describe_pet(pet_name="Michi", animal_type="cat")
    # create_profile("María")
    # create_profile("John", city="New York", country="USA")
    # calculate_price(100000, discount=0.1)

    # --- BLOQUE 3 ---
    # print(add_with_return(2, 3) + 10)
    # mn, mx, avg = get_statistics([10, 20, 30, 40])
    # print(f"Min: {mn}, Max: {mx}, Avg: {avg}")
    # print(divide(10, 0))   # None
    # demonstrate_scope()

    # --- BLOQUE 4 ---
    # print(square(5))
    # print(squared_list)
    # print(even_list)
    # print(sum_all(1, 2, 3, 4, 5))
    # create_user(name="Ana", age=30, city="Medellín")
    # print(apply_operation(4, 5, multiply))
    # print(apply_operation(4, 5, lambda a, b: a - b))

    # --- BLOQUE 5: RECURSIVIDAD ---
    # countdown(5)
    # print(factorial(4))                 # 24
    # print(sum_list([1, 2, 3, 4, 5]))    # 15
    # print(fibonacci(7))                 # 13
    # print(factorial_iterative(4))       # 24

    print("\n¡Listos para explorar las funciones! 🐍")
