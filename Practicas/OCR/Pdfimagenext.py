'''from pdfminer.high_level import extract_pages
for page_layout in extract_pages("D:\Proyectos\Python Pr\Practicas\OCR\example.pdf"):
    for element in page_layout:
        print(element)

def spaNormalizador():
    Al = Al.replace("¶a","á")
    Al = Al.replace("¶e","é")
    Al = Al.replace("¶‡","í")
    Al = Al.replace("¶o","ó")
    Al = Al.replace("¶u","ú")
    Al = Al.replace("~n","ñ")
    Al = Al.replace("¶A","Á")
    Al = Al.replace("\\",'"')'''
from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer
for page_layout in extract_pages("D:\Proyectos\Python Pr\Practicas\OCR\example.pdf"):
    for element in page_layout:
        if isinstance(element, LTTextContainer):
            print(element.get_text())