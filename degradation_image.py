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
    json_file = open("C:/Users/genay/Documents/MP/TIPE/images/"+type+"/via_region_data.json")
    f = json.load(json_file)
    while cpt < 877 :
        try :
            image_file = Image.open("C:/Users/genay/Documents/MP/TIPE/images/"
                                            +type+"/road"+str(cpt)+".png")
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
                        if color == "blanc":
                            #try :
                            new_img[i][j][k] = 0
                            #except:
                                #()
                        elif color == "noir":
                            #try :
                            new_img[i][j][k] = 256
                            #except:
                                #()
            Image.fromarray(new_img).save("C:/Users/genay/Documents/MP/TIPE/other_databases/degradees"
                                            +color+"/"+type+"/road"+str(cpt)+".png")
            print(cpt)
            cpt += 1
        except :    
            cpt += 1
            
#degrad("val","blanc")
#degrad("val","noir")

#degrad("train","blanc")
#degrad("train","noir")