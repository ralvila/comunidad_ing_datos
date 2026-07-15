"""
==========================================================
PYTHON MASTERS
BLOQUE 16 - BUENAS PRÁCTICAS Y DEBUGGING

Archivo:
16.1A_debugging_fundamentos.py

Tema:
Fundamentos del Debugging

Autor:
Comunidad de Ingeniería de Datos

==========================================================

OBJETIVOS

Al finalizar este archivo el estudiante podrá:

✓ Entender qué significa depurar (Debugging).
✓ Diferenciar bug, error, excepción y fallo.
✓ Comprender el ciclo de depuración.
✓ Aprender una metodología profesional para encontrar errores.
✓ Evitar uno de los errores más comunes de los programadores:
  modificar código sin entender el problema.

Este archivo es completamente teórico-práctico.
Lee TODOS los comentarios antes de ejecutar el código.

==========================================================
"""

###########################################################
# ¿QUÉ ES UN BUG?
###########################################################

"""
Un BUG es un comportamiento incorrecto del software.

No necesariamente significa que el programa se caiga.

Ejemplos:

• Un cálculo incorrecto.
• Un dato duplicado.
• Un archivo que nunca se guarda.
• Un botón que no funciona.
• Una consulta SQL demasiado lenta.
• Un DataFrame con registros repetidos.

En otras palabras:

Bug = cualquier comportamiento que no cumple
con lo esperado.
"""

###########################################################
# ¿POR QUÉ SE LLAMA BUG?
###########################################################

"""
La historia más famosa ocurrió en 1947.

Mientras trabajaban con el computador Harvard Mark II,
los ingenieros encontraron una polilla (bug)
atrapada entre los relés.

El computador dejó de funcionar correctamente.

Pegaron la polilla en el cuaderno de incidentes y
escribieron:

"First actual case of bug being found."

Aunque la palabra "bug" ya existía antes,
este evento la hizo extremadamente popular
en informática.
"""

###########################################################
# ¿QUÉ ES DEBUGGING?
###########################################################

"""
Debugging significa:

Encontrar la causa del problema,
entenderla
y corregirla.

No significa solamente arreglar el código.

La parte más importante es descubrir
POR QUÉ ocurrió el problema.
"""

###########################################################
# BUG VS ERROR VS EXCEPCIÓN VS FALLO
###########################################################

"""
Estos términos normalmente se confunden.

BUG
----
Defecto en el programa.

ERROR
------
Equivocación cometida por el programador.

EXCEPCIÓN
---------
Evento detectado por Python durante la ejecución.

FALLO (Failure)
---------------
Comportamiento visible para el usuario.

Ejemplo:

El desarrollador escribe:

10 / numero

sin validar numero.

Eso es un ERROR.

Cuando numero vale cero:

Python lanza una excepción:

ZeroDivisionError

El usuario observa que la aplicación se cerró.

Eso es un FALLO.

El BUG fue haber olvidado validar el dato.
"""

###########################################################
# EJEMPLO 1
###########################################################

numero = 0

# Este código producirá una excepción.
# Todavía NO vamos a manejar excepciones.
# Queremos observar el comportamiento.

# resultado = 10 / numero

"""
Pregunta:

¿Cuál fue realmente el bug?

Muchos responderían:

"Dividir entre cero."

Incorrecto.

El bug fue:

"No validar el valor antes de dividir."

Ese cambio de mentalidad es muy importante.
"""

###########################################################
# EL COSTO DE LOS BUGS
###########################################################

"""
Mientras más tarde descubras un bug,
más costoso será.

Ejemplo:

Durante desarrollo
Costo: Bajo

Durante pruebas
Costo: Medio

En producción
Costo: Alto

En un banco
Costo: Millones

En un hospital
Costo: Riesgo humano

En un avión
Costo: Catastrófico

Por eso existen tantas pruebas
antes de liberar software.
"""

###########################################################
# TIPOS DE BUGS
###########################################################

"""
Existen muchísimos tipos.

Algunos ejemplos:

• Bugs de lógica

• Bugs matemáticos

• Bugs de sintaxis

• Bugs de concurrencia

• Bugs de rendimiento

• Bugs de memoria

• Bugs de seguridad

• Bugs de integración

• Bugs por configuración

• Bugs por datos inesperados

Como Data Engineers,
los bugs por datos son extremadamente comunes.
"""

###########################################################
# EJEMPLO
###########################################################

ventas = [100, 250, 80, 120]

promedio = sum(ventas) / len(ventas)

