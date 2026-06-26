"""
==========================================================
PYTHON MASTERS
BLOQUE 16 - BUENAS PRÁCTICAS Y DEBUGGING

Archivo:
16.3B_organizacion_proyectos.py

PARTE 1 DE 3

Tema:
Organización Profesional de Proyectos en Python

Autor:
Comunidad de Ingeniería de Datos

==========================================================

OBJETIVOS

Al finalizar esta sección podrás:

✓ Comprender por qué es importante
  organizar correctamente un proyecto.

✓ Diferenciar un script de un proyecto.

✓ Conocer la estructura típica de un
  proyecto profesional en Python.

✓ Comprender el propósito de carpetas
  y módulos.

✓ Aplicar buenas prácticas para organizar
  proyectos escalables.

==========================================================
"""

###########################################################
# ¿POR QUÉ HABLAR DE ORGANIZACIÓN?
###########################################################

"""
Durante los primeros bloques del curso
hemos trabajado con archivos pequeños.

Por ejemplo.

variables.py

funciones.py

listas.py

Todo funciona correctamente.

Pero...

¿Qué ocurre cuando un proyecto tiene:

✓ 50 archivos?

✓ 120 módulos?

✓ 20 desarrolladores?

✓ 5 años de evolución?

Sin organización,
el proyecto se vuelve muy difícil
de mantener.

Una buena arquitectura comienza
con una buena organización.
"""

###########################################################
# SCRIPT VS PROYECTO
###########################################################

"""
Muchos estudiantes creen que son
lo mismo.

No lo son.

Un script normalmente:

✓ Tiene un único archivo.

✓ Resuelve una tarea específica.

✓ Tiene poca reutilización.

✓ Es pequeño.

Un proyecto:

✓ Tiene múltiples módulos.

✓ Está organizado por carpetas.

✓ Es reutilizable.

✓ Puede crecer durante años.

La organización cambia completamente.
"""

###########################################################
# EJEMPLO DE SCRIPT
###########################################################

"""
calculadora.py

----------------------

def sumar():

...

def restar():

...

def dividir():

...

def multiplicar():

...

print(...)

----------------------

Todo vive
en un único archivo.

Para aprender está bien.

Para un proyecto empresarial,
no.
"""

###########################################################
# EJEMPLO DE PROYECTO
###########################################################

"""
calculadora/

│

├── main.py

├── operaciones.py

├── utilidades.py

├── configuracion.py

├── constantes.py

└── tests/

Ya existe una separación
de responsabilidades.

Encontrar una funcionalidad
es mucho más sencillo.
"""

###########################################################
# LA IMPORTANCIA DE
# LAS CARPETAS
###########################################################

"""
Las carpetas permiten agrupar
elementos relacionados.

Por ejemplo.

clientes/

facturas/

productos/

usuarios/

configuracion/

Cada carpeta representa
un dominio del negocio.

Esto facilita la navegación
del proyecto.
"""

###########################################################
# PENSAR COMO UNA EMPRESA
###########################################################

"""
Imagina que trabajas
en un banco.

El proyecto tiene:

1.500 archivos.

Si todos estuvieran
en la misma carpeta,

sería prácticamente imposible
encontrar algo.

La organización reduce
la complejidad.
"""

###########################################################
# UNA CARPETA DEBE
# TENER UN PROPÓSITO
###########################################################

"""
No crees carpetas
porque sí.

Cada carpeta debe responder
una pregunta.

¿Qué tipo de archivos
almacena?

Ejemplos.

config/

Archivos de configuración.

--------------------------------

logs/

Archivos de log.

--------------------------------

tests/

Pruebas.

--------------------------------

docs/

Documentación.

--------------------------------

src/

Código fuente.

Todo tiene un lugar.
"""

###########################################################
# EL CONCEPTO DE MÓDULO
###########################################################

"""
Ya aprendimos que:

Cada archivo .py

es un módulo.

Por ejemplo.

clientes.py

productos.py

ventas.py

Cada módulo debería tener
una responsabilidad clara.

No mezclar funcionalidades.
"""

###########################################################
# MAL EJEMPLO
###########################################################

"""
utilidades.py

Contiene.

✓ Base de datos.

✓ API.

✓ Funciones matemáticas.

✓ Correos.

✓ Seguridad.

✓ Reportes.

✓ Validaciones.

Todo mezclado.

Con el tiempo
este archivo crecerá
enormemente.

Será muy difícil
de mantener.
"""

