import os
import img2pdf
from tkinter import filedialog as fd
from PIL import Image
import pathlib

def main():

    ''' display a dialog to select file names'''
    files = [] # will store image paths in a list format
    tokenized_files = [] # will contain list of tokens of each image path split using '/'
    filenames = fd.askopenfilenames() #tkinter function that opens dialogue box
    # filenames is in a tuple format, the loop below will convert it into list format
    for i in filenames:
        if (i.endswith('.jpg') or i.endswith('.png') or i.endswith('.jpeg')):
            files.append(i)
    for i in files:
        tokenized_files.append(i.split('/'))
    print(files)
    '''making sure all images are in same colour format'''
    for img_path in files:
        img = Image.open(img_path)
        img = img.convert('RGB')
        img.save(img_path)

    '''iterating through all filenames and converting them to pdf format'''
    fileName = input("Enter PDF name: ")
    pdfPath = ""
    for i in range(0, len(tokenized_files[0])-1):
        pdfPath  = pdfPath + tokenized_files[0][i] + "/"
    pdfPath = pdfPath + fileName + ".pdf"
    destination = open(pdfPath, "wb+") # opening the file handler for pdfPath
    '''now converting each image into a pdf and writing it into pdf file'''
    pdf_bytes = img2pdf.convert(files, options={"compress": False})
    destination.write(pdf_bytes)
    destination.close()
    print("Successfully created and stored the PDF")
    
main()
