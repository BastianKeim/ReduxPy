from asyncio import subprocess
from email.mime import image
from PIL import Image
import os
import time

#os.system("py -m pip install --upgrade pip")
#os.system("py -m pip install --upgrade Pillow")
#time.sleep(2)

workingfolder = os.getcwd()

folderName = workingfolder.split("\\")
nLetters = len(folderName)
nLetters = folderName[nLetters-1]

print("Current Working Folder is: " + workingfolder)
folder = workingfolder + ("/")
newfolder = workingfolder + ("/reduxed_") + nLetters


if __name__ == "__main__":
    if not os.path.exists(newfolder):
                os.mkdir(newfolder)
    for filename in os.listdir(folder):
        name, extension = os.path.splitext(folder + filename)

        if extension in (".jpg", ".jpeg",".png"):
            
            picture = Image.open(folder + filename)
            picture.save(f"{newfolder}/Compressed_{filename}", optimize=True, quality =80)
            print(f"Copying {filename} to new folder... please wait")

print("It finished! Go to watch and enjoy")
input("Press Enter to continue...")