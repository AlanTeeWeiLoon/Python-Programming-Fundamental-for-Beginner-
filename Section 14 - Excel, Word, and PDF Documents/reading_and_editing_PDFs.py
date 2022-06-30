import PyPDF2

print('\n1------------------------------------------------\n')
# PyPDF2.PdfFileReader()
# .numPages - number of pages of the PDF file

pdfFile = open('meetingminutes1.pdf', 'rb')
reader = PyPDF2.PdfFileReader(pdfFile)
a = reader.numPages 
print(a) # 19 - the page of the PDF file

print('\n2------------------------------------------------\n')
# .getPage()
# .extractText()

page = reader.getPage(0) # page start at 0, not 1
print(page.extractText()) # extract the text in PDF file to a string

print('\n3------------------------------------------------\n')
# print out all the text in PDF file

for pageNum in range(reader.numPages):
    print(reader.getPage(pageNum).extractText())

print('\n4------------------------------------------------\n')
# PyPDF2.PdfFileWriter()
# .addPage()
# .write()

pdf1File = open('meetingminutes1.pdf', 'rb')
pdf2File = open('meetingminutes2.pdf', 'rb')

reader1 = PyPDF2.PdfFileReader(pdf1File)
reader2 = PyPDF2.PdfFileReader(pdf2File)

writer = PyPDF2.PdfFileWriter()
for pageNum in range(reader1.numPages):
    page = reader1.getPage(pageNum)
    writer.addPage(page)

for pageNum in range(reader2.numPages):
    page = reader2.getPage(pageNum)
    writer.addPage(page)

outputFile = open('combinedminutes.pdf', 'wb')
writer.write(outputFile)
outputFile.close() # a combinedminutes.pdf PDF file created that combine content in 'meetingminutes1.pdf' and 'meetingminutes2.pdf'
pdf1File.close()
pdf2File.close()





            



