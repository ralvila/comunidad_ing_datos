/*
===========================================================
COMUNIDAD DE INGENIERÍA DE DATOS....
INTRODUCCIÓN A SQL

BLOQUE 6 - OBJETOS DE BASE DE DATOS
(VIEWS, CTE, STORED PROCEDURES Y TRIGGERS)

===========================================================

OBJETIVOS

Al finalizar este laboratorio podrás:

- Comprender qué es una View.
- Comprender qué es un CTE.
- Comprender qué es un Stored Procedure.
- Comprender qué es un Trigger.
- Identificar cuándo utilizar cada objeto.
- Comprender ventajas y desventajas.
- Reconocer escenarios reales de uso.
- Diferenciar entre alternativas similares.

===========================================================
REQUISITO
===========================================================

Este laboratorio asume que ya ejecutaste:

01_fundamentos_bases_datos.sql
02_consultas_basicas.sql
03_ordenamiento_agregaciones.sql
04_joins.sql
05_manipulacion_datos.sql

y que existe la base de datos ComunidadSQL.
*/

USE ComunidadSQL;
GO

/*
###########################################################
SECCIÓN 1 - VIEWS (VISTAS)
###########################################################

¿QUÉ ES UNA VIEW?

Una View es una consulta almacenada que se comporta
como una tabla virtual.

No almacena datos físicamente.

Cada vez que se consulta, SQL Server ejecuta
la consulta asociada a la vista.

VENTAJAS

- Simplifica consultas complejas.
- Reutiliza lógica.
- Facilita el acceso a datos.
- Oculta complejidad al usuario.

DESVENTAJAS

- No almacena datos.
- Puede generar problemas de rendimiento.
- Puede volverse difícil de mantener si existen
  muchas vistas encadenadas.

CUÁNDO UTILIZARLA

✔ Consultas reutilizables.
✔ Seguridad.
✔ Simplificación de acceso.

CUÁNDO EVITARLA

✖ Procesamientos complejos.
✖ Consultas extremadamente pesadas.
✖ Cadenas de vistas sobre vistas.
*/

CREATE VIEW vw_ventas_detalle
AS
SELECT
    v.venta_id,
    c.nombre AS cliente,
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
Consultar la vista.
*/

SELECT *
FROM vw_ventas_detalle;
GO

/*
Modificar una vista.
*/

ALTER VIEW vw_ventas_detalle
AS
SELECT
    v.venta_id,
    c.nombre AS cliente,
    c.ciudad,
    p.nombre_producto,
    v.cantidad,
    v.fecha_venta
FROM ventas v
INNER JOIN clientes c
    ON v.cliente_id = c.cliente_id
INNER JOIN productos p
    ON v.producto_id = p.producto_id;
GO

SELECT *
FROM vw_ventas_detalle;
GO

/*
###########################################################
SECCIÓN 2 - CTE (COMMON TABLE EXPRESSIONS)
###########################################################

¿QUÉ ES UN CTE?

Un CTE es un resultado temporal definido
mediante la cláusula WITH.

Existe únicamente durante la ejecución
de una consulta.

VENTAJAS

- Mejora la legibilidad.
- Divide consultas complejas.
- Facilita el mantenimiento.

DESVENTAJAS

- No puede reutilizarse posteriormente.
- No puede indexarse.
- No es ideal para grandes volúmenes.

CUÁNDO UTILIZARLO

✔ Consultas complejas.
✔ Resultados intermedios.
✔ Transformaciones simples.

CUÁNDO EVITARLO

✖ Procesos de múltiples etapas.
✖ Reutilización de datos.
✖ Grandes volúmenes de información.
*/

WITH ventas_por_cliente AS
(
    SELECT
        cliente_id,
        SUM(cantidad) AS total_unidades
    FROM ventas
    GROUP BY cliente_id
)
SELECT *
FROM ventas_por_cliente;
GO

/*
Filtrando el resultado del CTE.
*/

WITH ventas_por_cliente AS
(
    SELECT
        cliente_id,
        SUM(cantidad) AS total_unidades
    FROM ventas
    GROUP BY cliente_id
)
SELECT *
FROM ventas_por_cliente
WHERE total_unidades >= 3;
GO

/*
###########################################################
CTE VS TABLA TEMPORAL
###########################################################

CTE

✔ Más legible.
✔ Más simple.
✔ Una sola consulta.

TABLA TEMPORAL

✔ Reutilizable.
✔ Permite índices.
✔ Adecuada para grandes volúmenes.
✔ Múltiples transformaciones.

REGLA GENERAL

Si el resultado se utiliza una sola vez:

    CTE

Si el resultado se reutiliza varias veces:

    TABLA TEMPORAL
*/

/*
Ejemplo tabla temporal.
*/

SELECT
    cliente_id,
    SUM(cantidad) AS total_unidades
INTO #ventas_por_cliente
FROM ventas
GROUP BY cliente_id;

SELECT *
FROM #ventas_por_cliente;

