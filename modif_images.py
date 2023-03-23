from PIL import Image, ImageDraw
import numpy as np



def eclairement(coef):   #coef désigne l'augmentation de l'éclairement (recommandé entre 50 et 100) 
    cpt = 0 
    while cpt < 877:  
        image_file = Image.open("C:/Users/Elève/Documents/Prepa/TIPE/PANNEAU/data_detectron_reduite/all/road"+str(cpt)+".png")
        img = np.asarray(image_file)                  
        for i in range(len(img)):
            for j in range(len(img[i])):
                for k in range(0,3):
                    if img[i][j][k] + coef < 256:
                        img[i][j][k] += coef
        new_img = np.copy(img)
        Image.fromarray(new_img).save("C:/Users/Elève/Documents/Prepa/TIPE/PANNEAU/other_databases/eclaire50/road"+str(cpt)+".png")
        cpt += 1
        print(cpt)

eclairement(50)