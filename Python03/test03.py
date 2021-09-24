# from PyPDF2 import PdfFileMerger
# from PyPDF2 import PdfFileWriter, PdfFileReader
# from pdf import *
# import fitz
# from fpdf import FPDF
# from PIL import Image

# # with open("./cert/b.pdf", "rb") as in_f:
# #     input1 = PdfFileReader(in_f)
# #     output = PdfFileWriter()
# #     page = input1.getPage(0)
# #     print (page.mediaBox.getUpperRight_x(), page.mediaBox.getUpperRight_y())
# #     # page.cropBox.setLowerLeft = (0,0)   
# #     page.cropBox.lowerLeft = (0,670)   
# #     output.addPage(page)

# # with open("out02.pdf", "wb") as out_f:
# #     output.write(out_f)



# doc = fitz.open("./cert/b.pdf")
# page = doc.loadPage(0)  # number of page
# # pix = page.getPixmap()
# zoom = 1    # zoom factor
# mat = fitz.Matrix(zoom, zoom)
# pix = page.getPixmap(matrix = mat)
# output = "./static/picofvac.png"
# pix.writePNG(output)

# im = Image.open(output)
# im.size  # (364, 471)
# im.getbbox()  # (64, 89, 278, 267)
# print(im.getbbox())
# im2 = im.crop((122, 1245, 2540, 1685))
# im2.size  # (214, 178)
# im2.save("./static/cropvac.png")

# import os
# arr = os.listdir()
# print(arr)

num = input ("Enter number :")
print(num)
name1 = input("Enter name : ")
print(name1)
  
# Printing type of input value
print ("type of number", type(num))
print ("type of name", type(name1))