###########################################################
# BUEN EJEMPLO
###########################################################

"""
database.py

↓

Conexiones.

------------------------

email.py

↓

Correos.

------------------------

validaciones.py

↓

Validaciones.

------------------------

reportes.py

↓

Generación de reportes.

Cada módulo tiene
una responsabilidad.
"""

###########################################################
# SEPARACIÓN DE RESPONSABILIDADES
###########################################################

"""
Este concepto aparece
constantemente
en Ingeniería de Software.

Cada módulo debe encargarse
de una única área.

No mezclar.

Base de datos

con

Interfaz gráfica.

No mezclar.

Configuración

con

Lógica de negocio.

Mientras mayor sea
la separación,

más sencillo será
mantener el proyecto.
"""

###########################################################
# EJEMPLO
###########################################################

"""
Proyecto.

Tienda Online

Podríamos tener.

clientes/

productos/

ventas/

pagos/

inventario/

reportes/

Cada módulo representa
un proceso diferente
del negocio.
"""

###########################################################
# NOMBRES DE ARCHIVOS
###########################################################

"""
Los nombres también importan.

Malos ejemplos.

archivo1.py

nuevo.py

prueba.py

codigo.py

final.py

No describen
su contenido.

Buenos ejemplos.

clientes.py

facturas.py

inventario.py

autenticacion.py

configuracion.py

El nombre explica
el propósito.
"""

###########################################################
# EVITA ARCHIVOS GIGANTES
###########################################################

"""
Cuando un archivo
empieza a crecer demasiado,

es momento de dividirlo.

No existe un número exacto
de líneas.

Pero un archivo
de miles de líneas

normalmente indica
que varias responsabilidades
están mezcladas.
"""

###########################################################
# EJEMPLO
###########################################################

"""
clientes.py

120 líneas

↓

Muy fácil de leer.

----------------------------

clientes.py

3.500 líneas

↓

Difícil de navegar.

Difícil de revisar.

Difícil de mantener.

Probablemente
deba dividirse.
"""

###########################################################
# ORGANIZACIÓN
# POR FUNCIONALIDAD
###########################################################

"""
Existen muchas formas
de organizar un proyecto.

Una de las más utilizadas es:

Agrupar por funcionalidad.

Ejemplo.

clientes/

↓

Todo lo relacionado
con clientes.

No importa
si son consultas,
validaciones
o reportes.

Todo permanece
en el mismo dominio.
"""

###########################################################
# ORGANIZACIÓN
# POR CAPAS
###########################################################

"""
Otra estrategia muy utilizada.

Separar por capas.

Por ejemplo.

API

↓

Servicios

↓

Repositorio

↓

Base de datos

Cada capa
tiene una responsabilidad.

Más adelante
la estudiaremos
con detalle.
"""

###########################################################
# PENSAR EN EL FUTURO
###########################################################

"""
Cuando creamos
una carpeta
o un archivo,

debemos preguntarnos.

¿Cómo crecerá este proyecto?

No diseñes únicamente
para hoy.

Diseña para facilitar
el crecimiento futuro.
"""

###########################################################
# ERRORES COMUNES
###########################################################

"""
ERROR 1

Todo en un solo archivo.

------------------------------------

ERROR 2

Archivos con nombres ambiguos.

------------------------------------

ERROR 3

Carpetas sin propósito.

------------------------------------

ERROR 4

Duplicar módulos.

------------------------------------

ERROR 5

Mezclar responsabilidades.

------------------------------------

ERROR 6

Crear archivos gigantes.
"""

###########################################################
# BUENAS PRÁCTICAS
###########################################################

"""
✓ Organiza desde el inicio.

✓ Utiliza nombres claros.

✓ Separa responsabilidades.

✓ Divide archivos grandes.

✓ Agrupa funcionalidades.

✓ Mantén consistencia.

✓ Piensa en el crecimiento
del proyecto.
"""

###########################################################
# TIPS PROFESIONALES
###########################################################

