"""
==========================================================
PYTHON MASTERS
BLOQUE 16 - BUENAS PRÁCTICAS Y DEBUGGING

Archivo:
16.1B_debugging_herramientas.py

PARTE 1 DE 3

Tema:
Herramientas de Debugging en Python

Autor:
Comunidad de Ingeniería de Datos

==========================================================

OBJETIVOS

Al finalizar este archivo serás capaz de:

✓ Utilizar print() correctamente para depurar.
✓ Comprender cuándo print() deja de ser suficiente.
✓ Aprender estrategias profesionales de debugging.
✓ Identificar el flujo real de ejecución.
✓ Localizar variables incorrectas.
✓ Reducir el tiempo necesario para encontrar bugs.

En esta primera parte NO utilizaremos todavía el
Debugger de VSCode.

Primero aprenderemos la herramienta que todos los
programadores usan cuando empiezan: print().

Después veremos por qué los profesionales utilizan
debuggers.

==========================================================
"""

###########################################################
# ¿POR QUÉ NECESITAMOS HERRAMIENTAS?
###########################################################

"""
Encontrar un bug sin herramientas es muy difícil.

Imagina este escenario.

Una función recibe un número.

Ese número pasa por otras seis funciones.

Finalmente el resultado es incorrecto.

¿Cómo descubres dónde cambió?

Puedes intentar leer el código...

O puedes observar qué ocurre mientras
el programa se ejecuta.

Eso es exactamente lo que hace el debugging.
"""

###########################################################
# EL DEBUGGING CONSISTE EN OBSERVAR
###########################################################

"""
Cuando un médico hace un diagnóstico
no empieza recetando medicamentos.

Primero observa.

Pregunta.

Hace exámenes.

Después toma decisiones.

Debugging funciona exactamente igual.

Primero observamos.

Después entendemos.

Finalmente corregimos.
"""

###########################################################
# LA PRIMERA HERRAMIENTA:
# print()
###########################################################

"""
Todos los programadores del mundo
han utilizado print() para depurar.

No porque sea la mejor herramienta.

Sino porque es la más sencilla.

print() permite visualizar:

• Variables

• Resultados

• Condiciones

• Flujo del programa

• Contenido de listas

• Diccionarios

• Objetos

Es una herramienta extremadamente útil
cuando el programa es pequeño.
"""

###########################################################
# EJEMPLO 1
###########################################################

nombre = "Carlos"

print(nombre)

"""
Salida

Carlos

Muy sencillo.

Pero durante debugging normalmente
queremos más contexto.
"""

###########################################################
# MAL USO DE print()
###########################################################

numero = 10

print(numero)

"""
¿Qué significa ese 10?

No lo sabemos.

Si aparecen cincuenta números
en la consola será imposible saber
qué representa cada uno.

Por eso debemos imprimir información
descriptiva.
"""

###########################################################
# BUEN USO DE print()
###########################################################

numero = 10

print("Valor de numero:", numero)

"""
Salida

Valor de numero: 10

Mucho más claro.
"""

###########################################################
# EJEMPLO 2
###########################################################

precio = 25000
iva = 0.19

print("Precio:", precio)
print("IVA:", iva)

total = precio + (precio * iva)

print("Total:", total)

"""
Ahora podemos observar cómo cambian
los datos.

Este es el principio fundamental
del debugging.

Observar.

Nunca asumir.
"""

###########################################################
# DEBUGGING PASO A PASO
###########################################################

"""
Supongamos que obtenemos
un resultado incorrecto.

¿Cómo investigamos?

Paso 1

Imprimir la entrada.

Paso 2

Imprimir resultados intermedios.

Paso 3

Imprimir la salida.

Eso permite descubrir
en qué momento aparecen
los datos incorrectos.
"""

###########################################################
# EJEMPLO
###########################################################

numero = 8

print("Número inicial:", numero)

numero *= 5

print("Después de multiplicar:", numero)

numero -= 12

print("Después de restar:", numero)

numero /= 4

print("Resultado final:", numero)

"""
Cada print funciona como una fotografía.

Nos muestra el estado del programa
en un instante específico.
"""

###########################################################
# EJEMPLO 3
###########################################################

edad = 18

print("Edad:", edad)

if edad >= 18:
    print("Es mayor de edad")

