"""Input handling for podcast source documents."""

from pathlib import Path
from typing import List

from pypdf import PdfReader


def extract_pdf_text(pdf_path: str) -> str:
    """Extract readable text from a PDF and raise useful errors when needed."""
    if not pdf_path:
        raise ValueError("Please upload a PDF article first.")

    path = Path(pdf_path)
    if not path.exists():
        raise FileNotFoundError(f"PDF not found: {path.name}")
    if path.suffix.lower() != ".pdf":
        raise ValueError("The uploaded file must be a PDF.")

    reader = PdfReader(str(path))
    pages = [page.extract_text() or "" for page in reader.pages]
    text = "\n\n".join(page.strip() for page in pages if page.strip())

    if not text:
        raise ValueError(
            "No text could be extracted. This may be a scanned PDF; OCR can be added later."
        )

    return text


def combine_pdf_files(pdf_files: List[str]) -> str:
    """Extract and combine text from multiple PDF files."""
    if not pdf_files:
        raise ValueError("Please provide at least one PDF article.")

    articles = []
    for article_number, pdf_file in enumerate(pdf_files, start=1):
        article_text = extract_pdf_text(pdf_file)
        articles.append(f"SOURCE ARTICLE {article_number}:\n{article_text}")

    return "\n\n".join(articles)

