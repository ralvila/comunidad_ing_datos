"""
==========================================================
PYTHON MASTERS
BLOQUE 16 - BUENAS PRÁCTICAS Y DEBUGGING

Archivo:
16.2A_stack_trace.py

PARTE 1 DE 3

Tema:
Introducción al Stack Trace (Traceback)

Autor:
Comunidad de Ingeniería de Datos

==========================================================

OBJETIVOS

Al finalizar esta sección podrás:

✓ Comprender qué es un Stack Trace.
✓ Diferenciar Stack Trace y Call Stack.
✓ Leer un traceback de Python.
✓ Identificar la línea donde ocurrió un error.
✓ Comprender la anatomía de un traceback.
✓ Localizar rápidamente el origen de una excepción.

==========================================================
"""

###########################################################
# ¿QUÉ ES UN STACK TRACE?
###########################################################

"""
Uno de los mayores cambios entre un programador
principiante y uno experimentado es la forma
en que reaccionan cuando aparece un error.

Un principiante suele decir:

"Python se dañó."

Un desarrollador profesional hace exactamente
lo contrario.

Lee cuidadosamente el Stack Trace.

¿Por qué?

Porque casi siempre contiene toda la información
necesaria para encontrar el problema.

Aprender a leer un Stack Trace es una de las
habilidades más importantes para cualquier
desarrollador de Python.
"""

###########################################################
# ¿QUÉ ES UN TRACEBACK?
###########################################################

"""
En Python normalmente escucharás dos términos.

Traceback

y

Stack Trace

En la práctica suelen utilizarse como sinónimos.

Cuando Python encuentra una excepción que
nadie captura, imprime automáticamente
un Traceback.

Ese Traceback explica:

✓ Dónde ocurrió el error.

✓ Qué funciones fueron llamadas.

✓ Qué tipo de excepción apareció.

✓ El mensaje asociado al error.

Es como un reporte automático
del accidente.
"""

###########################################################
# PRIMER EJEMPLO
###########################################################

numero = 0

# Descomenta esta línea.

# resultado = 100 / numero

"""
Python mostrará algo parecido a esto.

-----------------------------------------

Traceback (most recent call last):

File "16.2A_stack_trace.py", line 75,
in <module>

resultado = 100 / numero

ZeroDivisionError:
division by zero

-----------------------------------------

Aunque parece mucha información,
realmente tiene solo cuatro partes.

Las estudiaremos una por una.
"""

###########################################################
# ANATOMÍA DE UN TRACEBACK
###########################################################

"""
Veamos nuevamente el mismo ejemplo.

-----------------------------------------

Traceback (most recent call last):

File "16.2A_stack_trace.py", line 75,
in <module>

resultado = 100 / numero

ZeroDivisionError:
division by zero

-----------------------------------------
"""

###########################################################
# PARTE 1
###########################################################

"""
Traceback (most recent call last)

Indica que Python comenzará
a mostrar el recorrido realizado
hasta llegar al error.

La frase:

most recent call last

significa:

"La llamada más reciente aparecerá
al final."

Es decir.

El verdadero error normalmente
está en las últimas líneas.

Muchos principiantes empiezan
a leer desde arriba.

Los desarrolladores experimentados
empiezan leyendo desde abajo.
"""

###########################################################
# PARTE 2
###########################################################

"""
File "16.2A_stack_trace.py"

Nos indica el archivo donde
apareció la excepción.

En proyectos pequeños habrá
un solo archivo.

En proyectos empresariales
pueden aparecer muchos.
"""

###########################################################
# PARTE 3
###########################################################

"""
line 75

Indica exactamente
la línea donde Python
detectó el problema.

No significa necesariamente
que allí nació el bug.

Solo significa que allí
la ejecución no pudo continuar.

La causa real puede encontrarse
varias funciones antes.
"""

###########################################################
# PARTE 4
###########################################################

"""
resultado = 100 / numero

Python muestra la línea
que produjo la excepción.

Esto facilita muchísimo
la investigación.

Especialmente en archivos
con miles de líneas.
"""

###########################################################
# PARTE 5
###########################################################

"""
ZeroDivisionError

Es el tipo de excepción.

Después aparece el mensaje.

division by zero

Ese mensaje normalmente
es suficiente para comprender
qué ocurrió.

Siempre léelo completo.

Nunca lo ignores.
"""

