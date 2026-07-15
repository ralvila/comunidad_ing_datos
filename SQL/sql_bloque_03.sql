/*
===========================================================
COMUNIDAD DE INGENIERÍA DE DATOS
INTRODUCCIÓN A SQL

BLOQUE 3 - ORDENAMIENTO Y AGREGACIONES
===========================================================

OBJETIVOS

Al finalizar este laboratorio podrás:

- Ordenar resultados utilizando ORDER BY.
- Utilizar ASC y DESC.
- Contar registros con COUNT.
- Realizar sumatorias con SUM.
- Calcular promedios con AVG.
- Obtener máximos y mínimos.
- Agrupar información con GROUP BY.
- Filtrar grupos utilizando HAVING.
- Resolver preguntas básicas de negocio.

===========================================================
REQUISITO
===========================================================

Este laboratorio asume que ya ejecutaste:

01_fundamentos_bases_datos.sql
02_consultas_basicas.sql

y que existe la base de datos ComunidadSQL.
*/

USE ComunidadSQL;
GO

/*
===========================================================
SECCIÓN 1 - DATOS ADICIONALES
===========================================================

Agregaremos más información para que
las agregaciones tengan más sentido.
*/

INSERT INTO ventas
VALUES
(5,1,3,2,'2024-05-06'),
(6,2,1,1,'2024-05-07'),
(7,2,2,5,'2024-05-08'),
(8,3,2,3,'2024-05-09'),
(9,4,1,1,'2024-05-10'),
(10,5,3,4,'2024-05-11'),
(11,6,2,2,'2024-05-12');

GO

/*
===========================================================
SECCIÓN 2 - ORDER BY
===========================================================

ORDER BY permite ordenar resultados.
*/

SELECT *
FROM clientes
ORDER BY nombre;

GO

SELECT *
FROM productos
ORDER BY precio;

GO

/*
===========================================================
SECCIÓN 3 - ASC
===========================================================

ASC = Ascendente

Es el comportamiento por defecto.
*/

SELECT *
FROM productos
ORDER BY precio ASC;

GO

SELECT *
FROM clientes
ORDER BY nombre ASC;

GO

/*
===========================================================
SECCIÓN 4 - DESC
===========================================================

DESC = Descendente
*/

SELECT *
FROM productos
ORDER BY precio DESC;

GO

SELECT *
FROM clientes
ORDER BY nombre DESC;

GO

/*
===========================================================
SECCIÓN 5 - COUNT
===========================================================

COUNT cuenta registros.
*/

SELECT COUNT(*) AS TotalClientes
FROM clientes;

GO

SELECT COUNT(*) AS TotalProductos
FROM productos;

GO

SELECT COUNT(*) AS TotalVentas
FROM ventas;

GO

/*
===========================================================
SECCIÓN 6 - SUM
===========================================================

SUM realiza sumatorias.
*/

SELECT
    SUM(cantidad) AS TotalUnidadesVendidas
FROM ventas;

GO

/*
===========================================================
SECCIÓN 7 - AVG
===========================================================

AVG calcula promedios.
*/

SELECT
    AVG(precio) AS PrecioPromedio
FROM productos;

GO

/*
===========================================================
SECCIÓN 8 - MIN
===========================================================

MIN obtiene el valor mínimo.
*/

SELECT
    MIN(precio) AS ProductoMasEconomico
FROM productos;

GO

/*
===========================================================
SECCIÓN 9 - MAX
===========================================================

MAX obtiene el valor máximo.
*/

SELECT
    MAX(precio) AS ProductoMasCostoso
FROM productos;

GO

/*
===========================================================
SECCIÓN 10 - GROUP BY
===========================================================

GROUP BY agrupa registros.
*/

SELECT
    ciudad,
    COUNT(*) AS CantidadClientes
FROM clientes
GROUP BY ciudad;

GO

/*
Cantidad de ventas por cliente.
*/

SELECT
    cliente_id,
    COUNT(*) AS TotalVentas
