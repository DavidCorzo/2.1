from PyPDF2 import PdfFileWriter, PdfFileReader
import math 

def get_height(filename): 
    input1 = PdfFileReader(open(filename, 'rb'))
    return input1.getPage(0).mediaBox



def split_pdf_to_two(filename,page_number):
    pdf_reader = PdfFileReader(open(filename, "rb"))
    try:
        assert page_number < pdf_reader.numPages
        pdf_writer1 = PdfFileWriter()
        pdf_writer2 = PdfFileWriter()

        for page in range(page_number):
            pdf_writer1.addPage(pdf_reader.getPage(page))

        for page in range(page_number,pdf_reader.getNumPages()):
            pdf_writer2.addPage(pdf_reader.getPage(page))

        with open("part1.pdf", 'wb') as file1:
            pdf_writer1.write(file1)

        with open("part2.pdf", 'wb') as file2:
            pdf_writer2.write(file2)

    except AssertionError as e:
        print("Error: The PDF you are cutting has less pages than you want to cut!")


if __name__ == "__main__":
    h = get_height("03--Bienes elasticos, bienes sustitutos y bienes elasticos e inelasticos.pdf")
    h = math.floor(h[3]/842)
    split_pdf_to_two("03--Bienes elasticos, bienes sustitutos y bienes elasticos e inelasticos.pdf",h)
