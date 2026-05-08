"""
BLOQUE 13 — EXCEPCIONES Y MANEJO DE ERRORES

Objetivo:
- Entender cómo manejar errores correctamente
- Aprender a prevenir fallos
- Construir programas más robustos
- Entender cómo debuggear mejor

IMPORTANTE:
👉 Los errores NO son malos.
👉 Un programador profesional sabe manejarlos.

Modo de uso:
- Ejecuta por secciones
- Rompe el código intencionalmente
- Lee COMPLETO el mensaje del error
- Analiza por qué ocurre
"""


# =====================================================
# 1. ¿QUÉ ES UNA EXCEPCIÓN?
# =====================================================

"""
Una excepción es un error que ocurre DURANTE la ejecución
del programa.

Cuando ocurre una excepción:
- Python detiene el flujo normal
- Busca quién puede manejar el error
- Si nadie lo maneja → el programa falla
"""

# -----------------------------------------------------
# EJEMPLO
# -----------------------------------------------------

# ❌ Error
# print(10 / 0)

# 💥 ZeroDivisionError

# =====================================================
# SYNTAX ERROR vs EXCEPTION
# =====================================================

"""
MUY IMPORTANTE:

SyntaxError:
👉 Python NO puede interpretar el código
👉 El programa ni siquiera empieza

Exception:
👉 Python empieza a ejecutar
👉 Pero falla durante la ejecución
"""


# =====================================================
# 1. SYNTAX ERROR
# =====================================================

# ❌ EJEMPLO 1
# if True
#     print("Hola")

# 💥 SyntaxError: expected ':'

"""
Python detecta el error ANTES de ejecutar.

👉 El programa nunca empieza
"""


# -----------------------------------------------------

# ❌ EJEMPLO 2
# print("Hola"

# 💥 SyntaxError: '(' was never closed

"""
El intérprete ni siquiera puede leer correctamente el código.
"""


# -----------------------------------------------------

# ❌ EJEMPLO 3
# for = 10

# 💥 SyntaxError

"""
No puedes usar palabras reservadas.
"""


# =====================================================
# 2. EXCEPTIONS (ERRORES EN EJECUCIÓN)
# =====================================================

"""
Aquí Python SÍ empieza a ejecutar.
Pero algo falla durante el proceso.
"""


# -----------------------------------------------------
# EJEMPLO 1 — ZeroDivisionError
# -----------------------------------------------------

print("Inicio programa")

x = 10 / 0

print("Fin programa")

# 💥 ZeroDivisionError

"""
👉 Python ejecutó parte del programa
👉 Luego encontró un problema
"""


# -----------------------------------------------------
# EJEMPLO 2 — ValueError
# -----------------------------------------------------

numero = int("hola")

# 💥 ValueError

"""
👉 int() intentó convertir
👉 pero el valor no era válido
"""


# -----------------------------------------------------
# EJEMPLO 3 — IndexError
# -----------------------------------------------------

lista = [1, 2, 3]

print(lista[10])

# 💥 IndexError

"""
👉 La lista existe
👉 Pero el índice no
"""


# =====================================================
# 3. DIFERENCIA CLAVE
# =====================================================

"""
SyntaxError:
❌ El código está mal escrito

Exception:
❌ La lógica o los datos fallaron
"""

# =====================================================
# 🧪 MINI RETO
# =====================================================

"""
Clasifica cada uno:

1.
print("Hola"

2.
int("abc")

3.
lista = [1,2]
lista[5]

4.
if x == 10
    print(x)

👉 ¿SyntaxError o Exception?
"""


# =====================================================
# 🧠 MENSAJES CLAVE
# =====================================================

# 1. SyntaxError = código mal escrito
# 2. Exception = error durante ejecución
# 3. SyntaxError detiene TODO inmediatamente
# 4. Exceptions pueden manejarse con try/except


# =====================================================
# 2. TRY / EXCEPT
# =====================================================

"""
try:
👉 código que puede fallar

except:
👉 qué hacer si falla
"""

# -----------------------------------------------------
# EJEMPLO BÁSICO
# -----------------------------------------------------

try:
    numero = int(input("Ingresa un número: "))
    print(numero)

