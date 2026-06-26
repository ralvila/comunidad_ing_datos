"""
==========================================================
PYTHON MASTERS
BLOQUE 16 - BUENAS PRÁCTICAS Y DEBUGGING

Archivo:
16.2B_logging_profesional.py

PARTE 1 DE 3

Tema:
Fundamentos del Logging Profesional

Autor:
Comunidad de Ingeniería de Datos

==========================================================

OBJETIVOS

Al finalizar esta sección podrás:

✓ Comprender qué es Logging.

✓ Entender por qué existe.

✓ Diferenciar print() de logging.

✓ Aprender cuándo utilizar cada uno.

✓ Configurar un logger básico.

✓ Comprender la estructura de un mensaje
  de log.

==========================================================
"""

###########################################################
# ¿QUÉ ES EL LOGGING?
###########################################################

"""
Una de las herramientas más importantes
en el desarrollo profesional es el Logging.

Logging consiste en registrar eventos
que ocurren durante la ejecución
de un programa.

No solamente errores.

También:

✓ Inicio del programa.

✓ Finalización.

✓ Usuarios conectados.

✓ Archivos procesados.

✓ Tiempo de ejecución.

✓ Advertencias.

✓ Errores.

✓ Excepciones.

✓ Eventos importantes.

Podemos pensar en un log
como el diario de vida
de una aplicación.
"""

###########################################################
# ¿POR QUÉ EXISTE EL LOGGING?
###########################################################

"""
Imagina esta situación.

Un usuario llama al equipo
de soporte.

Dice:

"La aplicación falló ayer
a las 3:15 PM."

Nadie estaba viendo
la pantalla.

Nadie sabe qué ocurrió.

Sin Logging.

Es prácticamente imposible
investigar.

Con Logging.

Podemos revisar exactamente
qué ocurrió.

Qué datos recibió.

Qué función estaba ejecutándose.

Qué excepción apareció.

Qué usuario estaba conectado.

Por eso todas las aplicaciones
profesionales utilizan Logging.
"""

###########################################################
# PRINT VS LOGGING
###########################################################

"""
Muchos principiantes creen que:

print()

y

logging

son lo mismo.

No lo son.

print()

Está pensado para mostrar información
al usuario o para realizar debugging
rápido.

Logging

Está diseñado para registrar eventos
de forma permanente.

Es decir.

Los logs pueden almacenarse
durante días,
meses
o incluso años.
"""

###########################################################
# EJEMPLO
###########################################################

nombre = "Laura"

print(nombre)

"""
Esto únicamente aparece
en la consola.

Cuando el programa termina,
esa información desaparece.

No queda ningún historial.
"""

###########################################################
# EJEMPLO DE LOGGING
###########################################################

import logging

logging.warning("Primer mensaje de logging.")

"""
Salida aproximada.

WARNING:root:Primer mensaje de logging.

Observa la diferencia.

Ya no solamente vemos
el mensaje.

También aparece:

✓ Nivel.

✓ Logger.

✓ Mensaje.
"""

###########################################################
# ¿CUÁNDO USAR PRINT?
###########################################################

"""
print() sigue siendo útil.

Por ejemplo.

✓ Mostrar resultados.

✓ Aprender Python.

✓ Pequeños scripts.

✓ Explicar ejercicios.

✓ Debugging rápido.

No tiene nada de malo.

Simplemente
no es suficiente
para proyectos grandes.
"""

###########################################################
# ¿CUÁNDO USAR LOGGING?
###########################################################

"""
Siempre que el programa
sea importante.

Ejemplos.

✓ APIs

✓ ETLs

✓ Data Pipelines

✓ Automatizaciones

✓ Backend

✓ Microservicios

✓ Aplicaciones Web

✓ Sistemas bancarios

✓ Sistemas empresariales

✓ Machine Learning

✓ Data Engineering

En esos escenarios,
Logging es indispensable.
"""

###########################################################
# EL MÓDULO LOGGING
###########################################################