print(promedio)

"""
Todo parece correcto.

Pero...

¿Qué pasa si ventas viene vacío?

ventas = []

El algoritmo tiene un bug.

No porque Python esté mal.

Sino porque nunca pensamos
en ese escenario.
"""

###########################################################
# EL PEOR ENEMIGO DEL DEBUGGING
###########################################################

"""
Modificar código al azar.

Muchos principiantes hacen esto:

"No funciona."

Cambian diez líneas.

"No funcionó."

Cambian veinte más.

Ahora el problema es peor.

Nunca hagas eso.

Primero entiende.

Después modifica.
"""

###########################################################
# LA METODOLOGÍA PROFESIONAL
###########################################################

"""
Los desarrolladores experimentados siguen
casi siempre el mismo proceso.

Paso 1

Reproducir el problema.

Si no puedes reproducirlo,
difícilmente podrás solucionarlo.

----------------------------------

Paso 2

Encontrar dónde ocurre.

No dónde crees.

Dónde realmente ocurre.

----------------------------------

Paso 3

Entender por qué ocurre.

No adivines.

Investiga.

----------------------------------

Paso 4

Corregir.

Haz el cambio mínimo necesario.

----------------------------------

Paso 5

Verificar.

Asegúrate de que:

• solucionaste el problema

• no rompiste otra cosa

Esto último se conoce como:

Regression Testing.
"""

###########################################################
# EJEMPLO DE MAL DEBUGGING
###########################################################

edad = "25"

# El desarrollador sospecha del print.

# print(edad)

# Luego sospecha de otra variable.

# Luego cambia media función.

"""
Pero el problema real puede estar
muchísimo antes.

Nunca asumas.

Verifica.
"""

###########################################################
# LOS TRES TIPOS DE PROGRAMADORES
###########################################################

"""
Nivel Junior

"Aquí debe estar el error."

Nivel Semi Senior

"Voy a revisar el flujo."

Nivel Senior

"Voy a demostrar con evidencia
dónde está exactamente."

La diferencia está en usar evidencia,
no intuición.
"""

###########################################################
# EL DEBUGGING ES INVESTIGACIÓN
###########################################################

"""
Imagina un detective.

No llega arrestando personas.

Primero reúne evidencia.

Hace preguntas.

Analiza.

Confirma hipótesis.

Después actúa.

Debugging es exactamente igual.
"""

###########################################################
# PRIMERA REGLA
###########################################################

"""
Nunca supongas.

Siempre verifica.

Si una variable "debería" valer 10...

Compruébalo.

Si un archivo "debería" existir...

Compruébalo.

Si un DataFrame "debería" tener datos...

Compruébalo.

Las suposiciones generan bugs.
"""

###########################################################
# EJERCICIO 1
###########################################################

"""
Sin ejecutar el código:

¿Qué bug existe aquí?

----------------------------------

precio = 50000
descuento = 0

valor = precio / descuento

----------------------------------

Pregunta:

¿Cuál es el bug?

A)

Dividir entre cero.

B)

Python está fallando.

C)

No validar el descuento.

Respuesta:

C.
"""

###########################################################
# EJERCICIO 2
###########################################################

"""
¿Qué harías primero?

A)

Modificar varias líneas.

B)

Agregar prints.

C)

Reproducir el problema.

D)

Reescribir toda la función.

Respuesta correcta:

C
"""

###########################################################
# EJERCICIO 3 (Difícil)
###########################################################

"""
Supón que un usuario dice:

"El sistema falla a veces."

¿Qué información necesitas antes
de modificar el código?

Escribe al menos cinco preguntas.

Ejemplo:

• ¿Qué estaba haciendo?
• ¿Qué datos ingresó?
• ¿Cuál fue el mensaje?
• ¿Siempre ocurre?
• ¿Desde cuándo?
"""

###########################################################
# EJEMPLO 2
###########################################################

def calcular_promedio(numeros):
    return sum(numeros) / len(numeros)


datos = [10, 20, 30, 40]

print(calcular_promedio(datos))

"""
Todo funciona.

Pero...

¿Qué ocurre si recibimos:

[]

La función fallará.

El verdadero problema no es Python.

El problema es asumir que la lista
siempre tendrá elementos.

Las suposiciones son una enorme fuente
de bugs.
"""

###########################################################
# BUGS INTERMITENTES
###########################################################

