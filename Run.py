from NeuralNetwork import NeuralNetwork
import time
class trainingData:
    def __init__(self, inputs, answers):
        self.inputs = inputs
        self.answers = answers

    def print(self):
        print(self.inputs)
        print(self.answers)

while(True):
    print("How many inputs do you want to put into the neural network?:")
    inputNumber = int(input())
    print("How many hidden layers (more layers means it has an easier time learning but require a longer time to train)?:")
    hiddenLayerNumber = int(input())
    print("How many output digits are you expecting (Answers are either 1 or 0)?:")
    outputNumber = int(input())
    print("Is this correct? Y or N")
    print("Number of Inputs Digits: ", inputNumber)
    print("Number of Hidden Layers: ", hiddenLayerNumber)
    print("Number of Outputs Digits: ", outputNumber)
    checkCorrect = input()
    if(checkCorrect == "Y" or checkCorrect == "y"):
        break;

nn = NeuralNetwork(inputNumber, hiddenLayerNumber, outputNumber)



trainingDataList = []
stopValue = True
while(stopValue):
    print("Input digit length: ", inputNumber)
    print("Provide and input:")
    inputValue = input().zfill(inputNumber)
    if(inputValue == "stop"):
        break
    if(len(str(inputValue).zfill(inputNumber)) != inputNumber):
        print("Not a valid input.")
        continue

    print("Provide the expected value: (consist of 1s or 0s)")
    expectedOutput = input().zfill(outputNumber)
    if(expectedOutput == "stop"):
        break
    if(len(str(expectedOutput).zfill(outputNumber)) != outputNumber):
        print("Not a valid input.")
        continue

    trainingDataList.append(trainingData(list(str(inputValue)), list(str(expectedOutput))))

    for i in trainingDataList:
        i.print()


print("Training: ", end="", flush=True)

for i in range(5000):
    for j in trainingDataList:
        nn.training(j.inputs, j.answers)
print("Done")

for i in trainingDataList:
    print(i.inputs, nn.feedForward(i.inputs))

while (True):
    print("\nWould you like to test an input? Y or N")
    testInput = input().zfill(inputNumber)

    if testInput == "y" or testInput == "Y":
        print("What is the input:")
        testIntInput = input().zfill(inputNumber)
        print(nn.feedForward(list(str(testIntInput))))

    elif testInput == "n" or testInput == "N":
        break;


print("\nIs this correct? Y or N")
correct = input()
if(correct == "n" or correct == "N"):
    while(True):
        print("Input to retrain:")
        retrainInput = input().zfill(inputNumber)
        if(retrainInput == "stop"):
            break;
        if (len(str(retrainInput).zfill(inputNumber)) != inputNumber):
            print("Not a valid input.")
            continue

        print("Provide the expected value: (consist of 1s or 0s)")
        retrainOutput = input().zfill(outputNumber)
        if (retrainOutput == "stop"):
            break
        if (len(str(retrainOutput).zfill(outputNumber)) != outputNumber):
            print("Not a valid input.")
            continue

        for i in range(100):
            nn.training(list(str(retrainInput)), list(str(retrainOutput)))

        for i in trainingDataList:
            print(i.inputs, nn.feedForward(i.inputs))


        print("Is this correct? Y or N")
        correct = input()
        if correct == "Y" or correct == "y":
            break;

print("TADA!")