"""
Python incluye un módulo
llamado logging.

No necesitamos instalar nada.

Simplemente:

import logging

Está disponible
en la biblioteca estándar.
"""

###########################################################
# PRIMER LOGGER
###########################################################

import logging

logging.warning("Hola Python Masters")

"""
Salida.

WARNING:root:Hola Python Masters

Veamos cada parte.
"""

###########################################################
# ANATOMÍA DE UN LOG
###########################################################

"""
WARNING:root:Hola Python Masters

Está compuesto por tres elementos.

-----------------------------------

WARNING

Nivel del mensaje.

-----------------------------------

root

Nombre del logger.

-----------------------------------

Hola Python Masters

Mensaje.

Más adelante aprenderemos
a personalizar completamente
cada uno de estos elementos.
"""

###########################################################
# ¿QUÉ ES UN LOGGER?
###########################################################

"""
Un Logger es un objeto
encargado de registrar eventos.

Podemos tener:

Logger principal.

Logger para Base de Datos.

Logger para API.

Logger para Seguridad.

Logger para ETLs.

Cada uno puede registrar
información diferente.
"""

###########################################################
# BASICCONFIG
###########################################################

"""
La forma más sencilla
de configurar Logging
es utilizando:

logging.basicConfig()

Permite definir:

✓ Nivel mínimo.

✓ Formato.

✓ Archivo.

✓ Codificación.

✓ Fecha.

Es el punto de partida
para la mayoría
de proyectos pequeños.
"""

###########################################################
# EJEMPLO
###########################################################

import logging

logging.basicConfig(level=logging.INFO)

logging.info("Programa iniciado.")

"""
Ahora permitimos
que aparezcan mensajes INFO.

Más adelante veremos
todos los niveles.
"""

###########################################################
# FORMATO DE LOS MENSAJES
###########################################################

"""
Un log profesional
normalmente contiene.

Fecha.

Hora.

Nivel.

Nombre del logger.

Mensaje.

Ejemplo.

2026-03-25 09:15:22

INFO

main

Programa iniciado.

Toda esa información
puede configurarse.
"""

###########################################################
# EJEMPLO
###########################################################

import logging

logging.basicConfig(

    level=logging.INFO,

    format="%(levelname)s - %(message)s"

)

logging.info("Conexión establecida.")

"""
Salida.

INFO - Conexión establecida.
"""

###########################################################
# PLACEHOLDERS DEL FORMAT
###########################################################

"""
Los formatos utilizan
placeholders.

Los más comunes son.

%(levelname)s

Nivel.

-------------------------

%(message)s

Mensaje.

-------------------------

%(asctime)s

Fecha y hora.

-------------------------

%(name)s

Nombre del logger.

-------------------------

%(filename)s

Archivo.

-------------------------

%(lineno)d

Número de línea.

Más adelante veremos
muchos más.
"""

###########################################################
# EJEMPLO
###########################################################

import logging

logging.basicConfig(

    level=logging.INFO,

    format="%(asctime)s | %(levelname)s | %(message)s"

)

logging.info("Proceso iniciado.")

"""
Salida aproximada.

2026-03-25 10:30:14

INFO

Proceso iniciado.
"""

###########################################################
# ¿POR QUÉ ES IMPORTANTE
# LA FECHA?
###########################################################

"""
Imagina un ETL.

Comienza a las

08:00

y termina a las

08:45

Sin fecha.

No sabemos cuándo ocurrió.

Sin hora.

No sabemos cuánto tardó.

Con Logging.

Todo queda registrado.
"""

###########################################################
# EJEMPLO
###########################################################

import logging

logging.basicConfig(

    level=logging.INFO,

    format="%(asctime)s | %(message)s"

)

logging.info("Inicio del procesamiento.")

logging.info("Archivo cargado.")

logging.info("Proceso finalizado.")

"""
Con estos tres mensajes
podemos reconstruir
la ejecución completa.
"""