###########################################################
# LOS PRINCIPIANTES HACEN ESTO
###########################################################

"""
Aparece un error.

Lo primero que hacen es:

Cerrar la consola.

Buscar en Google.

Modificar código.

Todo excepto leer
el traceback.

La mejor herramienta
ya estaba delante de ellos.

Simplemente no la utilizaron.
"""

###########################################################
# CÓMO LEER UN TRACEBACK
###########################################################

"""
Metodología recomendada.

Paso 1

Ir al final del traceback.

Paso 2

Leer el tipo de excepción.

Paso 3

Leer el mensaje.

Paso 4

Identificar la línea.

Paso 5

Analizar el contexto.

Este procedimiento
resuelve una enorme cantidad
de errores cotidianos.
"""

###########################################################
# EJEMPLO
###########################################################

texto = "Python"

# print(texto + 10)

"""
Obtendremos algo parecido a:

-----------------------------------------

TypeError

can only concatenate str
(not "int") to str

-----------------------------------------

La excepción ya nos está diciendo
qué ocurrió.

Intentamos unir

str

con

int

No necesitamos adivinar.
"""

###########################################################
# OTRO EJEMPLO
###########################################################

numeros = [10, 20]

# print(numeros[5])

"""
Resultado.

IndexError

list index out of range

Observa el mensaje.

No dice:

Python falló.

Dice exactamente
qué ocurrió.

Se intentó acceder
a una posición inexistente.
"""

###########################################################
# OTRO EJEMPLO
###########################################################

persona = {
    "nombre": "Laura"
}

# print(persona["edad"])

"""
Resultado.

KeyError

'edad'

El diccionario no posee
esa clave.

Otra vez.

El traceback ya nos dio
la respuesta.
"""

###########################################################
# OTRO EJEMPLO
###########################################################

# print(variable_inexistente)

"""
Resultado.

NameError

name 'variable_inexistente'
is not defined

Nuevamente.

Python describe exactamente
el problema.
"""

###########################################################
# EL TRACEBACK NO ES EL ENEMIGO
###########################################################

"""
Muchos estudiantes sienten miedo
cuando aparece un traceback.

En realidad es exactamente
lo contrario.

El traceback intenta ayudarte.

Mientras más rápido aprendas
a leerlo,

más rápido solucionarás bugs.
"""

###########################################################
# STACK TRACE VS CALL STACK
###########################################################

"""
Estos conceptos suelen confundirse.

CALL STACK

Representa las funciones activas
durante la ejecución.

Existe incluso cuando
no hay errores.

------------------------------------

STACK TRACE

Es el reporte generado
cuando ocurre una excepción.

Se construye utilizando
la información del Call Stack.

Podemos decir que:

Call Stack

↓

Excepción

↓

Stack Trace
"""

###########################################################
# EJEMPLO CON FUNCIONES
###########################################################

def multiplicar(a, b):
    return a * b


def calcular():
    return multiplicar(5, 8)


resultado = calcular()

print(resultado)

"""
No ocurre ningún error.

Sin embargo.

Internamente existe un Call Stack.

main()

↓

calcular()

↓

multiplicar()

↓

retorno

Si apareciera una excepción,

Python construiría el Traceback
a partir de esa información.
"""

###########################################################
# ¿POR QUÉ APARECE
# "MOST RECENT CALL LAST"?
###########################################################

"""
Imagina este recorrido.

main()

↓

funcion_a()

↓

funcion_b()

↓

funcion_c()

↓

Error

Python imprimirá:

main()

funcion_a()

funcion_b()

funcion_c()

Error

Es decir.

La llamada más reciente
aparece al final.

Por eso debemos empezar
la lectura desde abajo.
"""

###########################################################
# BUENAS PRÁCTICAS
###########################################################

"""
✓ Lee primero el final.

✓ Identifica la excepción.

✓ Lee completamente el mensaje.

✓ Localiza la línea.

✓ Analiza el contexto.

✓ No ignores el traceback.

✓ No copies únicamente
la última línea.

Todo el traceback
contiene información útil.
"""

###########################################################
# TIPS PROFESIONALES
###########################################################

