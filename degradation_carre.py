from PIL import Image, ImageDraw
import numpy as np
import random as rd

import json

def moy(L):
    s = 0
    for e in L :
        s += e
    return s/len(L)


def degrad(type,color):
    cpt = 0
    json_file = open("C:/Users/Elève/Documents/Prepa/TIPE/PANNEAU/via_region_data.json")
    f = json.load(json_file)
    while cpt < 877 :
        try :
            image_file = Image.open("C:/Users/Elève/Documents/Prepa/TIPE/PANNEAU/images/road"+str(cpt)+".png")
            img = np.array(image_file)  
            new_img = np.copy(img)
            dict = f["road"+str(cpt)]["regions"]["0"]["shape_attributes"]
            all_x = dict["all_points_x"]
            all_y = dict["all_points_y"]
            x0 = int(moy(all_x)) #all_x[rd.randint(0,len(all_x)-1)]#
            y0 = int(moy(all_y)) #all_y[rd.randint(0,len(all_y)-1)]#
            for i in range(x0-30,x0+30):
                for j in range(y0-30,y0+30):
                    for k in range(3):
                        if color == "noir":
                            try :
                                new_img[j][i][k] = 0
                            except:
                                ()
                        elif color == "blanc":
                            try :
                                new_img[j][i][k] = 256
                            except:
                                ()
            Image.fromarray(new_img).save("C:/Users/Elève/Documents/Prepa/TIPE/PANNEAU/degradation/images_degradees_carres/road"+str(cpt)+".png")
            print(cpt)
            cpt += 1
        except :    
            cpt += 1

# degrad("val","blanc")

def bruitage(type,color,P):     #P le pourcentage de points que l'on souhaite recouvrir sur le panneau
    cpt = 0
    json_file = open("C:/Users/Elève/Documents/Prepa/TIPE/PANNEAU/via_region_data.json")
    f = json.load(json_file)
    while cpt < 877 :
        try :
            image_file = Image.open("C:/Users/Elève/Documents/Prepa/TIPE/PANNEAU/images/road"+str(cpt)+".png")
            img = np.array(image_file)  
            new_img = np.copy(img)
            dict = f["road"+str(cpt)]["regions"]["0"]["shape_attributes"]
            all_x = dict["all_points_x"]
            all_y = dict["all_points_y"]
            min_x = min(all_x)
            max_x = max(all_x)
            min_y = min(all_y)
            max_y = max(all_y)
            A = (max_x - min_x)*(max_y - min_y)
            N = round((P/100)*A)
            for _ in range(N):
                x = rd.randint(min_x,max_x)
                y = rd.randint(min_y,max_y)
                for k in range(3):
                    if color == "blanc":
                       new_img[y][x][k] = 0
                    else:
                        new_img[y][x][k] = 256
            Image.fromarray(new_img).save("C:/Users/Elève/Documents/Prepa/TIPE/PANNEAU/degradation/images_floutees/"+str(P)+"/road"+str(cpt)+".png")
            print(cpt)
            cpt += 1
        except :
            cpt += 1

floutage("val","noir",99)
            
