# GLITCH TASK

A minimal task manager built with Python and SQLite. Terminal + Web version with glitch aesthetics.

A minimal task manager built in Python. It started as a terminal practice using SQLite and evolved into a web version with Flask and glitch animations.

## Overview

GLITCH TASK has two versions sharing the same database:

- CLI: main.py for terminal usage
- WEB: app.py for browser with glitch styled UI

## Features

CLI:
- Create tasks
- View pending and completed tasks
- Complete / uncomplete tasks
- Edit tasks
- Delete tasks
- Search tasks
- Show progress statistics

WEB (Flask):
- Full CRUD in browser
- Glitch / cyberpunk UI with animations
- Mobile responsive (Termux friendly)
- Same SQLite persistence

## Tech Stack

- Python 3.11+
- Flask
- SQLite3
- HTML / CSS / JavaScript

## Installation and Usage

Clone:
  git clone https://github.com/KeithOnArch404/glitch-tasks.git
  cd glitch-tasks

Run terminal version:
  python main.py

Run web version:
  pip install flask
  python app.py
  Then open http://localhost:5000

On Termux:
  pkg install python
  pip install flask
  python app.py

## Database

Uses SQLite glitch.db auto-created on first run.

Table tasks:
- id: INTEGER PRIMARY KEY
- tarea: TEXT
- completa: INTEGER - 0 = pending, 1 = completed

## Project Structure

  glitchtask/
    - main.py
    - app.py
    - database.py
    - templates/index.html
    - static/style.css
    - static/script.js

## Project Status

In active development. Started as a learning exercise for Python and SQLite and grew into a functional task manager with a web interface.

Next: REST API, dark/light toggle, deploy.

Built on Arch + Termux by Keith.

