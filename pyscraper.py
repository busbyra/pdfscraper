''' YOU NEED TO DOWNLOAD PyPDF2 into whatever version of Python you're using '''

import PyPDF2
from sys import argv

# I didn't add in help files in this script. Basically:  First argument is book, second argument is page number.

book = argv[1]
page = argv[2]
print(argv)
with open(argv[1], 'rb') as pdfFileObj:
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    pageObj = pdfReader.getPage(int(argv[2]))
    print(pageObj.extractText())
    
    # This will show you the number of pages in the book
    pdfReader.numPages
    print(pdfReader.numPages)
