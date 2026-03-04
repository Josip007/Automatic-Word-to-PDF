import pdfplumber
from pathlib import Path
from transformers import pipeline
import time
import torch

# Use GPU if available for faster inference, otherwise fall back to CPU.
# Note: PyTorch GPU acceleration works best with NVIDIA GPUs (CUDA support).
# AMD GPUs are generally not supported unless using ROCm on Linux.
device = 0 if torch.cuda.is_available() else -1
print(f"Using: {'GPU' if device == 0 else 'CPU'}")

print("Loading AI model...")
summarizer = pipeline("summarization", model="facebook/bart-large-cnn", device=device)
print("Model ready.")


def extract_text_from_pdf(pdf_path):
    """Extracts all text content from a PDF file."""
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text.strip()


def summarize_text(text):
    """
        Summarizes the given text using BART model.
        Splits into chunks if text is too long (BART max ~1024 tokens(words)).
    """
    max_chunk_length = 1000
    chunks = [text[i:i + max_chunk_length] for i in range(0, len(text), max_chunk_length)]

    summaries = []
    for i, chunk in enumerate(chunks):
        print(f"Summarizing chunk {i + 1}/{len(chunks)}...")

        # Measure summarization speed per chunk
        start = time.time()
        result = summarizer(chunk, max_length=150, min_length=40, do_sample=False)
        end = time.time()

        print(f"Chunk {i + 1} done in {end - start:.2f}s")
        summaries.append(result[0]["summary_text"])

    return "\n\n".join(summaries)

def process_pdf(pdf_path):
    """ Full pipeline: extracts text from PDF and saves an AI-generated summary as .txt """
    pdf_path = Path(pdf_path)
    txt_path = pdf_path.with_suffix(".txt")

    print("Extracting text from:", pdf_path.name)
    text = extract_text_from_pdf(pdf_path)

    if not text:
        print("No text found in PDF, skipping.")
        return

    print("Generating AI summary...")
    summary = summarize_text(text)

    txt_path.write_text(summary, encoding="utf-8")
    print("Summary saved:", txt_path)

# test(edit path to your liking)
path = Path(r"C:\Users\Josip\Desktop\ai-document-pipeline\Documents\50 page sample PDF.indd.pdf")
process_pdf(path)