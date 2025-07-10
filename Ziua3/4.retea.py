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
    

class NeuralNetwork:

    def __init__(self):
        weights = [0, 1]
        bias = 0

        self.hidden1 = Neuron(weights, bias)
        self.hidden2 = Neuron(weights, bias)
        self.output = Neuron(weights, bias)

    def feedforward(self, input):
        ouput_hidden1 = self.hidden1.feedforward(input)
        ouput_hidden2 = self.hidden2.feedforward(input)

        result_output_layer = self.output.feedforward([ouput_hidden1, ouput_hidden2])

        return result_output_layer
    

my_network = NeuralNetwork()
x = [2, 3]
final_result = my_network.feedforward(x)
print(final_result)