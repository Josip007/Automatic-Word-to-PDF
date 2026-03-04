import time
from watchdog.events import FileSystemEventHandler
from converter import convert_to_pdf

# Dictionary used to store the last time a file was converted
# This helps prevent multiple conversions triggered by rapid filesystem events
last_converted = {}



class WordHandler(FileSystemEventHandler):

    def should_convert(self, path):
        """
            Filesystem event handler that reacts to Word document changes.

            This handler listens for file creation and modification events
            and triggers the Word → PDF conversion pipeline.
            Word often triggers multiple filesystem events when saving
            a document. This function prevents repeated conversions within a short time window (debounce mechanism).
        """
        now = time.time()
        last = last_converted.get(path, 0)

        if now - last < 5:
            return False

        last_converted[path] = now
        return True


    def on_created(self, event):
        # Triggered on new file creation
        if event.src_path.endswith(".docx") and "~$" not in event.src_path:

            if self.should_convert(event.src_path):

                print("New word file detected:", event.src_path)
                time.sleep(1)
                convert_to_pdf(event.src_path)

    def on_modified(self, event):
        # Triggered on modified files
        if event.src_path.endswith(".docx") and "~$" not in event.src_path:

            if self.should_convert(event.src_path):

                print("Word file modified:", event.src_path)
                time.sleep(1)
                convert_to_pdf(event.src_path)