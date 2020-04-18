import numpy as np
from Matrix import Matrix


def sigmoid(input):
    output = input
    for i in range(len(input)):
        output[i] = 1/(1 + np.exp(-input[i]))
    return output

def dSigmoid(input):
    output = input
    for i in range(len(input.values)):
        output.values[i] = input.values[i] * (1 - input.values[i])
    return output
    # output = Matrix(1,1)
    # output.values = input.values * (1 - input.values)
    # return output

def round(self, array):
    for i in self:
        if i > .5:
            i = 1
        else:
            i = 0
    return self

class NeuralNetwork:
    # NUMBER OF NODES
    inputNodes = 0
    hiddenNodes = 0
    outputNodes = 0
    # WEIGHTS
    weights_ih = Matrix(hiddenNodes, inputNodes)
    weights_ho = Matrix(hiddenNodes, outputNodes)
    weights_ih.randomize()
    weights_ho.randomize()
    # BIAS
    biasHidden = Matrix(hiddenNodes, 1)
    biasOutput = Matrix(outputNodes, 1)
    biasHidden.randomize()
    biasOutput.randomize()
    # Learning rate
    learningRate = 0

    def __init__(self, numberOfInputs, numberOfHidden, numberOfOutput):
        # NODES
        self.inputNodes = numberOfInputs
        self.hiddenNodes = numberOfHidden
        self.outputNodes = numberOfOutput
        # WEIGHTS
        self.weights_ih = Matrix(numberOfHidden, numberOfInputs)
        self.weights_ho = Matrix(numberOfOutput, numberOfHidden)
        self.weights_ih.randomize()
        self.weights_ho.randomize()
        # BIAS
        self.biasHidden = Matrix(numberOfHidden, 1)
        self.biasOutput = Matrix(numberOfOutput, 1)
        self.biasHidden.randomize()
        self.biasOutput.randomize()
        # Learning Rate
        self.learningRate = Matrix(1,1)
        self.learningRate.values = np.array([[.1]])

    def feedForward(self, inputArray):
        inputs = Matrix.fromArray(inputArray)
        hidden = Matrix.staticMultiply(self.weights_ih, inputs)
        hidden.add(self.biasHidden)
        # ACTIVATION FUNCTION
        hidden.values = sigmoid(hidden.values)

        output = Matrix.staticMultiply(self.weights_ho, hidden)
        output.add(self.biasOutput)
        output.values = sigmoid(output.values)
        output = Matrix.toArray(output.values)
        output = np.around(output)
        return output

    def training(self, inputArray, answers):
        #Feed Forward
        inputs = Matrix.fromArray(inputArray)
        hidden = Matrix.staticMultiply(self.weights_ih, inputs)
        hidden.add(self.biasHidden)
        # ACTIVATION FUNCTION
        hidden.values = sigmoid(hidden.values)

        output = Matrix.staticMultiply(self.weights_ho, hidden)
        output.add(self.biasOutput)
        output.values = sigmoid(output.values)

        #convert array to matrix object
        answers = Matrix.fromArray(answers)

        #calculate error
        #error = answer - outputs
        output_error = Matrix.subtract(answers, output)

        #calculate gradient
        gradient = dSigmoid(output)
        gradient.multiply(output_error)
        gradient.multiply(self.learningRate)


        #calculate deltas
        hidden_transposed = Matrix.transpose(hidden)
        weight_ho_deltas = Matrix.staticMultiply(gradient, hidden_transposed)

        self.weights_ho.add(weight_ho_deltas)
        self.biasOutput.add(gradient)

        #calculate hidden layer error
        weights_ho_transposed = Matrix.transpose(self.weights_ho)
        hidden_errors = Matrix.staticMultiply(weights_ho_transposed, output_error)

        hidden_gradient = dSigmoid(hidden)
        hidden_gradient.multiply(hidden_errors)
        hidden_gradient.multiply(self.learningRate)

        #calculate input to hidden deltas
        input_transpose = Matrix.transpose(inputs)
        weights_ih_deltas = Matrix.staticMultiply(hidden_gradient, input_transpose)

        self.weights_ih.add(weights_ih_deltas)
        self.biasHidden.add(hidden_gradient)