"""
TIP 1

Es mucho más fácil
mantener una buena estructura
desde el principio
que reorganizar
un proyecto enorme.

------------------------------------

TIP 2

Si no sabes
dónde guardar un archivo,

probablemente
la estructura necesita
mejorarse.

------------------------------------

TIP 3

No diseñes pensando
en un desarrollador.

Diseña pensando
en un equipo.

------------------------------------

TIP 4

La organización
es una inversión.

Reduce tiempo
de mantenimiento
durante años.
"""

###########################################################
# EJERCICIO 1
###########################################################

"""
Actualmente tienes
un archivo llamado.

utilidades.py

Contiene.

✓ Conexión a SQL Server.

✓ Funciones matemáticas.

✓ Envío de correos.

✓ Validaciones.

¿Cómo lo dividirías?

No escribas código.

Diseña la nueva estructura.
"""

###########################################################
# EJERCICIO 2
###########################################################

"""
Diseña la estructura
de un proyecto
para una biblioteca.

Debe incluir módulos
para.

✓ Libros.

✓ Usuarios.

✓ Préstamos.

✓ Reportes.

✓ Configuración.

Piensa en carpetas
y archivos.
"""

###########################################################
# EJERCICIO 3 (Difícil)
###########################################################

"""
Imagina que ingresas
a una empresa.

El proyecto tiene
2.300 archivos.

Todos están
en la carpeta raíz.

Describe paso a paso
cómo comenzarías
a reorganizar
el proyecto.

No escribas código.

Piensa como
un Arquitecto de Software.
"""

"""
==========================================================
PYTHON MASTERS
BLOQUE 16 - BUENAS PRÁCTICAS Y DEBUGGING

Archivo:
16.3B_organizacion_proyectos.py

PARTE 2 DE 3

Tema:
Estructura Profesional de Proyectos Python

Autor:
Comunidad de Ingeniería de Datos

==========================================================

OBJETIVOS

Al finalizar esta sección podrás:

✓ Comprender la estructura típica de un
  proyecto profesional.

✓ Conocer el propósito de __init__.py.

✓ Entender para qué sirven README.md,
  requirements.txt y .gitignore.

✓ Comprender el uso de variables de entorno.

✓ Organizar correctamente archivos
  de configuración.

✓ Preparar un proyecto para trabajo
  colaborativo.

==========================================================
"""

###########################################################
# ¿CÓMO SE VE UN PROYECTO PROFESIONAL?
###########################################################

"""
Hasta ahora hemos trabajado con proyectos
muy pequeños.

Sin embargo, un proyecto empresarial suele
tener una estructura como esta.

mi_proyecto/

│

├── src/

├── tests/

├── docs/

├── logs/

├── config/

├── requirements.txt

├── README.md

├── .gitignore

├── .env

└── main.py

Cada elemento tiene
una responsabilidad específica.

Nada está ubicado al azar.
"""

###########################################################
# LA CARPETA src/
###########################################################

"""
src significa:

Source

o

Código fuente.

Su propósito es contener
todo el código de la aplicación.

Por ejemplo.

src/

│

├── clientes.py

├── productos.py

├── ventas.py

└── utilidades.py

Muchas empresas utilizan esta carpeta
para separar claramente el código
de otros recursos del proyecto.
"""

###########################################################
# LA CARPETA tests/
###########################################################

"""
Aquí se almacenan
las pruebas automatizadas.

Ejemplo.

tests/

│

├── test_clientes.py

├── test_productos.py

└── test_ventas.py

Nunca mezcles pruebas
con el código principal.

Mantenerlas separadas facilita
el mantenimiento.
"""

###########################################################
# LA CARPETA docs/
###########################################################

"""
Contiene la documentación.

Ejemplos.

✓ Manuales.

✓ Diagramas.

✓ Arquitectura.

✓ Guías de instalación.

✓ Casos de uso.

No toda la documentación
debe vivir dentro del código.
"""

###########################################################
# LA CARPETA logs/
###########################################################

"""
Aquí pueden almacenarse
los archivos generados
por el sistema de Logging.

Ejemplo.

logs/

│

├── aplicacion.log

├── errores.log

└── auditoria.log

Esto evita llenar
la carpeta principal
con archivos temporales.
"""

###########################################################
# LA CARPETA config/
###########################################################

"""
Su objetivo es almacenar
la configuración del proyecto.

Ejemplo.

config/

│

├── desarrollo.py

├── pruebas.py

└── produccion.py

Esto permite cambiar
el comportamiento
sin modificar
el código principal.
"""

