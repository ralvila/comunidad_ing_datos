"""
==========================================================
PYTHON MASTERS
BLOQUE 16 - BUENAS PRÁCTICAS Y DEBUGGING

Archivo:
16.3A_buenas_practicas.py

PARTE 1 DE 3

Tema:
Fundamentos de las Buenas Prácticas de Programación

Autor:
Comunidad de Ingeniería de Datos

==========================================================

OBJETIVOS

Al finalizar esta sección podrás:

✓ Comprender qué son las buenas prácticas.

✓ Escribir código más limpio y legible.

✓ Comprender por qué el código es leído
  muchas más veces de las que es escrito.

✓ Identificar malas prácticas comunes.

✓ Escribir código pensando en otros
  desarrolladores.

==========================================================
"""

###########################################################
# ¿QUÉ SON LAS BUENAS PRÁCTICAS?
###########################################################

"""
Las buenas prácticas son un conjunto
de recomendaciones que ayudan a escribir
software:

✓ Más fácil de leer.

✓ Más fácil de mantener.

✓ Más fácil de probar.

✓ Más fácil de ampliar.

✓ Más fácil de corregir.

No son reglas obligatorias.

Son recomendaciones obtenidas
después de décadas de experiencia
desarrollando software.
"""

###########################################################
# ¿POR QUÉ SON IMPORTANTES?
###########################################################

"""
Imagina dos programas.

Programa A

Funciona correctamente.

Programa B

También funciona correctamente.

¿Cuál es mejor?

Todavía no lo sabemos.

Ahora imagina que,
seis meses después,
otro desarrollador debe modificar
ese código.

Si el Programa A es claro
y el Programa B es confuso,

el Programa A será mucho más valioso.

En el desarrollo profesional,
el código no solo debe funcionar.

Debe ser comprensible.
"""

###########################################################
# EL CÓDIGO SE LEE MÁS
# DE LO QUE SE ESCRIBE
###########################################################

"""
Una frase muy conocida dice:

"Code is read far more often
than it is written."

Un desarrollador puede escribir
una función una sola vez.

Pero esa misma función puede ser leída:

• Durante una revisión de código.

• Durante una corrección.

• Durante una optimización.

• Durante una auditoría.

• Durante una migración.

Es decir.

El tiempo invertido
en escribir código claro
se recupera muchas veces.
"""

###########################################################
# CÓDIGO QUE FUNCIONA
# VS CÓDIGO PROFESIONAL
###########################################################

"""
Observa este ejemplo.
"""

###########################################################
# MAL EJEMPLO
###########################################################

a = 150

b = 0.19

c = a + (a * b)

print(c)

"""
¿Funciona?

Sí.

¿Es claro?

No.

¿Qué representa "a"?

¿Qué representa "b"?

¿Qué representa "c"?

Nadie lo sabe.
"""

###########################################################
# BUEN EJEMPLO
###########################################################

precio = 150

iva = 0.19

precio_total = precio + (precio * iva)

print(precio_total)

"""
Produce exactamente
el mismo resultado.

Pero ahora cualquier persona
entiende el código
sin necesidad de explicaciones.

La diferencia está
en la legibilidad.
"""

###########################################################
# LA LEGIBILIDAD
###########################################################

"""
La legibilidad es la facilidad
con la que una persona puede
comprender el código.

El código debe ser entendido
por personas.

No únicamente
por el intérprete de Python.

Cuando escribimos código,
nuestro principal lector
es otro desarrollador.
"""

###########################################################
# EL COSTO DEL MAL CÓDIGO
###########################################################

"""
Un código difícil de leer
genera muchos problemas.

✓ Más bugs.

✓ Más tiempo de mantenimiento.

✓ Más errores.

✓ Más tiempo para capacitar
  nuevos integrantes.

✓ Mayor costo para la empresa.

Por eso las compañías invierten
tanto tiempo en revisiones de código.
"""

###########################################################
# EL CÓDIGO ES COMUNICACIÓN
###########################################################