else:
    print("Es menor de edad")

"""
No solamente podemos imprimir variables.

También podemos imprimir qué camino
está tomando el programa.
"""

###########################################################
# RASTREAR EL FLUJO
###########################################################

"""
Muchas veces el bug no está
en una variable.

Está en el flujo.

Por ejemplo.

¿Entró al if?

¿Entró al else?

¿Entró al for?

¿Entró al while?

Los print ayudan a responder
estas preguntas.
"""

###########################################################
# EJEMPLO
###########################################################

numero = 12

print("Inicio")

if numero > 10:
    print("Entró al primer if")

print("Continúa")

print("Fin")

"""
Salida

Inicio

Entró al primer if

Continúa

Fin
"""

###########################################################
# DEBUGGING EN FUNCIONES
###########################################################

"""
Las funciones suelen esconder
gran parte de los bugs.

Veamos cómo inspeccionarlas.
"""

###########################################################
# EJEMPLO
###########################################################

def cuadrado(numero):

    print("Entró a cuadrado()")

    print("Número recibido:", numero)

    resultado = numero ** 2

    print("Resultado:", resultado)

    return resultado


valor = cuadrado(7)

print("Valor retornado:", valor)

"""
Ahora sabemos exactamente
qué ocurrió dentro de la función.

Sin print()

Solo conoceríamos el resultado final.
"""

###########################################################
# DEBUGGING EN BUCLES
###########################################################

"""
Los loops son otra fuente frecuente
de errores.

Veamos cómo inspeccionarlos.
"""

###########################################################
# EJEMPLO
###########################################################

numeros = [10, 20, 30]

for numero in numeros:

    print("Iteración actual:", numero)

"""
Salida

Iteración actual: 10

Iteración actual: 20

Iteración actual: 30
"""

###########################################################
# EJEMPLO
###########################################################

total = 0

for numero in [4, 8, 12]:

    print("----------------")

    print("Total antes:", total)

    print("Número:", numero)

    total += numero

    print("Total después:", total)

print("Resultado final:", total)

"""
Observa cómo podemos reconstruir
todo el proceso.

No solamente el resultado.
"""

###########################################################
# DEBUGGING DE LISTAS
###########################################################

frutas = ["Manzana", "Pera", "Mango"]

print("Lista completa:")

print(frutas)

print()

print("Cantidad:", len(frutas))

print()

print("Primer elemento:", frutas[0])

"""
Con pocos prints podemos entender
el estado completo de la colección.
"""

###########################################################
# DEBUGGING DE DICCIONARIOS
###########################################################

cliente = {
    "nombre": "Laura",
    "edad": 30,
    "activo": True
}

print(cliente)

print()

print("Nombre:", cliente["nombre"])

print("Edad:", cliente["edad"])

print("Activo:", cliente["activo"])

"""
Cuando trabajamos con estructuras
grandes resulta muy útil imprimir
solamente la información relevante.
"""

###########################################################
# IMPRIMIR DEMASIADO TAMBIÉN ES UN ERROR
###########################################################

"""
Muchos principiantes hacen esto.

print(variable1)

print(variable2)

print(variable3)

print(variable4)

print(variable5)

print(variable6)

print(variable7)

...

Después la consola tiene miles
de líneas.

Y encontrar información útil
es casi imposible.

El debugging debe ser intencional.

Cada print debe responder
una pregunta específica.
"""

###########################################################
# BUENA PRÁCTICA
###########################################################

"""
Antes de escribir un print,
pregúntate.

¿Qué quiero comprobar?

Ejemplos.

✓ ¿La función recibió el dato correcto?

✓ ¿Entró al if?

✓ ¿El cálculo fue correcto?

✓ ¿La lista llegó vacía?

✓ ¿El archivo realmente existe?

Cada print debe tener un propósito.
"""

###########################################################
# TIP PROFESIONAL
###########################################################

"""
No escribas:

print(variable)

Escribe:

print("Total antes de aplicar descuento:", total)

Dentro de seis meses,
agradecerás haber sido descriptivo.
"""

###########################################################
# EJERCICIO 1
###########################################################

