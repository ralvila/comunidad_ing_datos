"""
==========================================================
PYTHON MASTERS
BLOQUE 16 - BUENAS PRÁCTICAS Y DEBUGGING

Archivo:
16.3C_proyecto_profesional.py

PARTE 1 DE 4

Tema:
Cómo desarrollar un Proyecto Profesional en Python

Autor:
Comunidad de Ingeniería de Datos

==========================================================

OBJETIVOS

Al finalizar esta sección podrás:

✓ Comprender el ciclo de vida de un proyecto.

✓ Diferenciar programar de desarrollar software.

✓ Aprender cómo inicia un proyecto profesional.

✓ Comprender la importancia de la planificación.

✓ Conocer las fases de desarrollo utilizadas
  por equipos profesionales.

==========================================================
"""

###########################################################
# ¿QUÉ ES UN PROYECTO DE SOFTWARE?
###########################################################

"""
Hasta este momento del curso
hemos aprendido:

✓ Variables

✓ Condicionales

✓ Bucles

✓ Funciones

✓ Colecciones

✓ Programación Orientada a Objetos

✓ Excepciones

✓ Módulos

✓ Archivos

✓ Debugging

✓ Logging

✓ Buenas prácticas

✓ Organización de proyectos

Ahora ha llegado el momento
de unir todos esos conocimientos.

Eso es precisamente
un proyecto profesional.

Un proyecto no consiste
en escribir muchas líneas de código.

Consiste en resolver
un problema real
mediante software.
"""

###########################################################
# PROGRAMAR VS
# DESARROLLAR SOFTWARE
###########################################################

"""
Estos conceptos
no significan lo mismo.

Programar consiste en escribir código.

Desarrollar software incluye además:

✓ Comprender el problema.

✓ Diseñar la solución.

✓ Planificar.

✓ Programar.

✓ Probar.

✓ Documentar.

✓ Desplegar.

✓ Mantener.

Es un proceso mucho más amplio.
"""

###########################################################
# EL ERROR MÁS COMÚN
###########################################################

"""
Cuando un desarrollador
recibe un nuevo proyecto,
muchas veces hace esto.

Abre VS Code.

↓

Crea main.py

↓

Empieza a escribir código.

Este es uno de los errores
más comunes.

Antes de escribir una línea,
debemos comprender
el problema.
"""

###########################################################
# EL CICLO DE VIDA
###########################################################

"""
Todo proyecto profesional
recorre varias etapas.

Problema

↓

Análisis

↓

Diseño

↓

Implementación

↓

Pruebas

↓

Despliegue

↓

Mantenimiento

En este archivo estudiaremos
cada una de ellas.
"""

###########################################################
# ETAPA 1
# COMPRENDER EL PROBLEMA
###########################################################

"""
Todo comienza
con una necesidad.

Ejemplo.

Una empresa recibe
archivos Excel.

Un empleado los procesa
manualmente.

Tarda cuatro horas.

El objetivo del proyecto
no es "programar".

El objetivo es:

Reducir esas cuatro horas.

El código es únicamente
el medio para lograrlo.
"""

###########################################################
# HACER PREGUNTAS
###########################################################

"""
Antes de diseñar
una solución,
debemos comprender
el problema.

Algunas preguntas.

✓ ¿Qué ocurre actualmente?

✓ ¿Qué se quiere lograr?

✓ ¿Quién utilizará el sistema?

✓ ¿Qué datos existen?

✓ ¿Qué restricciones hay?

✓ ¿Qué ocurre si algo falla?

Mientras más comprendamos
el problema,
mejor será la solución.
"""

###########################################################
# EJEMPLO
###########################################################

"""
Problema.

Procesar un archivo
de clientes.

Antes de programar
deberíamos preguntar.

¿Cuál es el formato?

¿Cuántos registros?

¿Puede venir vacío?

¿Qué columnas son obligatorias?

¿Existen duplicados?

Estas preguntas
evitan muchos bugs.
"""

###########################################################
# ETAPA 2
# ANALIZAR LA SOLUCIÓN
###########################################################

"""
Una vez comprendido
el problema,

debemos analizar
la solución.

No programar.

Analizar.

Por ejemplo.

Entrada.

↓

Proceso.

↓

Salida.

Esto nos permite visualizar
el flujo completo.
"""

###########################################################
# EJEMPLO
###########################################################

"""
Entrada.

clientes.csv

↓

Validación.

↓

Transformación.

↓

Carga SQL Server.

↓

Reporte final.

Todo esto
puede diseñarse
antes de escribir código.
"""

###########################################################
# ETAPA 3
# DISEÑAR
###########################################################

"""
El diseño responde preguntas como.

¿Cuántos módulos?

¿Qué funciones?

¿Qué clases?

¿Qué carpetas?

¿Qué dependencias?

¿Cómo crecerá
el proyecto?

Un buen diseño
reduce enormemente
el mantenimiento futuro.
"""

###########################################################
# DIAGRAMAS
###########################################################

"""
Muchas empresas utilizan diagramas
antes de programar.

Ejemplos.

Diagramas de flujo.

Arquitectura.

UML.

Casos de uso.

Secuencia.

No son obligatorios.

Pero ayudan
a visualizar
la solución.
"""

###########################################################
# NO PIENSES EN CÓDIGO
###########################################################

"""
Durante el diseño
deberíamos pensar
en responsabilidades.

No en sintaxis.

Ejemplo.

Incorrecto.

"Voy a utilizar pandas."

Correcto.

"Necesito leer un archivo CSV."

La herramienta
se elige después.
"""

