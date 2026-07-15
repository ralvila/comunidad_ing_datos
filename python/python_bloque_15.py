"""
BLOQUE 15 — MANEJO DE ARCHIVOS

Modo de uso:
- Ejecuta por secciones
- Lee TODOS los comentarios
- Predice antes de ejecutar
- Modifica ejemplos
- Rompe el código intencionalmente
- Analiza los errores

IMPORTANTE:

Este bloque es uno de los más importantes del curso.

Hasta ahora toda la información vivía únicamente en memoria.

Cuando el programa terminaba:
👉 todo desaparecía

Los archivos permiten:

✔ guardar información
✔ recuperar información
✔ compartir información
✔ construir aplicaciones reales

Todo sistema profesional utiliza archivos:

- logs
- configuraciones
- reportes
- exportaciones
- CSV
- JSON
- datasets

Este bloque es la puerta de entrada
al mundo real.
"""

# =====================================================
# 1. ¿QUÉ ES UN ARCHIVO?
# =====================================================

"""
Un archivo es información almacenada
de forma permanente en disco.

Piensa en él como una libreta.

Variables:
    viven en memoria

Archivos:
    viven en disco

Cuando el programa termina:

Variables:
    desaparecen

Archivos:
    permanecen
"""

nombre = "Juan"

print(nombre)

# Cuando termina el programa:
# nombre desaparece

# Cuando escribimos un archivo:
# la información queda guardada


# =====================================================
# 2. OPEN()
# =====================================================

"""
open() es la función que permite
abrir archivos.

Sintaxis:

open(ruta, modo)
"""

# Abrir archivo para lectura

# archivo = open("ejemplo.txt", "r")
# archivo.close()

"""
TIP:

Siempre pregúntate:

¿Para qué estoy abriendo el archivo?

Leer?
Escribir?
Agregar?

El modo depende de eso.
"""


# =====================================================
# 3. MODOS DE APERTURA
# =====================================================

"""
r = read

w = write

a = append

x = create

r+ = read + write
"""

"""
TRUCO DE MEMORIA

r -> Read

w -> Write

a -> Append
"""


# =====================================================
# 4. WRITE()
# =====================================================

"""
write() escribe contenido
dentro del archivo.
"""

# archivo = open("saludo.txt", "w")
#
# archivo.write("Hola Python")
#
# archivo.close()

"""
IMPORTANTE:

El modo "w" tiene un comportamiento
que suele sorprender a los principiantes.

Si el archivo ya existe:

👉 se borra completamente

y luego se vuelve a escribir.
"""

# ERROR COMÚN

"""
Muchos creen que write()
agrega información.

NO.

write() depende del modo.

Si usas:

w

el contenido anterior desaparece.
"""

# EJEMPLO

"""
Archivo original:

Hola
Mundo

Ejecutas:

open("archivo.txt", "w")

Resultado:

Todo el contenido anterior desaparece.
"""


# =====================================================
# 5. APPEND
# =====================================================

"""
append significa:

agregar

sin borrar lo existente
"""

# archivo = open("log.txt", "a")
#
# archivo.write("\nNuevo evento")
#
# archivo.close()

"""
CASO REAL

Imagina:

Sistema bancario
Sistema de ventas
Sistema de auditoría

NO quieres perder registros.

Por eso se utiliza append.
"""

"""
Pregunta típica de entrevista:

¿Qué modo usarías para guardar logs?

Respuesta:

append (a)

Porque los logs crecen continuamente.
"""


# =====================================================
# 6. READ()
# =====================================================

"""
Lee TODO el archivo.
"""

# with open("saludo.txt", "r") as archivo:
#
#     contenido = archivo.read()
#
#     print(contenido)

"""
DETALLE IMPORTANTE

read() mueve el cursor al final.
"""

# with open("saludo.txt", "r") as archivo:
#
#     print(archivo.read())
#
#     print(archivo.read())

"""
Resultado:

Hola Python

''
"""

"""
ANALOGÍA

read()

es como leer un libro.

Cuando llegas al final:

ya no hay más páginas.
"""


# =====================================================
# 7. LEER LÍNEA POR LÍNEA
# =====================================================

