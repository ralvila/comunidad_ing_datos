/*
===========================================================
COMUNIDAD DE INGENIERÍA DE DATOS
INTRODUCCIÓN A SQL

BLOQUE 2 - CONSULTAS BÁSICAS
===========================================================

OBJETIVOS

Al finalizar este laboratorio podrás:

- Consultar información utilizando SELECT.
- Seleccionar columnas específicas.
- Utilizar alias con AS.
- Eliminar duplicados con DISTINCT.
- Limitar resultados con TOP.
- Filtrar información con WHERE.
- Utilizar operadores de comparación.
- Utilizar operadores lógicos.
- Utilizar IN y NOT IN.
- Utilizar BETWEEN.
- Utilizar LIKE.
- Utilizar IS NULL e IS NOT NULL.

===========================================================
REQUISITO
===========================================================

Este laboratorio asume que ya ejecutaste:

01_fundamentos_bases_datos.sql

y que existe la base de datos ComunidadSQL.
*/

USE ComunidadSQL;
GO

/*
===========================================================
SECCIÓN 1 - DATOS ADICIONALES
===========================================================

Insertaremos algunos registros adicionales
para tener más información sobre la cual trabajar.
*/

INSERT INTO clientes
VALUES
(4,'Pedro','Bogotá','2024-04-01'),
(5,'María','Barranquilla','2024-04-15'),
(6,'Juan','Bogotá','2024-05-01');

GO

/*
===========================================================
SECCIÓN 2 - SELECT
===========================================================

SELECT permite consultar información.

El símbolo * significa:
"Traiga todas las columnas".
*/

SELECT *
FROM clientes;

GO

/*
Consultar columnas específicas.
*/

SELECT
    cliente_id,
    nombre
FROM clientes;

GO

/*
===========================================================
SECCIÓN 3 - ALIAS (AS)
===========================================================

Los alias permiten cambiar temporalmente
el nombre de una columna en el resultado.
*/

SELECT
    cliente_id AS IdCliente,
    nombre AS NombreCliente,
    ciudad AS CiudadCliente
FROM clientes;

GO

/*
===========================================================
SECCIÓN 4 - DISTINCT
===========================================================

DISTINCT elimina valores duplicados.
*/

SELECT ciudad
FROM clientes;

GO

SELECT DISTINCT ciudad
FROM clientes;

GO

/*
===========================================================
SECCIÓN 5 - TOP
===========================================================

TOP limita la cantidad de registros retornados.
*/

SELECT TOP 3 *
FROM clientes;

GO

SELECT TOP 2
    nombre,
    ciudad
FROM clientes;

GO

/*
===========================================================
SECCIÓN 6 - WHERE
===========================================================

WHERE permite filtrar registros.
*/

SELECT *
FROM clientes
WHERE ciudad = 'Bogotá';

GO

SELECT *
FROM clientes
WHERE ciudad = 'Cali';

GO

/*
===========================================================
SECCIÓN 7 - OPERADORES DE COMPARACIÓN
===========================================================

=
<>
>
<
>=
<=
*/

SELECT *
FROM productos
WHERE precio = 80;

GO

SELECT *
FROM productos
WHERE precio > 100;

GO

SELECT *
FROM productos
WHERE precio >= 120;

GO

SELECT *
FROM productos
WHERE precio < 1000;

GO

SELECT *
FROM productos
WHERE precio <> 80;

GO

/*
===========================================================
SECCIÓN 8 - OPERADORES LÓGICOS
===========================================================

AND
OR
NOT
*/

SELECT *
FROM clientes
WHERE ciudad = 'Bogotá'
AND cliente_id > 3;

GO

SELECT *
FROM clientes
WHERE ciudad = 'Bogotá'
OR ciudad = 'Cali';

GO

SELECT *
FROM clientes
WHERE NOT ciudad = 'Bogotá';

GO