###########################################################
# DIVIDE EL PROBLEMA
###########################################################

"""
Los proyectos grandes
deben dividirse.

Ejemplo.

Leer archivo.

↓

Validar datos.

↓

Transformar.

↓

Guardar.

↓

Generar reporte.

Resolver pequeños problemas
es mucho más sencillo
que resolver uno enorme.
"""

###########################################################
# CASO REAL
###########################################################

"""
Supongamos un ETL.

Muchos principiantes
escribirían una función
de 500 líneas.

Un desarrollador profesional
la dividiría.

leer_archivo()

↓

validar_datos()

↓

transformar()

↓

guardar()

↓

notificar()

Cada función
tiene una única responsabilidad.
"""

###########################################################
# PIENSA EN EL FUTURO
###########################################################

"""
Cuando diseñes un proyecto
pregúntate.

¿Qué ocurrirá
si mañana cambia
el formato del archivo?

¿Y si llegan
10 millones de registros?

¿Y si debemos agregar
otra fuente de datos?

Diseñar pensando
en el crecimiento
reduce futuras modificaciones.
"""

###########################################################
# DOCUMENTAR EL DISEÑO
###########################################################

"""
No confíes únicamente
en la memoria.

Documenta.

✓ Objetivo.

✓ Arquitectura.

✓ Decisiones.

✓ Restricciones.

✓ Supuestos.

Esto facilita
la incorporación
de nuevos integrantes
al equipo.
"""

###########################################################
# ERRORES COMUNES
###########################################################

"""
ERROR 1

Programar inmediatamente.

------------------------------------

ERROR 2

No comprender
el problema.

------------------------------------

ERROR 3

No documentar.

------------------------------------

ERROR 4

No dividir
el problema.

------------------------------------

ERROR 5

Diseñar pensando
únicamente
en el presente.
"""

###########################################################
# BUENAS PRÁCTICAS
###########################################################

"""
✓ Comprende el problema.

✓ Haz preguntas.

✓ Diseña antes
de programar.

✓ Divide responsabilidades.

✓ Documenta.

✓ Piensa en el crecimiento.

✓ Valida tus suposiciones.

✓ No empieces escribiendo código.
"""

###########################################################
# TIPS PROFESIONALES
###########################################################

"""
TIP 1

Un problema bien entendido
ya está parcialmente resuelto.

------------------------------------

TIP 2

Nunca aceptes requisitos
ambiguos.

Pregunta.

------------------------------------

TIP 3

Los mejores desarrolladores
dedican más tiempo
al diseño
que a escribir código.

------------------------------------

TIP 4

Si puedes explicar
la solución
sin mostrar código,

probablemente
comprendes realmente
el problema.

------------------------------------

TIP 5

El código cambia.

Las buenas decisiones
de diseño
permanecen durante años.
"""

###########################################################
# EJERCICIO 1
###########################################################

"""
Una empresa desea automatizar
la carga de archivos Excel.

Antes de programar,
escribe al menos
10 preguntas
que realizarías
al cliente.
"""

###########################################################
# EJERCICIO 2
###########################################################

"""
Diseña el flujo
de un sistema
que procese pedidos.

Incluye.

✓ Entrada.

✓ Validaciones.

✓ Transformaciones.

✓ Almacenamiento.

✓ Reportes.

No escribas código.

Utiliza únicamente
una secuencia lógica.
"""

###########################################################
# EJERCICIO 3
###########################################################

"""
Analiza.

"Necesitamos un programa
para controlar inventario."

¿Qué información
consideras insuficiente?

¿Qué preguntas harías
antes de comenzar
el desarrollo?
"""

###########################################################
# EJERCICIO 4 (Difícil)
###########################################################

"""
Supón que eres
el Arquitecto de Software
de una compañía.

Debes diseñar
una plataforma ETL
que procese información
de 50 clientes diferentes.

Describe.

✓ Cómo comenzarías.

✓ Qué información recopilarías.

✓ Qué documentos crearías.

✓ Cómo dividirías
el proyecto.

✓ Qué riesgos identificarías.

No escribas código.

Piensa como
un Arquitecto de Software.
"""

"""
==========================================================
PYTHON MASTERS
BLOQUE 16 - BUENAS PRÁCTICAS Y DEBUGGING

Archivo:
16.3C_proyecto_profesional.py

PARTE 2 DE 4

Tema:
Construcción e Implementación de un Proyecto Profesional

Autor:
Comunidad de Ingeniería de Datos

==========================================================

OBJETIVOS

Al finalizar esta sección podrás:

✓ Transformar un diseño en un proyecto real.

✓ Organizar correctamente los módulos.

✓ Comprender el flujo completo de desarrollo.

✓ Aplicar buenas prácticas durante la implementación.

✓ Preparar un proyecto para mantenimiento futuro.

==========================================================
"""

###########################################################
# DEL DISEÑO AL CÓDIGO
###########################################################

"""
En la parte anterior aprendimos
que nunca debemos comenzar
escribiendo código.

Primero entendemos el problema.

Después diseñamos.

Ahora llega el momento
de implementar la solución.

La implementación consiste
en convertir el diseño
en software funcional.

Pero debemos hacerlo
de manera organizada.

No escribiendo todo
en un único archivo.
"""

###########################################################
# IMPLEMENTAR
# NO ES ESCRIBIR CÓDIGO
###########################################################

"""
Muchos desarrolladores creen que
implementar significa únicamente
programar.

En realidad implica mucho más.

✓ Crear la estructura.

✓ Organizar carpetas.

✓ Definir módulos.

✓ Configurar dependencias.

✓ Implementar funcionalidades.

✓ Escribir pruebas.

✓ Documentar.

Todo hace parte
de la implementación.
"""