###########################################################
# ¿QUÉ ES __init__.py?
###########################################################

"""
Una de las preguntas
más comunes.

¿Para qué sirve
__init__.py?

Este archivo indica
que una carpeta
debe comportarse
como un paquete Python.

Además permite.

✓ Inicializar paquetes.

✓ Exportar módulos.

✓ Ejecutar configuraciones.

✓ Simplificar importaciones.

En versiones modernas de Python
algunos paquetes funcionan
sin este archivo.

Sin embargo,
continúa siendo una excelente
práctica incluirlo.
"""

###########################################################
# EJEMPLO
###########################################################

"""
clientes/

│

├── __init__.py

├── modelos.py

├── servicios.py

└── validaciones.py

Ahora toda la carpeta
puede tratarse
como un paquete.
"""

###########################################################
# README.md
###########################################################

"""
Uno de los archivos
más importantes
de cualquier proyecto.

Es la puerta de entrada
para nuevos desarrolladores.

Un buen README responde.

✓ ¿Qué hace el proyecto?

✓ ¿Cómo instalarlo?

✓ ¿Cómo ejecutarlo?

✓ ¿Qué dependencias necesita?

✓ ¿Quién lo mantiene?

Nunca subestimes
la importancia
de un buen README.
"""

###########################################################
# ¿QUÉ DEBERÍA CONTENER
# UN README?
###########################################################

"""
Como mínimo.

✓ Nombre.

✓ Descripción.

✓ Requisitos.

✓ Instalación.

✓ Ejecución.

✓ Estructura.

✓ Ejemplos.

✓ Licencia.

✓ Autor.

Mientras más claro sea,
más fácil será comenzar
a trabajar en el proyecto.
"""

###########################################################
# requirements.txt
###########################################################

"""
Python utiliza librerías externas.

Por ejemplo.

pandas

numpy

requests

pytest

Todas ellas deberían registrarse
en un único archivo.

requirements.txt

Esto permite instalar
las dependencias
con un solo comando.

pip install -r requirements.txt
"""

###########################################################
# EJEMPLO
###########################################################

"""
requirements.txt

----------------------

pandas==2.2.3

numpy==2.1.1

requests==2.32.3

python-dotenv==1.0.1

pytest==8.3.3

----------------------

Cada proyecto
debe controlar
las versiones utilizadas.
"""

###########################################################
# ¿POR QUÉ FIJAR VERSIONES?
###########################################################

"""
Imagina que tú utilizas.

pandas 2.2

Y otro desarrollador utiliza.

pandas 3.0

Tal vez el código
ya no funcione igual.

Las versiones garantizan
que todos trabajen
con el mismo entorno.
"""

###########################################################
# .gitignore
###########################################################

"""
Git registra cambios
en los archivos.

Pero existen archivos
que nunca deberían
subirse al repositorio.

Por ejemplo.

✓ Logs.

✓ Entornos virtuales.

✓ Archivos temporales.

✓ Credenciales.

✓ Cache.

Para eso existe.

.gitignore
"""

###########################################################
# EJEMPLO
###########################################################

"""
.gitignore

----------------------

__pycache__/

*.pyc

.env

.venv/

logs/

*.log

----------------------

Git ignorará
esos archivos.
"""

###########################################################
# VARIABLES DE ENTORNO
###########################################################

"""
Muchos proyectos
necesitan información
confidencial.

Por ejemplo.

✓ Contraseñas.

✓ Tokens.

✓ URLs.

✓ Claves API.

Nunca deben escribirse
directamente
en el código.

Para ello utilizamos
variables de entorno.
"""

###########################################################
# MAL EJEMPLO
###########################################################

PASSWORD = "Admin123"

TOKEN = "ABC123XYZ"

"""
Este código
es un riesgo enorme.

Si llega al repositorio,

cualquier persona
podría verlo.
"""

###########################################################
# BUEN EJEMPLO
###########################################################

"""
.env

----------------------

DB_SERVER=localhost

DB_NAME=ventas

DB_USER=admin

DB_PASSWORD=********

API_KEY=********

----------------------

El código leerá
esas variables
sin exponerlas.
"""

###########################################################
# python-dotenv
###########################################################

