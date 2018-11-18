import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join
import pathlib

sets=["201", "202", "203"]
classes = ["bot"]

def convert(size, box):
    dw = 1./size[0]
    dh = 1./size[1]
    x = (box[0] + box[1])/2.0
    y = (box[2] + box[3])/2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)

def convert_annotation(folder, image_id):
    in_file = open('project/coordination/annotations/%s/%s.xml'%(folder, image_id))
    out_file = open('project/coordination/labels/%s/%s.txt'%(folder, image_id), 'w')
    
    tree=ET.parse(in_file)
    root = tree.getroot()
    
    filename = root.find("filename")

    for obj in root.iter('object'):

        cls = obj.find('name').text
        polygon = obj.find('polygon')
        points = polygon.findall('pt')

        x_pts, y_pts = set(), set()

        for point in points:
            x_pts.add(float(point.find('x').text))
            y_pts.add(float(point.find('y').text))

        x_pts, y_pts = sorted(x_pts), sorted(y_pts)
        xmin, xmax, ymin, ymax = x_pts[0], x_pts[1], y_pts[0], y_pts[1]

        if cls not in classes:
            print("Could not find class for {}".format(cls))
            continue

        cls_id = classes.index(cls)

        print("Class {} at {}, {}, {}, {}".format(cls_id, xmin, xmax, ymin, ymax))

        w = 640.
        h = 480.

        b = (xmin, xmax, ymin, ymax)
        bb = convert((w,h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')

    out_file.close()

wd = getcwd()

for folder in sets:
    if not os.path.exists(wd + '/project/coordination/labels/%s'%(folder)):
        os.makedirs(wd + '/project/coordination/labels/%s'%(folder))
    
    annotations = pathlib.Path().glob("project/coordination/annotations/%s/*.xml" % (folder))
    list_file = open('dataset_images_%s.txt' % (folder), 'w')

    for annotation in annotations:
        list_file.write(wd + '/project/coordination/frames/%s/%s.jpg\n'%(folder, annotation.stem))
        convert_annotation(folder, annotation.stem)

    list_file.close()


