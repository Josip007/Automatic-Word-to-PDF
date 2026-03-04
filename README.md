# 📄 Automatic Word to PDF + AI Summarization Pipeline

A Python tool that automatically converts Word documents (.docx) to PDF and generates an AI-powered summary whenever a file is added or modified in a watched folder.

The application monitors a folder in real time and triggers a full pipeline whenever a Word document is created or changed.

---

# 🚀 Features

- Automatic Word → PDF conversion
- AI-powered document summarization using Facebook's BART model
- GPU acceleration support (NVIDIA CUDA)
- Real-time filesystem monitoring using watchdog
- Uses Microsoft Word COM automation for accurate PDF export
- Retry mechanism to handle file locks during saving
- Debounce logic to prevent multiple conversions triggered by Word save events
- Clean modular structure for easy extension

---

# ⚙️ How it works

The application continuously watches a folder and reacts to filesystem events.

```
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
Text extraction from PDF
↓
AI summarization (BART model)
↓
PDF + TXT summary saved
```

---

# 📦 Requirements

- Windows OS
- Microsoft Word installed
- Python 3.8+
- NVIDIA GPU (optional, for faster summarization)

This project uses Word automation via COM, so it only works on Windows systems with Microsoft Word installed.

---

# 🛠 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/Automatic-Word-to-PDF.git
cd Automatic-Word-to-PDF
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create the watched folder:

```bash
mkdir Documents
```

---

# ▶️ Usage

Start the watcher:

```bash
python main.py
```

Now copy or save any `.docx` file into the `Documents/` folder.

The program will automatically generate:
- A corresponding `.pdf` file
- A `.txt` file containing an AI-generated summary

Example:

```
Documents/
  report.docx
  report.pdf
  report.txt  ← AI summary
```

---

# 📁 Project Structure

```
Automatic-Word-to-PDF/
  main.py          → Application entry point
  watcher.py       → Filesystem event handling
  converter.py     → Word → PDF conversion logic
  summarizer.py    → Text extraction + AI summarization
  requirements.txt
  Documents/       → Folder monitored for Word files
```

---

# 🤖 AI Model

This project uses [facebook/bart-large-cnn](https://huggingface.co/facebook/bart-large-cnn) for document summarization.

- The model is downloaded automatically on first run (~1.6GB) and cached locally
- GPU is used automatically if available (NVIDIA CUDA), otherwise falls back to CPU

> **Note:** For faster inference on lower-end hardware, replace `facebook/bart-large-cnn` with `sshleifer/distilbart-cnn-12-6` in `summarizer.py` — same quality, 2x faster.

---

# ⚠️ Limitations

- Works only on Windows
- Requires Microsoft Word to be installed
- Conversion relies on Word COM automation
- First run requires ~1.6GB model download

---

# 🔮 Future Improvements

Possible extensions for this project:

- RAG (Retrieval Augmented Generation) for document Q&A
- Export structured document data as JSON
- Batch document processing
- Cloud storage integration
- Support for other document formats

Potential future pipeline:

```
Word → PDF → Text Extraction → AI Summary → JSON Output
                                    ↓
                              RAG Document Q&A
```