except:
    print("Ocurrió un error")


# TIP:
# Esto funciona, PERO es mala práctica


# -----------------------------------------------------
# BUENA PRÁCTICA
# -----------------------------------------------------

try:
    numero = int(input("Ingresa un número: "))
    print(numero)

except ValueError:
    print("Debes ingresar un número válido")


# TIP PRO:
# Capturar errores específicos SIEMPRE


# -----------------------------------------------------
# ¿QUÉ PASA INTERNAMENTE?
# -----------------------------------------------------

"""
1. Python entra al try
2. Si todo sale bien → ignora except
3. Si ocurre excepción → salta al except
"""


# =====================================================
# 3. EXCEPT ESPECÍFICOS
# =====================================================

"""
Python tiene MUCHOS tipos de excepciones.
"""

# -----------------------------------------------------
# ValueError
# -----------------------------------------------------

try:
    edad = int("hola")

except ValueError:
    print("No se puede convertir texto a entero")


# -----------------------------------------------------
# TypeError
# -----------------------------------------------------

try:
    resultado = "10" + 5

except TypeError:
    print("Tipos incompatibles")


# -----------------------------------------------------
# IndexError
# -----------------------------------------------------

try:
    lista = [1, 2, 3]
    print(lista[10])

except IndexError:
    print("Índice fuera de rango")


# TIP:
# El tipo de excepción te dice QUÉ salió mal


# =====================================================
# 4. MÚLTIPLES EXCEPT
# =====================================================

try:
    numero = int(input("Número: "))
    resultado = 10 / numero

except ValueError:
    print("Entrada inválida")

except ZeroDivisionError:
    print("No puedes dividir entre cero")


# TIP:
# Orden importa en algunos casos


# =====================================================
# 5. CAPTURAR EL ERROR COMO VARIABLE
# =====================================================

try:
    numero = int("hola")

except ValueError as error:
    print("Ocurrió un error:")
    print(error)


# TIP PRO:
# MUY útil para debugging


# =====================================================
# 6. ELSE
# =====================================================

"""
else se ejecuta SOLO si NO hubo errores
"""

try:
    numero = int(input("Número: "))

except ValueError:
    print("Error")

else:
    print("Todo salió bien")
    print(numero)


# TIP:
# else evita mezclar lógica con manejo de errores


# =====================================================
# 7. FINALLY
# =====================================================

"""
finally SIEMPRE se ejecuta

Haya error o no
"""

try:
    archivo = open("test.txt")

except FileNotFoundError:
    print("Archivo no encontrado")

finally:
    print("Finalizando proceso")


# TIP:
# finally se usa mucho para:
# - cerrar archivos
# - cerrar conexiones
# - liberar recursos


# =====================================================
# 8. RAISE
# =====================================================

"""
raise permite lanzar errores manualmente
"""

edad = -5

if edad < 0:
    raise ValueError("La edad no puede ser negativa")


# TIP:
# raise se usa para validar reglas de negocio


# =====================================================
# 9. EXCEPCIONES PERSONALIZADAS (DETALLADO)
# =====================================================

"""
Python permite crear nuestros propios tipos de errores.

¿Para qué sirve esto?

👉 Para representar errores específicos del negocio o sistema.

Ejemplos reales:
- Edad inválida
- Usuario bloqueado
- Saldo insuficiente
- Archivo corrupto
- Token expirado

Esto hace el código:
- más claro
- más mantenible
- más profesional
"""


# -----------------------------------------------------
# 1. CREAR EXCEPCIÓN PERSONALIZADA
# -----------------------------------------------------

class EdadInvalidaError(Exception):
    pass

"""
¿Qué significa esto?

👉 Estamos creando un nuevo tipo de error.

Hereda de Exception:
- por eso se comporta como una excepción normal
"""


# -----------------------------------------------------
# 2. USO BÁSICO
# -----------------------------------------------------

def validar_edad(edad):

    if edad < 0:
        raise EdadInvalidaError("La edad no puede ser negativa")

    print("Edad válida")


# -----------------------------------------------------
# EJEMPLO
# -----------------------------------------------------

try:
    validar_edad(-5)

except EdadInvalidaError as error:
    print(error)


