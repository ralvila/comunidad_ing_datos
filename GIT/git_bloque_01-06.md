# Introducción a Git y GitHub

## Objetivo General

Al finalizar este módulo, el participante será capaz de utilizar Git y GitHub para gestionar versiones de código, colaborar en proyectos de equipo, trabajar con ramas, resolver conflictos y aplicar buenas prácticas utilizadas en proyectos reales de Ingeniería de Datos y Databricks.

---

# BLOQUE 1 — Fundamentos de Control de Versiones

## Objetivo

Comprender qué es el control de versiones, por qué existe Git y cuáles son los conceptos fundamentales para trabajar de forma profesional en proyectos de software y datos.

---

## ¿Qué es un sistema de control de versiones?

Un sistema de control de versiones (Version Control System - VCS) permite almacenar el historial de cambios realizados sobre archivos y proyectos.

### Problema sin control de versiones

Es común encontrar archivos como:

```text
reporte_final.xlsx
reporte_final_v2.xlsx
reporte_final_v3.xlsx
reporte_final_definitivo.xlsx
reporte_final_ahora_si.xlsx
```

Esto genera:

- Pérdida de trazabilidad.
- Dificultad para identificar cambios.
- Problemas al trabajar en equipo.
- Riesgo de sobrescribir trabajo.

### Beneficios

- Historial completo de cambios.
- Recuperación de versiones anteriores.
- Trabajo colaborativo.
- Auditoría de modificaciones.
- Mayor seguridad en los desarrollos.

---

## ¿Qué es Git?

Git es un sistema de control de versiones distribuido creado por Linus Torvalds en 2005.

### Características

- Gratuito y Open Source.
- Muy rápido.
- Distribuido.
- Permite trabajo offline.
- Estándar de la industria.

---

## Git vs GitHub

### Git

Es la herramienta de control de versiones.

### GitHub

Es una plataforma que almacena repositorios Git en la nube y agrega funcionalidades colaborativas.

| Git | GitHub |
|------|---------|
| Herramienta | Plataforma |
| Funciona localmente | Funciona en la nube |
| Control de versiones | Colaboración |
| Gratuito | Tiene planes gratuitos y pagos |

---

## Conceptos fundamentales

### Repositorio

Contenedor donde Git almacena el historial del proyecto.

### Commit

Fotografía del estado del proyecto en un momento específico.

### Branch

Línea independiente de desarrollo.

### Merge

Proceso de unir cambios entre ramas.

### Remote

Repositorio remoto alojado en GitHub.

---

## Arquitectura de Git

```text
Working Directory
        │
        ▼
Staging Area
        │
        ▼
Local Repository
        │
        ▼
Remote Repository (GitHub)
```

### Working Directory

Archivos que estamos modificando.

### Staging Area

Zona temporal donde seleccionamos cambios para un commit.

### Local Repository

Historial almacenado localmente.

### Remote Repository

Repositorio compartido en GitHub.

---

## Flujo básico

```text
Modificar archivo
        │
        ▼
git add
        │
        ▼
git commit
        │
        ▼
git push
```

---

## Ejemplo práctico

```bash
git init

echo "Hola Git" > archivo.txt

git add archivo.txt

git commit -m "Primer commit"
```

---

## Ejercicio

1. Crear una carpeta llamada `mi_primer_repo`.
2. Inicializar Git.
3. Crear un archivo README.
4. Realizar el primer commit.

---

# BLOQUE 2 — Primeros pasos con Git y GitHub

## Objetivo

Configurar Git, crear repositorios y conectarlos con GitHub.

---

## Instalación

### Git

Descargar desde:

https://git-scm.com

---

## Herramientas recomendadas

### VS Code

Editor recomendado para el curso.

### Git Bash

Terminal incluida con Git.

---

## Configuración inicial

### Configurar usuario

```bash
git config --global user.name "Tu Nombre"
```

### Configurar correo

```bash
git config --global user.email "correo@empresa.com"
```

### Ver configuración

```bash
git config --list
```

---

## Crear repositorio local

```bash
git init
```

---

## Estados de un archivo

```text
Untracked
Tracked
Modified
Staged
Committed
```

---

## Comandos básicos

### Ver estado

```bash
git status
```

### Agregar archivos

```bash
git add archivo.py
```

### Agregar todo

```bash
git add .
```

### Crear commit

```bash
git commit -m "Descripción"
```

### Ver historial

```bash
git log
```

---

## Crear repositorio en GitHub

1. Crear cuenta.
2. Crear repositorio.
3. Copiar URL.

---

## Conectar repositorio local

```bash
git remote add origin URL_REPOSITORIO
```

Ejemplo:

```bash
git remote add origin https://github.com/usuario/proyecto.git
```

---

## Enviar cambios

```bash
git push -u origin main
```

---

## Descargar cambios

```bash
git pull
```

---

## README.md

Archivo principal de documentación.

Ejemplo:

```markdown
# Proyecto ETL

Proyecto de ejemplo para aprender Git.
```

---

## .gitignore

Permite ignorar archivos.

Ejemplo:

```text
__pycache__/
*.pyc
.env
.venv/
```

---

## Ejercicio

Crear un repositorio GitHub y publicar un proyecto Python.

---

# BLOQUE 3 — Branches y Trabajo Paralelo

## Objetivo

Aprender a trabajar con ramas para desarrollar funcionalidades de forma segura.

---

## ¿Qué es una rama?

Una rama permite desarrollar cambios sin afectar la versión principal.

---

## Estructura básica

```text
main
 ├── feature/login
 ├── feature/api
 └── feature/reportes
```

---

## Ver ramas

```bash
git branch
```

---

## Crear rama

```bash
git branch feature-login
```

---

## Cambiar de rama