"""
Programar no consiste únicamente
en darle instrucciones
a una computadora.

También consiste
en comunicar ideas.

Un buen programa cuenta
una historia.

Al leerlo,
deberíamos entender
qué intenta hacer
sin necesidad de preguntarle
al autor.
"""

###########################################################
# LOS NOMBRES IMPORTAN
###########################################################

"""
El primer paso para escribir
código limpio
es utilizar buenos nombres.

Comparemos.
"""

###########################################################
# MAL EJEMPLO
###########################################################

x = 25

y = 1200000

z = x * y

"""
¿Qué significa x?

¿Qué representa y?

¿Qué contiene z?

Es imposible saberlo.
"""

###########################################################
# BUEN EJEMPLO
###########################################################

cantidad_productos = 25

precio_unitario = 1_200_000

valor_total = cantidad_productos * precio_unitario

"""
No necesitamos comentarios.

Los nombres ya explican
el propósito del código.
"""

###########################################################
# LOS NOMBRES DEBEN
# EXPLICAR SU PROPÓSITO
###########################################################

"""
Una variable debe responder
la pregunta:

¿Qué almacena?

Ejemplos.

✔ edad

✔ salario

✔ temperatura

✔ clientes_activos

✔ fecha_procesamiento

Mientras más específico sea el nombre,
más fácil será comprender el código.
"""

###########################################################
# EVITA ABREVIATURAS
###########################################################

"""
Muchos desarrolladores escriben:

cli

usr

tmp

cfg

cnt

¿Todos entenderán
esas abreviaturas?

Probablemente no.

Siempre que sea posible,
prefiere nombres completos.
"""

###########################################################
# MAL EJEMPLO
###########################################################

emp = []

for cli in emp:

    print(cli)

###########################################################
# BUEN EJEMPLO
###########################################################

clientes = []

for cliente in clientes:

    print(cliente)

"""
Este código es mucho más claro.

Incluso alguien que nunca
ha visto el proyecto
podrá comprenderlo.
"""

###########################################################
# EVITA NOMBRES ENGAÑOSOS
###########################################################

"""
Observa esta variable.

lista_clientes

¿Realmente es una lista?

Veamos.
"""

lista_clientes = {
    "Ana": 25,
    "Carlos": 30
}

"""
No.

Es un diccionario.

El nombre induce al error.

Siempre procura que el nombre
describa correctamente
el tipo y el propósito.
"""

###########################################################
# CONSISTENCIA
###########################################################

"""
Una de las mejores prácticas
es mantener consistencia.

Si utilizas:

cliente

No cambies luego a:

usuario

persona

cliente_actual

comprador

para representar exactamente
el mismo concepto.

Elegir un nombre
y mantenerlo
facilita enormemente
la lectura.
"""

###########################################################
# CÓDIGO AUTOEXPLICATIVO
###########################################################

"""
El mejor comentario
es aquel que no hace falta.

Veamos un ejemplo.
"""

###########################################################
# MAL EJEMPLO
###########################################################

# Suma dos números

def suma(a, b):
    return a + b

"""
El comentario
no aporta información.

La función ya lo dice.
"""

###########################################################
# BUEN EJEMPLO
###########################################################

def calcular_total_factura(subtotal, iva):
    return subtotal + (subtotal * iva)

"""
No necesita comentarios.

El nombre explica perfectamente
qué hace.
"""

###########################################################
# EL PRINCIPIO DE MENOR SORPRESA
###########################################################

"""
Cuando alguien lee una función,
espera que se comporte
como su nombre indica.

Ejemplo.

calcular_promedio()

Debe calcular un promedio.

No debería además:

✓ Guardar un archivo.

✓ Enviar un correo.

✓ Modificar una base de datos.

Una función
debe hacer
lo que promete.
"""

###########################################################
# PEQUEÑAS MEJORAS
###########################################################

"""
Muchas veces
el código mejora únicamente
cambiando nombres.

Observa.
"""

###########################################################
# ANTES
###########################################################

n = 18

if n >= 18:

    print("OK")

###########################################################
# DESPUÉS
###########################################################

edad = 18

if edad >= 18:

    print("Mayor de edad")

