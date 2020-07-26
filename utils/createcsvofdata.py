import os
import csv

class_labels = {"BEANS": 1, "CAKE": 2, "CANDY": 3, "CEREAL": 4, "CHIPS": 5, "CHOCOLATE": 6, "COFFEE": 7, "CORN": 8, "FISH": 9, "FLOUR": 10, "HONEY": 11, "JAM": 12, "JUICE": 13, "MILK": 14, "NUTS": 15, "OIL": 16, "PASTA": 17, "RICE": 18, "SODA": 19, "SPICES": 20, "SUGAR": 21, "TEA": 22, "TOMATO_SAUCE": 23, "VINEGAR": 24, "WATER": 25}

src_dir = './datasets/freiburg/images'

with open('./datasets/freiburg/annotatedimages.csv', 'w') as csvfile:
    filewriter = csv.writer(csvfile)
    for subdir, dirs, files in os.walk(src_dir):
        for file in files:
            label = class_labels[os.path.basename(subdir)]
            filewriter.writerow([os.path.join(subdir, file), label])
        