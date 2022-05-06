# Gustavo Cocone Zavaleta | GitHub: @EgirlBuchona | © 2022
# Proyecto: Gestor de Eventos en Python

class GestorEventos:
    def __init__(self):
        self.eventos = []

    def crear_evento(self, nombre, fecha, descripcion):
        evento = {"nombre": nombre, "fecha": fecha, "descripcion": descripcion}
        self.eventos.append(evento)
        print(f"Evento '{nombre}' creado exitosamente.")

    def eliminar_evento(self, nombre):
        for evento in self.eventos:
            if evento["nombre"] == nombre:
                self.eventos.remove(evento)
                print(f"Evento '{nombre}' eliminado exitosamente.")
                return
        print(f"No se encontró el evento '{nombre}'.")

    def modificar_evento(self, nombre, nuevo_nombre=None, nueva_fecha=None, nueva_descripcion=None):
        for evento in self.eventos:
            if evento["nombre"] == nombre:
                if nuevo_nombre:
                    evento["nombre"] = nuevo_nombre
                if nueva_fecha:
                    evento["fecha"] = nueva_fecha
                if nueva_descripcion:
                    evento["descripcion"] = nueva_descripcion
                print(f"Evento '{nombre}' modificado exitosamente.")
                return
        print(f"No se encontró el evento '{nombre}'.")

    def listar_eventos(self):
        if not self.eventos:
            print("No hay eventos registrados.")
            return
        print("Lista de eventos:")
        for evento in self.eventos:
            print(f"Nombre: {evento['nombre']}, Fecha: {evento['fecha']}, Descripción: {evento['descripcion']}")

if __name__ == "__main__":
    gestor = GestorEventos()
    while True:
        print("\nGestor de Eventos")
        print("1. Crear evento")
        print("2. Eliminar evento")
        print("3. Modificar evento")
        print("4. Listar eventos")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            nombre = input("Nombre del evento: ")
            fecha = input("Fecha del evento: ")
            descripcion = input("Descripción del evento: ")
            gestor.crear_evento(nombre, fecha, descripcion)
        elif opcion == "2":
            nombre = input("Nombre del evento a eliminar: ")
            gestor.eliminar_evento(nombre)
        elif opcion == "3":
            nombre = input("Nombre del evento a modificar: ")
            nuevo_nombre = input("Nuevo nombre (dejar vacío si no desea cambiar): ")
            nueva_fecha = input("Nueva fecha (dejar vacío si no desea cambiar): ")
            nueva_descripcion = input("Nueva descripción (dejar vacío si no desea cambiar): ")
            gestor.modificar_evento(nombre, nuevo_nombre or None, nueva_fecha or None, nueva_descripcion or None)
        elif opcion == "4":
            gestor.listar_eventos()
        elif opcion == "5":
            print("Saliendo del Gestor de Eventos.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")
