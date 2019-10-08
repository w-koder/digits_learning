from PIL import Image

# picture_size = 0


def read_labels(filename):
    print("read_labels:")
    with open(filename, 'rb') as bytesIO:

        magic = bytesIO.read1(4)
        # print(int.from_bytes(magic, byteorder='big'))

        number_of_labels = int.from_bytes(bytesIO.read1(4), byteorder='big')
        # print("number_of_labels =", number_of_labels)

        print("read_labels done")
        return list(bytesIO.read1(number_of_labels))


def read_images(filename, show_image_i=-1):
    print("read_images:")
    with open(filename, 'rb') as bytesIO:

        magic = bytesIO.read1(4)
        # print("magic =", int.from_bytes(magic, byteorder='big'))

        number_of_images = int.from_bytes(bytesIO.read1(4), byteorder='big')
        number_of_rows = int.from_bytes(bytesIO.read1(4), byteorder='big')
        number_of_columns = int.from_bytes(bytesIO.read1(4), byteorder='big')

        # picture_size = number_of_rows

        # print("number_of_images =", number_of_images)
        # print("number_of_rows =", number_of_rows)
        # print("number_of_columns =", number_of_columns)
        all_images = []

        for i in range(number_of_images):
            data = bytesIO.read1(number_of_rows * number_of_columns)
            # print(data)
            image = Image.frombytes(mode='L', size=(number_of_rows, number_of_columns), data=data)
            pixels = [image.getdata()[i] for i in range(number_of_rows * number_of_columns)]
            all_images.append(pixels)
            if i == show_image_i:
                image.show()

    print("read_images done")
    return all_images


# def main_test():
#     images_filename = '..\\train-images-idx3-ubyte\\train-images.idx3-ubyte'
#     pixels = read_images(images_filename)
#
#     labels_filename = '..\\train-labels-idx1-ubyte\\train-labels.idx1-ubyte'
#     labels = read_labels(labels_filename)
#
#
# main_test()