###########################################################
# COMENZANDO EL PROYECTO
###########################################################

"""
Supongamos que construiremos
un sistema para procesar
ventas diarias.

Antes de crear funciones
debemos preparar
la estructura.

Ejemplo.

ventas_etl/

│

├── src/

├── tests/

├── config/

├── logs/

├── docs/

├── README.md

├── requirements.txt

└── main.py

Esta será nuestra base.
"""

###########################################################
# ¿QUÉ IMPLEMENTAR PRIMERO?
###########################################################

"""
Una excelente estrategia consiste
en construir primero
la estructura principal.

Después implementar
las funcionalidades.

No intentes construir
todo al mismo tiempo.

Avanza paso a paso.
"""

###########################################################
# DESARROLLO INCREMENTAL
###########################################################

"""
Los proyectos profesionales
se desarrollan
de manera incremental.

No esperamos
hasta terminar todo.

Construimos pequeñas partes.

Las probamos.

Las mejoramos.

Y continuamos.

Este enfoque reduce
la cantidad de errores.
"""

###########################################################
# EJEMPLO
###########################################################

"""
Proyecto ETL.

Primera iteración.

✓ Leer archivo.

-----------------------

Segunda iteración.

✓ Validar datos.

-----------------------

Tercera iteración.

✓ Transformar información.

-----------------------

Cuarta iteración.

✓ Guardar resultados.

Cada etapa
se valida antes
de continuar.
"""

###########################################################
# IMPLEMENTAR
# UNA RESPONSABILIDAD
# A LA VEZ
###########################################################

"""
Evita desarrollar
varias funcionalidades
simultáneamente.

Por ejemplo.

Incorrecto.

Leer archivos.

Guardar datos.

Enviar correos.

Generar reportes.

Todo al mismo tiempo.

Correcto.

Finalizar completamente
una funcionalidad.

Probarla.

Documentarla.

Y continuar con la siguiente.
"""

###########################################################
# EL ARCHIVO main.py
###########################################################

"""
Muchos principiantes convierten
main.py
en el proyecto completo.

Eso es un error.

main.py debería actuar
como punto de entrada.

Su trabajo consiste
en coordinar.

No en implementar
toda la lógica.

Idealmente debería ser
un archivo pequeño.
"""

###########################################################
# EJEMPLO
###########################################################

"""
main.py

↓

Inicializa configuración.

↓

Inicializa Logging.

↓

Ejecuta servicios.

↓

Finaliza.

Toda la lógica real
vive en otros módulos.
"""

###########################################################
# MODULARIDAD
###########################################################

"""
La modularidad consiste
en dividir el proyecto
en piezas independientes.

Cada módulo resuelve
un problema específico.

Ejemplo.

lectura.py

↓

Lee archivos.

-----------------------

validacion.py

↓

Valida información.

-----------------------

transformacion.py

↓

Transforma datos.

-----------------------

carga.py

↓

Carga resultados.

Cada módulo puede mantenerse
de manera independiente.
"""

###########################################################
# DESARROLLAR
# FUNCIONES PEQUEÑAS
###########################################################

"""
Ya aprendimos este principio.

Ahora lo aplicaremos
a proyectos completos.

Cada función debería realizar
una tarea específica.

Esto facilita.

✓ Pruebas.

✓ Reutilización.

✓ Debugging.

✓ Mantenimiento.
"""

###########################################################
# EVITA DUPLICAR LÓGICA
###########################################################

"""
Durante la implementación
es muy común copiar
y pegar código.

Resiste esa tentación.

Si una funcionalidad
aparece varias veces,

convierte esa lógica
en una función
o una clase reutilizable.
"""

###########################################################
# IMPLEMENTA
# DE LO GENERAL
# A LO ESPECÍFICO
###########################################################

"""
Una buena estrategia consiste
en implementar primero
los componentes principales.

Por ejemplo.

Configuración.

↓

Logging.

↓

Lectura.

↓

Procesamiento.

↓

Salida.

No comiences
por pequeños detalles.
"""

###########################################################
# PRUEBAS DURANTE
# EL DESARROLLO
###########################################################

"""
No esperes
hasta terminar
todo el proyecto.

Prueba continuamente.

Después de cada módulo.

Después de cada función.

Después de cada cambio importante.

Mientras más pronto descubras
un error,

más barato será corregirlo.
"""

###########################################################
# EL USO DEL CONTROL
# DE VERSIONES
###########################################################

"""
Todo proyecto profesional
debería utilizar
un sistema de control
de versiones.

El más utilizado es Git.

¿Por qué?

Permite.

✓ Registrar cambios.

✓ Recuperar versiones.

✓ Trabajar en equipo.

✓ Revisar código.

✓ Integrar funcionalidades.

Git forma parte
del desarrollo profesional.
"""

###########################################################
# COMMITS PEQUEÑOS
###########################################################

"""
Evita realizar
un único commit
con miles de cambios.

Es preferible realizar
commits pequeños.

Ejemplo.

✓ Agregar lectura CSV.

✓ Implementar validaciones.

✓ Corregir bug de fechas.

✓ Agregar Logging.

Cada commit
debe representar
una mejora concreta.
"""

###########################################################
# MENSAJES DE COMMIT
###########################################################

"""
Un buen commit
debe explicar
qué cambió.

Ejemplos.

Agregar validación
de clientes duplicados.

Implementar carga
de archivos Excel.

Corregir cálculo
de impuestos.

Evita mensajes como.

Cambios.

Corrección.

Versión nueva.

No aportan información.
"""