/*
===========================================================
SECCIÓN 9 - IN
===========================================================

IN permite comparar contra múltiples valores.
*/

SELECT *
FROM clientes
WHERE ciudad IN ('Bogotá','Cali');

GO

/*
===========================================================
SECCIÓN 10 - NOT IN
===========================================================
*/

SELECT *
FROM clientes
WHERE ciudad NOT IN ('Bogotá','Cali');

GO

/*
===========================================================
SECCIÓN 11 - BETWEEN
===========================================================

BETWEEN permite trabajar con rangos.
*/

SELECT *
FROM productos
WHERE precio BETWEEN 50 AND 200;

GO

SELECT *
FROM clientes
WHERE cliente_id BETWEEN 2 AND 5;

GO

/*
===========================================================
SECCIÓN 12 - LIKE
===========================================================

LIKE permite realizar búsquedas de texto.

%  = cualquier cantidad de caracteres
_  = un único carácter
*/

SELECT *
FROM clientes
WHERE nombre LIKE 'A%';

GO

SELECT *
FROM clientes
WHERE nombre LIKE '%a';

GO

SELECT *
FROM clientes
WHERE nombre LIKE '%ar%';

GO

/*
===========================================================
SECCIÓN 13 - IS NULL
===========================================================

Crearemos una tabla para entender los valores NULL.
*/

CREATE TABLE empleados
(
    empleado_id INT PRIMARY KEY,
    nombre VARCHAR(100),
    correo VARCHAR(100)
);

GO

INSERT INTO empleados
VALUES
(1,'Carlos','carlos@empresa.com'),
(2,'Laura',NULL),
(3,'Pedro',NULL);

GO

SELECT *
FROM empleados;

GO

/*
Consultar registros con valores NULL.
*/

SELECT *
FROM empleados
WHERE correo IS NULL;

GO

/*
Consultar registros que sí tienen valor.
*/

SELECT *
FROM empleados
WHERE correo IS NOT NULL;

GO

/*
===========================================================
SECCIÓN 14 - COMBINANDO FILTROS
===========================================================

En proyectos reales es común combinar
múltiples condiciones.
*/

SELECT *
FROM clientes
WHERE ciudad = 'Bogotá'
AND cliente_id BETWEEN 1 AND 10;

GO

SELECT *
FROM clientes
WHERE nombre LIKE 'M%'
OR ciudad = 'Cali';

GO

SELECT *
FROM productos
WHERE precio > 50
AND precio < 1000;

GO

/*
===========================================================
EJERCICIOS
===========================================================

1. Consulte todos los registros de clientes.

2. Consulte únicamente las columnas:
   nombre y ciudad.

3. Muestre los nombres de los clientes
   utilizando alias.

4. Obtenga las ciudades sin duplicados.

5. Consulte los primeros 3 clientes.

6. Consulte los clientes de Bogotá.

7. Consulte los clientes que NO son de Bogotá.

8. Consulte los productos con precio mayor a 100.

9. Consulte los productos con precio
   entre 50 y 500.

10. Consulte los clientes de Bogotá o Cali.

11. Consulte los clientes cuyo nombre
    empiece por la letra P.

12. Consulte los clientes cuyo nombre
    termine en la letra a.

13. Consulte los empleados que no tienen correo.

14. Consulte los empleados que sí tienen correo.

15. Construya una consulta utilizando:
    WHERE + AND + BETWEEN.

16. Construya una consulta utilizando:
    WHERE + OR + LIKE.

===========================================================
RETO
===========================================================

Construya una consulta que cumpla
las siguientes condiciones:

- Mostrar únicamente nombre y ciudad.
- Clientes de Bogotá o Barranquilla.
- Que su identificador sea mayor a 2.
- Ordene el resultado mentalmente antes
  de ejecutarlo y prediga qué registros
  deberían aparecer.

===========================================================
FIN DEL LABORATORIO
===========================================================
*/