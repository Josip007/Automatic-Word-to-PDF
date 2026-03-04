from pathlib import Path
import time
import pythoncom
import win32com.client

"""
    Defining a function for converting a Word (.docx) document to PDF.
    This function uses Microsoft Word COM automation.
"""

# Initializing COM for the current thread.
def convert_to_pdf(docx_path):

    pythoncom.CoInitialize()
    word = None

    try:
        abs_path = str(Path(docx_path).resolve())
        pdf_path = str(Path(abs_path).with_suffix(".pdf"))

        word = win32com.client.Dispatch("Word.Application")
        word.Visible = False
        word.DisplayAlerts = False

        doc = None

        for attempt in range(5):
            try:
                time.sleep(1)
                doc = word.Documents.Open(
                    abs_path,
                    ConfirmConversions=False,
                    ReadOnly=True,
                    AddToRecentFiles=False
                )
                print("Opened on attempt:", attempt + 1)
                break
            except Exception as e:
                print("Attempt", attempt + 1, "failed:", e)

        if doc is None:
            print("Could not open file")
            return

        doc.SaveAs(pdf_path, FileFormat=17)
        doc.Close(SaveChanges=False)

        print("PDF created:", pdf_path)

    finally:
        if word:
            word.Quit()
        pythoncom.CoUninitialize()