###########################################################
# DOCUMENTAR
# MIENTRAS DESARROLLAS
###########################################################

"""
La documentación
no debe escribirse
únicamente al final.

Cada vez que agregues
una funcionalidad importante.

Actualiza.

✓ README.

✓ Diagramas.

✓ Manuales.

✓ Comentarios.

Esto evita olvidar
información importante.
"""

###########################################################
# REVISIÓN CONTINUA
###########################################################

"""
Antes de considerar
una funcionalidad terminada
pregúntate.

✓ ¿Funciona?

✓ ¿Está documentada?

✓ ¿Tiene Logging?

✓ ¿Sigue las buenas prácticas?

✓ ¿Puede reutilizarse?

✓ ¿El código es legible?

Solo entonces
continúa con
la siguiente tarea.
"""

###########################################################
# CASO REAL
###########################################################

"""
Supongamos un proyecto ETL.

Primera semana.

✓ Estructura.

✓ Configuración.

✓ Logging.

Segunda semana.

✓ Lectura.

✓ Validaciones.

Tercera semana.

✓ Transformaciones.

Cuarta semana.

✓ Carga.

✓ Reportes.

Cada semana
produce un incremento
funcional del proyecto.
"""

###########################################################
# ERRORES COMUNES
###########################################################

"""
ERROR 1

Programar todo
en main.py.

------------------------------------

ERROR 2

No probar
durante el desarrollo.

------------------------------------

ERROR 3

Duplicar código.

------------------------------------

ERROR 4

No utilizar Git.

------------------------------------

ERROR 5

Realizar commits gigantes.

------------------------------------

ERROR 6

Documentar únicamente
al finalizar.

------------------------------------

ERROR 7

Implementar demasiadas
funcionalidades al mismo tiempo.
"""

###########################################################
# BUENAS PRÁCTICAS
###########################################################

"""
✓ Desarrolla por etapas.

✓ Implementa una responsabilidad
a la vez.

✓ Mantén módulos pequeños.

✓ Utiliza Git.

✓ Realiza commits frecuentes.

✓ Prueba continuamente.

✓ Documenta durante el desarrollo.

✓ Mantén el proyecto organizado.

✓ Reutiliza código.

✓ Evita duplicaciones.
"""

###########################################################
# TIPS PROFESIONALES
###########################################################

"""
TIP 1

Los mejores proyectos
crecen poco a poco.

No aparecen terminados
de un día para otro.

------------------------------------

TIP 2

Si una funcionalidad
no puede probarse
de forma independiente,

probablemente sea demasiado grande.

------------------------------------

TIP 3

Un commit debe contar
una pequeña historia.

No toda la historia
del proyecto.

------------------------------------

TIP 4

Nunca sacrifiques
la organización
por desarrollar
más rápido.

La deuda técnica
siempre termina cobrando intereses.

------------------------------------

TIP 5

Desarrollar despacio
pero correctamente
suele ser más rápido
que corregir cientos de errores
al final.
"""

###########################################################
# EJERCICIO 1
###########################################################

"""
Diseña el orden
en que implementarías
un sistema de facturación.

Incluye.

✓ Configuración.

✓ Base de datos.

✓ Clientes.

✓ Facturas.

✓ Reportes.

Justifica el orden elegido.
"""

###########################################################
# EJERCICIO 2
###########################################################

"""
Observa el siguiente proyecto.

main.py

↓

2.800 líneas.

¿Qué problemas
podrían aparecer?

¿Cómo comenzarías
a reorganizarlo?
"""

###########################################################
# EJERCICIO 3
###########################################################

"""
Escribe cinco ejemplos
de buenos mensajes
de commit.

Todos deben describir
cambios diferentes
en un proyecto Python.
"""

###########################################################
# EJERCICIO 4 (Difícil)
###########################################################

"""
Supón que lideras
un equipo de cinco desarrolladores.

Deben construir
un pipeline de datos.

Diseña un plan
de implementación
por etapas.

Indica.

✓ Qué desarrollar primero.

✓ Qué módulos crear.

✓ Cómo dividir el trabajo.

✓ Cuándo realizar pruebas.

✓ Cuándo integrar cambios.

No escribas código.

Piensa como
un Tech Lead.
"""

"""
==========================================================
PYTHON MASTERS
BLOQUE 16 - BUENAS PRÁCTICAS Y DEBUGGING

Archivo:
16.3C_proyecto_profesional.py

PARTE 3 DE 4

Tema:
Preparando un Proyecto para Producción

Autor:
Comunidad de Ingeniería de Datos

==========================================================

OBJETIVOS

Al finalizar esta sección podrás:

✓ Comprender qué significa que un proyecto
  esté listo para producción.

✓ Aplicar buenas prácticas antes del despliegue.

✓ Integrar pruebas, Logging y manejo de errores.

✓ Preparar un proyecto para trabajo en equipo.

✓ Comprender el concepto de deuda técnica.

==========================================================
"""

###########################################################
# ¿QUÉ SIGNIFICA
# "PASAR A PRODUCCIÓN"?
###########################################################

"""
Durante el desarrollo
trabajamos en un ambiente
controlado.

Podemos modificar código.

Podemos reiniciar el programa.

Podemos corregir errores.

Pero cuando un proyecto
llega a producción,

será utilizado por usuarios reales.

Cada error puede significar:

✓ Pérdida de dinero.

✓ Pérdida de información.

✓ Clientes insatisfechos.

✓ Interrupciones del servicio.

Por eso un proyecto
debe prepararse cuidadosamente
antes de ser publicado.
"""