DROP TABLE #ventas_por_cliente;
GO

/*
###########################################################
SECCIÓN 3 - STORED PROCEDURES
###########################################################

¿QUÉ ES UN STORED PROCEDURE?

Es un conjunto de instrucciones SQL almacenadas
dentro de SQL Server.

Puede recibir parámetros.

Puede reutilizarse múltiples veces.

VENTAJAS

- Reutilización.
- Centralización de lógica.
- Automatización.
- Mantenimiento sencillo.

DESVENTAJAS

- Puede volverse complejo.
- Puede ocultar lógica crítica.
- Puede crecer demasiado.

CUÁNDO UTILIZARLO

✔ ETLs.
✔ Automatizaciones.
✔ Procesos repetitivos.
✔ Consultas parametrizadas.

CUÁNDO EVITARLO

✖ Aplicaciones completas.
✖ Reglas complejas de negocio.
✖ Procesos difíciles de mantener.
*/

CREATE PROCEDURE sp_listar_clientes
AS
BEGIN

    SELECT *
    FROM clientes;

END;
GO

EXEC sp_listar_clientes;
GO

/*
Stored Procedure con parámetros.
*/

CREATE PROCEDURE sp_clientes_por_ciudad
(
    @ciudad VARCHAR(50)
)
AS
BEGIN

    SELECT *
    FROM clientes
    WHERE ciudad = @ciudad;

END;
GO

EXEC sp_clientes_por_ciudad 'Bogotá';
GO

EXEC sp_clientes_por_ciudad 'Cali';
GO

/*
###########################################################
SECCIÓN 4 - TRIGGERS
###########################################################

¿QUÉ ES UN TRIGGER?

Es un procedimiento que se ejecuta
automáticamente cuando ocurre un evento.

Eventos comunes:

- INSERT
- UPDATE
- DELETE

VENTAJAS

- Auditoría.
- Históricos.
- Validaciones automáticas.

DESVENTAJAS

- Difíciles de identificar.
- Pueden afectar rendimiento.
- Generan lógica oculta.

CUÁNDO UTILIZARLOS

✔ Auditoría.
✔ Históricos.
✔ Trazabilidad.

CUÁNDO EVITARLOS

✖ ETLs.
✖ Integraciones.
✖ Procesamientos pesados.
*/

/*
Tabla de auditoría.
*/

CREATE TABLE auditoria_clientes
(
    auditoria_id INT IDENTITY(1,1),
    cliente_id INT,
    nombre VARCHAR(100),
    fecha_evento DATETIME
);
GO

/*
Trigger de auditoría.
*/

CREATE TRIGGER trg_clientes_insert
ON clientes
AFTER INSERT
AS
BEGIN

    INSERT INTO auditoria_clientes
    (
        cliente_id,
        nombre,
        fecha_evento
    )
    SELECT
        cliente_id,
        nombre,
        GETDATE()
    FROM inserted;

END;
GO

/*
Probar el trigger.
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
    100,
    'Cliente Trigger',
    'Bogotá',
    GETDATE()
);
GO

/*
Verificar auditoría.
*/

SELECT *
FROM auditoria_clientes;
GO

/*
###########################################################
COMPARACIÓN FINAL
###########################################################

VIEW

- Consulta reutilizable.
- No recibe parámetros.
- Se comporta como tabla.

CTE

- Resultado temporal.
- Existe durante una consulta.
- Mejora legibilidad.

TABLA TEMPORAL

- Resultado temporal físico.
- Reutilizable.
- Ideal para procesos complejos.

STORED PROCEDURE

- Proceso reutilizable.
- Puede recibir parámetros.
- Muy utilizado en ETLs.

TRIGGER

- Ejecución automática.
- Responde a eventos.
- Utilizado para auditoría.

###########################################################
EJERCICIOS
###########################################################

1. Cree una vista que muestre únicamente
   los clientes de Bogotá.

2. Cree un CTE que calcule el total de
   ventas por cliente.

3. Cree un CTE que muestre únicamente
   clientes con más de 2 ventas.

4. Cree una tabla temporal con el total
   de ventas por producto.

5. Cree un Stored Procedure que liste
   todos los productos.

6. Cree un Stored Procedure que reciba
   una ciudad y filtre clientes.

7. Inserte un nuevo cliente y valide
   que el Trigger registre el evento.

8. Compare las diferencias entre:

   - View y CTE
   - CTE y Tabla Temporal
   - Stored Procedure y Trigger

###########################################################
PREGUNTAS DE REFLEXIÓN
###########################################################

1. ¿Por qué una View no reemplaza una tabla?

2. ¿Cuándo utilizarías un CTE y cuándo
   una tabla temporal?

3. ¿Por qué un Stored Procedure puede ser
   útil en un proceso ETL?

4. ¿Por qué un Trigger puede generar
   problemas de rendimiento?

5. ¿Qué riesgos existen cuando una base
   de datos tiene demasiados Triggers?

###########################################################
FIN DEL LABORATORIO
###########################################################
*/