```bash
git checkout feature-login
```

---

## Crear y cambiar

```bash
git checkout -b feature-login
```

---

## Método moderno

```bash
git switch -c feature-login
```

---

## Fusionar cambios

```bash
git merge feature-login
```

---

## Fast Forward

Git simplemente avanza el puntero.

---

## Merge Commit

Git genera un commit especial de integración.

---

## Eliminar rama

```bash
git branch -d feature-login
```

---

## Buenas prácticas

### Features

```text
feature/login
feature/clientes
feature/api-productos
```

### Correcciones

```text
bugfix/error-fecha
```

### Emergencias

```text
hotfix/error-produccion
```

---

## Ejercicio

Desarrollar dos funcionalidades simultáneamente utilizando ramas.

---

# BLOQUE 4 — GitHub Profesional

## Objetivo

Aprender flujos colaborativos utilizados en equipos reales.

---

## Pull Requests

Un Pull Request permite solicitar la integración de cambios.

---

## Flujo

```text
Branch
  ↓
Push
  ↓
Pull Request
  ↓
Review
  ↓
Merge
```

---

## Beneficios

- Revisión de código.
- Control de calidad.
- Discusión técnica.
- Prevención de errores.

---

## Code Review

### Revisar

- Calidad del código.
- Legibilidad.
- Seguridad.
- Rendimiento.
- Buenas prácticas.

---

## Opciones

### Approve

```text
Apruebo los cambios.
```

### Request Changes

```text
Se requieren ajustes.
```

### Comment

```text
Comentario informativo.
```

---

## GitHub Issues

Permiten gestionar tareas.

Ejemplo:

```text
#12 Crear proceso ETL
```

---

## Milestones

Agrupan múltiples tareas.

---

## GitHub Projects

Permiten crear tableros Kanban.

```text
To Do
Doing
Done
```

---

## Protección de ramas

Recomendado proteger:

```text
main
master
```

---

## Reglas recomendadas

- No permitir push directo.
- Requerir Pull Request.
- Requerir aprobación.
- Ejecutar validaciones automáticas.

---

## Ejercicio

Crear Pull Request entre compañeros y realizar revisión cruzada.

---

# BLOQUE 5 — Conflictos, Historial y Recuperación

## Objetivo

Comprender cómo resolver problemas comunes y recuperar cambios.

---

## Historial

```bash
git log
```

Versión resumida:

```bash
git log --oneline
```

---

## Comparar cambios

```bash
git diff
```

---

## ¿Qué es un conflicto?

Ocurre cuando dos cambios afectan la misma sección del código.

---

## Ejemplo

```text
<<<<<<< HEAD
print("Versión A")
=======
print("Versión B")
>>>>>>> feature
```

---

## Resolver conflicto

1. Analizar cambios.
2. Decidir resultado final.
3. Eliminar marcas.
4. Guardar archivo.
5. Commit.

---

## Restaurar cambios

```bash
git restore archivo.py
```

---

## Revertir commit

```bash
git revert HASH
```

---

## Reset

### Soft

```bash
git reset --soft HASH
```

### Mixed

```bash
git reset HASH
```

### Hard

```bash
git reset --hard HASH
```

---

## Recuperar commits eliminados

```bash
git reflog
```

---

## Ejercicio

Generar conflictos intencionalmente y resolverlos.

---

# BLOQUE 6 — Git para Ingeniería de Datos y Databricks

## Objetivo

Aplicar Git en proyectos reales de datos.

---

## ¿Qué debe versionarse?

### Sí

- Código Python.
- SQL.
- Notebooks.
- Configuraciones.
- Infraestructura.
- Documentación.

### No

- Datos.
- Archivos temporales.
- Credenciales.
- Secretos.

---

## Estructura profesional

```text
proyecto/
│
├── src/
├── notebooks/
├── tests/
├── docs/
├── config/
├── README.md
└── .gitignore
```

---

## Git y Databricks Repos

### ¿Qué son?

Integración nativa entre GitHub y Databricks.

Permiten:

- Sincronizar notebooks.
- Trabajar con ramas.
- Crear Pull Requests.
- Integrarse con CI/CD.

---

## Flujo recomendado

```text
main
  │
  └── feature
          │
          ▼
     Pull Request
          │
          ▼
        Merge
          │
          ▼
       Deploy
```

---

## Introducción a CI/CD

### CI

Continuous Integration.

Validación automática de cambios.

### CD

Continuous Delivery / Deployment.

Despliegue automatizado.

---

## GitHub Actions

Ejemplo:

```yaml
name: Python Tests

on:
  push:

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: Ejecutar pruebas
        run: pytest
```

---

## Versionado Semántico

Formato:

```text
MAJOR.MINOR.PATCH
```

Ejemplos:

```text
1.0.0
1.1.0
1.1.1
2.0.0
```

### MAJOR

Cambios incompatibles.

### MINOR

Nuevas funcionalidades.

### PATCH

Correcciones.

---

## Proyecto Final

El estudiante deberá:

- Crear repositorio GitHub.
- Trabajar mediante ramas.
- Resolver conflictos.
- Crear Pull Requests.
- Realizar Code Review.
- Documentar el proyecto.
- Publicar una versión estable.

---

# Resultados Esperados

Al finalizar el módulo el participante podrá:

✅ Utilizar Git localmente.

✅ Trabajar con GitHub profesionalmente.

✅ Crear y administrar ramas.

✅ Resolver conflictos.

✅ Realizar Pull Requests.

✅ Ejecutar revisiones de código.

✅ Aplicar Git en proyectos colaborativos.

✅ Trabajar con Databricks Repos.

✅ Comprender los fundamentos de CI/CD.

✅ Aplicar buenas prácticas utilizadas en equipos de Ingeniería de Datos.