FROM ventas
GROUP BY cliente_id;

GO

/*
Cantidad total de unidades vendidas
por producto.
*/

SELECT
    producto_id,
    SUM(cantidad) AS TotalUnidades
FROM ventas
GROUP BY producto_id;

GO

/*
===========================================================
SECCIÓN 11 - MÚLTIPLES AGRUPACIONES
===========================================================
*/

SELECT
    cliente_id,
    producto_id,
    SUM(cantidad) AS TotalCantidad
FROM ventas
GROUP BY
    cliente_id,
    producto_id;

GO

/*
===========================================================
SECCIÓN 12 - HAVING
===========================================================

HAVING permite filtrar grupos.

WHERE filtra registros.

HAVING filtra grupos.
*/

SELECT
    ciudad,
    COUNT(*) AS CantidadClientes
FROM clientes
GROUP BY ciudad
HAVING COUNT(*) > 1;

GO

/*
Clientes con más de una venta.
*/

SELECT
    cliente_id,
    COUNT(*) AS TotalVentas
FROM ventas
GROUP BY cliente_id
HAVING COUNT(*) > 1;

GO

/*
Productos con más de 3 unidades vendidas.
*/

SELECT
    producto_id,
    SUM(cantidad) AS TotalUnidades
FROM ventas
GROUP BY producto_id
HAVING SUM(cantidad) > 3;

GO

/*
===========================================================
SECCIÓN 13 - AGREGACIONES + ORDER BY
===========================================================

Es muy común combinar agrupaciones
con ordenamientos.
*/

SELECT
    cliente_id,
    COUNT(*) AS TotalVentas
FROM ventas
GROUP BY cliente_id
ORDER BY TotalVentas DESC;

GO

SELECT
    producto_id,
    SUM(cantidad) AS TotalUnidades
FROM ventas
GROUP BY producto_id
ORDER BY TotalUnidades DESC;

GO

/*
===========================================================
SECCIÓN 14 - CASOS DE NEGOCIO
===========================================================

Preguntas típicas que responden
las agregaciones.
*/

-- ¿Cuántos clientes existen?

SELECT COUNT(*) AS TotalClientes
FROM clientes;

GO

-- ¿Cuántas ventas se realizaron?

SELECT COUNT(*) AS TotalVentas
FROM ventas;

GO

-- ¿Cuántas unidades se vendieron?

SELECT SUM(cantidad) AS TotalUnidadesVendidas
FROM ventas;

GO

-- ¿Cuál es el producto más costoso?

SELECT MAX(precio) AS ProductoMasCostoso
FROM productos;

GO

-- ¿Cuál es el producto más económico?

SELECT MIN(precio) AS ProductoMasEconomico
FROM productos;

GO

/*
===========================================================
EJERCICIOS
===========================================================

1. Liste todos los clientes ordenados
   por nombre ascendente.

2. Liste todos los clientes ordenados
   por nombre descendente.

3. Liste los productos ordenados
   por precio descendente.

4. Cuente la cantidad total de clientes.

5. Cuente la cantidad total de ventas.

6. Calcule el promedio de precios.

7. Obtenga el precio máximo.

8. Obtenga el precio mínimo.

9. Calcule el total de unidades vendidas.

10. Obtenga la cantidad de clientes
    por ciudad.

11. Obtenga la cantidad de ventas
    por cliente.

12. Obtenga las unidades vendidas
    por producto.

13. Muestre únicamente las ciudades
    con más de un cliente.

14. Muestre únicamente los clientes
    con más de una venta.

15. Ordene el resultado anterior
    de mayor a menor.

===========================================================
RETO
===========================================================

Construya una consulta que responda:

¿Cuáles son los clientes que han realizado
más ventas?

El resultado debe incluir:

- cliente_id
- cantidad de ventas

Y debe estar ordenado de mayor
a menor cantidad de ventas.

===========================================================
FIN DEL LABORATORIO
===========================================================
*/