###########################################################
# LOGGING COMO HISTORIAL
###########################################################

"""
Piensa en un avión.

Después de cada vuelo,
la caja negra conserva
todos los eventos.

Logging cumple
exactamente esa función.

Nos permite reconstruir
lo sucedido.

Incluso días después.
"""

###########################################################
# CASO REAL
###########################################################

"""
Supongamos un Data Pipeline.

08:00

Inicio.

↓

08:01

Archivo recibido.

↓

08:03

125.000 registros leídos.

↓

08:06

12 registros descartados.

↓

08:08

Carga completada.

Sin Logging.

No sabríamos
qué ocurrió.

Con Logging.

Toda la historia
queda registrada.
"""

###########################################################
# PRINT O LOGGING
###########################################################

"""
Regla sencilla.

¿El usuario necesita verlo?

↓

print()

--------------------------------

¿El desarrollador necesita
investigarlo después?

↓

logging
"""

###########################################################
# BUENAS PRÁCTICAS
###########################################################

"""
✓ Utiliza logging
en proyectos reales.

✓ Mantén mensajes claros.

✓ Registra eventos importantes.

✓ No registres información inútil.

✓ Configura correctamente
el formato.

✓ Incluye fecha y hora.

✓ Mantén consistencia
en los mensajes.
"""

###########################################################
# TIPS PROFESIONALES
###########################################################

"""
TIP 1

Un buen log responde preguntas.

No genera más preguntas.

------------------------------------

TIP 2

Escribe mensajes
como si otro desarrollador
fuera a leerlos.

------------------------------------

TIP 3

Piensa que investigarás
ese log dentro de seis meses.

¿Seguirá siendo claro?

------------------------------------

TIP 4

Un mensaje corto
pero específico
vale más que diez mensajes ambiguos.
"""

###########################################################
# EJERCICIO 1
###########################################################

"""
Convierte los siguientes print()
en mensajes de logging.

print("Programa iniciado")

print("Archivo leído")

print("Proceso terminado")

¿Qué nivel utilizarías
en cada uno?

Lo aprenderemos
en la siguiente parte.
"""

###########################################################
# EJERCICIO 2
###########################################################

"""
Diseña un formato
para una aplicación bancaria.

¿Qué información
consideras indispensable?

Piensa en:

✓ Fecha

✓ Hora

✓ Nivel

✓ Usuario

✓ Módulo

✓ Mensaje
"""

###########################################################
# EJERCICIO 3 (Difícil)
###########################################################

"""
Supón que eres responsable
de un pipeline que procesa
8 millones de registros diarios.

¿Qué eventos registrarías?

Haz una lista
de al menos diez mensajes
que consideres importantes.

No escribas código.

Piensa como un Data Engineer.
"""

"""
==========================================================
PYTHON MASTERS
BLOQUE 16 - BUENAS PRÁCTICAS Y DEBUGGING

Archivo:
16.2B_logging_profesional.py

PARTE 2 DE 3

Tema:
Logging Profesional en Python

Autor:
Comunidad de Ingeniería de Datos

==========================================================

OBJETIVOS

Al finalizar esta sección podrás:

✓ Comprender los niveles de Logging.

✓ Configurar loggers profesionales.

✓ Registrar excepciones.

✓ Guardar logs en archivos.

✓ Utilizar múltiples handlers.

✓ Crear loggers por módulo.

✓ Comprender la importancia del Stack Trace
  dentro de los logs.

==========================================================
"""

###########################################################
# LOS NIVELES DE LOGGING
###########################################################

"""
No todos los mensajes tienen
la misma importancia.

Por esa razón Python clasifica
los logs en niveles.

Los cinco niveles principales son:

DEBUG

↓

INFO

↓

WARNING

↓

ERROR

↓

CRITICAL

Cada uno representa un grado
de importancia diferente.

Elegir correctamente el nivel
es una buena práctica profesional.
"""