"""
TIP 1

El nombre de la excepción
ya suele indicar el problema.

------------------------------------

TIP 2

Nunca digas:

"No entiendo el error."

Di mejor:

"No entiendo esta parte
del traceback."

Eso facilita muchísimo
la investigación.

------------------------------------

TIP 3

No todos los errores
están donde ocurre
la excepción.

Piensa siempre
en la causa raíz.

------------------------------------

TIP 4

Acostúmbrate a leer
los mensajes completos.

No únicamente el nombre
de la excepción.
"""

###########################################################
# EJERCICIO 1
###########################################################

"""
Analiza.

TypeError

unsupported operand type(s)
for +

'list'

'int'

Pregunta.

¿Qué intentó hacer
el programador?

No ejecutes código.

Describe únicamente
la situación.
"""

###########################################################
# EJERCICIO 2
###########################################################

"""
Analiza.

IndexError

tuple index out of range

Pregunta.

¿Qué hipótesis formularías
antes de modificar el código?
"""

###########################################################
# EJERCICIO 3 (Difícil)
###########################################################

"""
Un compañero te envía únicamente
la siguiente captura.

---------------------------------

ValueError

invalid literal for int()

---------------------------------

No envía código.

No envía contexto.

¿Qué información le pedirías
antes de intentar ayudarlo?

Escribe al menos cinco preguntas.
"""

"""
==========================================================
PYTHON MASTERS
BLOQUE 16 - BUENAS PRÁCTICAS Y DEBUGGING

Archivo:
16.2A_stack_trace.py

PARTE 2 DE 3

Tema:
Interpretando Stack Traces Profesionales

==========================================================

OBJETIVOS

Al finalizar esta sección podrás:

✓ Interpretar Stack Traces complejos.
✓ Analizar múltiples llamadas de funciones.
✓ Encontrar la verdadera causa del error.
✓ Comprender el recorrido de ejecución.
✓ Analizar errores reales de proyectos.

==========================================================
"""

###########################################################
# RECORDANDO EL CALL STACK
###########################################################

"""
En la parte anterior aprendimos que:

Cada vez que una función llama otra función,
Python crea una nueva entrada en el Call Stack.

Por ejemplo.

main()

↓

leer_archivo()

↓

procesar_clientes()

↓

calcular_descuentos()

↓

guardar_resultado()

Cada llamada queda registrada.

Si ocurre una excepción,
Python imprimirá todo ese recorrido.

Ese recorrido es precisamente
el Stack Trace.
"""

###########################################################
# PRIMER TRACEBACK COMPLETO
###########################################################

def dividir(numero1, numero2):
    return numero1 / numero2


def calcular():
    return dividir(100, 0)


# calcular()

"""
Si ejecutamos calcular(),
Python mostrará algo parecido a:

--------------------------------------------------

Traceback (most recent call last):

File "16.2A_stack_trace.py", line 58,
in <module>

calcular()

File "16.2A_stack_trace.py", line 54,
in calcular

return dividir(100, 0)

File "16.2A_stack_trace.py", line 50,
in dividir

return numero1 / numero2

ZeroDivisionError:
division by zero

--------------------------------------------------
"""

###########################################################
# ¿CÓMO LEER ESTE TRACEBACK?
###########################################################

"""
Observemos el recorrido.

main()

↓

calcular()

↓

dividir()

↓

ZeroDivisionError

El Stack Trace nos muestra
el camino completo.

No solamente dónde explotó.

También cómo llegó hasta allí.
"""

###########################################################
# IMPORTANTE
###########################################################

"""
Muchos desarrolladores principiantes
leen únicamente:

ZeroDivisionError

Y dejan de leer.

Eso es un error.

Las funciones anteriores contienen
información extremadamente valiosa.

Ellas muestran el recorrido
de la ejecución.
"""

###########################################################
# EJEMPLO MÁS GRANDE
###########################################################

def leer():
    return [10, 20, 30]


def transformar(datos):
    return calcular(datos)


def calcular(datos):
    return datos[10]


# transformar(leer())

"""
El traceback sería similar a:

main()

↓

transformar()

↓

calcular()

↓

IndexError

Observa cómo el Stack Trace
permite reconstruir
todo el flujo.
"""

###########################################################
# EL ÚLTIMO ERROR NO SIEMPRE
# ES EL PRIMER BUG
###########################################################

