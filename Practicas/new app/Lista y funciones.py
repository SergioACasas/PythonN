lista = [('Practical Python and OpenCV (Adrian Rosebrock) (z-lib.org)','D:/Documents/Programacion/Practical Python and OpenCV (Adrian Rosebrock) (z-lib.org)'),('OCR with OpenCV, Tesseract, and Python (Adrian Rosebrock) (z-lib.org).pdf','D:/Documents/Programacion/OCR with OpenCV, Tesseract, and Python (Adrian Rosebrock) (z-lib.org).pdf')]

"""for x , y in lista:
    n= f"{x}----{y}"
    print(n)"""

"""for x , y in lista:
    n= "%s----%s"
    print(n%(x,y))"""

old= r'\b\n\\'
new= '\b\n\\'
print(old)
print(new)
"""m = "comida' y muchas \" otras' cosas'"
m = m.replace("'", r"\'")
m = m.replace('"', r'\"')"""
m = "comida' y muchas \" otras' \\ cosas'"
m = m.replace("\\","/")
m = m.replace("'", r"\'")
m = m.replace('"', r'\"')

print (m)