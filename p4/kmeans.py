import operator
import matplotlib.pyplot as plt
import math
import csv

                        ## The code is written in Python using PyCharm ##

##########################################################################
# Opening the training data file
def loadTrainingData(fname):
    csvFile = open(fname,'r')
    lines = csv.reader(csvFile)
    data_set = list(lines)
    data_set.pop(0)
    for column in range(len(data_set)):
        for row in range(len(data_set[0])):
            data_set[column][row] = float(data_set[column][row])
    return data_set
##########################################################################

def euclideanDistance(ins1, ins2, noOfcolumns):
    distance = 0
    for x in range(noOfcolumns):
        distance += pow((ins1[x] - ins2[x]), 2)
    return math.sqrt(distance)

##########################################################################
def getNeighborsData(trainingSet, test_row, k):
    neighbors = []
    number_of_columns = len(test_row) - 1
    for x in range(len(trainingSet)):
        dist = euclideanDistance(test_row, trainingSet[x], number_of_columns)
        neighbors.append((trainingSet[x], dist))
    neighbors.sort(key=operator.itemgetter(1))
    k_neighbors_price_range = []
    for i in range(k):
        k_neighbors_price_range.append(neighbors[i][0][20])
    return k_neighbors_price_range
###########################################################################

def getResponse(neighbors):
    class_votes = {}
    for x in range(len(neighbors)):
        response = neighbors[x]
        if response in class_votes:
            class_votes[response] += 1
        else:
            class_votes[response] = 1
    sorted_votes = sorted(class_votes.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_votes[0][0]
###########################################################################

def getAccuracy(test_set, predictions):
    correct = 0
    for x in range(len(test_set)):
        if test_set[x][-1] == predictions[x]:
            correct += 1
    print("Correct: ", correct)
    return (correct / float(len(test_set))) * 100


def main():
    training_data_file = 'train.csv'
    testing_data_file = 'test.csv'
    training_set = loadTrainingData(training_data_file)
    test_set = loadTrainingData(testing_data_file)
    print("\n\nTraining set: ", len(training_set))
    print("Testing set: ", len(test_set))
    y_coordinate = []
    k = 10
    k_neighbors_price_ranges = []


    ## Taking the prices of each neighbor for every row
    print("\nCalculating Euclidean Distance \nPlease wait for few seconds...")
    for x in range(len(test_set)):
        k_neighbors_price_range = getNeighborsData(training_set, test_set[x], k)
        k_neighbors_price_ranges.append(k_neighbors_price_range)
    print("\nEuclidean Distance calculations are done!\n\n")
    for j in range(1, k + 1):
        predictions = []
        print("#####################################")
        print("K: ", j)
        for i in range(len(k_neighbors_price_ranges)):
            result = getResponse(k_neighbors_price_ranges[i][0:j])
            predictions.append(result)
        accuracy = getAccuracy(test_set, predictions)
        print("Accuracy: " + str(accuracy) + "%\n")
        print("#####################################")
        y_coordinate.append(accuracy)
#############################################################################
## Plot the graph

    f = plt.figure()
    plt.plot(range(1, 11), y_coordinate)
    f.savefig("plot.pdf", bbox_inches='tight')


main()