"""
La lógica es exactamente
la misma.

Pero el código
es mucho más fácil
de comprender.
"""

###########################################################
# BUENAS PRÁCTICAS
###########################################################

"""
✓ Utiliza nombres claros.

✓ Escribe código legible.

✓ Evita abreviaturas.

✓ Mantén consistencia.

✓ Haz que el código
  explique su propósito.

✓ Piensa en el próximo
  desarrollador.

✓ Recuerda que el código
  será leído muchas veces.
"""

###########################################################
# TIPS PROFESIONALES
###########################################################

"""
TIP 1

Si necesitas explicar
qué hace una variable,

probablemente
debería tener
un mejor nombre.

------------------------------------

TIP 2

Los nombres largos
pero claros
son mejores
que nombres cortos
pero ambiguos.

------------------------------------

TIP 3

El código limpio
reduce errores.

No solamente
mejora la apariencia.

------------------------------------

TIP 4

Un buen nombre
puede eliminar
la necesidad
de escribir comentarios.
"""

###########################################################
# EJERCICIO 1
###########################################################

"""
Reescribe las siguientes variables.

a

b

c

x

tmp

Utiliza nombres
que expliquen claramente
su propósito.
"""

###########################################################
# EJERCICIO 2
###########################################################

"""
Observa.

def calc(x, y):

    return x * y

¿Cómo mejorarías?

✓ Nombre de la función.

✓ Parámetros.

✓ Variable de retorno.
"""

###########################################################
# EJERCICIO 3 (Difícil)
###########################################################

"""
Un compañero entrega
el siguiente código.

------------------------------------------------

a = 100

b = 0.19

c = a + (a * b)

if c > 100:

    d = True

else:

    d = False

------------------------------------------------

Sin cambiar
la lógica del programa,

reescríbelo aplicando
buenas prácticas.

Piensa especialmente en:

✓ Nombres.

✓ Legibilidad.

✓ Claridad.
"""

"""
==========================================================
PYTHON MASTERS
BLOQUE 16 - BUENAS PRÁCTICAS Y DEBUGGING

Archivo:
16.3A_buenas_practicas.py

PARTE 2 DE 3

Tema:
Principios Fundamentales del Código Limpio

Autor:
Comunidad de Ingeniería de Datos

==========================================================

OBJETIVOS

Al finalizar esta sección podrás:

✓ Aplicar los principios DRY, KISS y YAGNI.

✓ Escribir funciones pequeñas y reutilizables.

✓ Evitar duplicación de código.

✓ Eliminar números mágicos.

✓ Comprender el principio de responsabilidad
  única.

✓ Escribir código más fácil de mantener.

==========================================================
"""

###########################################################
# EL CÓDIGO LIMPIO
###########################################################

"""
Existe una frase muy conocida
en Ingeniería de Software.

"Cualquier persona puede escribir
código que una computadora entienda.

Los buenos desarrolladores escriben
código que las personas puedan entender."

El objetivo de esta sección es aprender
las reglas más utilizadas por los equipos
de desarrollo profesionales.

Muchas de ellas aparecen en revisiones
de código (Code Reviews).

También son evaluadas durante
entrevistas técnicas.
"""

###########################################################
# DRY
###########################################################

"""
DRY significa:

Don't Repeat Yourself

(No te repitas.)

Uno de los errores más comunes
es copiar y pegar código.

¿Por qué es un problema?

Porque cuando debamos corregir
un error tendremos que hacerlo
en muchos lugares.

Mientras más código duplicado exista,

más costoso será el mantenimiento.
"""

###########################################################
# MAL EJEMPLO
###########################################################

precio1 = 100
total1 = precio1 + (precio1 * 0.19)

precio2 = 250
total2 = precio2 + (precio2 * 0.19)

precio3 = 400
total3 = precio3 + (precio3 * 0.19)

"""
El mismo cálculo aparece
tres veces.

¿Qué ocurre si cambia el IVA?

Tendremos que modificar
las tres líneas.
"""

###########################################################
# BUEN EJEMPLO
###########################################################