# TIP:
# raise lanza manualmente el error


# -----------------------------------------------------
# 3. ¿QUÉ MÁS PUEDO HACER DENTRO DE LA FUNCIÓN?
# -----------------------------------------------------

"""
MUY IMPORTANTE:

La función puede tener:
- múltiples validaciones
- lógica compleja
- diferentes excepciones
- transformaciones
- reglas de negocio
"""


# -----------------------------------------------------
# EJEMPLO MÁS REAL
# -----------------------------------------------------

class EdadInvalidaError(Exception):
    pass


def registrar_usuario(nombre, edad):

    # Validar tipo
    if not isinstance(nombre, str):
        raise TypeError("El nombre debe ser texto")

    # Validar vacío
    if nombre.strip() == "":
        raise ValueError("El nombre no puede estar vacío")

    # Validar edad negativa
    if edad < 0:
        raise EdadInvalidaError("La edad no puede ser negativa")

    # Validar edad exagerada
    if edad > 120:
        raise EdadInvalidaError("Edad fuera de rango humano")

    # Si todo sale bien
    print(f"Usuario {nombre} registrado correctamente")


# -----------------------------------------------------
# USO
# -----------------------------------------------------

try:
    registrar_usuario("Santiago", -10)

except EdadInvalidaError as error:
    print("Error de edad:", error)

except TypeError as error:
    print("Error de tipo:", error)

except ValueError as error:
    print("Error de valor:", error)


# -----------------------------------------------------
# 4. PERSONALIZAR MÁS LA EXCEPCIÓN
# -----------------------------------------------------

class SaldoInsuficienteError(Exception):

    def __init__(self, saldo, retiro):

        self.saldo = saldo
        self.retiro = retiro

        mensaje = (
            f"Saldo insuficiente. "
            f"Saldo actual: {saldo}, "
            f"retiro solicitado: {retiro}"
        )

        super().__init__(mensaje)


# -----------------------------------------------------
# USO
# -----------------------------------------------------

def retirar_dinero(saldo, monto):

    if monto > saldo:
        raise SaldoInsuficienteError(saldo, monto)

    return saldo - monto


try:
    retirar_dinero(100, 500)

except SaldoInsuficienteError as error:
    print(error)


# TIP PRO:
# Aquí la excepción contiene información útil


# -----------------------------------------------------
# 5. ¿POR QUÉ ESTO ES IMPORTANTE?
# -----------------------------------------------------

"""
Sin excepciones personalizadas:

❌ ValueError
❌ Exception

👉 muy genérico


Con excepciones personalizadas:

✔ UsuarioBloqueadoError
✔ TokenExpiradoError
✔ SaldoInsuficienteError

👉 mucho más claro
"""


# -----------------------------------------------------
# 6. CASOS REALES (MUY IMPORTANTES)
# -----------------------------------------------------

"""
En sistemas reales se usan TODO el tiempo:

Backend:
- UsuarioNoEncontradoError
- PermisoDenegadoError

Data Engineering:
- ArchivoCorruptoError
- SchemaInvalidoError

APIs:
- TokenExpiradoError
- LimiteRateExceededError
"""


# -----------------------------------------------------
# 7. BUENAS PRÁCTICAS
# -----------------------------------------------------

# ✔ Crear excepciones específicas
# ✔ Mensajes claros
# ✔ Agregar contexto útil
# ✔ Capturar errores específicos

# ❌ No usar Exception para todo
# ❌ No ocultar errores


# -----------------------------------------------------
# 💣 EJERCICIOS AVANZADOS
# -----------------------------------------------------

# -----------------------------------------------------
# 🔴 EJERCICIO 1
# -----------------------------------------------------

"""
Crear:

class PasswordDebilError(Exception)

Validar:
- mínimo 8 caracteres
- al menos un número
"""


# -----------------------------------------------------
# 🔴 EJERCICIO 2
# -----------------------------------------------------

"""
Crear:

class ProductoSinStockError(Exception)

Simular:
- compra de productos
- lanzar excepción si stock = 0
"""


# -----------------------------------------------------
# 🔴 EJERCICIO 3
# -----------------------------------------------------

"""
Crear:

class ArchivoCorruptoError(Exception)

Validar:
- extensión .csv
- contenido no vacío
"""