"""
Una librería muy utilizada
es:

python-dotenv

Permite cargar automáticamente
las variables definidas
en el archivo .env.

Ejemplo.

from dotenv import load_dotenv

import os

load_dotenv()

usuario = os.getenv("DB_USER")

password = os.getenv("DB_PASSWORD")

Ahora las credenciales
no aparecen
en el código fuente.
"""

###########################################################
# CONFIGURACIÓN CENTRALIZADA
###########################################################

"""
Evita escribir configuraciones
en muchos archivos.

Mejor crea
un único módulo.

config.py

Allí podrás definir.

✓ URLs.

✓ Puertos.

✓ Rutas.

✓ Variables.

✓ Configuración general.

Esto facilita
el mantenimiento.
"""

###########################################################
# EJEMPLO
###########################################################

"""
config.py

----------------------

HOST = "localhost"

PORT = 8000

DEBUG = True

----------------------

Otros módulos simplemente
importan la configuración.
"""

###########################################################
# SEPARA CONFIGURACIÓN
# DEL CÓDIGO
###########################################################

"""
El código debería contener
la lógica del negocio.

La configuración
debe vivir aparte.

Esto facilita.

✓ Cambiar ambientes.

✓ Automatizar despliegues.

✓ Configurar producción.

✓ Configurar pruebas.

Sin modificar
la lógica del programa.
"""

###########################################################
# ERRORES COMUNES
###########################################################

"""
ERROR 1

Guardar contraseñas
en el código.

------------------------------------

ERROR 2

No utilizar README.

------------------------------------

ERROR 3

Olvidar requirements.txt.

------------------------------------

ERROR 4

Subir el entorno virtual
al repositorio.

------------------------------------

ERROR 5

No utilizar .gitignore.

------------------------------------

ERROR 6

Mezclar configuración
con lógica del negocio.
"""

###########################################################
# BUENAS PRÁCTICAS
###########################################################

"""
✓ Mantén un README actualizado.

✓ Versiona dependencias.

✓ Utiliza .gitignore.

✓ Utiliza .env.

✓ Centraliza la configuración.

✓ Organiza documentación.

✓ Separa pruebas.

✓ Utiliza paquetes Python.

✓ Mantén una estructura consistente.
"""

###########################################################
# TIPS PROFESIONALES
###########################################################

"""
TIP 1

Si un desarrollador nuevo
no puede ejecutar
el proyecto en pocos minutos,

la documentación
probablemente necesita mejorar.

------------------------------------

TIP 2

Nunca subas
credenciales
a Git.

Ni siquiera
en proyectos personales.

------------------------------------

TIP 3

Todo proyecto debería poder
instalarse únicamente con:

pip install -r requirements.txt

------------------------------------

TIP 4

El archivo README
es tan importante
como el propio código.

Muchas veces será
el primer archivo
que alguien leerá.
"""

###########################################################
# EJERCICIO 1
###########################################################

"""
Diseña un README
para un proyecto
de análisis de ventas.

Debe incluir.

✓ Descripción.

✓ Instalación.

✓ Ejecución.

✓ Dependencias.

✓ Autor.
"""

###########################################################
# EJERCICIO 2
###########################################################

"""
Analiza este proyecto.

main.py

clientes.py

ventas.py

config.py

README.md

¿Qué archivos
hacen falta
para convertirlo
en un proyecto profesional?
"""

###########################################################
# EJERCICIO 3
###########################################################

"""
Diseña un archivo
.gitignore

para un proyecto Python.

Incluye al menos
10 elementos
que deberían ignorarse.
"""

###########################################################
# EJERCICIO 4 (Difícil)
###########################################################

"""
Tu empresa almacena
las credenciales
directamente
en el código fuente.

Describe un plan
para migrar
todo el proyecto
a variables de entorno.

No escribas código.

Piensa como
un Arquitecto de Software.
"""

"""
==========================================================
PYTHON MASTERS
BLOQUE 16 - BUENAS PRÁCTICAS Y DEBUGGING

Archivo:
16.3B_organizacion_proyectos.py

PARTE 3 DE 3

Tema:
Arquitectura y Organización Profesional de Proyectos

Autor:
Comunidad de Ingeniería de Datos

==========================================================

OBJETIVOS

Al finalizar esta sección podrás:

✓ Comprender cómo se organiza un proyecto
  profesional en empresas.

✓ Entender la separación por capas.

✓ Diferenciar responsabilidades entre módulos.

✓ Comprender las importaciones en proyectos.

✓ Evitar dependencias circulares.

✓ Diseñar proyectos escalables y mantenibles.

==========================================================
"""