def calcular_total(precio, iva):
    return precio + (precio * iva)


print(calcular_total(100, 0.19))
print(calcular_total(250, 0.19))
print(calcular_total(400, 0.19))

"""
Ahora existe un único lugar
donde se encuentra la lógica.

Esto reduce errores
y facilita el mantenimiento.
"""

###########################################################
# KISS
###########################################################

"""
KISS significa:

Keep It Simple, Stupid.

(Mantenlo simple.)

Muchas veces creemos
que un código complejo
es mejor.

Ocurre exactamente lo contrario.

Mientras más simple sea una solución,

más fácil será:

✓ Comprenderla.

✓ Probarla.

✓ Corregirla.

✓ Mantenerla.
"""

###########################################################
# MAL EJEMPLO
###########################################################

numero = 10

resultado = ((numero * 1) + 0)

print(resultado)

"""
Todo ese cálculo
podría escribirse simplemente como:

resultado = numero
"""

###########################################################
# BUEN EJEMPLO
###########################################################

numero = 10

resultado = numero

print(resultado)

"""
Hace exactamente lo mismo.

Con menos código.

Y es mucho más fácil de entender.
"""

###########################################################
# YAGNI
###########################################################

"""
YAGNI significa:

You Aren't Gonna Need It

(No lo vas a necesitar.)

Este principio nos recuerda
que no debemos desarrollar
funcionalidades "por si acaso".

Muchos proyectos terminan
llenos de código
que nunca fue utilizado.

Eso aumenta:

✓ Complejidad.

✓ Tiempo de desarrollo.

✓ Riesgo de errores.

Desarrolla únicamente
lo que realmente necesitas.
"""

###########################################################
# EJEMPLO
###########################################################

"""
Supongamos que hoy
solo necesitamos calcular
el IVA.

No implementes desde ahora:

✓ Descuentos.

✓ Promociones.

✓ Cupones.

✓ Monedas internacionales.

✓ Impuestos especiales.

Cuando realmente se necesiten,
se desarrollarán.
"""

###########################################################
# RESPONSABILIDAD ÚNICA
###########################################################

"""
Uno de los principios más importantes
del desarrollo profesional.

Una función debe tener
una única responsabilidad.

Es decir.

Debe hacer una sola cosa.

Y hacerla bien.
"""

###########################################################
# MAL EJEMPLO
###########################################################

def procesar_clientes():

    print("Leyendo archivo")

    print("Validando datos")

    print("Calculando impuestos")

    print("Guardando información")

    print("Enviando correo")

"""
Esta función realiza
cinco tareas diferentes.

Si aparece un error,

¿Dónde investigamos?

Será difícil descubrirlo.
"""

###########################################################
# BUEN EJEMPLO
###########################################################

def leer_clientes():
    pass


def validar_clientes():
    pass


def calcular_impuestos():
    pass


def guardar_clientes():
    pass


def enviar_notificacion():
    pass

"""
Ahora cada función
tiene una única responsabilidad.

El mantenimiento será mucho
más sencillo.
"""

###########################################################
# FUNCIONES PEQUEÑAS
###########################################################

"""
No existe un número mágico
de líneas.

Pero una función debería ser
lo suficientemente pequeña
como para comprenderla
rápidamente.

Si una función ocupa
300 líneas,

probablemente esté haciendo
demasiadas cosas.
"""

###########################################################
# VENTAJAS DE LAS
# FUNCIONES PEQUEÑAS
###########################################################

"""
✓ Más fáciles de probar.

✓ Más fáciles de reutilizar.

✓ Más fáciles de leer.

✓ Más fáciles de depurar.

✓ Más fáciles de modificar.

Mientras más pequeña sea
una función,

más sencillo será encontrar
un bug.
"""

###########################################################
# EVITA NÚMEROS MÁGICOS
###########################################################

"""
Observa este ejemplo.
"""

###########################################################
# MAL EJEMPLO
###########################################################

salario = 3_500_000

salario_final = salario * 1.19

"""
¿De dónde salió 1.19?

Nadie lo sabe.

Eso se conoce como:

Número mágico.
"""