# -----------------------------------------------------
# 🔴 EJERCICIO 4
# -----------------------------------------------------

"""
Crear sistema bancario:

- validar saldo
- validar monto positivo
- validar límite diario

Cada error debe tener su propia excepción.
"""


# -----------------------------------------------------
# 🧠 MENSAJES CLAVE
# -----------------------------------------------------

# 1. Excepciones personalizadas representan reglas del negocio
# 2. Hacen el código más profesional
# 3. Ayudan muchísimo al debugging
# 4. Permiten separar tipos de errores
# 5. Son MUY usadas en sistemas grandes


# =====================================================
# 10. MALAS PRÁCTICAS (MUY IMPORTANTE)
# =====================================================

# -----------------------------------------------------
# ❌ EXCEPT VACÍO
# -----------------------------------------------------

try:
    x = 10 / 0

except:
    print("Error")


"""
PROBLEMA:
👉 Oculta el error real
👉 Hace debugging más difícil
"""


# -----------------------------------------------------
# ❌ IGNORAR ERRORES
# -----------------------------------------------------

try:
    x = 10 / 0

except ZeroDivisionError:
    pass

"""
⚠️ Esto puede ser peligrosísimo
"""


# -----------------------------------------------------
# ❌ DEMASIADA LÓGICA EN TRY
# -----------------------------------------------------

# ❌ Malo
try:
    x = int(input())
    y = 10 / x
    print(y)
    print("Fin")

except:
    print("Error")

# ✔ Mejor
try:
    x = int(input())

except ValueError:
    print("Número inválido")

else:
    try:
        y = 10 / x
        print(y)

    except ZeroDivisionError:
        print("No dividir por cero")


# =====================================================
# 11. DEBUGGING Y STACK TRACE
# =====================================================

"""
Debugging:
👉 proceso de encontrar y corregir errores

NO es solo arreglar bugs.
Es entender:
- qué pasó
- dónde pasó
- por qué pasó

Una de las habilidades MÁS importantes de un programador.
"""


# -----------------------------------------------------
# 1. ¿QUÉ ES UN STACK TRACE?
# -----------------------------------------------------

"""
El stack trace es el historial del error.

Muestra:
- qué funciones se ejecutaron
- en qué orden
- dónde falló exactamente
"""

# -----------------------------------------------------
# EJEMPLO
# -----------------------------------------------------

def dividir(a, b):
    return a / b


def calcular():
    return dividir(10, 0)


calcular()


# 💥 Stack trace aproximado:

"""
Traceback (most recent call last):

  File "main.py", line 11, in <module>
    calcular()

  File "main.py", line 8, in calcular
    return dividir(10, 0)

  File "main.py", line 4, in dividir
    return a / b

ZeroDivisionError: division by zero
"""


# -----------------------------------------------------
# 2. ¿CÓMO LEERLO?
# -----------------------------------------------------

"""
MUCHA gente lee mal los errores.

👉 Empiezan arriba.
👉 Y normalmente el error importante está ABAJO.
"""


# -----------------------------------------------------
# ORDEN CORRECTO
# -----------------------------------------------------

"""
1. Tipo de error
2. Mensaje
3. Línea exacta
4. Flujo de llamadas
"""


# -----------------------------------------------------
# 3. PARTE MÁS IMPORTANTE
# -----------------------------------------------------

"""
La línea MÁS importante normalmente es:

ZeroDivisionError: division by zero
"""

"""
¿Qué nos dice?

Tipo:
👉 ZeroDivisionError

Mensaje:
👉 division by zero
"""


# -----------------------------------------------------
# 4. ENTENDER EL FLUJO
# -----------------------------------------------------

"""
Stack trace = pila de llamadas

main
 ↓
calcular()
 ↓
dividir()
 ↓
ERROR
"""

# TIP:
# El error muchas veces NO ocurre donde crees


# -----------------------------------------------------
# 5. EJEMPLO MÁS REAL
# -----------------------------------------------------

def obtener_usuario(data):
    return data["usuario"]


def procesar():
    data = {}
    return obtener_usuario(data)


procesar()


# 💥

"""
KeyError: 'usuario'
"""

