from PyPDF2 import PdfFileMerger
from PyPDF2 import PdfFileWriter, PdfFileReader
import fitz
from fpdf import FPDF

pdfs = ['./static/demo/pdf0.pdf','./static/demo/pdf1.pdf']

merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("result.pdf")
merger.close()

with open("result.pdf", "rb") as in_f:
    input1 = PdfFileReader(in_f)
    output = PdfFileWriter()

    numPages = input1.getNumPages()
    print ("document has %s pages." % numPages)

    for i in range(numPages):
        page = input1.getPage(i)
        print (page.mediaBox.getUpperRight_x(), page.mediaBox.getUpperRight_y())
        page.trimBox.lowerLeft = (30, 25)
        page.trimBox.upperRight = (50, 50)
        page.cropBox.lowerLeft = (0,670)        
        output.addPage(page)

    with open("out.pdf", "wb") as out_f:
        output.write(out_f)


# pdfs = ['./static/demo0.pdf', './static/demo1.pdf', './static/demo2.pdf', './static/demo3.pdf','./static/demo4.pdf','./static/demo5.pdf']
count = 0
for pdf in pdfs:
    doc = fitz.open(pdf)
    page = doc.loadPage(0)  # number of page
    # pix = page.getPixmap()
    zoom = 4    # zoom factor
    mat = fitz.Matrix(zoom, zoom)
    pix = page.getPixmap(matrix = mat)
    output = "outfile"+str(count)+".png"
    pix.writePNG(output)
    count += 1

pdf = FPDF(unit = "pt", format = [595, 842])
new_row = 0
for i in range(len(pdfs)):
    if new_row == 0:
        pdf.add_page()
    elif i % 4 == 0:
        new_row = 0
        pdf.add_page()

    print()
    pdf.image("outfile"+str(i)+".png", 0, 0+new_row,595,842)
    new_row+=200


pdf.output("combine.pdf", "F") 