###########################################################
# ¿POR QUÉ EXISTE UNA ARQUITECTURA?
###########################################################

"""
Una aplicación pequeña puede funcionar
perfectamente con cinco archivos.

Pero...

¿Qué ocurre cuando el proyecto tiene:

✓ 30 desarrolladores?

✓ 10 microservicios?

✓ 250 módulos?

✓ Miles de usuarios?

Sin una arquitectura clara,
el proyecto se vuelve muy difícil
de mantener.

La arquitectura permite organizar
el software para que pueda crecer
durante años sin perder claridad.
"""

###########################################################
# ARQUITECTURA EN CAPAS
###########################################################

"""
Una de las organizaciones más utilizadas
en proyectos empresariales es la separación
por capas.

Visualmente podríamos representarla así.

Usuario

↓

API / Interfaz

↓

Servicios

↓

Repositorio

↓

Base de Datos

Cada capa tiene
una responsabilidad específica.

Una capa nunca debería hacer
el trabajo de otra.
"""

###########################################################
# CAPA DE PRESENTACIÓN
###########################################################

"""
Es la capa que interactúa
con el usuario.

Ejemplos.

✓ API REST

✓ Página Web

✓ Aplicación de escritorio

✓ Línea de comandos (CLI)

Su trabajo consiste en:

✓ Recibir solicitudes.

✓ Validar entradas básicas.

✓ Mostrar respuestas.

No debería contener
la lógica del negocio.
"""

###########################################################
# CAPA DE SERVICIOS
###########################################################

"""
Aquí vive
la lógica del negocio.

Por ejemplo.

✓ Calcular descuentos.

✓ Validar reglas.

✓ Procesar pagos.

✓ Aplicar promociones.

✓ Orquestar procesos.

Es una de las capas
más importantes.

No debería conocer
cómo funciona
la base de datos.
"""

###########################################################
# CAPA DE REPOSITORIO
###########################################################

"""
Su responsabilidad es acceder
a la información.

Ejemplos.

✓ SQL Server

✓ PostgreSQL

✓ MongoDB

✓ Archivos CSV

✓ APIs externas

El resto del proyecto
no debería preocuparse
por cómo se obtienen
los datos.

Solo solicita la información.
"""

###########################################################
# CAPA DE DATOS
###########################################################

"""
Aquí viven los datos.

Ejemplos.

✓ Tablas.

✓ Archivos.

✓ Data Lake.

✓ Data Warehouse.

✓ Objetos en memoria.

Es la capa más cercana
al almacenamiento.
"""

###########################################################
# EJEMPLO DE ESTRUCTURA
###########################################################

"""
mi_proyecto/

│

├── api/

│   ├── clientes.py

│   └── productos.py

│

├── services/

│   ├── clientes.py

│   └── ventas.py

│

├── repositories/

│   ├── clientes.py

│   └── ventas.py

│

├── models/

│   ├── cliente.py

│   └── venta.py

│

├── config/

├── tests/

└── main.py

Cada carpeta representa
una responsabilidad diferente.
"""

###########################################################
# LOS MODELOS
###########################################################

"""
La carpeta models
normalmente contiene
las estructuras del negocio.

Ejemplo.

Cliente

Producto

Factura

Venta

Empleado

Estas clases representan
objetos reales
del dominio del negocio.
"""

###########################################################
# IMPORTACIONES
###########################################################

"""
En proyectos grandes
las importaciones
también deben organizarse.

Ejemplo.

import os

import logging

import pandas as pd

from services.clientes import ClienteService

from repositories.ventas import VentaRepository

Mantener un orden
facilita la lectura.
"""

###########################################################
# IMPORTACIONES ABSOLUTAS
###########################################################

"""
Generalmente se prefieren
las importaciones absolutas.

Ejemplo.

from services.ventas import VentaService

En lugar de.

from ..services import VentaService

Las importaciones absolutas
son más fáciles
de mantener
cuando el proyecto crece.
"""

###########################################################
# DEPENDENCIAS CIRCULARES
###########################################################

