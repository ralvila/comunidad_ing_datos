/*
===========================================================
COMUNIDAD DE INGENIERÍA DE DATOS
INTRODUCCIÓN A SQL

BLOQUE 4 - JOINS
===========================================================

OBJETIVOS

Al finalizar este laboratorio podrás:

- Comprender qué es un JOIN.
- Entender por qué existen las relaciones entre tablas.
- Utilizar INNER JOIN.
- Utilizar LEFT JOIN.
- Utilizar RIGHT JOIN.
- Utilizar FULL JOIN.
- Comprender relaciones 1:1.
- Comprender relaciones 1:N.
- Comprender relaciones N:N.
- Consultar información distribuida en múltiples tablas.

===========================================================
REQUISITO
===========================================================

Este laboratorio asume que ya ejecutaste:

01_fundamentos_bases_datos.sql
02_consultas_basicas.sql
03_ordenamiento_agregaciones.sql

y que existe la base de datos ComunidadSQL.
*/

USE ComunidadSQL;
GO

/*
===========================================================
SECCIÓN 1 - ¿POR QUÉ NECESITAMOS JOINS?
===========================================================

En bases de datos relacionales la información
normalmente está distribuida en varias tablas.

Por ejemplo:

clientes
productos
ventas

La tabla ventas almacena únicamente
los identificadores de clientes y productos.

Para obtener información completa
debemos relacionar las tablas.
*/

SELECT *
FROM clientes;

GO

SELECT *
FROM productos;

GO

SELECT *
FROM ventas;

GO

/*
===========================================================
SECCIÓN 2 - RELACIÓN UNO A MUCHOS (1:N)
===========================================================

Un cliente puede realizar muchas ventas.

clientes (1) -----> (N) ventas
*/

SELECT
    c.cliente_id,
    c.nombre,
    v.venta_id,
    v.fecha_venta
FROM clientes c
INNER JOIN ventas v
    ON c.cliente_id = v.cliente_id;

GO

/*
===========================================================
SECCIÓN 3 - INNER JOIN
===========================================================

INNER JOIN devuelve únicamente
los registros que existen en ambas tablas.
*/

SELECT
    c.cliente_id,
    c.nombre,
    c.ciudad,
    v.venta_id,
    v.fecha_venta
FROM clientes c
INNER JOIN ventas v
    ON c.cliente_id = v.cliente_id;

GO

/*
===========================================================
SECCIÓN 4 - INNER JOIN ENTRE TRES TABLAS
===========================================================

Podemos encadenar múltiples JOINs.
*/

SELECT
    c.nombre,
    p.nombre_producto,
    v.cantidad,
    v.fecha_venta
FROM ventas v
INNER JOIN clientes c
    ON v.cliente_id = c.cliente_id
INNER JOIN productos p
    ON v.producto_id = p.producto_id;

GO

/*
===========================================================
SECCIÓN 5 - PREPARACIÓN PARA LEFT JOIN
===========================================================

Crearemos algunos registros sin ventas.
*/

INSERT INTO clientes
VALUES
(7,'Andrés','Bogotá','2024-06-01'),
(8,'Natalia','Cali','2024-06-05');

GO

/*
===========================================================
SECCIÓN 6 - LEFT JOIN
===========================================================

LEFT JOIN devuelve:

- Todos los registros de la tabla izquierda.
- Coincidencias de la tabla derecha.

Si no existe coincidencia,
los valores aparecerán como NULL.
*/

SELECT
    c.cliente_id,
    c.nombre,
    v.venta_id,
    v.fecha_venta
FROM clientes c
LEFT JOIN ventas v
    ON c.cliente_id = v.cliente_id
ORDER BY c.cliente_id;

GO

/*
Identificar clientes sin ventas.
*/

SELECT
    c.cliente_id,
    c.nombre,
    v.venta_id
FROM clientes c
LEFT JOIN ventas v
    ON c.cliente_id = v.cliente_id
WHERE v.venta_id IS NULL;

GO