###########################################################
# DEBUG
###########################################################

"""
DEBUG representa información
muy detallada.

Normalmente solo interesa
durante el desarrollo.

Ejemplos.

✓ Variables.

✓ Parámetros.

✓ Resultados intermedios.

✓ Flujo interno.

Generalmente NO se habilita
en producción.
"""

###########################################################
# EJEMPLO
###########################################################

import logging

logging.basicConfig(level=logging.DEBUG)

numero = 15

logging.debug(f"Valor recibido: {numero}")

"""
Salida aproximada.

DEBUG:root:Valor recibido: 15
"""

###########################################################
# INFO
###########################################################

"""
INFO representa eventos normales
del sistema.

Ejemplos.

✓ Inicio del programa.

✓ Usuario autenticado.

✓ Archivo cargado.

✓ Pipeline iniciado.

✓ Proceso finalizado.

Es probablemente
el nivel más utilizado
en producción.
"""

###########################################################
# EJEMPLO
###########################################################

logging.info("Proceso iniciado.")

logging.info("Archivo cargado correctamente.")

###########################################################
# WARNING
###########################################################

"""
WARNING significa:

Algo inesperado ocurrió.

Pero el programa
todavía puede continuar.

Ejemplos.

✓ Archivo vacío.

✓ Registro duplicado.

✓ Valor nulo.

✓ Configuración antigua.

Todavía no es un error.

Pero merece atención.
"""

###########################################################
# EJEMPLO
###########################################################

clientes = []

if not clientes:

    logging.warning(
        "La lista de clientes está vacía."
    )

###########################################################
# ERROR
###########################################################

"""
ERROR indica que ocurrió
un problema.

Una operación falló.

Pero el sistema
todavía puede continuar.

Ejemplos.

✓ Error al leer archivo.

✓ Error de conexión.

✓ Error de autenticación.

✓ Consulta SQL fallida.

Este nivel suele requerir
intervención del equipo.
"""

###########################################################
# EJEMPLO
###########################################################

try:

    resultado = 10 / 0

except ZeroDivisionError:

    logging.error(
        "No fue posible realizar la división."
    )

###########################################################
# CRITICAL
###########################################################

"""
CRITICAL representa
errores extremadamente graves.

Generalmente indican que
el sistema no puede continuar.

Ejemplos.

✓ Base de datos caída.

✓ Memoria insuficiente.

✓ Configuración inexistente.

✓ Servicio crítico fuera de línea.

Estos mensajes normalmente
generan alertas automáticas.
"""

###########################################################
# EJEMPLO
###########################################################

logging.critical(
    "No fue posible conectar con la base de datos."
)

###########################################################
# RESUMEN DE NIVELES
###########################################################

"""
DEBUG

Información técnica.

-----------------------------------

INFO

Eventos normales.

-----------------------------------

WARNING

Algo inesperado.

-----------------------------------

ERROR

Una operación falló.

-----------------------------------

CRITICAL

El sistema no puede continuar.
"""

###########################################################
# ¿QUÉ NIVEL DEBO USAR?
###########################################################

"""
Una regla sencilla.

¿Estoy investigando?

↓

DEBUG

-----------------------------

¿Todo salió bien?

↓

INFO

-----------------------------

¿Algo extraño ocurrió?

↓

WARNING

-----------------------------

¿Falló una operación?

↓

ERROR

-----------------------------

¿El sistema debe detenerse?

↓

CRITICAL
"""

###########################################################
# LOGGER POR MÓDULO
###########################################################

"""
Los proyectos profesionales
normalmente NO utilizan
el logger principal (root).

Cada módulo tiene
su propio logger.

Para ello utilizamos:

logging.getLogger(__name__)
"""

###########################################################
# EJEMPLO
###########################################################

import logging

logger = logging.getLogger(__name__)

logger.info("Logger del módulo inicializado.")

"""
¿Por qué es útil?

Porque permite identificar
exactamente qué archivo
generó cada mensaje.
"""