###########################################################
# ¿CUÁNDO ESTÁ LISTO
# UN PROYECTO?
###########################################################

"""
Muchos desarrolladores responden:

"Cuando funciona."

En realidad esa respuesta
es insuficiente.

Un proyecto profesional
está listo cuando:

✓ Funciona.

✓ Está probado.

✓ Está documentado.

✓ Tiene Logging.

✓ Maneja errores.

✓ Puede mantenerse.

✓ Puede escalar.

✓ Puede ser utilizado
por otros desarrolladores.
"""

###########################################################
# CHECKLIST DE PRODUCCIÓN
###########################################################

"""
Antes de desplegar un proyecto
deberíamos responder.

✓ ¿El código funciona?

✓ ¿Las pruebas pasan?

✓ ¿La documentación está actualizada?

✓ ¿Las credenciales están protegidas?

✓ ¿Existe Logging?

✓ ¿Se manejan excepciones?

✓ ¿Existe configuración por ambientes?

✓ ¿El proyecto puede instalarse?

✓ ¿El README está actualizado?

Si alguna respuesta es "No",

probablemente todavía
no sea momento
de desplegar.
"""

###########################################################
# PRUEBAS
###########################################################

"""
Un proyecto profesional
debe probarse.

No solamente
ejecutarse una vez.

Debemos comprobar.

✓ Casos normales.

✓ Casos límite.

✓ Datos incorrectos.

✓ Entradas vacías.

✓ Errores esperados.

Mientras más pruebas existan,

mayor confianza tendremos
en el sistema.
"""

###########################################################
# EJEMPLO
###########################################################

"""
Supongamos una función
que calcula descuentos.

No basta con probar:

100

También debemos probar.

0

Valores negativos.

Valores muy grandes.

Valores nulos.

Solo así podremos confiar
en la implementación.
"""

###########################################################
# LOGGING
###########################################################

"""
Antes de producción
todo proyecto debería registrar.

Inicio.

Fin.

Advertencias.

Errores.

Tiempo de ejecución.

Eventos importantes.

Recuerda.

En producción
no tendremos un debugger.

Los logs serán
nuestra principal herramienta.
"""

###########################################################
# MANEJO DE EXCEPCIONES
###########################################################

"""
Ningún proyecto profesional
debería finalizar
inesperadamente.

Las excepciones deben:

✓ Capturarse.

✓ Registrarse.

✓ Informarse correctamente.

✓ Permitir una recuperación
cuando sea posible.

El usuario nunca debería
ver un traceback técnico.
"""

###########################################################
# CONFIGURACIÓN
###########################################################

"""
Un mismo proyecto
puede ejecutarse
en diferentes ambientes.

Desarrollo.

↓

Pruebas.

↓

Producción.

Cada ambiente
puede utilizar.

✓ Bases de datos distintas.

✓ APIs distintas.

✓ Credenciales distintas.

Por eso la configuración
debe estar separada
del código.
"""

###########################################################
# VARIABLES DE ENTORNO
###########################################################

"""
Nunca almacenes
información sensible
dentro del código.

Ejemplos.

✗ Contraseñas.

✗ Tokens.

✗ API Keys.

✗ Cadenas de conexión.

Utiliza siempre
variables de entorno.

Esto mejora:

✓ Seguridad.

✓ Mantenimiento.

✓ Despliegue.
"""

###########################################################
# DOCUMENTACIÓN
###########################################################

"""
Antes de entregar
un proyecto,

pregúntate.

¿Otra persona podría
instalarlo sin mi ayuda?

Si la respuesta es no,

la documentación
necesita mejorar.

Recuerda.

Un README completo
ahorra muchas horas
de soporte.
"""

###########################################################
# CALIDAD DEL CÓDIGO
###########################################################

"""
Antes de desplegar.

Revisa.

✓ Nombres.

✓ Organización.

✓ Duplicación.

✓ Funciones grandes.

✓ Variables ambiguas.

✓ Comentarios.

✓ PEP 8.

Una pequeña revisión
puede evitar muchos problemas.
"""

###########################################################
# DEUDA TÉCNICA
###########################################################

"""
Uno de los conceptos
más importantes
del desarrollo profesional.

La deuda técnica aparece
cuando tomamos atajos.

Por ejemplo.

"No importa,
después lo arreglamos."

Muchas veces
ese "después"
nunca llega.

Con el tiempo
el proyecto
se vuelve cada vez
más difícil
de mantener.
"""

###########################################################
# EJEMPLOS
###########################################################

"""
Ejemplos
de deuda técnica.

✓ Código duplicado.

✓ Variables ambiguas.

✓ Funciones gigantes.

✓ Sin documentación.

✓ Sin pruebas.

✓ Sin Logging.

✓ Sin manejo de errores.

Todo funciona.

Pero el mantenimiento
se vuelve muy costoso.
"""

###########################################################
# CÓMO REDUCIR
# LA DEUDA TÉCNICA
###########################################################

"""
Algunas estrategias.

✓ Refactorizar continuamente.

✓ Documentar.

✓ Escribir pruebas.

✓ Realizar Code Reviews.

✓ Mantener módulos pequeños.

✓ Eliminar código muerto.

✓ Corregir problemas
antes de agregar
nuevas funcionalidades.
"""

###########################################################
# CODE REVIEW
###########################################################

"""
Antes de integrar cambios,

otro desarrollador
debería revisar.

No para encontrar culpables.

Sino para mejorar
la calidad del software.

Durante una revisión
normalmente se analizan.

✓ Arquitectura.

✓ Legibilidad.

✓ Seguridad.

✓ Rendimiento.

✓ Buenas prácticas.
"""

