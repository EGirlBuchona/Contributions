import os

def find_temp_files(folder_path):
    """Busca archivos temporales en una carpeta específica."""
    temp_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(('.tmp', '.log', '.bak')):
                temp_files.append(os.path.join(root, file))
    return temp_files

def delete_files(files):
    """Elimina los archivos especificados."""
    for file in files:
        try:
            os.remove(file)
            print(f"Archivo eliminado: {file}")
        except Exception as e:
            print(f"No se pudo eliminar {file}: {e}")

if __name__ == "__main__":
    folder_path = input("Ingrese la ruta de la carpeta para limpiar archivos temporales: ")
    temp_files = find_temp_files(folder_path)
    if temp_files:
        print("Archivos temporales encontrados:")
        for file in temp_files:
            print(file)
        confirm = input("¿Desea eliminar estos archivos? (s/n): ")
        if confirm.lower() == 's':
            delete_files(temp_files)
        else:
            print("Operación cancelada.")
    else:
        print("No se encontraron archivos temporales.")