"""
Sin ejecutar el código.

def multiplicar(a, b):

    resultado = a * b

    return resultado

¿En qué lugares agregarías print()
para verificar:

• Parámetros.

• Resultado.

• Valor retornado.

Intenta hacerlo antes
de continuar.
"""

###########################################################
# EJERCICIO 2
###########################################################

"""
Supón que un usuario dice:

"Mi pedido nunca aparece."

¿Qué imprimirías?

A)

Toda la base de datos.

B)

Cada variable del programa.

C)

Solo la información relacionada
con ese pedido.

Respuesta:

C.

Debugging consiste en reducir
la cantidad de información.
No aumentarla.
"""

"""
==========================================================
PYTHON MASTERS
BLOQUE 16 - BUENAS PRÁCTICAS Y DEBUGGING

Archivo:
16.1B_debugging_herramientas.py

PARTE 2 DE 3

Tema:
El Debugger Profesional de VS Code

==========================================================

OBJETIVOS

Al finalizar esta sección podrás:

✓ Comprender qué es un debugger.
✓ Utilizar Breakpoints.
✓ Utilizar Step Over.
✓ Utilizar Step Into.
✓ Utilizar Step Out.
✓ Continuar la ejecución (Continue).
✓ Reiniciar una sesión de debugging.
✓ Inspeccionar variables.
✓ Comprender el Call Stack.
✓ Utilizar Watches.

A partir de este punto dejaremos de depender
de print() y comenzaremos a trabajar como lo
hacen los desarrolladores profesionales.

==========================================================
"""

###########################################################
# ¿QUÉ ES UN DEBUGGER?
###########################################################

"""
Un debugger es una herramienta que permite
detener temporalmente un programa mientras
está ejecutándose.

Durante esa pausa podemos:

✓ Ver variables.

✓ Cambiar variables.

✓ Revisar funciones.

✓ Observar listas.

✓ Inspeccionar objetos.

✓ Ver el flujo del programa.

Todo esto SIN modificar el código.

Esa es la enorme ventaja frente a print().
"""

###########################################################
# ¿POR QUÉ LOS PROFESIONALES
# PREFIEREN EL DEBUGGER?
###########################################################

"""
Supongamos que una función tiene
250 líneas.

Con print() probablemente necesitaríamos
escribir muchos mensajes.

Con un debugger simplemente detenemos
la ejecución exactamente donde queremos.

Podemos revisar todo el estado
del programa en pocos segundos.

Mucho más rápido.

Mucho más limpio.

Mucho más profesional.
"""

###########################################################
# BREAKPOINTS
###########################################################

"""
La herramienta más importante
de un debugger.

Un Breakpoint es un punto donde
el programa se detendrá.

Cuando llegue a esa línea:

La ejecución se pausa.

El programa NO termina.

Simplemente espera a que el desarrollador
decida qué hacer.

En VS Code basta con hacer clic
a la izquierda del número de línea.

Aparecerá un punto rojo.

Ese es el Breakpoint.
"""

###########################################################
# EJEMPLO
###########################################################

precio = 120

descuento = 0.15

# ← Coloca aquí un Breakpoint

total = precio - (precio * descuento)

print(total)

"""
Cuando el programa llegue aquí:

precio = 120

descuento = 0.15

Todavía NO habrá calculado total.

Podrás inspeccionar ambas variables.
"""

###########################################################
# ¿QUÉ OCURRE CUANDO
# EL PROGRAMA SE DETIENE?
###########################################################

"""
VS Code mostrará varias ventanas.

Variables

Call Stack

Watch

Debug Console

Toolbar

Cada una tiene una función diferente.

Las estudiaremos una por una.
"""

###########################################################
# VARIABLES
###########################################################

"""
La ventana Variables muestra
todas las variables disponibles.

Ejemplo.

numero = 10

nombre = "Laura"

activo = True

lista = [1,2,3]

diccionario = {"A":10}

Sin escribir un solo print()
podemos ver todos esos valores.

Incluso listas enormes.

Incluso objetos.

Incluso DataFrames.
"""

###########################################################
# STEP OVER
###########################################################

"""
Atajo habitual

F10

Step Over significa:

Ejecuta la siguiente línea.

Si encuentra una función...

NO entra.

Simplemente ejecuta esa función
completa.

Después continúa con la siguiente línea.

Es la opción más utilizada.
"""