"""
Uno de los problemas
más comunes
en proyectos grandes.

Ejemplo.

clientes.py

importa ventas.py

↓

ventas.py

importa clientes.py

↓

clientes.py

↓

ventas.py

↓

clientes.py

Python no podrá resolver
correctamente
estas dependencias.

Esto recibe el nombre de:

Dependencia circular.
"""

###########################################################
# ¿CÓMO EVITARLAS?
###########################################################

"""
La solución normalmente consiste
en mejorar la arquitectura.

No en buscar trucos.

Algunas estrategias.

✓ Separar responsabilidades.

✓ Crear módulos comunes.

✓ Reducir acoplamiento.

✓ Revisar el diseño.

Generalmente,
la dependencia circular
es una señal
de un problema
de arquitectura.
"""

###########################################################
# ACOPLAMIENTO
###########################################################

"""
El acoplamiento indica
qué tanto depende
un módulo de otro.

Mientras menor sea
el acoplamiento,

más fácil será:

✓ Probar.

✓ Reutilizar.

✓ Cambiar.

✓ Escalar.

Buscamos módulos
lo más independientes posible.
"""

###########################################################
# COHESIÓN
###########################################################

"""
La cohesión mide
qué tan relacionadas
están las responsabilidades
de un módulo.

Alta cohesión.

↓

Todas las funciones
trabajan
sobre el mismo tema.

Baja cohesión.

↓

El módulo contiene
funciones sin relación.

Siempre buscamos:

Alta cohesión.

Bajo acoplamiento.
"""

###########################################################
# ORGANIZACIÓN PARA
# DATA ENGINEERING
###########################################################

"""
Una posible estructura.

etl/

│

├── extract/

├── transform/

├── load/

├── utils/

├── config/

├── logging/

├── validation/

├── tests/

└── main.py

Cada carpeta representa
una etapa del pipeline.

Esta organización
es muy común
en proyectos ETL.
"""

###########################################################
# EJEMPLO REAL
###########################################################

"""
extract/

↓

Lee información.

----------------------

transform/

↓

Limpia datos.

----------------------

validation/

↓

Valida calidad.

----------------------

load/

↓

Carga resultados.

Cada etapa
tiene una única responsabilidad.
"""

###########################################################
# EVITA LOS MÓDULOS "CAJÓN"
###########################################################

"""
Un error muy frecuente
es crear archivos llamados.

utils.py

helpers.py

misc.py

common.py

Y terminar almacenando allí
cualquier función.

Con el tiempo
estos archivos
se convierten
en enormes "cajones"
difíciles de mantener.

Si un módulo crece demasiado,
divídelo por responsabilidad.
"""

###########################################################
# ESCALABILIDAD
###########################################################

"""
Una buena arquitectura
permite que el proyecto crezca.

Agregar un nuevo módulo
no debería requerir
modificar veinte archivos.

Mientras más aislados
estén los componentes,

más sencillo será
escalar el sistema.
"""

###########################################################
# CASO EMPRESARIAL
###########################################################

"""
Supongamos
una plataforma bancaria.

Podríamos encontrar.

clientes/

cuentas/

transferencias/

prestamos/

auditoria/

seguridad/

Cada dominio
evoluciona
de manera independiente.

Eso facilita
el trabajo paralelo
de múltiples equipos.
"""

###########################################################
# ERRORES COMUNES
###########################################################

"""
ERROR 1

Todo el código
en main.py.

------------------------------------

ERROR 2

Dependencias circulares.

------------------------------------

ERROR 3

Archivos gigantes.

------------------------------------

ERROR 4

Módulos
con múltiples responsabilidades.

------------------------------------

ERROR 5

Importaciones desordenadas.

------------------------------------

ERROR 6

Configuración mezclada
con lógica del negocio.

------------------------------------

ERROR 7

Crear carpetas
sin propósito.
"""

###########################################################
# CHECKLIST DE ORGANIZACIÓN
###########################################################

"""
Antes de iniciar un proyecto,
pregúntate.

✓ ¿Cada carpeta tiene un propósito?

✓ ¿Cada módulo tiene una única responsabilidad?

✓ ¿Las dependencias son claras?

✓ ¿Existen dependencias circulares?

✓ ¿El proyecto puede crecer?

✓ ¿La configuración está separada?

✓ ¿Las pruebas están aisladas?

✓ ¿Existe documentación?

✓ ¿La estructura es consistente?
"""