"""
Existen bugs que aparecen siempre.

Y otros que aparecen "a veces".

Estos últimos son los más difíciles.

Ejemplos:

✓ Solo cuando hay muchos usuarios.

✓ Solo en producción.

✓ Solo algunos días.

✓ Solo con ciertos archivos.

✓ Solo con ciertos datos.

✓ Solo cuando la conexión es lenta.

Los bugs intermitentes requieren
paciencia y mucha evidencia.
"""

###########################################################
# SÍNTOMAS VS CAUSA RAÍZ
###########################################################

"""
Uno de los errores más comunes es corregir
el síntoma.

No la causa.

Ejemplo:

El programa genera:

IndexError

Muchos creen que el bug está en la línea
que produjo el error.

No necesariamente.

Tal vez una lista fue construida
incorrectamente veinte funciones antes.

La excepción únicamente revela
dónde explotó el problema.

No siempre dónde nació.
"""

###########################################################
# EJEMPLO
###########################################################

usuarios = ["Ana", "Carlos"]

indice = 5

# print(usuarios[indice])

"""
La excepción ocurre aquí.

Pero el bug puede ser que:

• El índice fue calculado mal.

• Se eliminaron elementos.

• Nunca llegaron todos los registros.

La línea donde aparece el error
no siempre contiene el bug.
"""

###########################################################
# EL MÉTODO DE LAS HIPÓTESIS
###########################################################

"""
Los desarrolladores profesionales
no trabajan adivinando.

Trabajan formulando hipótesis.

Ejemplo.

Hipótesis 1

La variable llega vacía.

↓

Verificar.

Si es falso...

Hipótesis 2

La consulta SQL devuelve pocos registros.

↓

Verificar.

Si también es falso...

Hipótesis 3

El archivo viene incompleto.

↓

Verificar.

Cada hipótesis debe demostrarse.

Nunca asumirse.
"""

###########################################################
# LOS PRINTS NO SON DEBUGGING
###########################################################

"""
Muchos principiantes creen que hacer esto
es depurar:

print(variable)

print(variable2)

print(variable3)

Aunque puede ayudar,
eso NO es debugging profesional.

Más adelante aprenderemos:

✓ Breakpoints

✓ Debugger

✓ Stack Trace

✓ Inspección de variables

✓ Step Into

✓ Step Over

✓ Watches

Estas herramientas permiten observar
el programa sin modificar el código.
"""

###########################################################
# ¿POR QUÉ ES DIFÍCIL ENCONTRAR BUGS?
###########################################################

"""
Porque el cerebro humano hace suposiciones.

Ejemplo.

El desarrollador piensa:

"Estoy seguro de que esa variable vale 5."

Pero nunca la verificó.

Después de dos horas descubre
que realmente vale None.

La mayor parte del tiempo perdido
en debugging ocurre porque creemos
saber algo que nunca comprobamos.
"""

###########################################################
# EL COSTO DE UN MAL DEBUGGING
###########################################################

"""
Imagina esta situación.

Hay un bug.

El desarrollador modifica diez archivos.

El bug desaparece.

Excelente.

¿Verdad?

No necesariamente.

Tal vez rompió otros procesos.

Tal vez creó nuevos bugs.

Tal vez aumentó la complejidad.

Un buen desarrollador intenta realizar
el cambio más pequeño posible.
"""

###########################################################
# CAMBIOS PEQUEÑOS
###########################################################

"""
Regla profesional.

Nunca hagas veinte cambios al mismo tiempo.

Haz uno.

Prueba.

Si funciona...

Haz el siguiente.

Así podrás identificar exactamente
qué modificación resolvió el problema.
"""

###########################################################
# DOCUMENTAR LOS HALLAZGOS
###########################################################

"""
Cuando un bug es complejo,
es recomendable escribir:

✓ Qué ocurrió.

✓ Cómo reproducirlo.

✓ Qué hipótesis se probaron.

✓ Cuál era la causa.

✓ Cómo se solucionó.

Esto evita que otro desarrollador
pierda varias horas investigando
el mismo problema.

Los equipos profesionales suelen registrar
esta información en herramientas como:

• Jira

• Azure DevOps

• GitHub Issues

• Confluence

• Wikis internas
"""

###########################################################
# BUENAS PRÁCTICAS
###########################################################

"""
✓ Nunca asumas.

✓ Verifica cada hipótesis.

✓ Reproduce el problema.

✓ Cambia una sola cosa a la vez.

✓ No elimines código sin entenderlo.

✓ Conserva evidencia.

✓ Comprende el flujo completo.

✓ Piensa en la causa raíz.

✓ No culpes inmediatamente a Python.

✓ Aprende a leer mensajes de error.
"""

