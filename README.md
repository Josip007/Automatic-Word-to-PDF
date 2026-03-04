# 📄 docx-to-pdf-watcher

A simple Python tool that automatically converts Word documents (.docx) to PDF whenever a file is added or modified in a watched folder.

The application monitors a folder in real time and triggers a conversion pipeline whenever a Word document is created or changed.

---

# 🚀 Features

- Automatic Word → PDF conversion
- Real-time filesystem monitoring using watchdog
- Uses Microsoft Word COM automation for accurate PDF export
- Retry mechanism to handle file locks during saving
- Debounce logic to prevent multiple conversions triggered by Word save events
- Clean modular structure for easy extension

---

# ⚙️ How it works

The application continuously watches a folder and reacts to filesystem events.

User saves Word document  
↓  
Filesystem event detected  
↓  
Watchdog observer  
↓  
WordHandler event handler  
↓  
Debounce filter  
↓  
Word → PDF conversion  
↓  
PDF file created  

---

# 📦 Requirements

- Windows OS
- Microsoft Word installed
- Python 3.8+

This project uses Word automation via COM, so it only works on Windows systems with Microsoft Word installed.

---

# 🛠 Installation

Clone the repository:

git clone https://github.com/your-username/docx-to-pdf-watcher.git  
cd docx-to-pdf-watcher

Install dependencies:

pip install -r requirements.txt

Create the watched folder:

mkdir Documents

---

# ▶️ Usage

Start the watcher:

python main.py

Now copy or save any .docx file into the Documents/ folder.

The program will automatically generate a corresponding .pdf file in the same folder.

Example:

Documents/  
report.docx  
report.pdf  

---

# 📁 Project Structure

docx-to-pdf-watcher

main.py        → Application entry point  
watcher.py     → Filesystem event handling  
converter.py   → Word → PDF conversion logic  
requirements.txt  
Documents      → Folder monitored for Word files  

---

# ⚠️ Limitations

- Works only on Windows
- Requires Microsoft Word to be installed
- Conversion relies on Word COM automation

---

# 🔮 Future Improvements

Possible extensions for this project:

- Extract text from generated PDFs
- AI-based document summarization
- Export structured document data as JSON
- Batch document processing
- Cloud storage integration

Potential future pipeline:

Word → PDF → Text Extraction → AI Summary → JSON Output

---

# 📜 License

MIT License

---

# 👨‍💻 Author

Built as a small automation tool and learning project using:

Python  
Watchdog  
Windows COM automation  
Microsoft Word