###########################################################
# LOGGING EN ARCHIVOS
###########################################################

"""
Hasta ahora todos los mensajes
aparecen en la consola.

Pero normalmente queremos
guardarlos.

Para ello utilizamos:

filename
"""

###########################################################
# EJEMPLO
###########################################################

import logging

logging.basicConfig(

    filename="aplicacion.log",

    level=logging.INFO

)

logging.info("Aplicación iniciada.")

"""
Ahora el mensaje
se almacenará
en un archivo.

Esto permite investigar
problemas incluso días después.
"""

###########################################################
# FORMATO PROFESIONAL
###########################################################

"""
Un formato habitual es.

Fecha

Hora

Nivel

Archivo

Línea

Mensaje

Veamos cómo configurarlo.
"""

###########################################################
# EJEMPLO
###########################################################

logging.basicConfig(

    level=logging.INFO,

    format=(
        "%(asctime)s | "
        "%(levelname)s | "
        "%(filename)s:%(lineno)d | "
        "%(message)s"
    )

)

logging.info("Configuración completada.")

"""
Salida aproximada.

2026-03-28 09:15:18

INFO

main.py:55

Configuración completada.
"""

###########################################################
# MÚLTIPLES HANDLERS
###########################################################

"""
Un Handler indica
dónde se enviará el log.

Ejemplos.

Consola.

Archivo.

Servidor remoto.

Azure Monitor.

Elastic.

Splunk.

Datadog.

Podemos utilizar varios
al mismo tiempo.
"""

###########################################################
# EJEMPLO
###########################################################

import logging

logger = logging.getLogger("mi_logger")

logger.setLevel(logging.INFO)

console = logging.StreamHandler()

file = logging.FileHandler("aplicacion.log")

logger.addHandler(console)

logger.addHandler(file)

logger.info("Mensaje enviado a dos destinos.")

"""
El mismo mensaje aparecerá:

✓ Consola.

✓ Archivo.

Al mismo tiempo.
"""

###########################################################
# LOGGING DE EXCEPCIONES
###########################################################

"""
Uno de los mayores errores
de los principiantes es registrar
solamente el mensaje.

Ejemplo.

"Error al abrir archivo."

Eso no es suficiente.

Necesitamos conocer
la excepción completa.
"""

###########################################################
# EJEMPLO
###########################################################

try:

    10 / 0

except Exception as error:

    logging.error(error)

"""
Esto registra únicamente
el texto de la excepción.

Podemos hacerlo mucho mejor.
"""

###########################################################
# LOGGING.EXCEPTION()
###########################################################

"""
Existe una función especializada.

logging.exception()

Hace dos cosas.

✓ Registra el mensaje.

✓ Registra automáticamente
el Stack Trace.

Es una excelente práctica.
"""

###########################################################
# EJEMPLO
###########################################################

try:

    10 / 0

except Exception:

    logging.exception(
        "Ocurrió un error inesperado."
    )

"""
El log contendrá.

Mensaje.

+

Stack Trace completo.

Esto facilita enormemente
el diagnóstico.
"""

###########################################################
# EXC_INFO
###########################################################

"""
También podemos utilizar.

exc_info=True

para registrar
la excepción completa.
"""

###########################################################
# EJEMPLO
###########################################################

try:

    int("Python")

except Exception:

    logging.error(

        "No fue posible convertir.",

        exc_info=True

    )

"""
Obtendremos.

Mensaje.

+

Traceback.

Muy útil
para producción.
"""

###########################################################
# ROTACIÓN DE LOGS
###########################################################

"""
Imagina un sistema
que funciona 24 horas.

Después de varios meses
el archivo podría medir
decenas de gigabytes.

Por eso existen
los Rotating Handlers.

Ellos crean automáticamente
nuevos archivos.

Más adelante aprenderemos
a utilizarlos.
"""

###########################################################
# BUENAS PRÁCTICAS
###########################################################