###########################################################
# BUEN EJEMPLO
###########################################################

IVA = 0.19

salario = 3_500_000

salario_final = salario * (1 + IVA)

"""
Ahora el código explica
el significado del valor.

Además,

si cambia el IVA,

solo debemos modificar
una línea.
"""

###########################################################
# CONSTANTES
###########################################################

"""
Las constantes ayudan
a eliminar números mágicos.

Por convención,
en Python se escriben
en MAYÚSCULAS.

Ejemplos.

IVA

PI

MAX_INTENTOS

TIEMPO_ESPERA

RUTA_DATOS

Aunque Python no impide
modificarlas,

se considera una convención
no hacerlo.
"""

###########################################################
# REUTILIZACIÓN
###########################################################

"""
Si escribes el mismo código
varias veces,

probablemente debas crear
una función.

Las funciones permiten reutilizar
la lógica.

Eso reduce:

✓ Errores.

✓ Tiempo.

✓ Duplicación.
"""

###########################################################
# EJEMPLO
###########################################################

def convertir_a_mayusculas(texto):
    return texto.upper()


print(convertir_a_mayusculas("python"))

print(convertir_a_mayusculas("masters"))

print(convertir_a_mayusculas("datos"))

"""
Una sola función.

Tres usos diferentes.
"""

###########################################################
# REFACTORIZACIÓN
###########################################################

"""
Refactorizar significa:

Mejorar el código

sin modificar
su comportamiento.

Ejemplos.

✓ Mejorar nombres.

✓ Dividir funciones.

✓ Eliminar duplicación.

✓ Mejorar estructura.

✓ Hacer el código
más legible.

El resultado debe seguir
siendo exactamente
el mismo.
"""

###########################################################
# EJEMPLO
###########################################################

"""
Antes.
"""

a = 100
b = 0.19
c = a + (a * b)

"""
Después.
"""

precio = 100
iva = 0.19
precio_total = precio + (precio * iva)

"""
El comportamiento no cambió.

La legibilidad sí.
"""

###########################################################
# CÓDIGO ACOPLADO
###########################################################

"""
Cuando varias funciones
dependen demasiado
unas de otras,

decimos que existe
alto acoplamiento.

Esto dificulta:

✓ Pruebas.

✓ Cambios.

✓ Reutilización.

Siempre intenta escribir
funciones independientes.
"""

###########################################################
# BUENAS PRÁCTICAS
###########################################################

"""
✓ Evita duplicar código.

✓ Escribe funciones pequeñas.

✓ Mantén una única responsabilidad.

✓ Elimina números mágicos.

✓ Utiliza constantes.

✓ Refactoriza continuamente.

✓ Mantén las soluciones simples.

✓ Desarrolla únicamente
lo necesario.
"""

###########################################################
# TIPS PROFESIONALES
###########################################################

"""
TIP 1

La mejor línea de código
es la que nunca fue necesaria.

------------------------------------

TIP 2

Duplicar código
duplica el mantenimiento.

------------------------------------

TIP 3

Cada función debe responder
una sola pregunta.

¿Qué hace?

Si la respuesta contiene
la palabra "y",

probablemente hace
demasiadas cosas.

------------------------------------

TIP 4

Refactorizar no significa
agregar funcionalidades.

Significa mejorar
la calidad del código.
"""

###########################################################
# EJERCICIO 1
###########################################################

"""
Reescribe el siguiente código
aplicando DRY.

precio1 = 120
precio2 = 450
precio3 = 700

Cada uno calcula el IVA
por separado.
"""

###########################################################
# EJERCICIO 2
###########################################################

"""
Analiza esta función.

def procesar():

    leer()

    validar()

    transformar()

    guardar()

    enviar_correo()

¿Cumple el principio
de responsabilidad única?

Justifica tu respuesta.
"""

###########################################################
# EJERCICIO 3
###########################################################

"""
Identifica los números mágicos.

tiempo = 30

descuento = precio * 0.15

if intentos == 5:

    ...

¿Cómo mejorarías
este código?
"""

