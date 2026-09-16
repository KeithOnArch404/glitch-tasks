import sqlite3

db = sqlite3.connect("glitch.db")
cursor = db.cursor()

cursor.execute(""" CREATE TABLE IF NOT EXISTS tasks( id INTEGER PRIMARY KEY AUTOINCREMENT, tarea TEXT NOT NULL, completa INTEGER NOT NULL)""")

db.commit()

def pedir_numero(mensaje):
    try:
        numero = int(input(mensaje))
        
    except ValueError:
        print("[!] El ID debe ser un numero.")
        return None
        
    return numero

def show():
    print("[GLITCH TASK]")
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
        print("[!] No se encontraron resultados!")
        print()
        return
    
    pendientes = []
    completadas = []
    
    for task in resultados:
        if task[2] == 0:
            pendientes.append(task)
        else:
            completadas.append(task)
    
    print()
    print("        [TAREAS GLITCH!]")
    print()
    print("====PENDIENTES=====================")
    print()
    for task in pendientes:
        print(f"{task[0]} [ ]: {task[1]}")
    print()
    print("====COMPLETADAS====================")
    print()
    for task in completadas:
        print(f"{task[0]} [x]: {task[1]}")
    print()
    print("===================================")
    print()
    
def show_tasks():
    cursor.execute("SELECT * FROM tasks")
    resultados = cursor.fetchall()
    
    mostrar_resultados(resultados)
    
    cursor.execute(
        "SELECT COUNT(*) FROM tasks WHERE completa = 1"
    )
    completas = cursor.fetchone()[0]
    
    cursor.execute(
        "SELECT COUNT(*) FROM tasks WHERE completa = 0"
    )
    incompletas = cursor.fetchone()[0]
    
    total = completas + incompletas
    
    if total > 0:
        porcentaje = completas / total * 100
    else:
        porcentaje = 0
        
    print("        [ESTADISTICAS]")
    print()
    print(f"Total: {total}")
    print(f"Completadas: {completas}")
    print(f"Pendientes: {incompletas}")
    print(f"Progreso: {porcentaje:.1f}%")
    print()
     
def add_task():
    task_input = input("Agregar tarea: ")
    
    if task_input == "":
        print("[!] Debes agregar un nombre!")
        return
        
    cursor.execute(
        "INSERT INTO tasks (tarea, completa) VALUES (?,?)", (task_input, 0)
        )
        
    db.commit()
        
    print("[+] Tarea agregada!")
    print()
    
def complete_task():
    complete = pedir_numero("Que tarea deseas completar?: ")
        
    if complete is None:
        return
    
    cursor.execute(
        "UPDATE tasks SET completa = 1 WHERE id = ?", (complete,)
        )
        
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
    
    cursor.execute(
        "UPDATE tasks SET completa = 0 WHERE id = ?", (unmark,)
    )
    
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
        
    cursor.execute(
        "DELETE FROM tasks WHERE id = ?", (borrar,)
        )
        
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
    
    task_edit = input("Escribe la nueva tarea: ")
    
    cursor.execute("UPDATE tasks SET tarea = ? WHERE id = ?", (task_edit,edit)
    )
    
    db.commit()
    
    if cursor.rowcount == 1:
        print("[*] Tarea editada!")
    else:
        print("[!] No se encontro esa tarea!")
        
    print()
    
def search_task():
    busqueda = input("Que tarea deseas buscar?: ")
    
    if busqueda == "":
        show_tasks()
        return
    
    cursor.execute(
        "SELECT * FROM tasks WHERE tarea LIKE ?", (f"%{busqueda}%",)
        )
    
    resultados = cursor.fetchall()
    
    mostrar_resultados(resultados)
    
while True:
    show()
    choice = input("\n> ")
    
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
    
db.close()