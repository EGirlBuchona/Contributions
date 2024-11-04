import datetime

tasks = []

def add_task(name, priority, deadline):
    """Añade una tarea con nombre, prioridad y fecha límite."""
    task = {
        'name': name,
        'priority': priority,
        'deadline': deadline,
        'created_at': datetime.datetime.now()
    }
    tasks.append(task)
    print(f"Tarea añadida: {name}")

def list_tasks():
    """Lista las tareas ordenadas por prioridad y fecha límite."""
    sorted_tasks = sorted(tasks, key=lambda x: (x['priority'], x['deadline']))
    for task in sorted_tasks:
        status = "Vencida" if task['deadline'] < datetime.datetime.now() else "Pendiente"
        print(f"{task['name']} - Prioridad: {task['priority']} - Fecha límite: {task['deadline']} - Estado: {status}")

if __name__ == "__main__":
    # Ejemplo de uso
    add_task("Terminar proyecto", 1, datetime.datetime(2022, 1, 5))
    add_task("Comprar víveres", 2, datetime.datetime(2022, 1, 4))
    list_tasks()
