''' YOU NEED TO DOWNLOAD PyPDF2 into whatever version of Python you're using '''

import PyPDF2
#from sys import argv

# I didn't add in help files in this script. Basically:  First argument is book, second argument is page number.

book = input("Name of pdf (include .pdf): ")
page = int(input("Page Number: "))
        
with open(book, 'rb') as pdfFileObj:
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    pageObj = pdfReader.getPage(page)
    print(pageObj.extractText())
    
    # This will show you the number of pages in the book
    pdfReader.numPages
    print(pdfReader.numPages)

