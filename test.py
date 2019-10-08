import os
from pathlib import PurePath

import MyNetClassifier
import read
import output_bmp
import numpy as np

from SVMClassifier import SVMClassifier


def test():
    data_dir = PurePath(os.getcwd()) / '..' / 'data'

    images_filename = data_dir / 'train-images-idx3-ubyte' / 'train-images.idx3-ubyte'
    train_images = read.read_images(images_filename)
    # train_images = None

    labels_filename = data_dir / 'train-labels-idx1-ubyte' / 'train-labels.idx1-ubyte'
    train_labels = read.read_labels(labels_filename)

    images_filename = data_dir / 't10k-images-idx3-ubyte' / 't10k-images.idx3-ubyte'
    test_images = read.read_images(images_filename)
    # test_images = None

    labels_filename = data_dir / 't10k-labels-idx1-ubyte' / 't10k-labels.idx1-ubyte'
    test_labels = read.read_labels(labels_filename)

    # output_bmp.output_all_images("test", test_images)
    # output_bmp.output_all_images("train", train_images)

    # net = MyNetClassifier.MyNetClassifier(28)

    # net.init_random_params()

    svnC = SVMClassifier()
    svnC.train(train_images[0:10000], train_labels[0:10000])

    # print(svnC.predict(train_images[0]))

    for i in range(100):
        predicted = svnC.predict(test_images[i])[0]
        right = test_labels[i]
        print(str(i) + " " + "right" if predicted == right else f"false p={predicted} r={right}")





test()