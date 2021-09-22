import os
from io import StringIO
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
import pandas as pd
import csv
import fitz
import random
import os
from fpdf import FPDF
from PIL import Image
from PyPDF2 import PdfFileMerger
from PyPDF2 import PdfFileWriter, PdfFileReader

def remove_images():
    folder_path = (r'./static/')
    #using listdir() method to list the files of the folder
    test = os.listdir(folder_path)
    #taking a loop to remove all the images
    #using ".png" extension to remove only png images
    #using os.remove() method to remove the files
    for images in test:
        if images.endswith(".png"):
            os.remove(os.path.join(folder_path, images))


def remove_pdf():
    folder_path = (r'./static/uploadpdf')
    #using listdir() method to list the files of the folder
    test = os.listdir(folder_path)
    #taking a loop to remove all the images
    #using ".png" extension to remove only png images
    #using os.remove() method to remove the files
    for images in test:
        if images.endswith(".pdf"):
            os.remove(os.path.join(folder_path, images))    


def remove_outfiles():
    folder_path = (r'./static/outfiles')
    #using listdir() method to list the files of the folder
    test = os.listdir(folder_path)
    #taking a loop to remove all the images
    #using ".png" extension to remove only png images
    #using os.remove() method to remove the files
    for images in test:
        if images.endswith(".png"):
            os.remove(os.path.join(folder_path, images)) 

def remove_demofiles():
    folder_path = (r'./static/demo')
    #using listdir() method to list the files of the folder
    test = os.listdir(folder_path)
    #taking a loop to remove all the images
    #using ".png" extension to remove only png images
    #using os.remove() method to remove the files
    for images in test:
        if images.endswith(".pdf"):
            os.remove(os.path.join(folder_path, images)) 

APP_FOLDER = './cert/'

totalFiles = 0

for base, dirs, files in os.walk(APP_FOLDER):
    for Files in files:
        totalFiles += 1

if totalFiles == 0:
   err= input("Your Certification Directory is empty.")
   print(err)
