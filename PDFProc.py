import PyPDF2
import sys




def pdfcombine(pdf_list):
    merger = PyPDF2.PdfMerger()

    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write('output.pdf')

def pdfsplit():

    sample_pdf1 = open('C:\downloads\VenueSigned1.pdf', mode='rb')
    sample_pdf2 = open('C:\downloads\VenueSigned2.pdf', mode='rb')

    input_pdf1 = PyPDF2.PdfReader(sample_pdf1)
    input_pdf2 = PyPDF2.PdfReader(sample_pdf2)
    output_pdf  = PyPDF2.PdfWriter()

 

    output_pdf.add_page(input_pdf1.pages[0])
    output_pdf.add_page(input_pdf1.pages[1])
    output_pdf.add_page(input_pdf1.pages[2])
    output_pdf.add_page(input_pdf2.pages[0])   #  Insert page from second document 
    output_pdf.add_page(input_pdf1.pages[4])
    output_pdf.add_page(input_pdf1.pages[5])
    output_pdf.add_page(input_pdf1.pages[6])
    output_pdf.add_page(input_pdf1.pages[7])
    output_pdf.add_page(input_pdf1.pages[8])


    with open("C:\downloads\output2.pdf","wb") as output_file: 
        output_pdf.write(output_file)


inputs = sys.argv[1:]
## pdfcombine(inputs)
pdfsplit()