"""
Una idea muy importante.

El lugar donde Python detecta
el error

NO siempre coincide

con el lugar donde nació el bug.

Ejemplo.

Función A

↓

Función B

↓

Función C

↓

Función D

↓

Exception

Quizá el dato incorrecto
se generó en la Función A.

Pero solamente explotó
en la Función D.

Por eso debemos seguir
todo el recorrido.
"""

###########################################################
# EJEMPLO
###########################################################

def leer_precio():
    return "100"


def calcular_iva(precio):
    return precio * 0.19


precio = leer_precio()

# calcular_iva(precio)

"""
TypeError

can't multiply sequence
by non-int

Muchos pensarían que
el problema está en calcular_iva().

Realmente comenzó antes.

leer_precio() devolvió
un string.

La causa raíz estaba allí.
"""

###########################################################
# PENSAR COMO UN INVESTIGADOR
###########################################################

"""
Cuando aparece un traceback,
haz estas preguntas.

1.

¿Qué variable produjo el error?

↓

2.

¿Quién creó esa variable?

↓

3.

¿Quién llamó esa función?

↓

4.

¿Quién llamó la anterior?

↓

Así llegamos
a la causa raíz.
"""

###########################################################
# ERRORES ENCADENADOS
###########################################################

"""
En proyectos grandes
una excepción puede generar otra.

Ejemplo.

Intentamos abrir un archivo.

↓

No existe.

↓

El programa intenta leerlo.

↓

Falla nuevamente.

↓

Aparece otro error.

No todos los errores
son independientes.

Muchos son consecuencia
de otro anterior.
"""

###########################################################
# EJEMPLO
###########################################################

def cargar_archivo():
    archivo = None

    return archivo.read()


# cargar_archivo()

"""
Obtendremos algo parecido a:

AttributeError

'NoneType' object
has no attribute 'read'

La excepción visible
es AttributeError.

Pero la causa verdadera fue:

archivo = None

El verdadero bug ocurrió antes.
"""

###########################################################
# TRAZAS LARGAS
###########################################################

"""
En proyectos empresariales
es normal encontrar tracebacks
como este.

main()

↓

API

↓

Controller

↓

Service

↓

Repository

↓

Database

↓

Driver SQL

↓

Excepción

No te asustes.

Simplemente analiza
una función a la vez.
"""

###########################################################
# ¿DEBO LEER TODO EL TRACEBACK?
###########################################################

"""
Sí.

Especialmente cuando
hay muchas funciones.

Cada línea aporta información.

Archivos.

Funciones.

Líneas.

Módulos.

No ignores ninguna.
"""

###########################################################
# EJEMPLO DE INTERPRETACIÓN
###########################################################

"""
Supón el siguiente traceback.

--------------------------------

File clientes.py
line 85

↓

File descuentos.py
line 20

↓

File impuestos.py
line 10

↓

TypeError

--------------------------------

¿Cómo investigarlo?

Paso 1

Leer TypeError.

↓

Paso 2

Ir a impuestos.py.

↓

Paso 3

Revisar qué datos recibió.

↓

Paso 4

Retroceder a descuentos.py.

↓

Paso 5

Encontrar quién envió
el dato incorrecto.

Así trabajan
los desarrolladores profesionales.
"""

###########################################################
# STACK TRACE EN MÓDULOS
###########################################################

"""
Cuando un proyecto tiene
varios archivos,
el traceback muestra
todos ellos.

Ejemplo.

main.py

↓

clientes.py

↓

facturacion.py

↓

impuestos.py

↓

ZeroDivisionError

Esto permite identificar
exactamente qué módulo
originó el problema.
"""

###########################################################
# IMPORTANCIA DEL NOMBRE
# DE LAS FUNCIONES
###########################################################

"""
Observa estos nombres.

funcion1()

funcion2()

funcion3()

Ahora observa estos.

leer_clientes()

validar_cliente()

guardar_factura()

¿Cuál traceback
sería más fácil interpretar?

Los nombres claros
facilitan enormemente
el debugging.
"""

###########################################################
# CÓMO ANALIZAR
# UN STACK TRACE
###########################################################