###########################################################
# EJEMPLO
###########################################################

def suma(a, b):
    return a + b


x = 5
y = 7

resultado = suma(x, y)

print(resultado)

"""
Si presionamos F10 estando
sobre la línea:

resultado = suma(x,y)

El debugger NO entra
a la función.

Simplemente calcula:

12

Y continúa.

Muy útil cuando sabemos
que la función funciona bien.
"""

###########################################################
# STEP INTO
###########################################################

"""
Atajo habitual

F11

Step Into significa:

Entrar dentro de la función.

Es extremadamente útil cuando
creemos que el bug está
dentro de ella.
"""

###########################################################
# EJEMPLO
###########################################################

def calcular_total(precio, iva):

    subtotal = precio

    impuesto = subtotal * iva

    total = subtotal + impuesto

    return total


resultado = calcular_total(100, 0.19)

print(resultado)

"""
Con F11 podremos observar:

subtotal

↓

impuesto

↓

total

línea por línea.

Exactamente igual
que si camináramos por dentro
de la función.
"""

###########################################################
# STEP OUT
###########################################################

"""
Atajo habitual

Shift + F11

Sirve para salir rápidamente
de una función.

Imagina que entraste por error
a una función enorme.

No necesitas recorrer
las 300 líneas.

Simplemente utiliza:

Step Out

El debugger terminará la función
y volverá al punto donde fue llamada.
"""

###########################################################
# CONTINUE
###########################################################

"""
Atajo habitual

F5

Continue significa:

Continúa ejecutando normalmente
hasta encontrar el siguiente Breakpoint.

No avanza línea por línea.

Simplemente continúa.
"""

###########################################################
# RESTART
###########################################################

"""
Permite reiniciar completamente
la sesión de debugging.

Muy útil cuando modificamos código.

En lugar de cerrar el programa
podemos reiniciarlo inmediatamente.
"""

###########################################################
# STOP
###########################################################

"""
Finaliza completamente
la ejecución.

Es equivalente a cancelar
la sesión de debugging.
"""

###########################################################
# CALL STACK
###########################################################

"""
Uno de los conceptos más importantes.

Call Stack significa:

La pila de llamadas.

Muestra todas las funciones
que llevaron hasta el punto actual.

Ejemplo.

main()

↓

leer_archivo()

↓

procesar_clientes()

↓

calcular_descuento()

↓

validar()

Si el programa está detenido
dentro de validar(),

el Call Stack mostrará exactamente
ese recorrido.

Es una herramienta indispensable
cuando trabajamos con proyectos grandes.
"""

###########################################################
# EJEMPLO
###########################################################

def funcion_c():

    numero = 15

    return numero


def funcion_b():

    return funcion_c()


def funcion_a():

    return funcion_b()


resultado = funcion_a()

"""
Coloca un Breakpoint
dentro de funcion_c().

Observa el Call Stack.

Verás algo similar a:

funcion_c()

↓

funcion_b()

↓

funcion_a()

↓

main
"""

###########################################################
# WATCHES
###########################################################

"""
Las Watches permiten observar
variables específicas.

Ejemplo.

total

clientes

contador

No necesitamos buscarlas
entre cientos de variables.

El debugger siempre las mostrará.

Muy útil en proyectos grandes.
"""

###########################################################
# DEBUG CONSOLE
###########################################################

"""
Mientras el programa está detenido
podemos escribir expresiones.

Ejemplo.

precio

↓

120

precio * descuento

↓

18

len(clientes)

↓

125

Podemos hacer pequeños cálculos
sin modificar el código.

Esta característica es extremadamente
útil para investigar bugs.
"""

###########################################################
# BREAKPOINTS CONDICIONALES
###########################################################

"""
VS Code permite crear Breakpoints
que solo se activan si una condición
es verdadera.

Ejemplo.

contador == 500

El programa recorrerá las primeras
499 iteraciones normalmente.

Solo se detendrá cuando:

contador == 500

Esto ahorra muchísimo tiempo.
"""

###########################################################
# EJEMPLO
###########################################################

for numero in range(1000):

    print(numero)

"""
Coloca un Breakpoint condicional.

Condición:

numero == 750

El programa se detendrá
únicamente en esa iteración.
"""