###########################################################
# EJERCICIO 4 (Difícil)
###########################################################

"""
Supón que encuentras
una función de 450 líneas.

Describe paso a paso
cómo comenzarías
a refactorizarla.

No escribas código.

Piensa como un desarrollador
profesional.
"""

"""
==========================================================
PYTHON MASTERS
BLOQUE 16 - BUENAS PRÁCTICAS Y DEBUGGING

Archivo:
16.3A_buenas_practicas.py

PARTE 3 DE 3

Tema:
Código Profesional, PEP 8 y Code Smells

Autor:
Comunidad de Ingeniería de Datos

==========================================================

OBJETIVOS

Al finalizar esta sección podrás:

✓ Comprender la importancia de PEP 8.

✓ Conocer The Zen of Python.

✓ Identificar Code Smells.

✓ Escribir comentarios correctamente.

✓ Realizar revisiones básicas de código.

✓ Evaluar la calidad de un programa
antes de enviarlo a producción.

==========================================================
"""

###########################################################
# PEP 8
###########################################################

"""
PEP significa:

Python Enhancement Proposal.

Existen muchos documentos PEP.

Uno de los más importantes es:

PEP 8

Es la guía oficial
de estilo para Python.

No define cómo resolver
problemas.

Define cómo escribir
el código.

Seguir PEP 8 hace que todos
los programas Python
tengan un estilo similar.

Eso facilita enormemente
la lectura.
"""

###########################################################
# ¿POR QUÉ EXISTE PEP 8?
###########################################################

"""
Imagina una empresa
con 100 desarrolladores.

Cada uno escribe
como quiere.

Unos usan MAYÚSCULAS.

Otros camelCase.

Otros snake_case.

Otros TAB.

Otros espacios.

El resultado sería
muy difícil de mantener.

PEP 8 unifica
la forma de escribir
el código.
"""

###########################################################
# VARIABLES
###########################################################

"""
PEP 8 recomienda utilizar:

snake_case

para:

✓ Variables

✓ Funciones

Ejemplo.
"""

###########################################################
# CORRECTO
###########################################################

nombre_cliente = "Laura"

fecha_procesamiento = "2026-04-01"

cantidad_registros = 250

###########################################################
# INCORRECTO
###########################################################

NombreCliente = "Laura"

nombreCliente = "Laura"

NOMBRECLIENTE = "Laura"

"""
Cada uno funciona.

Pero solamente el primero
sigue PEP 8.
"""

###########################################################
# CLASES
###########################################################

"""
Las clases utilizan:

PascalCase

Ejemplo.
"""

class ClientePremium:
    pass


class ProcesadorVentas:
    pass

"""
Las clases NO utilizan
snake_case.
"""

###########################################################
# CONSTANTES
###########################################################

"""
Las constantes se escriben
en MAYÚSCULAS.

Ejemplos.
"""

IVA = 0.19

MAXIMO_INTENTOS = 5

RUTA_DATOS = "/datos"

###########################################################
# ESPACIOS
###########################################################

"""
PEP 8 recomienda utilizar
espacios para mejorar
la lectura.

Veamos.
"""

###########################################################
# MAL EJEMPLO
###########################################################

x=5+3

###########################################################
# BUEN EJEMPLO
###########################################################

x = 5 + 3

"""
El resultado es idéntico.

Pero la segunda versión
es mucho más legible.
"""

###########################################################
# LÍNEAS MUY LARGAS
###########################################################

"""
PEP 8 recomienda
que las líneas
no sean excesivamente largas.

Cuando una instrucción
crece demasiado,

es mejor dividirla
en varias líneas.

Esto mejora
la legibilidad.
"""

###########################################################
# IMPORTACIONES
###########################################################

"""
Las importaciones deben ubicarse
al inicio del archivo.

Ejemplo.

import os

import logging

import pandas as pd

No es recomendable
importar módulos
a mitad del código,
salvo casos muy específicos.
"""

###########################################################
# COMENTARIOS
###########################################################

"""
Los comentarios deben explicar:

¿Por qué?

No solamente:

¿Qué?

Muchos comentarios
repiten exactamente
lo que ya dice el código.
"""

