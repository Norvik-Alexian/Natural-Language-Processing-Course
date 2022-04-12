import PyPDF2

with open('../UPDATED_NLP_COURSE/00-Python-Text-Basics/US_Declaration.pdf', mode='rb') as myfile:
    pdf_reader = PyPDF2.PdfFileReader(myfile)
    print(pdf_reader.numPages)
    page_one = pdf_reader.getPage(0)
    print(page_one.extractText())
    myfile.close()

with open('../UPDATED_NLP_COURSE/00-Python-Text-Basics/US_Declaration.pdf', mode='rb') as file:
    pdf_reader = PyPDF2.PdfFileReader(file)
    page_one = pdf_reader.getPage(0)
    pdf_writer = PyPDF2.PdfFileWriter()
    pdf_writer.addPage(page_one)
    with open('files/mypdf.pdf', 'wb') as output_pdf:
        pdf_writer.write(output_pdf)

with open('files/mypdf.pdf', 'rb') as file:
    pdf_reader = PyPDF2.PdfFileReader(file)
    print(pdf_reader.numPages)

with open('../UPDATED_NLP_COURSE/00-Python-Text-Basics/US_Declaration.pdf', mode='rb') as file:
    pdf_text = [0]
    pdf_reader = PyPDF2.PdfFileReader(file)

    for page in range(pdf_reader.numPages):
        pages = pdf_reader.getPage(page)
        pdf_text.append(pages.extractText())

    print(len(pdf_text))
