/*
===========================================================
COMUNIDAD DE INGENIERÍA DE DATOS
INTRODUCCIÓN A SQL

BLOQUE 5 - MANIPULACIÓN DE DATOS
===========================================================

OBJETIVOS

Al finalizar este laboratorio podrás:

- Insertar registros utilizando INSERT.
- Actualizar registros utilizando UPDATE.
- Eliminar registros utilizando DELETE.
- Comprender la importancia de la cláusula WHERE.
- Entender los riesgos asociados a UPDATE y DELETE.
- Realizar operaciones básicas de mantenimiento de datos.

===========================================================
REQUISITO
===========================================================

Este laboratorio asume que ya ejecutaste:

01_fundamentos_bases_datos.sql
02_consultas_basicas.sql
03_ordenamiento_agregaciones.sql
04_joins.sql

y que existe la base de datos ComunidadSQL.
*/

USE ComunidadSQL;
GO

/*
===========================================================
SECCIÓN 1 - CONSULTAR ESTADO INICIAL
===========================================================

Antes de modificar información es una buena
práctica consultar los datos existentes.
*/

SELECT *
FROM clientes;

GO

SELECT *
FROM productos;

GO

/*
===========================================================
SECCIÓN 2 - INSERT
===========================================================

INSERT permite agregar nuevos registros
a una tabla.
*/

INSERT INTO clientes
(
    cliente_id,
    nombre,
    ciudad,
    fecha_registro
)
VALUES
(
    9,
    'Camila',
    'Bogotá',
    '2024-06-15'
);

GO

/*
Verificar resultado.
*/

SELECT *
FROM clientes
WHERE cliente_id = 9;

GO

/*
Insertar múltiples registros.
*/

INSERT INTO productos
(
    producto_id,
    nombre_producto,
    precio
)
VALUES
(4,'Monitor',900.00),
(5,'Audífonos',250.00),
(6,'Webcam',180.00);

GO

SELECT *
FROM productos;

GO

/*
===========================================================
SECCIÓN 3 - UPDATE
===========================================================

UPDATE permite modificar registros existentes.
*/

UPDATE clientes
SET ciudad = 'Manizales'
WHERE cliente_id = 9;

GO

/*
Verificar actualización.
*/

SELECT *
FROM clientes
WHERE cliente_id = 9;

GO

/*
Actualizar múltiples columnas.
*/

UPDATE productos
SET
    nombre_producto = 'Monitor Gamer',
    precio = 1200.00
WHERE producto_id = 4;

GO

SELECT *
FROM productos
WHERE producto_id = 4;

GO

/*
===========================================================
SECCIÓN 4 - IMPORTANCIA DEL WHERE
===========================================================

WHERE limita los registros afectados.

Sin WHERE todos los registros serán modificados.

IMPORTANTE:

NO EJECUTAR LA SIGUIENTE INSTRUCCIÓN.
*/

-- UPDATE clientes
-- SET ciudad = 'Bogotá';

/*
¿Qué ocurriría?

Todos los clientes quedarían con ciudad Bogotá.
*/

/*
===========================================================
SECCIÓN 5 - DELETE
===========================================================

DELETE permite eliminar registros.
*/

INSERT INTO clientes
VALUES
(
    10,
    'Cliente Temporal',
    'Bogotá',
    '2024-06-20'
);

GO

SELECT *
FROM clientes
WHERE cliente_id = 10;

GO

/*
Eliminar el registro.
*/

DELETE FROM clientes
WHERE cliente_id = 10;

GO

/*
Verificar eliminación.
*/

SELECT *
FROM clientes
WHERE cliente_id = 10;

GO

/*
===========================================================
SECCIÓN 6 - RIESGO DE DELETE SIN WHERE
===========================================================

IMPORTANTE:

NO EJECUTAR LA SIGUIENTE INSTRUCCIÓN.
*/

-- DELETE FROM clientes;

/*
¿Qué ocurriría?

Todos los registros de la tabla serían eliminados.
*/

/*
===========================================================
SECCIÓN 7 - VALIDACIÓN ANTES DE MODIFICAR
===========================================================

Una buena práctica consiste en ejecutar
primero un SELECT utilizando exactamente
el mismo filtro.
*/

SELECT *
FROM clientes
WHERE cliente_id = 9;

GO

/*
Si el resultado es correcto,
entonces ejecutamos el UPDATE.
*/

UPDATE clientes
SET ciudad = 'Bogotá'
WHERE cliente_id = 9;

GO

/*
Verificar resultado.
*/

SELECT *
FROM clientes
WHERE cliente_id = 9;

GO

/*
===========================================================
SECCIÓN 8 - ESCENARIO REAL
===========================================================

Supongamos que un producto cambió de precio.
*/

SELECT *
FROM productos
WHERE producto_id = 5;

GO

UPDATE productos
SET precio = 300.00
WHERE producto_id = 5;

GO

SELECT *
FROM productos
WHERE producto_id = 5;

GO

/*
===========================================================
SECCIÓN 9 - BUENAS PRÁCTICAS
===========================================================

1. Siempre ejecutar un SELECT antes
   de un UPDATE.

2. Siempre ejecutar un SELECT antes
   de un DELETE.

3. Validar cuántos registros serán afectados.

4. Utilizar filtros específicos.

5. Evitar UPDATE y DELETE sin WHERE.

6. Validar resultados después de modificar
   información.

===========================================================
RESUMEN
===========================================================

INSERT
    Agrega registros.

UPDATE
    Modifica registros existentes.

DELETE
    Elimina registros existentes.

WHERE
    Limita los registros afectados.

===========================================================
EJERCICIOS
===========================================================

1. Inserte un nuevo cliente.

2. Inserte dos nuevos productos.

3. Consulte el cliente insertado.

4. Actualice la ciudad de un cliente.

5. Actualice el precio de un producto.

6. Verifique el resultado utilizando SELECT.

7. Inserte un cliente temporal.

8. Elimine el cliente temporal.

9. Verifique que fue eliminado.

10. Explique qué ocurriría si se ejecuta:

    UPDATE clientes
    SET ciudad = 'Bogotá';

11. Explique qué ocurriría si se ejecuta:

    DELETE FROM productos;

===========================================================
RETO
===========================================================

Realice las siguientes actividades:

1. Cree un nuevo cliente.

2. Cree un nuevo producto.

3. Modifique el nombre del cliente.

4. Modifique el precio del producto.

5. Consulte ambos registros.

6. Elimine los registros creados.

7. Verifique que ya no existan.

===========================================================
FIN DEL LABORATORIO
===========================================================
*/