"""
👉 El problema REAL:

data no tenía esa clave
"""


# -----------------------------------------------------
# 6. DEBUGGING MENTAL (MUY IMPORTANTE)
# -----------------------------------------------------

"""
Cuando veas un error, piensa:

1. ¿Qué esperaba Python?
2. ¿Qué recibió realmente?
3. ¿Qué variable tiene valor incorrecto?
4. ¿Dónde empezó el problema?
"""


# -----------------------------------------------------
# 7. ERROR MUY COMÚN
# -----------------------------------------------------

# ❌

def promedio(lista):
    return sum(lista) / len(lista)


print(promedio([]))

# 💥 ZeroDivisionError


"""
MUCHA gente piensa:
👉 "falló la división"

Pero el problema REAL:
👉 lista vacía
"""


# TIP PRO:
# El error visible no siempre es la causa real


# -----------------------------------------------------
# 8. DEBUGGING CON PRINT()
# -----------------------------------------------------

"""
La técnica más básica:
👉 imprimir valores
"""

def calcular_total(precio, cantidad):

    print("precio =", precio)
    print("cantidad =", cantidad)

    return precio * cantidad


calcular_total(100, "2")

# 💥

"""
Aquí puedes detectar:
cantidad era string, no int
"""


# -----------------------------------------------------
# 9. DEBUGGING EN PASOS
# -----------------------------------------------------

"""
Técnica profesional:

1. Reducir el problema
2. Aislar la línea
3. Verificar variables
4. Confirmar hipótesis
"""


# -----------------------------------------------------
# EJEMPLO
# -----------------------------------------------------

data = ["10", "20", "hola"]

# ❌ falla aquí:
# resultado = [int(x) for x in data]

# ✔ debug:
for x in data:
    print("Procesando:", x)
    print(int(x))


# -----------------------------------------------------
# 10. ERRORES ENCADENADOS
# -----------------------------------------------------

"""
A veces un error causa otro.
"""

# ❌

try:
    numero = int("hola")

except:
    print(resultado)

# 💥 NameError


"""
El error REAL era:
ValueError

Pero generamos otro error encima.
"""


# -----------------------------------------------------
# 11. STACK TRACE EN FUNCIONES
# -----------------------------------------------------

def a():
    b()

def b():
    c()

def c():
    x = 10 / 0

a()

"""
Stack trace:

a()
 ↓
b()
 ↓
c()
 ↓
ERROR
"""

# TIP:
# Mientras más profundo el sistema,
# más importante leer el trace correctamente


# -----------------------------------------------------
# 12. DEBUGGING PROFESIONAL
# -----------------------------------------------------

"""
Herramientas reales:
- breakpoints
- debugger
- logs
- stack traces
- monitoreo
"""

# TIP PRO:
# print() sirve...
# pero debugging profesional usa breakpoints


# -----------------------------------------------------
# 13. MALAS PRÁCTICAS
# -----------------------------------------------------

# ❌ Ignorar el error
# ❌ Leer solo la última línea
# ❌ Probar cosas aleatoriamente
# ❌ Capturar errores sin entenderlos


# -----------------------------------------------------
# 💣 EJERCICIOS AVANZADOS
# -----------------------------------------------------

# -----------------------------------------------------
# 🔴 EJERCICIO 1
# -----------------------------------------------------

"""
Analiza el stack trace:

¿Qué línea falla realmente?
¿Qué causó el problema?
"""

def dividir(a, b):
    return a / b

def procesar():
    return dividir(10, 0)

procesar()


# -----------------------------------------------------
# 🔴 EJERCICIO 2
# -----------------------------------------------------

"""
Detecta el problema REAL:
"""

def promedio(lista):
    return sum(lista) / len(lista)

print(promedio([]))


# -----------------------------------------------------
# 🔴 EJERCICIO 3
# -----------------------------------------------------

"""
Debuggear:
"""

data = ["10", "20", "hola", "40"]

resultado = [int(x) for x in data]


# -----------------------------------------------------
# 🔴 EJERCICIO 4
# -----------------------------------------------------

"""
Agregar prints estratégicos
para detectar:
- tipos
- valores
- flujo
"""


