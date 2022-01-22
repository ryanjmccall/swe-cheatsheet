"""
K-nearest neighbors (KNN) is a commonly used machine learning algorithm. In this exercise
you will implement a KNN classifier to first train the model given some data and then
to predict the labels for unseen data.
"""

TRAIN_X = [[-0.56609268, 0.11749865, -0.7657514, 1.00173918, 1.],
           [-0.63587199, -0.21052443, -2.65504997, -0.69705236, 1.],
           [1.64081183, 1.12999589, -1.12365889, 0.08600944, 1.],
           [-0.40046544, 0.68470095, 0.89202051, 1.4989387, 1.],
           [-0.61120999, 0.2593981, 0.61168084, 0.2697269, 1.],
           [-0.01044675, -0.36811214, 0.37314045, 0.6285882, 1.],
           [1.22472629, -0.45215746, 0.30795862, 0.48188224, 1.],
           [-0.31696489, -1.26490312, 0.19857967, 1.27315713, 1.],
           [0.60523791, -0.54445739, 0.83381999, -0.34457985, 1.],
           [2.03223487, -0.06955271, -1.4499377, 0.58363993, 1.]]

TRAIN_Y = [0, 1, 0, 0, 0, 1, 1, 1, 1, 0]

TEST_X = [[0.7695138, -0.71866324, -0.79215368, 0.94843848, 1],
          [-2.53898628, 0.16441869, 2.13857112, 1.85143163, 1],
          [2.94221919, -0.5960335, -0.49510827, 0.87702394, 1]]

import numpy as np
from collections import Counter


class KNN():
    def __init__(self, k=3):
        self.k = k

    def train(self, train_input, train_labels):
        """
        TODO: Fill in this function implementing the "training" procedure for KNN.
        Don't use any external libraries besides numpy :)
        :param train_input: A list containing a set of training data points, each represented as an n-dimensional
                            feature array of floats.
        :param train_labels: A list of the same size as `train_input` containing the binary (0/1) labels for each data point.
        :return: None
        """
        self.x = train_input
        self.y = train_labels

    def predict(self, test_input):
        """
        TODO: Fill in this function implementing inference for a trained model.
        Don't use any external libraries besides numpy :)
        :param test_input: A list containing a set of testing data points, each represented as an n-dimensional
                            feature array of floats.
        :return: A list of same size as `test_input` containing the predicted binary (0/1) labels for each point.
        """
        predictions = []
        for feats in test_input:
            # compute all distances to feats
            # get indicies of top k smallest distances
            # lookup train labels and find max occurring
            feats = np.array(feats)
            distances = [(i, np.linalg.norm(feats - np.array(b))) for i, b in enumerate(self.x)]
            distances.sort(key=lambda x: x[1])
            labels = [self.y[i] for i, _ in distances[:self.k]]
            pred = Counter(labels).most_common(1)[0][0]
            predictions.append(pred)

        return predictions


# Train model
model = KNN()
model.train(TRAIN_X, TRAIN_Y)
[
    model.predict(TEST_X)
]
