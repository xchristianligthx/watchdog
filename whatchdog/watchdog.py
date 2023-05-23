import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Clase que maneja los eventos del sistema de archivos
class FileEventHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        # Se ejecuta cuando ocurre cualquier evento en el sistema de archivos
        if event.is_directory:
            # Si es un directorio
            return
        elif event.event_type == 'created':
            # Si se crea un archivo
            print(f"Archivo creado: {event.src_path}")
            # Aquí puedes agregar tu lógica para realizar acciones con el archivo recién creado

# Ruta del directorio a monitorear
directory_to_watch = 'C:\Users\christian\Desktop\whatchdog'

# Crea un observador y asócialo con la clase que maneja los eventos
observer = Observer()
observer.schedule(FileEventHandler(), path=directory_to_watch, recursive=True)

# Inicia el observador en un hilo separado
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    # Detiene el observador si se presiona Ctrl + C
    observer.stop()

# Espera a que el observador termine antes de salir
observer.join()