###########################################################
# ¿CUÁNDO USAR STEP OVER?
###########################################################

"""
Cuando confías en la función.

Solo quieres conocer
el resultado.

Ejemplo.

resultado = sorted(lista)

No necesitas entrar
al código interno de Python.

Usa Step Over.
"""

###########################################################
# ¿CUÁNDO USAR STEP INTO?
###########################################################

"""
Cuando sospechas que el bug
está dentro de la función.

Especialmente si fue desarrollada
por tu equipo.
"""

###########################################################
# ¿CUÁNDO USAR STEP OUT?
###########################################################

"""
Cuando ya comprobaste que
esa función no contiene el problema.

No pierdas tiempo.

Sal inmediatamente.
"""

###########################################################
# TIPS PROFESIONALES
###########################################################

"""
✓ No coloques Breakpoints
en todas las líneas.

✓ Colócalos cerca del posible bug.

✓ Utiliza Step Over
la mayor parte del tiempo.

✓ Entra únicamente cuando
realmente sospeches de una función.

✓ Observa el Call Stack.

✓ Inspecciona variables
antes de modificar código.

✓ Aprende los atajos
(F5, F10, F11).

Te harán mucho más productivo.
"""

###########################################################
# EJERCICIO 1
###########################################################

"""
Sin ejecutar el código.

¿Qué herramienta utilizarías?

A)

Quieres saber qué valor recibe
una función.

B)

Quieres entrar dentro de ella.

Respuesta.

Breakpoint

+

Step Into
"""

###########################################################
# EJERCICIO 2
###########################################################

"""
Tienes un loop de 2 millones
de iteraciones.

Quieres detenerte únicamente
cuando contador sea igual
a 1.500.000.

¿Qué herramienta usarías?

Respuesta.

Conditional Breakpoint.
"""

###########################################################
# EJERCICIO 3 (Difícil)
###########################################################

"""
Supón que una función llama
otras siete funciones.

No sabes dónde aparece
el dato incorrecto.

Diseña una estrategia utilizando:

✓ Breakpoints.

✓ Step Into.

✓ Step Over.

✓ Call Stack.

✓ Watches.

No escribas código.

Describe únicamente el proceso
de investigación.
"""

"""
==========================================================
PYTHON MASTERS
BLOQUE 16 - BUENAS PRÁCTICAS Y DEBUGGING

Archivo:
16.1B_debugging_herramientas.py

PARTE 3 DE 3

Tema:
Casos Reales de Debugging y Buenas Prácticas Profesionales

==========================================================

OBJETIVOS

Al finalizar esta sección podrás:

✓ Depurar programas completos.
✓ Identificar la causa raíz de un bug.
✓ Evitar errores comunes durante el debugging.
✓ Aplicar una metodología profesional.
✓ Resolver problemas similares a los encontrados
  en proyectos reales.

==========================================================
"""

###########################################################
# DEL PROBLEMA A LA SOLUCIÓN
###########################################################

"""
Ya conoces las herramientas.

Ahora aprenderemos algo aún más importante.

¿Cómo piensa un desarrollador profesional
cuando aparece un bug?

La mayoría de los errores NO se solucionan
escribiendo código.

Se solucionan investigando.

Las herramientas solamente aceleran
esa investigación.
"""

###########################################################
# CASO REAL 1
###########################################################

"""
Un usuario informa:

"El sistema calcula descuentos incorrectos."

No dice más.

¿Cómo empezamos?

NO modificamos código.

Primero reproducimos el problema.
"""

###########################################################
# EJEMPLO
###########################################################

def calcular_descuento(precio, porcentaje):
    return precio - (precio * porcentaje)


resultado = calcular_descuento(100, 20)

print(resultado)

"""
El resultado esperado era:

80

Pero obtenemos:

-1900

¿Por qué?

Con un Breakpoint podemos observar:

precio = 100

porcentaje = 20

Aquí descubrimos el problema.

La función esperaba:

0.20

No:

20

El bug NO estaba en la operación.

Estaba en la interpretación
del dato recibido.
"""

###########################################################
# CASO REAL 2
###########################################################

"""
Un usuario informa:

"Faltan clientes en el reporte."

No aparece ninguna excepción.

¿Qué hacemos?

Investigar el flujo.
"""