###########################################################
# BUENAS PRÁCTICAS
###########################################################

"""
✓ Diseña antes de programar.

✓ Organiza por responsabilidad.

✓ Mantén módulos pequeños.

✓ Evita dependencias circulares.

✓ Busca alta cohesión.

✓ Reduce el acoplamiento.

✓ Piensa en la escalabilidad.

✓ Mantén una arquitectura consistente.
"""

###########################################################
# TIPS PROFESIONALES
###########################################################

"""
TIP 1

Una buena arquitectura
reduce el número
de bugs.

------------------------------------

TIP 2

La organización
debe facilitar
el trabajo del equipo,
no complicarlo.

------------------------------------

TIP 3

Si encontrar una función
toma varios minutos,

probablemente la estructura
necesita mejorar.

------------------------------------

TIP 4

No diseñes únicamente
para el presente.

Diseña pensando
en los próximos años.

------------------------------------

TIP 5

La arquitectura perfecta
no existe.

La mejor arquitectura
es aquella que responde
a las necesidades
del proyecto.
"""

###########################################################
# EJERCICIO 1
###########################################################

"""
Diseña la estructura
de una API de comercio electrónico.

Debe incluir módulos para:

✓ Usuarios.

✓ Productos.

✓ Carrito.

✓ Pagos.

✓ Pedidos.

✓ Inventario.

Piensa en carpetas,
módulos
y responsabilidades.
"""

###########################################################
# EJERCICIO 2
###########################################################

"""
Supón que un archivo
llamado utils.py
tiene 2.500 líneas.

Describe cómo comenzarías
a dividirlo.

No escribas código.

Justifica cada decisión.
"""

###########################################################
# EJERCICIO 3
###########################################################

"""
Analiza el siguiente proyecto.

main.py

clientes.py

ventas.py

productos.py

database.py

Todo el proyecto
está en la carpeta raíz.

¿Cómo lo reorganizarías
utilizando carpetas
y arquitectura por capas?
"""

###########################################################
# EJERCICIO 4 (Difícil)
###########################################################

"""
Tu empresa quiere construir
una plataforma de Ingeniería
de Datos.

Debe contener:

✓ Ingesta.

✓ Validaciones.

✓ Transformaciones.

✓ Calidad de datos.

✓ Logging.

✓ Configuración.

✓ Notificaciones.

✓ Monitoreo.

Diseña una estructura
profesional de carpetas.

Justifica cada decisión
como si fueras
el Arquitecto del proyecto.
"""

###########################################################
# REFLEXIÓN FINAL
###########################################################

"""
Un desarrollador junior
piensa:

"¿Dónde pongo este archivo?"

Un desarrollador senior
piensa:

"¿Qué responsabilidad
tiene este archivo?"

La diferencia
parece pequeña.

Pero cambia completamente
la calidad
de la arquitectura.

La organización
no consiste
en crear carpetas.

Consiste
en diseñar software
que pueda crecer
sin perder claridad.
"""

###########################################################
# RESUMEN GENERAL DEL TEMA
###########################################################

"""
Durante este tema aprendiste:

✓ Diferencia entre
script
y proyecto.

✓ Organización
por carpetas.

✓ Organización
por módulos.

✓ Separación
de responsabilidades.

✓ __init__.py.

✓ README.md.

✓ requirements.txt.

✓ .gitignore.

✓ Variables de entorno.

✓ Configuración.

✓ Arquitectura por capas.

✓ Importaciones.

✓ Dependencias circulares.

✓ Cohesión.

✓ Acoplamiento.

✓ Organización
para Data Engineering.

✓ Escalabilidad.

✓ Buenas prácticas.

✓ Casos reales.

✓ Checklist profesional.

==========================================================

MENSAJE FINAL

La estructura de un proyecto
es como los planos
de un edificio.

Dos edificios pueden tener
la misma cantidad de pisos.

Pero aquel con mejores planos
será más fácil de construir,
mantener y ampliar.

Lo mismo ocurre con el software.

Una buena organización
no hace que el programa
funcione más rápido.

Hace que el equipo
pueda evolucionarlo
durante años
con mucho menos esfuerzo.

==========================================================
FIN DEL ARCHIVO
==========================================================
"""