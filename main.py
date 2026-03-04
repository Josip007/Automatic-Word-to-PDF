from pathlib import Path
import time
from watchdog.observers import Observer
from watcher import WordHandler

# Directory that will be monitored for Word documents
INPUT_FOLDER = Path("Documents")

# Create an instance of our filesystem event handler
event_handler = WordHandler()

# Register the handler to watch the INPUT_FOLDER
# recursive=False means only this folder is monitored
observer = Observer()
observer.schedule(event_handler, str(INPUT_FOLDER), recursive=False)

observer.start()

print("Watching folder:", INPUT_FOLDER.resolve())

# Keep the program running indefinitely
# The observer runs in a separate thread
try:
    while True:
        time.sleep(2)

# Allow graceful shutdown when pressing CTRL+C
except KeyboardInterrupt:
    observer.stop()

observer.join()