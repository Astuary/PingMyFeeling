import os
import io
import git
import shutil
import urllib
import zipfile
import tarfile
import requests
from subprocess import call
from urllib.request import urlretrieve

dataset_url_freiburg = "http://aisdatasets.informatik.uni-freiburg.de/freiburg_groceries_dataset/freiburg_groceries_dataset.tar.gz"

dataset_url_epfl_food_11 = "https://www.kaggle.com/vermaavi/food11/download" 

dataset_url_d2s = "ftp://guest:GU.205dldo@ftp.softronics.ch/mvtec_d2s/v1.0/d2s_images_v1.tar.xz"

dataset_url_d2s_annotations = "ftp://guest:GU.205dldo@ftp.softronics.ch/mvtec_d2s/v1.1/d2s_annotations_v1.1.tar.xz"

dataset_url_grocery_store = "https://github.com/marcusklasson/GroceryStoreDataset.git"

dataset_url_magdeburg = "http://cse.iks.cs.ovgu.de/downloads/groceries/md_groceries.zip"

if __name__ == "__main__":    
    print("Downloading Freiburg dataset.")
    urlretrieve(dataset_url_freiburg, "./datasets/freiburg_groceries_dataset.tar.gz")
    print("Extracting Freiburg dataset.")
    call(["tar", "-xf", "./datasets/freiburg_groceries_dataset.tar.gz", "-C", "./datasets/freiburg"])
    os.remove("./datasets/freiburg_groceries_dataset.tar.gz")
    print("Done.")

    print("Downloading EPFL Food-11 dataset.")
    r = requests.get(dataset_url_epfl_food_11, stream=True)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    print("Extracting EPFL Food-11 dataset.")
    z.extractall("./datasets/food_11")
    z.close()
    print("Done.")

    print("Downloading Densely Segmented Supermarket dataset.")
    urlretrieve(dataset_url_d2s, "./datasets/densely_segmented_supermarket.tar.gz")
    urlretrieve(dataset_url_d2s_annotations, "./datasets/densely_segmented_supermarket_annotations.tar.gz")
    print("Extracting Densely Segmented Supermarket dataset.")
    tar = tarfile.open('./datasets/densely_segmented_supermarket.tar.gz')
    tar.extractall('./datasets/d2s')
    tar.close()
    tar = tarfile.open('./datasets/densely_segmented_supermarket_annotations.tar.gz')
    tar.extractall('./datasets/d2s')
    tar.close()
    os.remove("./datasets/densely_segmented_supermarket.tar.gz")
    os.remove("./datasets/densely_segmented_supermarket_annotations.tar.gz")
    print("Done.")

    print("Downloading Grocery Store dataset.")
    git.Git("./datasets").clone(dataset_url_grocery_store)
    print("Moving Grocery Store dataset.")
    shutil.move("./datasets/GroceryStoreDataset/dataset", "./datasets/grocerystore")
    print("Done.")

    print("Downloading Magdeburg Groceries dataset.")
    r = requests.get(dataset_url_magdeburg, stream=True)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    print("Extracting Magdeburg Groceries dataset.")
    z.extractall("./datasets/magdeburg")
    z.close()
    print("Done.")