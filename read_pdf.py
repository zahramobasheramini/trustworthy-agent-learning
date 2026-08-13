from pypdf import PdfReader


reader = PdfReader("documents/test.pdf")

text = ""

for page in reader.pages:
    text += page.extract_text() + "\n"


with open("documents/extracted_pdf.txt", "w", encoding="utf-8") as file:
    file.write(text)


print("PDF text saved.")