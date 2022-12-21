import cv2
import numpy as np
import random as rd
 
image = cv2.imread('C://Users/romai/Documents/Prepa/TIPE/Code/stop.png')
print(image) 

height, width = image.shape[:2]
center = (width/2, height/2)

def rota(image, center, height, width):

    for i in range(360):

        tx = rd.randint(0,200)
        ty = rd.randint(0,200)
        translation_matrix = np.array([
            [1, 0, tx],
            [0, 1, ty]
        ], dtype=np.float32)
        translated_image = cv2.warpAffine(src=image, M=translation_matrix, dsize=(width, height))
        rotate_matrix = cv2.getRotationMatrix2D(center=center, angle=i, scale=1)
        rotated_image = cv2.warpAffine(src=translated_image, M=rotate_matrix, dsize=(width, height))
        cv2.imwrite('C://Users/romai/Documents/Prepa/TIPE/new_database_png/stop/rotated_stop'+str(i)+ '.png', rotated_image)

rota(image, center, height, width)