# PROBLEMĂ REZOLVATĂ: Adăugat importul numpy
import numpy as np

def mse_loss(y_real, y_prezis):
    return ((np.array(y_real) - np.array(y_prezis)) ** 2).mean()

def sigmoid(x):
    return 1/ ( 1 + np.exp(-x))

def deriv_sigmoid(x):
    fx = sigmoid(x)
    return fx * (1 - fx)

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
        self.w1 = np.random.normal()
        self.w2 = np.random.normal()
        self.w3 = np.random.normal()
        self.w4 = np.random.normal()
        self.w5 = np.random.normal()
        self.w6 = np.random.normal()

        self.b1 = np.random.normal() 
        self.b2 = np.random.normal() 
        self.b3 = np.random.normal() 

        self.hidden1 = Neuron([self.w1, self.w2], self.b1)
        self.hidden2 = Neuron([self.w3, self.w4], self.b2)
        self.output = Neuron([self.w5, self.w6], self.b3)


    def feedforward(self, input):
        ouput_hidden1 = self.hidden1.feedforward(input)
        ouput_hidden2 = self.hidden2.feedforward(input)

        result_output_layer = self.output.feedforward([ouput_hidden1, ouput_hidden2])

        return result_output_layer
    

    def train(self, input_data, real_output_data):

        learning_rate = 0.1 # 0.01 0.001
        EPOCH = 100000
        for i in range(EPOCH): 
            for x, y_true in zip(input_data, real_output_data):
                sum_hidden1 = self.w1 * x[0] + self.w2 * x[1] + self.b1
                h1 = sigmoid(sum_hidden1)

                sum_hidden2 = self.w3 * x[0] + self.w4 * x[1] + self.b2
                h2 = sigmoid(sum_hidden2)

                sum_output2 = self.w5 * h1 + self.w6 * h2 + self.b3
                o1 = sigmoid(sum_output2)

                y_prezis = o1

                # Calculul loss-ului: ((y_true - y_prezis) ** 2) / 2

                derivata_y_prezis = -2 * (y_true - y_prezis)

                derivata_w5_y_prezis = h1 * deriv_sigmoid(sum_output2)
                derivata_w6_y_prezis = h2 * deriv_sigmoid(sum_output2)
                derivata_b3_y_prezis = deriv_sigmoid(sum_output2)

                derivata_h1_y_prezis = self.w5 * deriv_sigmoid(sum_output2)
                derivata_h2_y_prezis = self.w6 * deriv_sigmoid(sum_output2)

                derivata_w1_h1 = x[0] * deriv_sigmoid(sum_hidden1)
                derivata_w2_h1 = x[1] * deriv_sigmoid(sum_hidden1)
                derivata_b1_h1 = deriv_sigmoid(sum_hidden1)

                derivata_w3_h2 = x[0] * deriv_sigmoid(sum_hidden2)
                derivata_w4_h2 = x[1] * deriv_sigmoid(sum_hidden2)
                derivata_b2_h2 = deriv_sigmoid(sum_hidden2)


                # Actualizări pentru hidden layer 1:
                self.w1 = self.w1 - learning_rate * derivata_y_prezis * derivata_h1_y_prezis * derivata_w1_h1
                self.w2 = self.w2 - learning_rate * derivata_y_prezis * derivata_h1_y_prezis * derivata_w2_h1
                self.b1 = self.b1 - learning_rate * derivata_y_prezis * derivata_h1_y_prezis * derivata_b1_h1

                # Actualizări pentru hidden layer 2:
                self.w3 = self.w3 - learning_rate * derivata_y_prezis * derivata_h2_y_prezis * derivata_w3_h2
                self.w4 = self.w4 - learning_rate * derivata_y_prezis * derivata_h2_y_prezis * derivata_w4_h2
                self.b2 = self.b2 - learning_rate * derivata_y_prezis * derivata_h2_y_prezis * derivata_b2_h2
                
                # Actualizări pentru output layer:
                self.w5 = self.w5 - learning_rate * derivata_y_prezis * derivata_w5_y_prezis
                self.w6 = self.w6 - learning_rate * derivata_y_prezis * derivata_w6_y_prezis
                self.b3 = self.b3 - learning_rate * derivata_y_prezis * derivata_b3_y_prezis
                







date_initiale = {
    "Alina" : [60, 165, True],
    "Bogdan" : [72, 183, False],
    "Ciprian" : [69, 178, False],
    "Diana" : [55, 152, True]
}

date_de_test = {
    "Florin" : [92, 183, False],
    "Emilia" : [62, 163, True],
    "George" : [77, 198, False],
    "Iulia" : [58, 156, True]
}


def preprocesare(input_data):
    kg, inaltime, *restul =  input_data
    return (kg - 61, inaltime - 168, *restul)


input_data = []
for data_point in date_initiale.values():
    input_data.append(preprocesare(data_point))

print(input_data)


real_output_data = np.array([1, 0, 0, 1])

my_network = NeuralNetwork()

# ECHIVALENT lui fit
my_network.train(input_data, real_output_data)






for name in date_initiale:
    individ = np.array(date_initiale[name][:2])
    individ = preprocesare(individ)
    print("Datele individului", individ)
    # ECHIVALENT lui predict
    print(f"Probabilitatea {name} de a fi femeie este:", my_network.feedforward(individ))/Users/silviu/Desktop/ExercitiuNN/NN_masini.py