import PyPDF2
pdfFileObj = open(r'./webstersChoice.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

pageObject = pdfReader.getPage(34)
print(pageObject.extractText(), 'page')
print(pdfReader.getNumPages(), 'number of pages page22 to ')
pdfFileObj.close()