"""
MUY común en Data Engineering.
"""

# with open("usuarios.txt", "r") as archivo:
#
#     for linea in archivo:
#
#         print(linea)

"""
CASO REAL

Archivos de:

1 millón
10 millones
100 millones de líneas

NO puedes cargar todo en memoria.

Por eso se procesan línea por línea.
"""

"""
TIP PRO

Siempre pregúntate:

¿Cuánto mide el archivo?

Si pesa varios GB:

read()

probablemente NO sea buena idea.
"""


# =====================================================
# 8. CONTEXT MANAGER
# =====================================================

"""
EL TEMA MÁS IMPORTANTE DEL BLOQUE
"""

# MAL EJEMPLO

# archivo = open("datos.txt")
#
# contenido = archivo.read()
#
# archivo.close()

"""
PROBLEMA
"""

# archivo = open("datos.txt")
#
# raise Exception("Error")
#
# archivo.close()

"""
Nunca se ejecuta:

archivo.close()
"""

"""
SOLUCIÓN
"""

# with open("datos.txt") as archivo:
#
#     contenido = archivo.read()

"""
¿QUÉ HACE WITH?

1. abre archivo
2. ejecuta código
3. cierra archivo automáticamente
"""

"""
REGLA PROFESIONAL

Si ves:

open()

sin

with

en código profesional...

probablemente es un code smell.
"""


# =====================================================
# 9. FILE NOT FOUND
# =====================================================

# try:
#
#     with open("archivo_inexistente.txt") as archivo:
#
#         print(archivo.read())
#
# except FileNotFoundError:
#
#     print("Archivo no encontrado")

"""
Una de las excepciones más comunes
en Python real.
"""


# =====================================================
# 10. EJEMPLO REAL — MINI LOGGER
# =====================================================

"""
Los logs son archivos que almacenan
eventos importantes del sistema.

Ejemplos:

2026-06-18 LOGIN
2026-06-18 LOGOUT
2026-06-18 CREATE_USER

MUY utilizado en:

- APIs
- Microservicios
- Aplicaciones web
- Data Engineering
"""

from datetime import datetime


def registrar_evento(evento):

    with open("logs.txt", "a") as archivo:

        fecha = datetime.now()

        archivo.write(
            f"{fecha} - {evento}\n"
        )


# registrar_evento("LOGIN")
# registrar_evento("LOGOUT")


# =====================================================
# 11. EJEMPLO REAL — SISTEMA DE NOTAS
# =====================================================

"""
Archivo:

Ana,90
Juan,80
Pedro,60

Leer archivo.

Calcular:

- promedio
- nota máxima
- nota mínima
"""

# notas = []
#
# with open("notas.txt") as archivo:
#
#     for linea in archivo:
#
#         nombre, nota = linea.strip().split(",")
#
#         notas.append(int(nota))
#
# print(sum(notas) / len(notas))
# print(max(notas))
# print(min(notas))


# =====================================================
# 12. EJEMPLO REAL — BUSCADOR DE PALABRAS
# =====================================================

"""
Crear función:

buscar_palabra(
    archivo,
    palabra
)

Retornar:

True
False
"""


def buscar_palabra(nombre_archivo, palabra):

    with open(nombre_archivo, "r") as archivo:

        contenido = archivo.read()

        return palabra in contenido


# =====================================================
# 13. EJEMPLO REAL — CONTADOR DE FRECUENCIAS
# =====================================================

"""
Leer archivo.

Contar cuántas veces aparece
cada palabra.

Retornar:

{
    palabra: frecuencia
}
"""


def contar_palabras(nombre_archivo):

    frecuencias = {}

    with open(nombre_archivo, "r") as archivo:

        for linea in archivo:

            palabras = linea.split()

            for palabra in palabras:

                frecuencias[palabra] = (
                    frecuencias.get(palabra, 0) + 1
                )

    return frecuencias


# =====================================================
# 14. EJEMPLO AVANZADO — EXPORTAR REPORTE
# =====================================================

"""
Supongamos que tenemos información
en memoria y queremos exportarla.

MUY común en sistemas reales.
"""


