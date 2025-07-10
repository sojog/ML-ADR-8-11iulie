import numpy as np


def sigmoid(x):
    return 1/ ( 1 + np.exp(-x))


class Neuron:
    def __init__(self, weights, bias):
        self.weights = weights
        self.bias = bias

    def __str__(self):
        return f"Neuronul cu greutatile {self.weights} si bias {self.bias}"
        
    def feedforward(self, inputs):
        total = np.dot(self.weights, inputs) + self.bias
        return sigmoid(total)
    



neuron = Neuron([0, 1], 4) # __init__
print(neuron)              # __str__

print(neuron.feedforward([2, 3]))
