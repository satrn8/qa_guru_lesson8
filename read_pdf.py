from PyPDF2 import PdfReader


def test_pdf_number_of_pages():
    reader = PdfReader(".\\resources\\docs-pytest-org-en-latest.pdf")
    number_of_pages = len(reader.pages)
    print(number_of_pages)
    assert number_of_pages == 412


def test_read_pdf():
    reader = PdfReader(".\\resources\\docs-pytest-org-en-latest.pdf")
    number_of_pages = len(reader.pages)
    print(number_of_pages)
    page = reader.pages[0]
    text = page.extractText()
    print(text)
    assert "2022" in text