###########################################################
# MAL EJEMPLO
###########################################################

# Incrementa en uno

contador += 1

"""
El comentario
no aporta nada.
"""

###########################################################
# BUEN EJEMPLO
###########################################################

# Se incrementa el contador porque
# cada archivo procesado debe registrarse.

contador += 1

"""
Ahora entendemos
el motivo.
"""

###########################################################
# DOCUMENTACIÓN
###########################################################

"""
Las funciones importantes
deberían documentarse.

Python utiliza:

Docstrings.

Ellos permiten explicar.

✓ Qué hace.

✓ Parámetros.

✓ Retorno.

✓ Excepciones.

Más adelante veremos
cómo documentar proyectos
profesionales.
"""

###########################################################
# THE ZEN OF PYTHON
###########################################################

"""
Existe un conjunto
de principios filosóficos
conocidos como:

The Zen of Python.

Puedes verlo ejecutando.

import this

Aparecerán
19 principios.

No son reglas.

Son recomendaciones
para escribir
mejor software.
"""

###########################################################
# PRINCIPIOS IMPORTANTES
###########################################################

"""
Entre los más conocidos
se encuentran.

Beautiful is better than ugly.

Simple is better than complex.

Complex is better than complicated.

Readability counts.

Errors should never pass silently.

There should be one—
and preferably only one—
obvious way to do it.

Estos principios
influyen enormemente
en la comunidad Python.
"""

###########################################################
# CODE SMELLS
###########################################################

"""
Un Code Smell
es una señal
de que el código
podría mejorarse.

No significa
que exista un bug.

Significa que
podría aparecer
en el futuro.
"""

###########################################################
# EJEMPLOS DE CODE SMELLS
###########################################################

"""
✓ Funciones enormes.

✓ Variables ambiguas.

✓ Código duplicado.

✓ Comentarios innecesarios.

✓ Demasiados parámetros.

✓ Números mágicos.

✓ Condicionales excesivos.

✓ Clases gigantes.

✓ Código muerto.

✓ Archivos enormes.
"""

###########################################################
# EJEMPLO
###########################################################

def procesar():

    ...

"""
Imagina que esta función
tiene 700 líneas.

Probablemente
estemos frente
a un Code Smell.

No necesariamente
es un error.

Pero merece
una revisión.
"""

###########################################################
# CÓDIGO MUERTO
###########################################################

"""
Código muerto
es código
que nunca se ejecuta.

Ejemplo.

Funciones olvidadas.

Variables nunca utilizadas.

Condiciones imposibles.

Mientras más código muerto exista,

más difícil será
mantener el proyecto.
"""

###########################################################
# REVISIONES DE CÓDIGO
###########################################################

"""
Las empresas realizan
Code Reviews.

Antes de integrar cambios,
otro desarrollador revisa:

✓ Legibilidad.

✓ Nombres.

✓ Arquitectura.

✓ Seguridad.

✓ Buenas prácticas.

✓ Rendimiento.

No buscan criticar personas.

Buscan mejorar
el software.
"""

###########################################################
# CÓMO RECIBIR
# UN CODE REVIEW
###########################################################

"""
Un comentario
sobre el código

NO es un comentario
sobre el desarrollador.

Aceptar retroalimentación
es parte del crecimiento
profesional.

Todos recibimos
Code Reviews.

Incluso los desarrolladores
más experimentados.
"""

###########################################################
# CHECKLIST ANTES
# DE ENTREGAR CÓDIGO
###########################################################

"""
Antes de enviar
un Pull Request
pregúntate.

✓ ¿Los nombres son claros?

✓ ¿Existe código duplicado?

✓ ¿Hay números mágicos?

✓ ¿Las funciones hacen
una sola cosa?

✓ ¿El código sigue PEP 8?

✓ ¿El programa fue probado?

✓ ¿Existen comentarios
innecesarios?

✓ ¿Podría simplificarse?

✓ ¿El siguiente desarrollador
lo entenderá?
"""

###########################################################
# BUENAS PRÁCTICAS
###########################################################