# -----------------------------------------------------
# 🔴 EJERCICIO 5
# -----------------------------------------------------

"""
Crear sistema:
- función A llama B
- B llama C
- C falla

Leer stack trace completo
"""


# -----------------------------------------------------
# 🧠 MENSAJES CLAVE
# -----------------------------------------------------

# 1. Debugging es una habilidad CRÍTICA
# 2. Leer errores correctamente ahorra horas
# 3. El error visible no siempre es la causa real
# 4. Stack trace = historial del problema
# 5. Leer SIEMPRE:
#    - tipo
#    - línea
#    - mensaje
# 6. No adivines → investiga
# 7. Seniors debuggean mejor, no más rápido


# =====================================================
# 12. CASOS REALES
# =====================================================

# -----------------------------------------------------
# VALIDACIÓN DE LOGIN
# -----------------------------------------------------

usuarios = {
    "admin": "1234"
}

usuario = "admin"
password = "9999"

try:
    if usuarios[usuario] != password:
        raise ValueError("Contraseña incorrecta")

except KeyError:
    print("Usuario no existe")

except ValueError as e:
    print(e)


# -----------------------------------------------------
# VALIDACIÓN DE DATOS
# -----------------------------------------------------

data = ["10", "20", "hola", "40"]

numeros = []

for valor in data:
    try:
        numeros.append(int(valor))

    except ValueError:
        print(f"No se pudo convertir: {valor}")

print(numeros)


# =====================================================
# 💣 EJERCICIOS AVANZADOS
# =====================================================

# -----------------------------------------------------
# 🔴 EJERCICIO 1
# -----------------------------------------------------

"""
Crear función dividir(a,b)

Debe:
- manejar división por cero
- manejar tipos inválidos
- retornar mensaje personalizado
"""


# -----------------------------------------------------
# 🔴 EJERCICIO 2
# -----------------------------------------------------

"""
Dada una lista:
["10", "20", "hola", "", "50"]

👉 convertir todo a enteros
👉 ignorar inválidos
👉 mostrar cuáles fallaron
"""


# -----------------------------------------------------
# 🔴 EJERCICIO 3
# -----------------------------------------------------

"""
Crear sistema de login:

- validar usuario
- validar contraseña
- lanzar errores personalizados
"""


# -----------------------------------------------------
# 🔴 EJERCICIO 4
# -----------------------------------------------------

"""
Leer índices de una lista dinámicamente

👉 manejar IndexError
👉 seguir ejecutando programa
"""


# -----------------------------------------------------
# 🔴 EJERCICIO 5
# -----------------------------------------------------

"""
Simular cajero:

- retirar dinero
- validar saldo
- validar monto
- lanzar excepciones
"""


# -----------------------------------------------------
# 🔴 EJERCICIO 6
# -----------------------------------------------------

"""
Crear función:
validar_email(email)

Debe:
- verificar @
- verificar .
- lanzar ValueError si inválido
"""


# -----------------------------------------------------
# 🔴 EJERCICIO 7
# -----------------------------------------------------

"""
Procesar archivo:

- abrir archivo
- leer contenido
- manejar FileNotFoundError
- usar finally
"""


# -----------------------------------------------------
# 🔴 EJERCICIO 8
# -----------------------------------------------------

"""
Crear excepción personalizada:
EdadInvalidaError

Validar:
- edad > 0
- edad < 120
"""


# =====================================================
# 💣 EJERCICIOS NIVEL ENTREVISTA
# =====================================================

# 1.
# ¿Por qué capturar Exception puede ser peligroso?

# 2.
# ¿Cuál es la diferencia entre:
# except:
# except Exception:

# 3.
# ¿Cuándo usar raise?

# 4.
# ¿finally se ejecuta si hay return?

# 5.
# ¿Qué errores NO deberías ocultar?


# =====================================================
# 🧠 MENSAJES CLAVE
# =====================================================

# 1. Los errores SON NORMALES
# 2. try no reemplaza validaciones
# 3. Captura errores específicos
# 4. finally es para limpieza
# 5. raise permite controlar reglas
# 6. Leer errores = habilidad CRÍTICA
# 7. Debugging separa juniors de seniors


print("\nFin del bloque 13")