"""
Método recomendado.

Paso 1

Leer la excepción.

↓

Paso 2

Leer el mensaje.

↓

Paso 3

Ir a la línea.

↓

Paso 4

Inspeccionar variables.

↓

Paso 5

Retroceder por las funciones.

↓

Paso 6

Encontrar la causa raíz.

No empieces modificando código.

Empieza comprendiendo.
"""

###########################################################
# TIPS PROFESIONALES
###########################################################

"""
TIP 1

Mientras más grande
sea el proyecto,

más importante será
el Stack Trace.

-----------------------------------

TIP 2

Nunca ignores
las funciones anteriores.

Ellas cuentan la historia
del error.

-----------------------------------

TIP 3

Cuando un traceback
es muy largo,

analiza solamente
una función a la vez.

-----------------------------------

TIP 4

El primer bug
no siempre produce
la primera excepción.

Puede permanecer oculto
durante mucho tiempo.
"""

###########################################################
# BUENAS PRÁCTICAS
###########################################################

"""
✓ Utiliza nombres descriptivos.

✓ Divide funciones grandes.

✓ Mantén responsabilidades claras.

✓ Lee el traceback completo.

✓ Analiza el flujo.

✓ Busca la causa raíz.

✓ No culpes inmediatamente
a la última línea.
"""

###########################################################
# EJERCICIO 1
###########################################################

"""
Supón el siguiente recorrido.

main()

↓

leer()

↓

procesar()

↓

guardar()

↓

ValueError

Pregunta.

¿Por dónde comenzarías
la investigación?

Justifica tu respuesta.
"""

###########################################################
# EJERCICIO 2
###########################################################

"""
Un traceback tiene
18 funciones.

¿Qué harías?

A)

Modificar código.

B)

Leer únicamente
la excepción.

C)

Seguir el recorrido
función por función.

Respuesta.

C.
"""

###########################################################
# EJERCICIO 3 (Difícil)
###########################################################

"""
Imagina un proyecto
con cinco módulos.

clientes.py

productos.py

ventas.py

facturacion.py

api.py

Diseña una estrategia
para investigar un traceback
que atraviesa todos ellos.

No escribas código.

Describe únicamente
el proceso profesional
que seguirías.
"""

"""
==========================================================
PYTHON MASTERS
BLOQUE 16 - BUENAS PRÁCTICAS Y DEBUGGING

Archivo:
16.2A_stack_trace.py

PARTE 3 DE 3

Tema:
Stack Traces en Proyectos Reales

==========================================================

OBJETIVOS

Al finalizar esta sección podrás:

✓ Analizar Stack Traces de proyectos reales.
✓ Encontrar la causa raíz de una excepción.
✓ Interpretar tracebacks largos.
✓ Aplicar una metodología profesional.
✓ Resolver problemas similares a los encontrados
  en ambientes de producción.

==========================================================
"""

###########################################################
# EL STACK TRACE EN PRODUCCIÓN
###########################################################

"""
Hasta ahora hemos visto ejemplos pequeños.

En un proyecto empresarial,
un Stack Trace puede tener:

• 20 funciones.

• 15 archivos.

• librerías externas.

• frameworks.

• código propio.

La primera impresión suele ser:

"No entiendo nada."

Pero realmente solo debemos hacer
lo mismo que aprendimos.

Seguir el recorrido.
"""

###########################################################
# CASO REAL 1
###########################################################

"""
Supongamos la siguiente arquitectura.

Usuario

↓

API

↓

Controller

↓

Service

↓

Repository

↓

Base de datos

Durante una consulta aparece
una excepción.

El traceback podría verse así:

main.py

↓

api.py

↓

controller.py

↓

service.py

↓

repository.py

↓

TypeError

No debemos empezar
desde main.py.

Debemos comenzar
por la excepción.
"""

###########################################################
# EJEMPLO
###########################################################

def obtener_cliente():
    return "15"


def calcular_descuento(cliente):
    return cliente * 0.15


def generar_factura():
    cliente = obtener_cliente()
    return calcular_descuento(cliente)


# generar_factura()

"""
Traceback

↓

TypeError

↓

calcular_descuento()

↓

generar_factura()

↓

main()

Muchos pensarían:

"La función calcular_descuento
está mal."

No exactamente.

El verdadero problema fue que:

obtener_cliente()

retornó un string.

La causa raíz ocurrió antes.
"""

###########################################################
# CASO REAL 2
###########################################################