###########################################################
# DESPLIEGUE
###########################################################

"""
El despliegue consiste
en publicar el proyecto
para que otros usuarios
puedan utilizarlo.

Antes de desplegar.

Realiza.

✓ Pruebas.

✓ Validaciones.

✓ Respaldo.

✓ Revisión.

Nunca despliegues
cambios
que no han sido probados.
"""

###########################################################
# MONITOREO
###########################################################

"""
Después del despliegue
el trabajo no termina.

Ahora debemos monitorear.

✓ Logs.

✓ Rendimiento.

✓ Errores.

✓ Consumo de recursos.

✓ Uso del sistema.

El monitoreo permite detectar
problemas rápidamente.
"""

###########################################################
# CASO REAL
###########################################################

"""
Supongamos un ETL.

Antes de producción.

✓ Se ejecuta localmente.

✓ Se prueban archivos pequeños.

✓ Se prueban archivos grandes.

✓ Se generan logs.

✓ Se documenta.

✓ Se revisa el código.

✓ Se despliega.

Después.

Se monitorean
las primeras ejecuciones.

Así trabajan
muchas compañías.
"""

###########################################################
# ERRORES COMUNES
###########################################################

"""
ERROR 1

Desplegar
sin pruebas.

------------------------------------

ERROR 2

No utilizar Logging.

------------------------------------

ERROR 3

Guardar contraseñas
en el código.

------------------------------------

ERROR 4

No documentar.

------------------------------------

ERROR 5

Ignorar
la deuda técnica.

------------------------------------

ERROR 6

No monitorear
el sistema.

------------------------------------

ERROR 7

Modificar producción
directamente.
"""

###########################################################
# CHECKLIST FINAL
###########################################################

"""
Antes de producción.

□ Código probado.

□ Logging configurado.

□ Manejo de errores.

□ README actualizado.

□ Dependencias documentadas.

□ Variables de entorno.

□ Configuración correcta.

□ Pruebas exitosas.

□ Código revisado.

□ Documentación actualizada.

□ Seguridad validada.

□ Arquitectura revisada.
"""

###########################################################
# BUENAS PRÁCTICAS
###########################################################

"""
✓ Automatiza pruebas.

✓ Automatiza despliegues.

✓ Documenta continuamente.

✓ Monitorea producción.

✓ Reduce deuda técnica.

✓ Utiliza Code Reviews.

✓ Mantén alta calidad.

✓ Nunca publiques
código sin probar.
"""

###########################################################
# TIPS PROFESIONALES
###########################################################

"""
TIP 1

Un proyecto exitoso
no es el que tiene
más funcionalidades.

Es el que puede mantenerse
durante años.

------------------------------------

TIP 2

Cada despliegue
debe poder revertirse.

Nunca publiques cambios
sin una estrategia
de recuperación.

------------------------------------

TIP 3

La deuda técnica
crece silenciosamente.

Atiéndela
de manera continua.

------------------------------------

TIP 4

Las pruebas
deben generar confianza.

No únicamente
cumplir un requisito.

------------------------------------

TIP 5

Una buena documentación
es una inversión
para todo el equipo.
"""

###########################################################
# EJERCICIO 1
###########################################################

"""
Diseña un checklist
para publicar
una API REST.

Incluye al menos
15 verificaciones.

Piensa en.

✓ Seguridad.

✓ Logging.

✓ Rendimiento.

✓ Documentación.

✓ Configuración.
"""

###########################################################
# EJERCICIO 2
###########################################################

"""
Un proyecto funciona
correctamente.

Pero no tiene.

✓ README.

✓ Logging.

✓ Pruebas.

✓ Variables de entorno.

¿Lo publicarías?

Justifica
tu respuesta.
"""

###########################################################
# EJERCICIO 3
###########################################################

"""
Identifica ejemplos
de deuda técnica
que hayas visto
durante este curso.

Explica por qué
representan un riesgo.
"""

###########################################################
# EJERCICIO 4 (Difícil)
###########################################################

"""
Supón que debes preparar
un pipeline empresarial
para producción.

Describe paso a paso.

✓ Qué validarías.

✓ Qué documentos revisarías.

✓ Qué pruebas ejecutarías.

✓ Qué métricas monitorearías.

✓ Cómo confirmarías
que el despliegue
fue exitoso.

No escribas código.

Piensa como
un Arquitecto de Datos.
"""

"""
==========================================================
PYTHON MASTERS
BLOQUE 16 - BUENAS PRÁCTICAS Y DEBUGGING

Archivo:
16.3C_proyecto_profesional.py

PARTE 4 DE 4

Tema:
Proyecto Profesional Integrador y Crecimiento como Desarrollador

Autor:
Comunidad de Ingeniería de Datos

==========================================================

OBJETIVOS

Al finalizar esta sección podrás:

✓ Integrar todos los conocimientos del curso.

✓ Comprender el ciclo completo de un proyecto.

✓ Conocer el flujo de trabajo de un equipo
  profesional.

✓ Prepararte para entrevistas técnicas.

✓ Definir un plan de crecimiento como
  desarrollador Python.

==========================================================
"""

###########################################################
# EL PROYECTO TERMINÓ...
# ¿Y AHORA QUÉ?
###########################################################

