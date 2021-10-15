from pdf2image import convert_from_path

archivo_pdf = 'D:\Proyectos\Python Pr\Practicas\OCR\hojas faltantes manual clinico.pdf'
imagen = convert_from_path(archivo_pdf,dpi=300,last_page=3,output_folder='D:\Proyectos\Python Pr\Practicas\Datos',fmt='jpeg',output_file='')
#Name Generator
'''c = 1
for page in imagen:
    filename= "page_"+str(c)+'.jpg'
    page.save(filename,'JPEG')
    c+=1
    '''