"""
Un usuario reporta:

"La aplicación se cierra."

No sabemos nada más.

Primero reproducimos
el problema.

Nunca empieces modificando
código sin reproducir
el escenario.
"""

###########################################################
# EJEMPLO
###########################################################

def leer_archivo(nombre):

    archivo = open(nombre)

    contenido = archivo.read()

    archivo.close()

    return contenido


# leer_archivo("clientes.csv")

"""
Si el archivo no existe,
Python mostrará:

FileNotFoundError

El traceback ya nos dice
qué archivo faltó.

No necesitamos adivinar.
"""

###########################################################
# CASO REAL 3
###########################################################

"""
Una API devuelve:

None

Otra función esperaba:

Un diccionario.

Veamos qué sucede.
"""

###########################################################
# EJEMPLO
###########################################################

def consultar_api():
    return None


def obtener_nombre():

    datos = consultar_api()

    return datos["nombre"]


# obtener_nombre()

"""
Obtendremos:

TypeError

o

AttributeError

dependiendo del código.

Muchos desarrolladores
corrigen el último error.

Los desarrolladores senior
preguntan:

¿Por qué la API devolvió None?

Esa suele ser la verdadera causa.
"""

###########################################################
# CUANDO EL STACK TRACE
# PARECE INFINITO
###########################################################

"""
Algunos frameworks generan
tracebacks enormes.

Por ejemplo:

Django

Flask

FastAPI

PySpark

Databricks

Spark

Puede haber cientos de líneas.

No intentes leerlas todas
de inmediato.

Empieza por:

✓ La excepción.

✓ Tu código.

✓ Tus funciones.

Después revisa
las librerías externas.
"""

###########################################################
# EL ERROR PUEDE
# ESTAR EN LOS DATOS
###########################################################

"""
Una gran cantidad de bugs
no están en el código.

Están en los datos.

Ejemplo.

Esperábamos:

edad = 25

Recibimos:

edad = "veinticinco"

El traceback solamente
muestra dónde explotó.

La investigación debe continuar.
"""

###########################################################
# EJEMPLO
###########################################################

def calcular_impuesto(valor):
    return valor * 0.19


valor = "100"

# calcular_impuesto(valor)

"""
El traceback mostrará
un TypeError.

Pero el verdadero problema
es que alguien envió
un dato incorrecto.
"""

###########################################################
# TRACEBACKS EN CADENA
###########################################################

"""
A veces una excepción
produce otra.

Ejemplo.

Intentamos leer un archivo.

↓

El archivo no existe.

↓

Una variable queda en None.

↓

Intentamos acceder
a sus atributos.

↓

AttributeError

Si solucionamos únicamente
el AttributeError,

el problema volverá.

La causa original era:

FileNotFoundError.
"""

###########################################################
# METODOLOGÍA PROFESIONAL
###########################################################

"""
Cuando aparezca un traceback
utiliza este procedimiento.

1.

Lee la última línea.

↓

2.

Identifica la excepción.

↓

3.

Lee el mensaje.

↓

4.

Ve a la línea indicada.

↓

5.

Inspecciona variables.

↓

6.

Retrocede por las funciones.

↓

7.

Encuentra la causa raíz.

↓

8.

Corrige.

↓

9.

Prueba nuevamente.

↓

10.

Confirma que no aparecieron
nuevos errores.
"""

###########################################################
# LOS MENSAJES DE ERROR
# SON DOCUMENTACIÓN
###########################################################

"""
Los mensajes de Python
fueron escritos por personas.

No son textos aleatorios.

Intentan ayudarte.

Lee siempre:

✓ El tipo de excepción.

✓ El mensaje.

✓ El archivo.

✓ La línea.

✓ El recorrido.

Toda esa información
forma parte del diagnóstico.
"""

###########################################################
# BUENAS PRÁCTICAS
###########################################################

"""
✓ Nunca ignores un traceback.

✓ Guarda capturas completas.

✓ No recortes únicamente
la última línea.

✓ Aprende a identificar
la excepción rápidamente.

✓ Busca la causa raíz.

✓ Reproduce siempre
el problema.

✓ Utiliza el debugger
junto con el traceback.

Ambas herramientas
se complementan perfectamente.
"""

###########################################################
# TIPS PROFESIONALES
###########################################################

