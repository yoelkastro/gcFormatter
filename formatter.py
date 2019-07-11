import os
import fileinput
import random

gcBucket = "gs://pet-detection1"

for line in fileinput.FileInput("data/train_labels.csv",inplace=1):
    p = line[:]
    cont = p.split(",")
    cont[7] = cont[7][:-1]
    xmin = (int(cont[4])/int(cont[1]))
    ymin = (int(cont[5])/int(cont[2]))
    xmax = (int(cont[6])/int(cont[1]))
    ymax = (int(cont[7])/int(cont[2]))
    rand = random.randint(0, 10)
    print("UNASSIGNED," + gcBucket + "/images/train/"+cont[0]+","+cont[3]+","+str(xmin)+","+str(ymin)+",,,"+str(xmax)+","+str(ymax)+",,")