"""
Muchos estudiantes creen que
cuando el programa funciona
el proyecto ha terminado.

En realidad,
ese suele ser únicamente
el comienzo.

Ahora llegan nuevas etapas.

✓ Soporte.

✓ Corrección de errores.

✓ Nuevas funcionalidades.

✓ Optimización.

✓ Actualizaciones.

✓ Mantenimiento.

La mayor parte del tiempo
de vida de un proyecto
se dedica al mantenimiento.
"""

###########################################################
# EL CICLO COMPLETO
###########################################################

"""
Durante este curso recorrimos
el mismo camino
que sigue un proyecto real.

Problema

↓

Análisis

↓

Diseño

↓

Organización

↓

Implementación

↓

Pruebas

↓

Debugging

↓

Logging

↓

Documentación

↓

Despliegue

↓

Monitoreo

↓

Mantenimiento

Ese es el ciclo de vida
de la mayoría
de proyectos profesionales.
"""

###########################################################
# TODO ESTÁ CONECTADO
###########################################################

"""
Observa cómo todos los temas
del curso trabajan juntos.

Variables

↓

Funciones

↓

Módulos

↓

Paquetes

↓

POO

↓

Archivos

↓

Excepciones

↓

Debugging

↓

Logging

↓

Buenas prácticas

↓

Proyecto profesional

Cada bloque fue preparando
el siguiente.

Nada fue enseñado
por casualidad.
"""

###########################################################
# EL FLUJO DE UN EQUIPO
###########################################################

"""
En una empresa
el trabajo normalmente
se desarrolla así.

Analista

↓

Arquitecto

↓

Desarrolladores

↓

QA

↓

DevOps

↓

Producción

Cada integrante
cumple un papel diferente.

Comprender ese flujo
facilita el trabajo
en equipo.
"""

###########################################################
# TRABAJANDO EN EQUIPO
###########################################################

"""
Un buen desarrollador
no solamente escribe código.

También sabe.

✓ Escuchar.

✓ Comunicar.

✓ Documentar.

✓ Preguntar.

✓ Compartir conocimiento.

✓ Revisar código.

Las habilidades técnicas
y las habilidades personales
son igualmente importantes.
"""

###########################################################
# LA IMPORTANCIA
# DE LA DOCUMENTACIÓN
###########################################################

"""
Imagina que mañana
cambias de proyecto.

Otro desarrollador
continuará tu trabajo.

¿Qué encontrará?

Si existe documentación,

la transición será sencilla.

Si no existe,

el equipo perderá
muchas horas
intentando comprender
el sistema.

Documentar
es una responsabilidad
profesional.
"""

###########################################################
# EL VALOR
# DE LAS PRUEBAS
###########################################################

"""
Cada nueva funcionalidad
puede romper
una funcionalidad existente.

Por eso las pruebas
acompañan
todo el desarrollo.

Ellas nos brindan
confianza para evolucionar
el software
sin miedo.
"""

###########################################################
# EL VALOR
# DEL LOGGING
###########################################################

"""
Durante el desarrollo.

↓

Debugger.

En producción.

↓

Logging.

Ambas herramientas
trabajan juntas.

El Debugger ayuda
a encontrar problemas.

El Logging ayuda
a comprender
qué ocurrió
cuando el sistema
ya está funcionando.
"""

###########################################################
# EL VALOR
# DE LAS BUENAS PRÁCTICAS
###########################################################

"""
Las buenas prácticas
no existen
para hacer el código
más bonito.

Existen para disminuir.

✓ Errores.

✓ Tiempo de mantenimiento.

✓ Costos.

✓ Riesgos.

Cada pequeña mejora
se multiplica
durante toda la vida
del proyecto.
"""

###########################################################
# EL PORTAFOLIO
###########################################################

"""
Uno de los mejores recursos
para un desarrollador
es un buen portafolio.

No basta con decir:

"Sé Python."

Es mejor demostrarlo.

Construye proyectos reales.

Publica el código.

Documenta.

Escribe README.

Utiliza Git.

Eso habla mucho mejor
de tus habilidades.
"""

###########################################################
# PREPARÁNDOTE
# PARA UNA ENTREVISTA
###########################################################

"""
Muchas entrevistas
no buscan únicamente
conocimiento técnico.

También evalúan
cómo piensas.

Algunas preguntas comunes.

¿Cómo organizas
un proyecto?

¿Cómo depuras un error?

¿Cómo manejas excepciones?

¿Cómo documentas?

¿Cómo realizas pruebas?

Todo eso
lo hemos estudiado
durante este curso.
"""

###########################################################
# QUÉ ESPERA UNA EMPRESA
###########################################################

"""
Generalmente una empresa
espera que un desarrollador
pueda.

✓ Leer código existente.

✓ Comprender requisitos.

✓ Escribir código limpio.

✓ Corregir errores.

✓ Trabajar con Git.

✓ Colaborar en equipo.

✓ Documentar.

✓ Aprender continuamente.

La sintaxis
es solo una parte
del trabajo.
"""

###########################################################
# APRENDER NUNCA TERMINA
###########################################################

"""
Python evoluciona constantemente.

También lo hacen.

✓ Librerías.

✓ Frameworks.

✓ Herramientas.

✓ Arquitecturas.

Un desarrollador profesional
mantiene una actitud
de aprendizaje continuo.

Nunca dejamos
de aprender.
"""

###########################################################
# POSIBLES CAMINOS
###########################################################

"""
Después de dominar Python
puedes especializarte en.

✓ Data Engineering.

✓ Ciencia de Datos.

✓ Inteligencia Artificial.

✓ Machine Learning.

✓ Desarrollo Backend.

✓ Automatización.

✓ DevOps.

✓ Ciberseguridad.

✓ Cloud Computing.

Python abre la puerta
a muchas áreas.
"""