###########################################################
# EJEMPLO
###########################################################

clientes = [
    "Ana",
    "Carlos",
    "Laura",
    "Pedro"
]

for cliente in clientes[:-1]:
    print(cliente)

"""
Salida:

Ana

Carlos

Laura

Pedro nunca aparece.

Con un Breakpoint observamos:

clientes[:-1]

Y descubrimos inmediatamente
que el slicing elimina
el último elemento.
"""

###########################################################
# CASO REAL 3
###########################################################

"""
El programa funciona
para algunos usuarios.

Para otros no.

Esto suele indicar
que el problema depende
de los datos.

Siempre intenta conseguir
los datos originales
que produjeron el bug.
"""

###########################################################
# EJEMPLO
###########################################################

def promedio(valores):
    return sum(valores) / len(valores)


datos = []

# promedio(datos)

"""
El programa funciona durante meses.

Un día falla.

¿Por qué?

Nadie había probado
una lista vacía.

El debugger permite verificar
qué datos recibió realmente
la función.
"""

###########################################################
# CASO REAL 4
###########################################################

"""
Supongamos un sistema
con varias funciones.
"""

###########################################################
# EJEMPLO
###########################################################

def leer():
    datos = [10, 20, 30]
    return datos


def transformar(datos):
    return [dato * 2 for dato in datos]


def guardar(datos):
    print("Guardando:", datos)


datos = leer()

datos = transformar(datos)

guardar(datos)

"""
¿Dónde colocarías el primer Breakpoint?

Muchos principiantes
lo ponen en guardar().

Un desarrollador experimentado
lo coloca donde sospecha
que aparece el dato incorrecto.

Normalmente cerca
del origen del problema.
"""

###########################################################
# CUANDO EL BUG NO ES TUYO
###########################################################

"""
En proyectos reales
mucho código fue escrito
por otras personas.

No tengas miedo
de utilizar Step Into.

Comprender código ajeno
es parte del trabajo.
"""

###########################################################
# CUANDO EL BUG ES TUYO
###########################################################

"""
Curiosamente es más difícil.

¿Por qué?

Porque damos muchas cosas
por ciertas.

"Estoy seguro de que..."

Esa frase suele ser
el inicio de una larga sesión
de debugging.

Confía en la evidencia.

No en la memoria.
"""

###########################################################
# ERRORES COMUNES DURANTE EL DEBUGGING
###########################################################

"""
ERROR 1

Cambiar varias cosas al tiempo.

----------------------------------

ERROR 2

No reproducir el problema.

----------------------------------

ERROR 3

No leer completamente
el mensaje de error.

----------------------------------

ERROR 4

Suponer valores.

----------------------------------

ERROR 5

No revisar el Call Stack.

----------------------------------

ERROR 6

Ignorar casos extremos.

----------------------------------

ERROR 7

Eliminar código
porque "parece innecesario".
"""

###########################################################
# DEBUGGING EN PROYECTOS GRANDES
###########################################################

"""
En proyectos empresariales
es común encontrar:

100 archivos.

500 funciones.

Miles de líneas.

No intentes entender
todo el proyecto.

Empieza siguiendo
el flujo del dato.

Dato

↓

Transformación

↓

Resultado

El dato siempre deja pistas.
"""

###########################################################
# LA REGLA DE ORO
###########################################################

"""
Cada vez que encuentres
una variable incorrecta
pregúntate:

¿Quién la modificó?

Después repite.

¿Quién modificó esa?

Y continúa.

Tarde o temprano llegarás
al origen del bug.
"""

###########################################################
# ¿CUÁNDO DEJAR DE USAR print()?
###########################################################

"""
Cuando:

✓ El proyecto crece.

✓ Existen muchas funciones.

✓ Hay objetos grandes.

✓ Hay múltiples módulos.

✓ Trabajas con otros desarrolladores.

En ese momento
el Debugger será mucho
más eficiente.
"""

###########################################################
# BUENAS PRÁCTICAS
###########################################################

"""
✓ Usa nombres descriptivos.

✓ Mantén funciones pequeñas.

✓ Divide problemas grandes.

✓ Escribe código legible.

✓ Evita duplicación.

✓ Elimina código muerto.

✓ Escribe pruebas.

✓ Documenta bugs importantes.

✓ Aprende los atajos del debugger.

✓ Nunca depures con prisa.
"""