"""
✓ Sigue PEP 8.

✓ Utiliza nombres claros.

✓ Documenta correctamente.

✓ Refactoriza continuamente.

✓ Elimina código muerto.

✓ Acepta Code Reviews.

✓ Lee código
de otros desarrolladores.

✓ Aprende constantemente.
"""

###########################################################
# TIPS PROFESIONALES
###########################################################

"""
TIP 1

Escribe código
como si quien lo mantendrá
fuera alguien
que no conoce el proyecto.

------------------------------------

TIP 2

Si una función necesita
muchos comentarios,

probablemente
deba dividirse.

------------------------------------

TIP 3

El código limpio
no se escribe
a la primera.

Se construye
mediante refactorización.

------------------------------------

TIP 4

Cada revisión de código
es una oportunidad
de aprendizaje.

No una crítica personal.

------------------------------------

TIP 5

La mejor forma
de mejorar
es leer código
de desarrolladores
más experimentados.
"""

###########################################################
# EJERCICIO 1
###########################################################

"""
Analiza el siguiente código.

valor=100

if(valor>50):

 print("Mayor")

¿Qué recomendaciones
de PEP 8 aplicarías?
"""

###########################################################
# EJERCICIO 2
###########################################################

"""
Identifica
los posibles Code Smells.

✓ Función de 600 líneas.

✓ Variable llamada x.

✓ Código duplicado.

✓ Tres niveles
de condicionales anidados.

Explica por qué
cada uno representa
una señal de alerta.
"""

###########################################################
# EJERCICIO 3
###########################################################

"""
Lee el siguiente comentario.

# Suma dos números

def sumar(a, b):

    return a + b

¿El comentario aporta valor?

¿Cómo lo mejorarías?
"""

###########################################################
# EJERCICIO 4 (Difícil)
###########################################################

"""
Supón que debes revisar
el Pull Request
de un compañero.

Diseña un checklist
con al menos
15 criterios de calidad.

Incluye aspectos como.

✓ Legibilidad.

✓ Seguridad.

✓ Rendimiento.

✓ Modularidad.

✓ Documentación.

✓ Logging.

✓ Manejo de errores.

✓ Buenas prácticas.

Piensa como
un Tech Lead.
"""

###########################################################
# REFLEXIÓN FINAL
###########################################################

"""
La diferencia entre
un desarrollador junior
y uno senior
no suele estar
en la cantidad
de sintaxis que conoce.

Está en la calidad
del código
que produce.

Los desarrolladores
más experimentados:

✓ Escriben menos código.

✓ Reutilizan más.

✓ Simplifican.

✓ Refactorizan.

✓ Documentan.

✓ Automatizan.

✓ Previenen errores.

La excelencia
no aparece
por accidente.

Se construye
aplicando pequeñas
buenas prácticas
todos los días.
"""

###########################################################
# RESUMEN GENERAL DEL TEMA
###########################################################

"""
En este tema aprendiste:

✓ Qué son
las buenas prácticas.

✓ La importancia
de la legibilidad.

✓ Cómo elegir
buenos nombres.

✓ Código autoexplicativo.

✓ DRY.

✓ KISS.

✓ YAGNI.

✓ Responsabilidad única.

✓ Funciones pequeñas.

✓ Refactorización.

✓ Constantes.

✓ Números mágicos.

✓ PEP 8.

✓ The Zen of Python.

✓ Code Smells.

✓ Comentarios efectivos.

✓ Code Reviews.

✓ Checklist de calidad.

✓ Buenas prácticas
profesionales.

==========================================================

MENSAJE FINAL

Recuerda siempre:

El código que escribes hoy
será leído por alguien mañana.

Ese alguien puede ser:

• Un compañero.

• Un cliente.

• Tu futuro equipo.

• O incluso tú mismo
dentro de seis meses.

Escribe código
que haga ese trabajo
lo más sencillo posible.

Porque escribir código
es solo una parte del trabajo.

Mantenerlo durante años
es el verdadero desafío.

==========================================================
FIN DEL ARCHIVO
==========================================================
"""