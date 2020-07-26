from sklearn.model_selection import train_test_split
import pandas as pd

def splits(seed):
    metadata = pd.read_csv('./datasets/freiburg/annotatedimages.csv', names=["Path", "Label"])

    y = metadata.pop('Label')
    #print(y)

    X = metadata
    #print(X)

    train_X, val_X, train_y, val_y = train_test_split(X, y, test_size=0.25, random_state=seed, stratify=y)
    #print(train_X)
    #print(val_X)

    return (train_X, val_X, train_y, val_y)
