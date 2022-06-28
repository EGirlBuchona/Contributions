# Gustavo Cocone Zavaleta | GitHub: @EgirlBuchona | © 2022
# Proyecto: Script para Monitoreo de Archivos en Python

import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MonitorArchivos(FileSystemEventHandler):
    def on_created(self, event):
        print(f"Archivo creado: {event.src_path}")
    
    def on_deleted(self, event):
        print(f"Archivo eliminado: {event.src_path}")
    
    def on_modified(self, event):
        print(f"Archivo modificado: {event.src_path}")
    
    def on_moved(self, event):
        print(f"Archivo movido: {event.src_path} -> {event.dest_path}")

if __name__ == "__main__":
    ruta_monitoreo = input("Ingrese la ruta de la carpeta a monitorear: ").strip()
    
    if not os.path.exists(ruta_monitoreo):
        print("La carpeta no existe. Verifique la ruta.")
        exit()

    print(f"Monitoreando cambios en: {ruta_monitoreo}")
    
    event_handler = MonitorArchivos()
    observer = Observer()
    observer.schedule(event_handler, ruta_monitoreo, recursive=True)

    try:
        observer.start()
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