###########################################################
# TIPS PROFESIONALES
###########################################################

"""
TIP 1

Si un bug no puede reproducirse,
primero intenta conseguir exactamente
los mismos datos del usuario.

-----------------------------------

TIP 2

Nunca digas:

"No sé por qué ya funciona."

Si no sabes qué lo solucionó,
el bug puede regresar.

-----------------------------------

TIP 3

Mientras más simple sea una función,
más fácil será depurarla.

-----------------------------------

TIP 4

Las funciones largas suelen esconder bugs.

Divide problemas grandes
en funciones pequeñas.

-----------------------------------

TIP 5

Los nombres claros facilitan encontrar errores.

Compara:

a

vs

total_clientes_activos

¿Cuál transmite más información?
"""

###########################################################
# EJERCICIO 4
###########################################################

"""
Observa el código.

def calcular_total(precios):
    total = 0

    for precio in precios:
        total += precio

    return total / len(precios)

Pregunta.

¿Qué caso extremo no fue considerado?

Respuesta.

Una lista vacía.
"""

###########################################################
# EJERCICIO 5
###########################################################

"""
Un usuario informa:

"El sistema genera reportes incompletos."

Escribe una estrategia de debugging.

Debe incluir:

1. Cómo reproducirías el problema.

2. Qué información pedirías.

3. Qué hipótesis formularías.

4. Cómo validarías cada hipótesis.

5. Cómo comprobarías que el bug
   quedó solucionado.
"""

###########################################################
# EJERCICIO 6 (Difícil)
###########################################################

"""
Lee cuidadosamente.

Una API devuelve 1000 registros.

Tu programa solamente procesa 996.

No aparece ninguna excepción.

No existen errores visibles.

Pregunta.

¿Qué harías?

No escribas código.

Describe el proceso profesional
de investigación paso a paso.

Piensa como un ingeniero,
no como un programador que adivina.
"""

###########################################################
# RETO PYTHON MASTERS
###########################################################

"""
Analiza este código.

def calcular_descuento(precio, porcentaje):
    descuento = precio * porcentaje
    return precio - descuento

print(calcular_descuento(100, 20))

¿Por qué el resultado es incorrecto?

¿Cómo lo detectarías?

¿Qué pruebas escribirías?

¿Cómo evitarías que vuelva a ocurrir?

No respondas inmediatamente.

Primero sigue la metodología aprendida:

✓ Comprender.

✓ Reproducir.

✓ Formular hipótesis.

✓ Verificar.

✓ Corregir.

✓ Validar.
"""

###########################################################
# PREGUNTAS DE REFLEXIÓN
###########################################################

"""
1.

¿Por qué modificar código sin entender
el problema suele empeorar la situación?

------------------------------------------------

2.

¿Por qué una excepción no siempre indica
la causa raíz del bug?

------------------------------------------------

3.

¿Por qué los desarrolladores senior
dedican más tiempo investigando
que escribiendo código?

------------------------------------------------

4.

¿Cuál es la diferencia entre evidencia
y suposición durante un proceso
de debugging?

------------------------------------------------

5.

¿Cuál de todas las buenas prácticas
crees que tendrá mayor impacto
en tu carrera profesional?
"""

###########################################################
# RESUMEN GENERAL
###########################################################

"""
En este archivo aprendiste:

✓ Qué es un bug.

✓ Qué significa debugging.

✓ Diferencia entre:

    • Error
    • Bug
    • Excepción
    • Fallo

✓ Tipos de bugs.

✓ Causa raíz.

✓ Síntoma vs problema.

✓ Metodología profesional de depuración.

✓ Importancia de reproducir un problema.

✓ Cómo formular hipótesis.

✓ Por qué nunca debes modificar
  código al azar.

✓ Buenas prácticas profesionales.

Este conocimiento será la base para
los siguientes archivos del bloque.

En 16.1B aprenderás herramientas reales
de depuración en Python:

✓ print() estratégico

✓ Breakpoints

✓ Debugger de VS Code

✓ Inspección de variables

✓ Step Into

✓ Step Over

✓ Step Out

✓ Watches

✓ Call Stack

✓ Depuración de funciones

✓ Casos reales de debugging
en proyectos profesionales.

Recuerda:

Un excelente desarrollador no es quien
comete menos errores.

Es quien sabe encontrarlos,
entenderlos y solucionarlos
de forma sistemática y profesional.
"""

###########################################################
# FIN DEL ARCHIVO
###########################################################