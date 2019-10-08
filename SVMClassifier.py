import MLAlgorithmBase
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
import numpy as np


class SVMClassifier:
    def __init__(self):
        # self.clf = SVC(gamma='auto')
        self.clf = KNeighborsClassifier(n_neighbors=3)

    def train(self, images, labels):
        numpy_pictures = np.array(images)
        self.clf.fit(numpy_pictures, labels)

    def predict(self, image):
        return self.clf.predict([image])

    # def test(self, pictures, right_labels):
    #     pass