"""
✓ Utiliza niveles adecuados.

✓ Usa logger por módulo.

✓ Guarda logs en archivos.

✓ Registra excepciones completas.

✓ Incluye Stack Trace.

✓ Mantén formatos consistentes.

✓ No abuses del nivel DEBUG
en producción.
"""

###########################################################
# TIPS PROFESIONALES
###########################################################

"""
TIP 1

Un ERROR sin contexto
sirve de muy poco.

------------------------------------

TIP 2

Siempre registra
qué estaba intentando hacer
el programa.

------------------------------------

TIP 3

Los logs deben ayudar
a reconstruir la historia.

------------------------------------

TIP 4

Si un desarrollador necesita
leer el código para entender
el log,

el log probablemente
no es suficientemente claro.
"""

###########################################################
# EJERCICIO 1
###########################################################

"""
Clasifica cada situación.

Archivo cargado.

↓

¿DEBUG?

¿INFO?

¿WARNING?

¿ERROR?

¿CRITICAL?

--------------------------------

No fue posible conectar
con SQL Server.

↓

¿Qué nivel utilizarías?
"""

###########################################################
# EJERCICIO 2
###########################################################

"""
Modifica el siguiente código.

try:

    resultado = 50 / 0

except Exception:

    print("Error.")

Reemplaza print()
por un logging profesional.
"""

###########################################################
# EJERCICIO 3 (Difícil)
###########################################################

"""
Diseña el sistema de Logging
para un pipeline de datos.

Debe registrar.

✓ Inicio.

✓ Fin.

✓ Tiempo.

✓ Cantidad de registros.

✓ Advertencias.

✓ Excepciones.

✓ Archivo procesado.

✓ Usuario.

No escribas código.

Piensa como un Data Engineer.
"""

"""
==========================================================
PYTHON MASTERS
BLOQUE 16 - BUENAS PRÁCTICAS Y DEBUGGING

Archivo:
16.2B_logging_profesional.py

PARTE 3 DE 3

Tema:
Logging en Proyectos Profesionales

Autor:
Comunidad de Ingeniería de Datos

==========================================================

OBJETIVOS

Al finalizar esta sección podrás:

✓ Diseñar una estrategia de Logging profesional.

✓ Implementar Logging en proyectos reales.

✓ Comprender qué información registrar.

✓ Evitar errores comunes.

✓ Aplicar Logging en APIs, ETLs y Data Engineering.

==========================================================
"""

###########################################################
# EL LOGGING COMO HERRAMIENTA
# DE OBSERVABILIDAD
###########################################################

"""
Hasta ahora hemos aprendido
cómo utilizar logging.

Ahora aprenderemos
por qué es una de las herramientas
más importantes en la industria.

Cuando una aplicación llega
a producción:

Nadie está viendo la pantalla.

Nadie está ejecutando print().

Nadie sabe qué ocurre.

Los logs se convierten
en los ojos del desarrollador.

Sin ellos,
el sistema es prácticamente
una caja negra.
"""

###########################################################
# ¿QUÉ ES LA OBSERVABILIDAD?
###########################################################

"""
Observabilidad significa:

Ser capaces de comprender
qué está ocurriendo dentro
de un sistema.

Generalmente se apoya en tres pilares.

• Logs

• Métricas

• Trazas (Tracing)

En este curso nos centraremos
en el primer pilar:

Logging.
"""

###########################################################
# CASO REAL
###########################################################

"""
Supongamos un pipeline
que procesa ventas.

Sin logs únicamente sabemos
que el proceso terminó.

Con logs podemos conocer.

08:00

Inicio.

↓

08:00:12

Archivo recibido.

↓

08:01:08

153.420 registros leídos.

↓

08:01:12

27 registros descartados.

↓

08:01:30

Carga iniciada.

↓

08:03:45

Carga completada.

↓

08:03:46

Tiempo total:

226 segundos.

Ahora podemos reconstruir
todo el proceso.
"""

