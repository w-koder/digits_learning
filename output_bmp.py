import os
# import from PIL import Image

from pathlib import PurePath

import read


# def output_all_images(dir_name, image_datas):
#     os.mkdir(dir_name)
#     os.chdir(dir_name)
#
#     i = 0
#     for image_data in image_datas:
#         PIL.Im
#         im.save(str(i) + ".bmp")
#         i += 1
#
#     os.chdir('..')


if __name__ == '__main__':
    data_dir = PurePath(os.getcwd()) / '..' / 'data'
    # images_filename = data_dir / 'train-images-idx3-ubyte' / 'train-images.idx3-ubyte'
    # train_images = read.read_images(images_filename, 4)
    # output_all_images("train", train_images)

    labels_filename = data_dir / 'train-labels-idx1-ubyte' / 'train-labels.idx1-ubyte'
    train_labels = read.read_labels(labels_filename)
    print(train_labels)
    #
    # images_filename = data_dir /  't10k-images-idx3-ubyte' / 't10k-images.idx3-ubyte'
    # test_images = read.read_images(images_filename)

    labels_filename = data_dir / 't10k-labels-idx1-ubyte' / 't10k-labels.idx1-ubyte'
    test_labels = read.read_labels(labels_filename)

    with open("labels.txt", 'w') as f:
        f.write("train_labels: " + str(train_labels) + "\n")
        f.write("test_labels: " + str(test_labels) + "\n")

    # output_all_images("test", test_images)

