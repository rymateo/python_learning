import os

IMG_PATH = os.getcwd() + '/images/'

print IMG_PATH

files = os.listdir(IMG_PATH)

print files

for file in files:
    if (file.find('ques') != -1):
        new_fname = file[5:]
        print new_fname
        os.rename( IMG_PATH + file, IMG_PATH + new_fname )



