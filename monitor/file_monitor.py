from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class FileChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        print(f"[ALERT] Modified: {event.src_path}")

def start_monitor(path="."):
    observer = Observer()
    observer.schedule(FileChangeHandler(), path, recursive=True)
    observer.start()