###########################################################
# ENFOQUE PARA
# DATA ENGINEERING
###########################################################

"""
Si tu objetivo es
la Ingeniería de Datos,
el siguiente paso consiste
en dominar herramientas como.

✓ SQL.

✓ Apache Spark.

✓ Databricks.

✓ Airflow.

✓ Azure Data Factory.

✓ Kafka.

✓ Docker.

✓ Git.

✓ Cloud.

Python será
la base sobre la cual
construirás
todas esas habilidades.
"""

###########################################################
# CÓMO SEGUIR MEJORANDO
###########################################################

"""
Algunas recomendaciones.

Lee código.

Construye proyectos.

Participa en comunidades.

Resuelve problemas.

Realiza Code Reviews.

Aprende de otros.

No memorices.

Comprende.

La experiencia
se construye programando.
"""

###########################################################
# EL VERDADERO OBJETIVO
###########################################################

"""
El objetivo del curso
nunca fue memorizar sintaxis.

El objetivo fue desarrollar
la capacidad de resolver problemas.

Un buen desarrollador
no conoce todas las respuestas.

Sabe cómo encontrarlas.

Sabe investigar.

Sabe analizar.

Sabe aprender.
"""

###########################################################
# PROYECTO FINAL
###########################################################

"""
Como proyecto integrador
de Python Masters
podrías construir una aplicación
que reúna la mayoría
de los conceptos vistos.

Ejemplo.

Sistema de procesamiento
de archivos.

Debe incluir.

✓ Organización profesional.

✓ Funciones.

✓ Clases.

✓ Archivos.

✓ Excepciones.

✓ Logging.

✓ Configuración.

✓ Variables de entorno.

✓ Documentación.

✓ README.

✓ Git.

✓ Buenas prácticas.

✓ Pruebas.

✓ Manejo de errores.

✓ Modularidad.

Este proyecto representará
tu nivel como desarrollador.
"""

###########################################################
# RETO PYTHON MASTERS
###########################################################

"""
Imagina que acabas
de ser contratado
como Data Engineer.

Debes desarrollar
una plataforma que.

✓ Reciba archivos.

✓ Valide información.

✓ Transforme datos.

✓ Cargue resultados.

✓ Genere reportes.

✓ Registre Logs.

✓ Maneje errores.

✓ Permita configuración
por ambiente.

✓ Sea mantenible.

✓ Sea escalable.

Diseña completamente
el proyecto.

Incluye.

✓ Arquitectura.

✓ Carpetas.

✓ Módulos.

✓ Flujo.

✓ Logging.

✓ Configuración.

✓ Buenas prácticas.

✓ Estrategia de pruebas.

✓ Documentación.

No escribas código.

Diseña la solución
como si fueras
el Arquitecto Principal.
"""

###########################################################
# CHECKLIST DEL
# DESARROLLADOR PYTHON
###########################################################

"""
Antes de considerar
terminado un proyecto,
pregúntate.

□ ¿Comprendí el problema?

□ ¿La solución está documentada?

□ ¿El código es legible?

□ ¿Existe duplicación?

□ ¿Las funciones son pequeñas?

□ ¿El proyecto está organizado?

□ ¿Existe Logging?

□ ¿Se manejan excepciones?

□ ¿Las pruebas funcionan?

□ ¿Las dependencias están documentadas?

□ ¿Las credenciales están protegidas?

□ ¿El README está actualizado?

□ ¿El proyecto puede crecer?

□ ¿Otro desarrollador
podría continuar el trabajo?

Si todas las respuestas
son afirmativas,

estás muy cerca
de un proyecto profesional.
"""

###########################################################
# MENSAJE FINAL
###########################################################

"""
Llegar hasta este punto
significa que has recorrido
todo el camino fundamental
del lenguaje Python.

Ahora conoces.

✓ La sintaxis.

✓ Las estructuras de datos.

✓ La programación orientada
  a objetos.

✓ El manejo de archivos.

✓ El manejo de errores.

✓ El Debugging.

✓ El Logging.

✓ Las buenas prácticas.

✓ La organización
  de proyectos.

✓ El desarrollo profesional.

Pero recuerda.

Aprender un lenguaje
no te convierte
automáticamente
en un desarrollador experto.

La experiencia
se construye desarrollando
proyectos reales.

Cada proyecto nuevo
te enseñará algo
que ningún libro puede enseñar.

Sigue construyendo.

Sigue aprendiendo.

Sigue compartiendo conocimiento.

Ese es el camino
de un verdadero profesional.
"""

###########################################################
# RESUMEN GENERAL
# DEL BLOQUE 16
###########################################################

"""
Durante el Bloque 16 aprendiste:

✓ Fundamentos del Debugging.

✓ Herramientas de depuración.

✓ Breakpoints.

✓ Variables.

✓ Call Stack.

✓ Stack Trace.

✓ Logging profesional.

✓ Niveles de Logging.

✓ Logging en producción.

✓ Buenas prácticas.

✓ Clean Code.

✓ DRY.

✓ KISS.

✓ YAGNI.

✓ Responsabilidad única.

✓ PEP 8.

✓ Zen of Python.

✓ Organización profesional.

✓ Arquitectura de proyectos.

✓ Variables de entorno.

✓ Configuración.

✓ Git.

✓ README.

✓ requirements.txt.

✓ __init__.py.

✓ Desarrollo profesional.

✓ Preparación para producción.

✓ Proyecto integrador.

###########################################################
# FIN DEL CURSO PYTHON MASTERS
###########################################################

"""