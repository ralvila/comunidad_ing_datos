/*
===========================================================
COMUNIDAD DE INGENIERÍA DE DATOS
INTRODUCCIÓN A SQL

BLOQUE 1 - FUNDAMENTOS DE BASES DE DATOS Y SQL
===========================================================

OBJETIVOS

Al finalizar este laboratorio podrás:

- Comprender qué es una base de datos.
- Comprender qué es SQL.
- Entender qué es SQL Server.
- Identificar tablas, filas y columnas.
- Reconocer tipos de datos básicos.
- Comprender Primary Keys.
- Comprender Foreign Keys.
- Entender relaciones entre tablas.
- Explorar un modelo relacional sencillo.

===========================================================
SECCIÓN 1 - ¿QUÉ ES SQL?
===========================================================

SQL (Structured Query Language) es el lenguaje estándar
utilizado para trabajar con bases de datos relacionales.

Con SQL podemos:

- Consultar información.
- Insertar información.
- Actualizar información.
- Eliminar información.

Durante esta capacitación utilizaremos SQL Server.

===========================================================
SECCIÓN 2 - CREACIÓN DE BASE DE DATOS
===========================================================
*/

CREATE DATABASE ComunidadSQL;
GO

USE ComunidadSQL;
GO

/*
===========================================================
SECCIÓN 3 - TIPOS DE DATOS
===========================================================

Algunos tipos de datos comunes:

INT         -> Números enteros
DECIMAL     -> Números decimales
VARCHAR     -> Texto
DATE        -> Fecha
DATETIME    -> Fecha y hora

Crearemos una tabla únicamente para visualizar estos tipos.
*/

CREATE TABLE ejemplo_tipos_datos
(
    id INT,
    nombre VARCHAR(100),
    salario DECIMAL(10,2),
    fecha_nacimiento DATE,
    fecha_registro DATETIME
);

GO

/*
===========================================================
SECCIÓN 4 - TABLAS, FILAS Y COLUMNAS
===========================================================

Una tabla almacena información.

Cada registro corresponde a una fila.

Cada atributo corresponde a una columna.

También introduciremos el concepto de Primary Key.

Una Primary Key identifica de forma única cada registro.
*/

CREATE TABLE clientes
(
    cliente_id INT PRIMARY KEY,
    nombre VARCHAR(100),
    ciudad VARCHAR(50),
    fecha_registro DATE
);

GO

/*
===========================================================
SECCIÓN 5 - OTRA TABLA DEL MODELO
===========================================================

Crearemos una tabla de productos.
*/

CREATE TABLE productos
(
    producto_id INT PRIMARY KEY,
    nombre_producto VARCHAR(100),
    precio DECIMAL(10,2)
);

GO

/*
===========================================================
SECCIÓN 6 - FOREIGN KEYS Y RELACIONES
===========================================================

Una Foreign Key permite relacionar tablas.

En este ejemplo:

- Un cliente puede realizar muchas ventas.
- Un producto puede participar en muchas ventas.

La tabla ventas será la encargada de conectar
clientes y productos.
*/

CREATE TABLE ventas
(
    venta_id INT PRIMARY KEY,

    cliente_id INT,

    producto_id INT,

    cantidad INT,

    fecha_venta DATE,

    CONSTRAINT FK_ventas_clientes
        FOREIGN KEY (cliente_id)
        REFERENCES clientes(cliente_id),

    CONSTRAINT FK_ventas_productos
        FOREIGN KEY (producto_id)
        REFERENCES productos(producto_id)
);

GO

/*
===========================================================
SECCIÓN 7 - CARGA DE DATOS
===========================================================

Insertaremos algunos registros de ejemplo.
*/

INSERT INTO clientes
VALUES
(1,'Ana','Bogotá','2024-01-15'),
(2,'Carlos','Medellín','2024-02-01'),
(3,'Laura','Cali','2024-03-10');

GO

INSERT INTO productos
VALUES
(1,'Laptop',3500.00),
(2,'Mouse',80.00),
(3,'Teclado',120.00);

GO

INSERT INTO ventas
VALUES
(1,1,1,1,'2024-05-01'),
(2,1,2,2,'2024-05-02'),
(3,2,3,1,'2024-05-03'),
(4,3,1,1,'2024-05-05');

GO

/*
===========================================================
SECCIÓN 8 - EXPLORANDO LOS DATOS
===========================================================

Podemos consultar la información almacenada
utilizando SELECT.
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

/***********************************************************
MODELO RELACIONAL
************************************************************

                clientes
                    |
                    |
             cliente_id
                    |
                    |
                  ventas
                    |
                    |
             producto_id
                    |
                    |
                productos

Relaciones:

clientes (1) ------ (N) ventas

productos (1) ----- (N) ventas

************************************************************/

/*
===========================================================
EJERCICIOS
===========================================================

1. Inserte un nuevo cliente.

2. Inserte un nuevo producto.

3. Inserte una nueva venta.

4. Consulte todos los registros de la tabla clientes.

5. Consulte todos los registros de la tabla productos.

6. Consulte todos los registros de la tabla ventas.

7. Identifique cuáles son las Primary Keys
   de cada tabla.

8. Identifique cuáles son las Foreign Keys
   de la tabla ventas.

9. Explique la relación entre clientes y ventas.

10. Explique la relación entre productos y ventas.

11. Dibuje el modelo relacional de esta base de datos.

===========================================================
FIN DEL LABORATORIO
===========================================================
*/