"""
TIP 1

La mayoría de los bugs
no requieren escribir código.

Requieren comprender
el código existente.

----------------------------------

TIP 2

No luches contra el traceback.

Úsalo como guía.

----------------------------------

TIP 3

Cada traceback cuenta
una historia.

Aprende a leerla.

----------------------------------

TIP 4

Los mejores desarrolladores
leen muchísimo más
de lo que escriben.

----------------------------------

TIP 5

Si el traceback no tiene sentido,

es probable que todavía
no hayas encontrado
la causa raíz.
"""

###########################################################
# LABORATORIO 1
###########################################################

"""
Analiza cuidadosamente.
"""

###########################################################
# EJERCICIO
###########################################################

def obtener_total(precios):

    total = sum(precios)

    promedio = total / len(precios)

    return promedio


datos = []

# obtener_total(datos)

"""
Preguntas.

1.

¿Qué excepción aparecerá?

2.

¿Qué línea la produce?

3.

¿Cuál es la causa raíz?

4.

¿Cómo la investigarías
utilizando el debugger?
"""

###########################################################
# LABORATORIO 2
###########################################################

"""
Observa el siguiente flujo.

A()

↓

B()

↓

C()

↓

D()

↓

TypeError

Pregunta.

¿Dónde comenzarías
la investigación?

¿Por qué?
"""

###########################################################
# LABORATORIO 3
###########################################################

"""
Construye un programa con:

✓ Cuatro funciones.

✓ Una lista.

✓ Un diccionario.

✓ Una excepción.

Después:

1.

Ejecuta el programa.

2.

Lee completamente
el Stack Trace.

3.

Reconstruye el recorrido
de llamadas.

4.

Encuentra la causa raíz.

No modifiques código
hasta comprender
qué ocurrió.
"""

###########################################################
# RETO PYTHON MASTERS
###########################################################

"""
Imagina que eres
Data Engineer.

Una tubería procesa
10 millones de registros.

Después de dos horas
de ejecución aparece:

KeyError

El traceback contiene:

• notebooks

• funciones

• librerías

• módulos

• utilidades

Diseña una estrategia
profesional de investigación.

Debe incluir:

✓ Cómo leerías el traceback.

✓ Qué variables inspeccionarías.

✓ Dónde colocarías Breakpoints.

✓ Cómo utilizarías
el Call Stack.

✓ Cómo verificarías
la causa raíz.

✓ Cómo comprobarías
que realmente quedó resuelto.

No escribas código.

Describe únicamente
el proceso.
"""

###########################################################
# PREGUNTAS DE REFLEXIÓN
###########################################################

"""
1.

¿Por qué el Stack Trace
es una herramienta
y no un enemigo?

------------------------------------------------

2.

¿Por qué la última excepción
no siempre representa
el primer bug?

------------------------------------------------

3.

¿Qué ventajas tiene
combinar:

Debugger

+

Stack Trace?

------------------------------------------------

4.

¿Por qué un desarrollador
debe comprender el recorrido
de ejecución?

------------------------------------------------

5.

¿Cuál fue el aprendizaje
más importante que obtuviste
de este tema?
"""

###########################################################
# RESUMEN GENERAL DEL TEMA
###########################################################

"""
Durante este tema aprendiste:

✓ Qué es un Stack Trace.

✓ Qué es un Traceback.

✓ Diferencia con el Call Stack.

✓ Anatomía completa
de un traceback.

✓ Cómo interpretar
errores simples.

✓ Cómo interpretar
errores complejos.

✓ Cómo seguir
el recorrido de ejecución.

✓ Cómo encontrar
la causa raíz.

✓ Casos reales
de producción.

✓ Buenas prácticas.

✓ Tips profesionales.

✓ Estrategias de investigación.

✓ Laboratorios.

✓ Retos tipo Python Masters.

A partir de este momento
deberías sentirte cómodo
leyendo tracebacks de Python.

Recuerda siempre:

El objetivo no es memorizar
los mensajes de error.

El objetivo es desarrollar
la capacidad de investigar,
comprender y resolver problemas
de forma sistemática.

Un Stack Trace no es una señal
de que el programa fracasó.

Es una guía que Python te entrega
para ayudarte a encontrar
el problema.

==========================================================
FIN DEL ARCHIVO
==========================================================
"""