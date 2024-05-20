import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# pip install watchdog

class USBEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        print("Hello World! USB device detected:", event.src_path)

if __name__ == "__main__":
    path = "E:\\"
    
    event_handler = USBEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    
    try:
        observer.start()
        print(f"Watching for changes in {path}...")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    
    observer.join()
