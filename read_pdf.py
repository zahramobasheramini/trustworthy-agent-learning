from pathlib import Path

from pypdf import PdfReader


pdf_path = Path("documents/test.pdf")

if not pdf_path.exists():
    print("PDF file was not found.")
    exit()


reader = PdfReader(pdf_path)

print("Number of pages:", len(reader.pages))


for page_number, page in enumerate(reader.pages, start=1):
    text = page.extract_text()

    print(f"\n--- Page {page_number} ---")

    if text:
        print(text)
    else:
        print("No text was extracted from this page.")