import docx2txt
import os

# extract text
#text = docx2txt.process("dr.docx")

#print text

# extract text and write images in /tmp/img_dir
text = docx2txt.process("dr.docx", os.getcwd() + '\images' )