import MLAlgorithmBase
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import read


class MyNetClassifier:

    MAX_BIAS = 5

    def __init__(self, picture_size):
        self.layers_number_of_elements = np.array([picture_size*picture_size, 100, 50, 10])
        self.net_value = [np.zeros(size) for size in self.layers_number_of_elements]
        weights_shapes = zip(self.layers_number_of_elements[:-1], self.layers_number_of_elements[1:])
        self.net_weights = [np.random.random(shape) * 2 - 1 for shape in weights_shapes]
        self.biases = [np.random.random(layer_size) * MyNetClassifier.MAX_BIAS for layer_size in self.layers_number_of_elements[1:]]


    @staticmethod
    def _normalization_func(x):
        return 1/(1 + np.exp(-x))

    def train(self, images, labels):
        pass

    def predict(self, image):
        self.net_value[0] = image
        for i in range(1, len(self.net_value)):
            self.net_value[i] = MyNetClassifier._normalization_func(np.dot(self.net_value[i-1], self.net_weights[i-1]) - self.biases[i-1])

        return self.net_value[-1]

    # def test(self, pictures, right_labels):
    #     pass
