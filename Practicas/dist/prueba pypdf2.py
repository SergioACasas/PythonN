#Useless whitout the PyPDF2 lib
from PyPDF2 import PdfFileReader
file=open("D:\Proyectos\Python Pr\Practicas\dist\Aprenda-a-pensar-como-un-programador-con-python(1).pdf","rb")
pdf = PdfFileReader(file)
page = pdf.getPage(0)
pdfdata = page.extractText()
with open("D:\Proyectos\Python Pr\Practicas\dist\Test.txt","w",encoding="utf-8") as f:
    for page_num in range(pdf.numPages):
        # print('Page: {0}'.format(page_num))
        pageObj = pdf.getPage(page_num)
        try: 
            txt = pageObj.extractText().encode('ascii', 'ignore')
            print(''.center(100, '-'))
        except:
            pass
        else:
            f.write('Page {0}\n'.format(page_num+1))
            f.write(''.center(100, '-'))
            f.write(str(txt))
    f.close()