/*
===========================================================
SECCIÓN 7 - PREPARACIÓN PARA RIGHT JOIN
===========================================================

Crearemos una venta cuyo cliente
no exista para fines educativos.

NOTA:
En ambientes reales esto normalmente
no es posible debido a las Foreign Keys.
*/

CREATE TABLE ventas_demo
(
    venta_id INT,
    cliente_id INT,
    total DECIMAL(10,2)
);

GO

INSERT INTO ventas_demo
VALUES
(1,1,1000),
(2,2,500),
(3,999,800);

GO

/*
===========================================================
SECCIÓN 8 - RIGHT JOIN
===========================================================

RIGHT JOIN devuelve:

- Todos los registros de la tabla derecha.
- Coincidencias de la tabla izquierda.
*/

SELECT
    c.cliente_id,
    c.nombre,
    v.venta_id,
    v.total
FROM clientes c
RIGHT JOIN ventas_demo v
    ON c.cliente_id = v.cliente_id;

GO

/*
===========================================================
SECCIÓN 9 - FULL JOIN
===========================================================

FULL JOIN devuelve:

- Coincidencias.
- Registros exclusivos de la izquierda.
- Registros exclusivos de la derecha.
*/

SELECT
    c.cliente_id,
    c.nombre,
    v.venta_id,
    v.total
FROM clientes c
FULL JOIN ventas_demo v
    ON c.cliente_id = v.cliente_id;

GO

/*
===========================================================
SECCIÓN 10 - RELACIÓN MUCHOS A MUCHOS (N:N)
===========================================================

Ejemplo conceptual:

Un estudiante puede tomar muchos cursos.

Un curso puede tener muchos estudiantes.

Para resolver esta relación se utiliza
una tabla intermedia.

estudiantes
      |
      |
inscripciones
      |
      |
cursos

Esto es una relación muchos a muchos.
*/

/*
===========================================================
SECCIÓN 11 - RELACIÓN UNO A UNO (1:1)
===========================================================

Ejemplo conceptual:

empleados
      |
      |
credenciales

Cada empleado tiene una única credencial.

Cada credencial pertenece a un único empleado.
*/

/*
===========================================================
SECCIÓN 12 - JOINS EN ESCENARIOS REALES
===========================================================

Ventas realizadas por cada cliente.
*/

SELECT
    c.nombre,
    p.nombre_producto,
    v.cantidad,
    v.fecha_venta
FROM ventas v
INNER JOIN clientes c
    ON v.cliente_id = c.cliente_id
INNER JOIN productos p
    ON v.producto_id = p.producto_id
ORDER BY v.fecha_venta;

GO

/*
Cantidad total vendida por producto.
*/

SELECT
    p.nombre_producto,
    SUM(v.cantidad) AS TotalVendido
FROM ventas v
INNER JOIN productos p
    ON v.producto_id = p.producto_id
GROUP BY p.nombre_producto
ORDER BY TotalVendido DESC;

GO

/*
===========================================================
EJERCICIOS
===========================================================

1. Consulte los clientes y sus ventas
   utilizando INNER JOIN.

2. Consulte las ventas y sus productos
   utilizando INNER JOIN.

3. Consulte clientes, productos y ventas
   en una sola consulta.

4. Utilice LEFT JOIN para identificar
   clientes sin ventas.

5. Ejecute el RIGHT JOIN y explique
   los resultados.

6. Ejecute el FULL JOIN y explique
   los resultados.

7. Identifique qué registros aparecen
   con valores NULL.

8. Explique cuándo utilizaría:

   - INNER JOIN
   - LEFT JOIN
   - RIGHT JOIN
   - FULL JOIN

9. Dibuje la relación existente entre:

   clientes
   ventas
   productos

===========================================================
RETO
===========================================================

Construya una consulta que muestre:

- Nombre del cliente
- Nombre del producto
- Cantidad vendida
- Fecha de venta

Ordene el resultado por fecha de venta.

Utilice únicamente INNER JOIN.

===========================================================
FIN DEL LABORATORIO
===========================================================
*/