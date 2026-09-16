# GLITCH TASK

> a simple terminal task manager built with Python and SQLite.

## Descripcion

GLITCH TASK es un gestor de tareas para terminal desarrollado en Python.
Utiliza SQLite para almacenar las tareas de forma permanente.

## Funcionalidades

- Crear tareas
- Ver tareas pendientes y completadas
- Completar tareas
- Desmarcar tareas
- Editar tareas
- Eliminar tareas
- Buscar tareas
- Mostrar estadisticas de progreso
- Guardar las tareas usando SQLite

## Tecnologias

- Python
- SQLite
- SQL
- Markdown

## Como ejecurar

Clona o descarga el proyecto y ejecuta:

```bash
python main.py
```
La base de datos glitch.db se crea automaticamente al ejecutar el programa por primera vez.

## Uso

Al iniciar el programa aparecera un menu con las diferentes opciones disponibles:

```
[GLITCH TASK]

1. ver tarea
2. agregar tarea
3. completar tarea
4. desmarcar tarea
5. borrar tarea
6. editar tarea
7. buscar tarea
x. salir
```

Selecciona una opcion escribiendo el numero correspondiente.

## Base de datos

GLITCH TASK utiliza SQLite para guardar las tareas.

La informacion se guarda en una tabla llamada `tasks`, que contiene:

- `id`: identificador unico de cada tarea.
- `tarea`: nombre o descripcion de la tarea, asignada por el usuario.
- `completa`: indica si la tarea esta completada (`1`) o pendiente (`0`).

Gracias a SQLite, las tareas permanecen guardadas aunque el programa se cierre.

## Estado del proyecto

GLITCH TASK se encuentra actualmente en desarrollo.

El proyecto comenzo como una practica para aprender Python,
y fue creciendo hasta convertirse en un gestor de tareas funcional con persistencia de datos.