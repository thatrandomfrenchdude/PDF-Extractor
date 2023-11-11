from pdf_extractor import PDFExtractor

def test_extract_page():
    pdf = PDFExtractor("test_data/the_sorcerers_stone.pdf")
    text = pdf.extractPage(1)
    assert text is not None
    assert len(text) > 0
    assert type(text) == str