else:
    print("Powered by Muhammad Irfan bakali & team..!")
    num = input ("Do you really want to processed the files? (Y):")

    if num == "Y" or num=="y" or num == "YES" or num == "yes":
        print("You have total files to print are "+ str(totalFiles))
        remove_pdf()
        remove_outfiles()   
        remove_demofiles()      

        files = os.listdir("./cert/")
        pdf_generated_files = list()
        # print('multiple files')            
        loop_no = 0
        for f in files:                
            # print(f)                                          
            remove_images()                                
            # f.save("./static/uploadpdf/"+f.filename)  
            doc = fitz.open("./cert/"+f)
            page = doc.loadPage(0)  # number of page
            # pix = page.getPixmap()
            zoom = 1    # zoom factor
            mat = fitz.Matrix(zoom, zoom)
            pix = page.getPixmap(matrix = mat)
            output = "./static/picofvac.png"
            pix.writePNG(output)

            im = Image.open(output)
            im.size  # (364, 471)
            im.getbbox()  # (64, 89, 278, 267)
            # print(im.getbbox())
            im2 = im.crop((122, 1245, 2540, 1685))
            im2.size  # (214, 178)
            im2.save("./static/cropvac.png")
            
            def to_txt():
                input_ = open("./cert/"+f, 'rb')
                output = StringIO()

                manager = PDFResourceManager()
                converter = TextConverter(manager, output, laparams=LAParams())
                process_pdf(manager, converter, input_)

                return output.getvalue() 
            output = to_txt()
            # print(output)

            file2 = open(r"./static/input.txt","w")
            file2.write(output)

            file2.close()

            with open(r'./static/input.txt', 'r') as infile, open(r'./static/output.txt', 'w') as outfile:
                    data = infile.read()
                    data = data.replace(", ", " ")
                    outfile.write(data)                
                    outfile.close()

            with open('./static/output.txt', 'r') as infile, open('./static/log.csv', 'w') as outfile:
                    writer = csv.writer(outfile)
                    writer.writerows('h')
                    stripped = (line.strip() for line in infile)
                    lines = (line.split(",") for line in stripped if line)
                    writer = csv.writer(outfile)
                    writer.writerows(lines)


            df = pd.read_csv('./static/log.csv')

            ## Fastest would be using length of index

            # print("Number of rows ", len(df.index))

            ## If you want the column and row count then

            row_count, column_count = df.shape

            # print("Number of rows ", row_count)
            # print("Number of columns ", column_count)  


            doc = fitz.open("./cert/"+f)
            random_value = random.randint(3, 100000000000)

            for i in range(len(doc)):
                for img in doc.getPageImageList(i):
                    xref = img[0]
                    pix = fitz.Pixmap(doc, xref)
                    if pix.n < 5:       # this is GRAY or RGB
                        pix.writePNG("./static/p-"+str(random_value)+"-%s-%s.png" % (i, xref))
                    else:               # CMYK: convert to RGB first
                        pix1 = fitz.Pixmap(fitz.csRGB, pix)
                        pix1.writePNG("./static/p-"+str(random_value)+"-%s-%s.png" % (i, xref))
                        pix1 = None
                    pix = None
            df = pd.read_csv('./static/log.csv', delimiter=';')
            
            v_DOB = str(df.values[3]) 
            if len(v_DOB) == 19:
                u_name = str(df.values[2])        
                v_DOB = str(df.values[4])        
                v_CNIC = str(df.values[3])
                v_nationality = str(df.values[5])
                v_issue_date = str(df.values[0])
                v_certif =str(df.values[1])
            else:
                u_name = str(df.values[2])        
                v_DOB = str(df.values[3])        
                v_CNIC = str(df.values[5])
                v_nationality = str(df.values[4])
                v_issue_date = str(df.values[0])
                v_certif =str(df.values[1])


            img_uri01 = "./static/p-"+str(random_value)+"-0-5.png"
            img_uri02 = "./static/p-"+str(random_value)+"-0-8.png"
            img_uri03 = "./static/p-"+str(random_value)+"-0-12.png"
            img_uri04 = "./static/p-"+str(random_value)+"-0-15.png"
            img_uri05 = "./static/p-"+str(random_value)+"-0-3.png"

            


            pdf = FPDF(unit = "pt", format = [595, 842])

            pdf.add_page()
            pdf.image("./static/Front.JPG", 37, 00,241,153)
            pdf.image("./static/Back.JPG", 320, 00,241,153)            
            pdf.image("./static/barcode.jpeg", 430, 45,120,20)
            pdf.image(img_uri04, 200,30,30,15)   # fully vaccinated         
            pdf.image("./static/cropvac.png", 37, 100,241,50)            
            pdf.image(img_uri01, 230, 55,45,43) # person image
            pdf.image(img_uri03, 328, 35,90,90)  # QR code image      

            # # For Multiple Work Load
            # pdf.image("Front.jpeg", 27, 180,260,160)
            # pdf.image("Back.jpeg", 310, 180,260,160)

            # pdf.image("Front.jpeg", 27, 340,260,160)
            # pdf.image("Back.jpeg", 310, 340,260,160)

            # pdf.image("Front.jpeg", 27, 500,260,160)
            # pdf.image("Back.jpeg", 310, 500,260,160)

            # pdf.image("Front.jpeg", 27, 660,260,160)
            # pdf.image("Back.jpeg", 310, 660,260,160)
            
            # pdf.image("Back.jpeg", 300, 20,286.5,180.75)
            

            pdf.set_xy(105,48)
            pdf.set_font('arial', '', 6.0)
            pdf.multi_cell(0, 5, u_name[2:-2])

            pdf.set_xy(80,59)
            pdf.set_font('arial', '', 6.0)
            pdf.multi_cell(0, 5, v_DOB[2:-2])

            pdf.set_xy(160,59)
            pdf.set_font('arial', '', 6.0)
            pdf.multi_cell(0, 5, v_CNIC[2:-2])  
            
            pdf.set_xy(80,69)
            pdf.set_font('arial', '', 6.0)
            pdf.multi_cell(0, 5, v_nationality[2:-2])  

            # pdf.set_xy(188,77)
            # pdf.set_font('arial', '', 5.0)
            # pdf.multi_cell(0, 5, "Passport")    
            
            pdf.set_xy(475,18)
            pdf.set_font('arial', '', 6.0)
            pdf.multi_cell(0, 5, v_issue_date[2:-2])    
            
            pdf.set_xy(490,33)
            pdf.set_font('arial', '', 6.0)
            pdf.multi_cell(0, 5, v_certif[2:-2])    

            file_save = str("./static/demo/pdf"+str(loop_no)+".pdf")
            pdf_generated_files.append(file_save)
            pdf.output(file_save, "F")
            loop_no += 1
            # print("pdf completed")

        for item in pdf_generated_files:
            print(item[-9:]+" file convert to the card.")

        merger = PdfFileMerger()

        for pdf in pdf_generated_files:
            merger.append(pdf)

        merger.write("./static/result.pdf")
        merger.close()

        with open("./static/result.pdf", "rb") as in_f:
            input1 = PdfFileReader(in_f)
            output = PdfFileWriter()

            numPages = input1.getNumPages()
            # print ("document has %s pages." % numPages)

            for i in range(numPages):
                page = input1.getPage(i)
                # print (page.mediaBox.getUpperRight_x(), page.mediaBox.getUpperRight_y())
                page.trimBox.lowerLeft = (30, 25)
                page.trimBox.upperRight = (50, 50)
                page.cropBox.lowerLeft = (0,670)        
                output.addPage(page)

            with open("./static/out.pdf", "wb") as out_f:
                output.write(out_f)

        count = 0
        for pdf in pdf_generated_files:
            doc = fitz.open(pdf)
            page = doc.loadPage(0)  # number of page
            zoom = 4    # zoom factor
            mat = fitz.Matrix(zoom, zoom)
            pix = page.getPixmap(matrix = mat)
            # pix = page.getPixmap()
            output = "./static/outfiles/outfile"+str(count)+".png"
            pix.writePNG(output)
            count += 1

        pdf02 = FPDF(unit = "pt", format = [595, 842])
        new_row = 0
        for i in range(len(pdf_generated_files)):
            if new_row == 0:
                pdf02.add_page()
            elif i % 5 == 0:
                new_row = 0
                pdf02.add_page()

            print()
            pdf02.image("./static/outfiles/outfile"+str(i)+".png", 0, 23+new_row,595,842)
            new_row+=160


        pdf02.output("./output/combine-card.pdf", "F") 
        succ01=input("All the files are Convert into card successfully. \nPowered by Muhammad Irfan bakali & team..!")
        print(succ01)
    else:
       err01=  input("bye..!")
       print(err01)