#Funciona
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib import colors

pdfmetrics.registerFont(TTFont("abc","SakBunderan.ttf"))

def drawMyRuler(pdf):
    pdf.drawString(100,830,"|x100")
    pdf.drawString(200,830,"|x200")
    pdf.drawString(300,830,"|x300")
    pdf.drawString(400,830,"|x400")
    pdf.drawString(500,830,"|x500")
    pdf.drawString(550,830,"|x550")

    pdf.drawString(3,100,"_y100")
    pdf.drawString(3,200,"_y200")
    pdf.drawString(3,300,"_y300")
    pdf.drawString(3,400,"_y400")
    pdf.drawString(3,500,"_y500")
    pdf.drawString(3,600,"_y600")
    pdf.drawString(3,700,"_y700")
    pdf.drawString(3,800,"_y800")


name_file ="Nuevo pdf reportlab.pdf"
document_title ="Titulo del documento !"
titulo= "Nuevo titulo dentro del documento"
parrafo = ["Ahora vamos a explicar como funciona","el tipo de funciones","lineales o vectoriales"]
#Crea un documento y lo nombra.pdf
newpdf= canvas.Canvas(name_file)
#Se puede o no asignar una nueva fuente de caracteres true type font
newpdf.setFont("abc",15) 
#Crea un titulo al documento
newpdf.setTitle(document_title)
#Dibujar una string en el documento
newpdf.drawString(200,800,titulo) #Lee la posicion a la izquierda del string
#subtitulo y cambiamos el color de los caracteres
newpdf.setFont("Courier-Bold",12)
newpdf.setFillColorRGB(0,0,200)
newpdf.drawCentredString(200,750,titulo) #Lee la posicion al centro de el string
#Creamos una linea
newpdf.line(10,745,585,745)
#Cuerpo o parrafo
texto = newpdf.beginText(45,720)
texto.setFont("Courier",10)
texto.setFillColor(colors.purple)#otra forma de colorear texto pero requiere reportlab.lib colors
#Cargamos a la variable 'texto' con las lineas del parrafo 
for line in parrafo:
     texto.textLine(line)
newpdf.drawImage("new.png",200,300) #Tambien se puede cambiar el ancho y alto, se cuenta desde abajo e izquierda

newpdf.drawText(texto)

drawMyRuler(newpdf)
newpdf.save()