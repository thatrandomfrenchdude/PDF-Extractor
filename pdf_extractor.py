import argparse
from pathlib import Path
import fitz as pdfExtract

# references
# https://neurondai.medium.com/how-to-extract-text-from-a-pdf-using-pymupdf-and-python-caa8487cf9d
# https://python.plainenglish.io/10-python-automation-scripts-for-daily-problems-68991d28f490

# command line
# https://realpython.com/command-line-interfaces-python-argparse/


class PDFExtractor:
    def __init__(self, pdfFile):
        self.pdf_doc = pdfExtract.open(pdfFile)
        self.numPages = self.pdf_doc.page_count


    def extractPage(self, page_no):
        return self.pdf_doc.load_page(page_no).get_text()

    def extractRange(self, start, end):
        pages = []
        for page_no in range(start, end):
            pages.append(self.extractPage(page_no))
        return pages

    def extractAll(self):
        pages = []
        for page_no in range(self.numPages):
            pages.append(self.extractPage(page_no))
        return pages
    
    @staticmethod
    def saveText(text, save_path):
        with open(save_path, "w") as f:
            if type(text) == list:
                for page in text:
                    f.write(page)
            else:
                f.write(text)


def setup_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_path", help="path to the pdf file")
    parser.add_argument("output_path", help="path to the output file")
    return parser
    

if __name__ == "__main__":
    parser = setup_parser()
    args = parser.parse_args()
    
    print("Converting PDF...")

    # file paths
    input_path = Path(args.input_path)
    output_path = Path(args.output_path)

    # extract text
    pdf = PDFExtractor(input_path)
    pdf.saveText(pdf.extractAll(), output_path)

    