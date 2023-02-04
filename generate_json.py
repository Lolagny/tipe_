import json
import os

def build_regions(data):
    polygons = data["shapes"]
    Liste_shapes = []
    for e in polygons:
        shape_attributes = {
        "name": "polygon",
        "all_points_x": [],
        "all_points_y": [],
    }
        points = e["points"]
        for i in points:
            shape_attributes["all_points_x"].append(round(i[0]))
            shape_attributes["all_points_y"].append(round(i[1]))
        Liste_shapes.append(shape_attributes)
    dic = {}
    for i in range(len(Liste_shapes)):
        dic[str(i)] = {}
    for i in range(len(Liste_shapes)):
        dic[str(i)]["shape_attributes"] = Liste_shapes[i]
        dic[str(i)]["region_attributes"] = {}
    return dic

def build_dico(path):
    with open(path) as f:
        data = json.load(f)
    size = os.path.getsize(path)
    name = data["imagePath"]
    d = {
        "fileref": "",
        "size": size,
        "filename": name,
        "base64_img_data": "",
        "file_attributes": "",
        "regions": build_regions(data) 
    }
    return d

def json_complet():
    d = {}
    for i in range(0,877):              #Numéros des png pour lesquels on veut le json
        name = "road"+str(i)
        print(name)
        d[name] = build_dico('C:/Users/Elève/Documents/Prepa/TIPE/PANNEAU/data_detectron_reduite/road'+str(i)+'.json')
    return d

print(json_complet())