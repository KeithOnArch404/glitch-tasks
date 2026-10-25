import sqlite3

def get_connection():
    return sqlite3.connect("glitch.db")

def init_db():
    with get_connection() as db:
        cursor = db.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                tarea TEXT NOT NULL,
                completa INTEGER NOT NULL DEFAULT 0
            )
        """)
        db.commit()

def pedir_numero(mensaje):
    try:
        numero = int(input(mensaje).strip())
        if numero <= 0:
            print("[!] El ID debe de ser un numero positivo.")
            return None
        return numero
    except ValueError:
        print("[!] El ID debe ser un numero.")
        return None

def show():
    print("\n[GLITCH TASK]")
    print()
    print("1. ver tarea")
    print("2. agregar tarea")
    print("3. completar tarea")
    print("4. desmarcar tarea")
    print("5. borrar tarea")
    print("6. editar tarea")
    print("7. buscar tarea")
    print("x. salir")
    
def mostrar_resultados(resultados):
    if not resultados:
        print("[!] No se encontraron resultados!\n")
        return
    
    pendientes = [t for t in resultados if t[2] == 0]
    completadas = [t for t in resultados if t[2] == 1]
    
    print("\n        [TAREAS GLITCH!]\n")
    print("====PENDIENTES=====================\n")
    for task in pendientes:
        print(f"{task[0]} [ ]: {task[1]}")
        
    print("\n====COMPLETADAS====================\n")
    for task in completadas:
        print(f"{task[0]} [x]: {task[1]}")
        
    print("\n===================================\n")
    
def show_tasks():
    with get_connection() as db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM tasks")
        resultados = cursor.fetchall()
        mostrar_resultados(resultados)
    
        cursor.execute("SELECT COUNT(*) FROM tasks WHERE completa = 1")
        completas = cursor.fetchone()[0]
        cursor.execute("SELECT COUNT(*) FROM tasks WHERE completa = 0")
        incompletas = cursor.fetchone()[0]
        total = completas + incompletas
        porcentaje = (completas / total * 100) if total > 0 else 0
        
        print("        [ESTADISTICAS]")
        print(f"Total: {total}")
        print(f"Completadas: {completas}")
        print(f"Pendientes: {incompletas}")
        print(f"Progreso: {porcentaje:.1f}%\n")

def add_task():
    task_input = input("Agregar tarea: ").strip()
    if not task_input:
        print("[!] Debes agregar un nombre!\n")
        return

    with get_connection() as db:
        cursor = db.cursor()
        cursor.execute("INSERT INTO tasks (tarea, completa) VALUES (?, 0)", (task_input,))
        db.commit()
        print("[+] Tarea agregada!\n")

def complete_task():
    complete = pedir_numero("Que tarea deseas completar?: ")
    if complete is None:
        return

    with get_connection() as db:
        cursor = db.cursor()
        cursor.execute("UPDATE tasks SET completa = 1 WHERE id = ?", (complete,))
        db.commit()
        if cursor.rowcount == 1:
            print("[x] Tarea completada!")
        else:
            print("[!] No se encontro esa tarea!")
        print()
    
def unmark_task():
    unmark = pedir_numero("Que tarea deseas desmarcar?: ")
    if unmark is None:
        return
    
    with get_connection() as db:
        cursor = db.cursor()
        cursor.execute("UPDATE tasks SET completa = 0 WHERE id = ?", (unmark,))
        db.commit()
        if cursor.rowcount == 1:
            print("[<-] Tarea desmarcada!")
        else:
            print("[!] No se encontro esa tarea!")
        print()
    
def delete_task():
    borrar = pedir_numero("Que tarea deseas eliminar?: ")
    if borrar is None:
        return

    confirm = input(f"Seguro que deseas eliminar la tarea {borrar}? (s/n): ").strip().lower()
    if confirm != "s":
        print("[!] Cancelado\n")
        return

    with get_connection() as db:
        cursor = db.cursor()
        cursor.execute("DELETE FROM tasks WHERE id = ?", (borrar,))
        db.commit()
        if cursor.rowcount == 1:
            print("[-] Tarea eliminada!")
        else:
            print("[!] No se encontro esa tarea!")
        print()
    
def edit_task():
    edit = pedir_numero("Que tarea deseas editar?: ")
    if edit is None:
        return
    
    with get_connection() as db:
        cursor = db.cursor()
        cursor.execute("SELECT tarea FROM tasks WHERE id = ?", (edit,))
        resultado = cursor.fetchone()
   
        if not resultado:
            print("[!] No se encontro la tarea!\n")
            return 
    
        print(f"Tarea actual: {resultado[0]}")
        task_edit = input("Escribe la nueva tarea: ").strip()

        if not task_edit:
            print("[!] El nombre no puede estar vacio!\n")
            return

        cursor.execute("UPDATE tasks SET tarea = ? WHERE id = ?", (task_edit,edit))
        db.commit()
        print("[*] Tarea editada\n")

def search_task():
    busqueda = input("Que tarea deseas buscar?: ").strip()
    if busqueda == "":
        show_tasks()
        return

    with get_connection() as db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM tasks WHERE tarea LIKE ? COLLATE NOCASE", (f"%{busqueda}%",))
        resultados = cursor.fetchall()
        mostrar_resultados(resultados)

init_db()

while True:
    show()
    choice = input("\n> ").strip().lower()
    
    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        complete_task()
    elif choice == "4":
        unmark_task()
    elif choice == "5":
        delete_task()
    elif choice == "6":
        edit_task()
    elif choice == "7":
        search_task()
    elif choice == "x":
        print("Hasta luego!")
        break
    else:
        print("[!] Opcion no valida, intenta de nuevo.")