###########################################################
# EJEMPLO
###########################################################

import logging

logging.basicConfig(

    level=logging.INFO,

    format="%(asctime)s | %(levelname)s | %(message)s"

)

logging.info("Inicio del ETL")

logging.info("Leyendo archivo ventas.csv")

logging.info("153420 registros encontrados")

logging.info("Carga finalizada")

"""
Aunque parece sencillo,
ya estamos generando
un historial completo.
"""

###########################################################
# LOGGING EN ETLs
###########################################################

"""
Todo proceso ETL debería registrar,
como mínimo:

✓ Inicio.

✓ Fin.

✓ Archivo procesado.

✓ Cantidad de registros.

✓ Tiempo de ejecución.

✓ Registros descartados.

✓ Advertencias.

✓ Excepciones.

✓ Destino cargado.

✓ Resultado final.
"""

###########################################################
# EJEMPLO
###########################################################

logging.info("ETL iniciado.")

logging.info("Archivo: clientes.csv")

logging.info("Registros leídos: 25430")

logging.warning("15 registros duplicados.")

logging.info("Insertando datos...")

logging.info("Proceso terminado.")

###########################################################
# LOGGING EN APIS
###########################################################

"""
En una API normalmente registramos.

✓ Endpoint.

✓ Método HTTP.

✓ Usuario.

✓ Tiempo de respuesta.

✓ Código HTTP.

✓ Errores.

Esto permite investigar
incidentes rápidamente.
"""

###########################################################
# EJEMPLO
###########################################################

logging.info("GET /clientes")

logging.info("Usuario autenticado.")

logging.info("HTTP 200")

###########################################################
# LOGGING EN DATA ENGINEERING
###########################################################

"""
Como Data Engineers
trabajaremos constantemente
con pipelines.

Un buen log debería responder.

¿Qué archivo llegó?

¿Cuántos registros tenía?

¿Cuántos fueron válidos?

¿Cuántos fallaron?

¿Cuánto tardó?

¿Dónde quedó almacenado?

Si el log responde
esas preguntas,

el soporte será muchísimo
más sencillo.
"""

###########################################################
# QUÉ NUNCA DEBEMOS REGISTRAR
###########################################################

"""
Existen datos
que jamás deben aparecer
en los logs.

Por ejemplo.

✗ Contraseñas.

✗ Tokens.

✗ Claves privadas.

✗ Tarjetas de crédito.

✗ Datos médicos.

✗ Información personal sensible.

Los logs pueden permanecer
años almacenados.

Debemos protegerlos.
"""

###########################################################
# MAL EJEMPLO
###########################################################

usuario = "admin"

password = "123456"

logging.info(

    f"Usuario={usuario}, Password={password}"

)

"""
Este código representa
un enorme riesgo de seguridad.

Nunca hagas esto.
"""

###########################################################
# BUEN EJEMPLO
###########################################################

logging.info(

    f"Usuario autenticado: {usuario}"

)

"""
Registramos únicamente
la información necesaria.
"""

###########################################################
# MENSAJES ÚTILES
###########################################################

"""
Comparemos.

Malo.

Error.

------------------------------------

Bueno.

No fue posible leer
clientes.csv.

------------------------------------

Mucho mejor.

No fue posible leer
clientes.csv.

Ruta:

/datos/2026/clientes.csv

Motivo:

Archivo inexistente.

Mientras más contexto exista,
más sencillo será investigar.
"""

###########################################################
# MENSAJES CONSISTENTES
###########################################################

"""
Todos los mensajes
deberían seguir
un mismo estilo.

Ejemplo.

Inicio del proceso.

Archivo recibido.

Archivo validado.

Carga iniciada.

Carga completada.

Evita mezclar estilos.
"""

###########################################################
# LOGGING Y DEBUGGING
###########################################################

"""
No compiten.

Se complementan.

Durante desarrollo.

↓

Debugger.

Producción.

↓

Logging.

Muchas veces utilizaremos ambos.
"""

