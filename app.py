from flask import Flask, render_template, request, redirect, url_for
from database import get_connection, init_db

app = Flask(__name__)

init_db()

@app.route("/")
def home():
    busqueda = request.args.get("q", "").strip()

    with get_connection() as db:
        cursor = db.cursor()

        if busqueda:
            cursor.execute(
                "SELECT * FROM tasks WHERE tarea LIKE ? COLLATE NOCASE",
                (f"%{busqueda}%",)
            )
        else:
            cursor.execute("SELECT * FROM tasks")

        tasks = cursor.fetchall()
        
        cursor.execute("SELECT COUNT(*) FROM tasks")
        total = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(*) FROM tasks WHERE completa = 1")
        completadas = cursor.fetchone()[0]

        pendientes = total - completadas
        progreso = (completadas / total * 100) if total else 0

    return render_template(
    "index.html",
    tasks=tasks,
    busqueda=busqueda,
    total=total,
    completadas=completadas,
    pendientes=pendientes,
    progreso=progreso
)

@app.route("/add", methods=["POST"])
def add_task():
    tarea = request.form["tarea"].strip()
    
    if tarea:
        with get_connection() as db:
            cursor = db.cursor()
            cursor.execute("INSERT INTO tasks (tarea, completa) VALUES (?, 0)", (tarea,))
            db.commit()
    return redirect(url_for("home"))

@app.route("/complete/<int:task_id>", methods=["POST"])
def complete_task(task_id):
    with get_connection() as db:
        cursor = db.cursor()
        cursor.execute("UPDATE tasks SET completa = 1 WHERE id = ?", (task_id,))
        db.commit()
    return redirect(url_for("home"))

@app.route("/unmark/<int:task_id>", methods=["POST"])
def unmark_task(task_id):
    with get_connection() as db:
        cursor = db.cursor()
        cursor.execute("UPDATE tasks SET completa = 0 WHERE id = ?", (task_id,))
        db.commit()
    return redirect(url_for("home"))

@app.route("/edit/<int:task_id>", methods=["POST"])
def edit_task(task_id):
    tarea = request.form.get("tarea","").strip()
    
    if tarea:
        with get_connection() as db:
            cursor = db.cursor()
            cursor.execute(
                "UPDATE tasks SET tarea = ? WHERE id = ?",
                (tarea, task_id)
            )
            db.commit()

    return redirect(url_for("home"))
    
@app.route("/delete/<int:task_id>", methods=["POST"])
def delete_task(task_id):
    with get_connection() as db:
        cursor = db.cursor()
        cursor.execute(
            "DELETE FROM tasks WHERE id = ?",
            (task_id,)
        )
        db.commit()

    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)