def exportar_reporte(usuarios):

    with open("reporte.txt", "w") as archivo:

        for usuario in usuarios:

            archivo.write(
                f"{usuario}\n"
            )


usuarios = [
    "Juan",
    "Ana",
    "Pedro"
]

# exportar_reporte(usuarios)


# =====================================================
# 15. EJEMPLO AVANZADO — CARGAR CONFIGURACIÓN
# =====================================================

"""
Muchos sistemas leen archivos
de configuración.

config.txt

host=localhost
puerto=8080

Convertirlo en:

{
    "host": "localhost",
    "puerto": "8080"
}
"""


def cargar_configuracion(nombre_archivo):

    configuracion = {}

    with open(nombre_archivo) as archivo:

        for linea in archivo:

            clave, valor = linea.strip().split("=")

            configuracion[clave] = valor

    return configuracion


# =====================================================
# 16. EJERCICIOS NIVEL BAJO
# =====================================================

"""
EJERCICIO 1

Crear archivo:

bienvenida.txt

Guardar:

Bienvenido a Python Masters
"""

"""
EJERCICIO 2

Leer archivo y mostrar contenido.
"""

"""
EJERCICIO 3

Agregar una nueva línea usando append.
"""


# =====================================================
# 17. EJERCICIOS NIVEL MEDIO
# =====================================================

"""
EJERCICIO 4

Guardar una lista de nombres
en un archivo.
"""

"""
EJERCICIO 5

Leer archivo y contar líneas.
"""

"""
EJERCICIO 6

Leer archivo y contar palabras.
"""


# =====================================================
# 18. EJERCICIOS NIVEL ALTO
# =====================================================

"""
EJERCICIO 7

Sistema de notas.

Archivo:

Ana,90
Juan,80
Pedro,60

Calcular:

- promedio
- máximo
- mínimo
"""

"""
EJERCICIO 8

Crear mini logger.

Guardar eventos usando append.
"""

"""
EJERCICIO 9

Buscar una palabra dentro
de un archivo.

Retornar:

True
False
"""

"""
EJERCICIO 10

Leer archivo y generar:

{
    "Juan": 80,
    "Ana": 95,
    "Pedro": 60
}
"""


# =====================================================
# 19. EJERCICIOS NIVEL PYTHON MASTERS
# =====================================================

"""
EJERCICIO 11

Construir un mini sistema
de usuarios.

Opciones:

1. Registrar usuario
2. Listar usuarios
3. Buscar usuario

Persistencia obligatoria
en archivo de texto.

Manejar errores.

Usar:
- funciones
- excepciones
- context manager
"""

"""
EJERCICIO 12

Crear un sistema de auditoría.

Guardar:

fecha
usuario
acción

en archivo de logs.
"""

"""
EJERCICIO 13

Leer un archivo de ventas:

Juan,100
Ana,200
Pedro,150

Calcular:

- total ventas
- promedio
- vendedor con mayor venta
"""

"""
EJERCICIO 14

Construir un sistema de backup.

Leer un archivo.

Crear copia exacta
en otro archivo.
"""

"""
EJERCICIO 15

Implementar búsqueda
de texto estilo CTRL + F.

Debe retornar:

- cantidad de coincidencias
- líneas donde aparece
"""


# =====================================================
# 20. EJERCICIO NIVEL ENTREVISTA
# =====================================================

"""
Tienes un archivo de 5 GB.

¿Qué harías?

A)

archivo.read()

B)

for linea in archivo

¿POR QUÉ?
"""

"""
Respuesta esperada:

for linea in archivo

Porque consume mucha menos memoria.
"""


# =====================================================
# MENSAJES CLAVE DEL BLOQUE
# =====================================================

"""
1. Los archivos permiten persistencia.

2. write() sobrescribe.

3. append() agrega.

4. read() consume contenido.

5. with open() es la forma profesional.

6. FileNotFoundError es común.

7. Procesar línea por línea escala mejor.

8. Todo Data Engineer trabaja con archivos.

9. CSV, JSON y Parquet nacen de este concepto.

10. Aprender archivos es aprender persistencia.
"""