###########################################################
# LOGGING Y STACK TRACE
###########################################################

"""
Cuando ocurre una excepción
en producción,
normalmente no tenemos acceso
al debugger.

Pero sí tenemos los logs.

Por eso es tan importante
registrar:

logging.exception()

o

exc_info=True

Así conservaremos
el Stack Trace completo.
"""

###########################################################
# EJEMPLO
###########################################################

try:

    int("Python Masters")

except Exception:

    logging.exception(

        "Error durante la conversión."

    )

"""
El archivo de log contendrá.

Mensaje.

+

Stack Trace.

Eso facilita enormemente
el soporte.
"""

###########################################################
# ERRORES COMUNES
###########################################################

"""
ERROR 1

Registrar demasiada información.

------------------------------------

ERROR 2

No registrar excepciones.

------------------------------------

ERROR 3

Mensajes ambiguos.

------------------------------------

ERROR 4

No registrar tiempos.

------------------------------------

ERROR 5

No registrar cantidad
de registros.

------------------------------------

ERROR 6

Registrar datos sensibles.

------------------------------------

ERROR 7

Utilizar siempre
el nivel INFO.
"""

###########################################################
# RECOMENDACIONES
###########################################################

"""
Antes de escribir un log
pregúntate.

¿Este mensaje ayudará
a otro desarrollador
dentro de seis meses?

Si la respuesta es no,

probablemente el mensaje
deba mejorar.
"""

###########################################################
# CASO EMPRESARIAL
###########################################################

"""
Supongamos una carga diaria.

El soporte recibe
el siguiente log.

------------------------------------

08:00

Proceso iniciado.

08:00:08

Archivo ventas.csv recibido.

08:00:09

254.320 registros.

08:00:11

35 registros descartados.

08:00:20

Insertando datos.

08:02:18

Proceso finalizado.

------------------------------------

Sin abrir el código
ya podemos comprender
qué ocurrió.
"""

###########################################################
# LABORATORIO 1
###########################################################

"""
Construye un logger
para un ETL ficticio.

Debe registrar.

✓ Inicio.

✓ Archivo.

✓ Número de registros.

✓ Advertencias.

✓ Fin.

Utiliza INFO
y WARNING.
"""

###########################################################
# LABORATORIO 2
###########################################################

"""
Construye un programa
que provoque
una excepción.

Después registra.

✓ Mensaje.

✓ Stack Trace.

Utiliza:

logging.exception()
"""

###########################################################
# LABORATORIO 3
###########################################################

"""
Diseña un logger
para una API.

Registra.

✓ Endpoint.

✓ Usuario.

✓ Tiempo.

✓ Código HTTP.

✓ Excepciones.

No escribas
la implementación completa.

Diseña únicamente
la estrategia.
"""

###########################################################
# RETO PYTHON MASTERS
###########################################################

"""
Imagina que eres
el responsable
de una plataforma
de Ingeniería de Datos.

Cada noche se ejecutan
25 pipelines.

Diseña un estándar
de Logging.

Debe incluir.

✓ Formato.

✓ Niveles.

✓ Información obligatoria.

✓ Excepciones.

✓ Auditoría.

✓ Archivos.

✓ Rotación.

✓ Seguridad.

✓ Datos prohibidos.

✓ Convención de mensajes.

Piensa como
un Arquitecto de Datos.

No escribas código.

Diseña el estándar.
"""

###########################################################
# PREGUNTAS DE REFLEXIÓN
###########################################################

"""
1.

¿Por qué Logging
es indispensable
en producción?

------------------------------------------------

2.

¿Por qué print()
no reemplaza
al Logging?

------------------------------------------------

3.

¿Qué información
jamás registrarías?

------------------------------------------------

4.

¿Cuáles son los eventos
más importantes
en un ETL?

------------------------------------------------

5.

¿Qué características
debe tener
un buen mensaje
de Logging?
"""
