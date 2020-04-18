import numpy as np
class Matrix:
    rows = 0
    columns = 0
    values = []

    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.values = np.zeros((rows, columns))

    def randomize(self):
        self.values = np.random.rand(self.rows, self.columns)

    def add(self, input):
        if type(input) == int:
            self.values = self.values + input
        elif type(input) == Matrix:
            self.values = np.add(self.values, input.values)

    @staticmethod
    def subtract(input1, input2):
        input1Rows = len(input1.values)
        input2Rows = len(input2.values)
        input1Columns = len(input1.values[0])
        input2Columns = len(input2.values[0])
        output = Matrix(input1Rows, input2Columns)
        for i in range(0, input1Rows):
            for j in range(0, input2Columns):
                output.values[i][j] = input1.values[i][j] - input2.values[i][j]
        output.rows = len(output.values)
        output.columns = len(output.values[0])
        return output

    @staticmethod
    def fromArray(array):
        iterator = 0
        output = Matrix(len(array), 1)
        for i in array:
            output.values[iterator][0] = i
            iterator += 1
        # FACT CHECK THIS
        output.columns = len(output.values[0])
        output.rows = len(output.values)
        return output

    @staticmethod
    def toArray(array):
        output = array.flatten()
        return output

    @staticmethod
    def staticMultiply(matrix1, matrix2):
        # try:
            if type(matrix1) != Matrix or type(matrix2) != Matrix:
                return "NO"
            else:
                returnValue = Matrix(1, 1)
                returnValue.values = np.matmul(matrix1.values, matrix2.values)
                returnValue.rows = len(returnValue.values)
                returnValue.columns = len(returnValue.values[0])
                return returnValue
        # except Exception as e:
            # print(e)

    # TO MULTIPLY TWO MATRIXES TOGETHER THEY MUST BE THE SAME SHAPE
    def multiply(self, input):
        try:
            if type(input) == Matrix:
                for i in range(len(input.values)):
                    for j in range(len(input.values[0])):
                        self.values[i][j] *= input.values[i][j]
            else:
                self.values * input
        except Exception as e:
            print(e)

    @staticmethod
    def transpose(matrix):
        returnValue = Matrix(matrix.columns, matrix.rows)
        returnValue.values = np.transpose(matrix.values)
        returnValue.rows = len(returnValue.values)
        returnValue.columns = len(returnValue.values[0])
        return returnValue

    def toString(self):
        print(self.values)