###########################################################
# TIPS PROFESIONALES
###########################################################

"""
TIP 1

Los mejores desarrolladores
pasan más tiempo leyendo
que escribiendo.

--------------------------------

TIP 2

No intentes demostrar
que tienes razón.

Intenta demostrar
que tus hipótesis son falsas.

Así descubrirás la verdadera causa.

--------------------------------

TIP 3

Los bugs más difíciles
normalmente tienen causas simples.

--------------------------------

TIP 4

Si el problema desaparece
"porque sí"

No cierres el caso.

Encuentra la causa.

--------------------------------

TIP 5

Cada bug que solucionas
debe enseñarte algo.
"""

###########################################################
# LABORATORIO 1
###########################################################

"""
El siguiente programa
contiene varios errores.

Encuéntralos utilizando
únicamente el debugger.
"""

###########################################################
# EJERCICIO
###########################################################

def calcular_total(precios):

    total = 0

    for precio in precios:
        total += precio

    promedio = total / len(precios)

    return promedio


datos = [100, 250, 150]

print(calcular_total(datos))

"""
Preguntas.

1.

¿Qué variables observarías?

2.

¿Dónde colocarías Breakpoints?

3.

¿Usarías Step Into
o Step Over?

Justifica tu respuesta.
"""

###########################################################
# LABORATORIO 2
###########################################################

"""
Analiza cuidadosamente.
"""

###########################################################
# EJERCICIO
###########################################################

def aplicar_descuento(precio, descuento):

    descuento = descuento / 100

    return precio - precio * descuento


print(aplicar_descuento(500, 15))

"""
Objetivo.

Comprueba utilizando
el debugger que:

✓ precio vale 500.

✓ descuento inicialmente vale 15.

✓ descuento cambia a 0.15.

✓ El resultado final es correcto.
"""

###########################################################
# LABORATORIO 3 (Difícil)
###########################################################

"""
Construye el siguiente escenario.

Función A

↓

Función B

↓

Función C

↓

Función D

Coloca un Breakpoint
en la última función.

Analiza:

✓ Variables.

✓ Watches.

✓ Call Stack.

✓ Step Out.

✓ Continue.

Repite el ejercicio
hasta comprender completamente
cómo viaja la ejecución
entre funciones.
"""

###########################################################
# RETO PYTHON MASTERS
###########################################################

"""
Supón que trabajas
como Data Engineer.

Una tubería procesa
5 millones de registros.

El resultado final
tiene únicamente
4.998.321.

No existen excepciones.

No hay errores.

No hay mensajes.

Diseña una estrategia
de debugging.

Incluye:

✓ Hipótesis.

✓ Breakpoints.

✓ Validaciones.

✓ Variables.

✓ Call Stack.

✓ Datos de entrada.

✓ Datos de salida.

✓ Evidencias.

No escribas código.

Escribe el proceso
como si fueras
el ingeniero responsable.
"""

###########################################################
# REFLEXIÓN FINAL
###########################################################

"""
Un desarrollador junior
escribe código.

Un desarrollador semi senior
escribe código
y encuentra bugs.

Un desarrollador senior
evita que los bugs aparezcan.

La diferencia está
en cómo piensan.

No solamente
en cuánto saben programar.
"""

###########################################################
# RESUMEN GENERAL DEL ARCHIVO
###########################################################

"""
Ahora conoces las principales herramientas
de debugging utilizadas en Python.

Has aprendido:

✓ print() estratégico.

✓ Breakpoints.

✓ Variables.

✓ Watches.

✓ Debug Console.

✓ Continue.

✓ Restart.

✓ Stop.

✓ Step Over.

✓ Step Into.

✓ Step Out.

✓ Call Stack.

✓ Conditional Breakpoints.

✓ Metodología profesional.

✓ Casos reales.

✓ Laboratorios prácticos.

✓ Buenas prácticas.

✓ Tips profesionales.

Recuerda siempre:

No busques únicamente
hacer que el programa funcione.

Busca comprender por qué
dejó de funcionar.

Esa diferencia separa
a un programador
de un verdadero ingeniero de software.

==========================================================
FIN DEL ARCHIVO
==========================================================
"""
