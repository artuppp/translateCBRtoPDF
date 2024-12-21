import os
import glob
from pathlib import Path
import shutil
import tarfile
from PIL import Image

#FIRST PART, CHANGE NAME
files = [folder for folder in glob.glob("*") if (".cbr" in folder or ".cbz" in folder)]

index = 1
for file in files:
    print(file)
    p = Path(file)
    p.rename(str(index) + '.rar')
    if not os.path.exists(str(index)):
        os.makedirs(str(index))
    # os.rename(str(index) + ".zip", str(index) + "/" + str(index) + ".zip")

    #SECOND PART, EXTRACT IN SEPARATE FOLDERS
    # Abrir el archivo RAR
    os.system('"' + r'C:\Program Files\WinRAR\WinRAR.exe' + '" x ' + str(index) + '.rar ' + str(index)) 
    index+=1

#PART THREE, GET IMAGES FROM INSIDE OF A FOLDER
for i in range(1, len(files) + 1):
    directory = os.path.join(str(i))
    for root, dirs, files in os.walk(directory, topdown=False):
        for file in files:
            # Verify if file is an image
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff')):
                # Get path
                archivo_origen = os.path.join(root, file)
                archivo_destino = os.path.join(directory, file)
                # Move the image 
                shutil.move(archivo_origen, archivo_destino)
                    
                print(f"Moving {archivo_origen} to {archivo_destino}")
        # After moving the images, remove folder if it is empty
        for root, dirs, files in os.walk(directory, topdown=False):
            for dir in dirs:
                dir_path = os.path.join(root, dir)
                if not os.listdir(dir_path):  # If folder is empty
                    os.rmdir(dir_path)
                    print(f"Removing empty folder: {dir_path}")

#PART 4 load images 
images = []
for i in range(1,len(files) + 1):
    print(str(i))
    imagesPath = glob.glob(str(i) + "/*")
    for image in imagesPath:
        print("Loaded " + image)
        img = Image.open(image)
        images.append(img)

# PART 5 GENERATE PDF
images[0].save("output_PDF.pdf", "PDF" ,resolution=100.0, save_all=True, append_images=images[1:])