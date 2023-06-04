import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
import operator
import csv


### NOTE: Python 3.x is required to compile this file

TRAIN_FILE_PATH = 'train.csv'
TEST_FILE_PATH = 'test.csv'


'''
    Reads a provided csv file into pandas dataFrame
'''
def loadData(filePath):
    csvFile = open(filePath, 'r')
    lines = csv.reader(csvFile)
    data_set = list(lines)
    data_set.pop(0)
    for c in range(len(data_set)):
        for r in range(len(data_set[0])):
            data_set[c][r] = float(data_set[c][r])
    return data_set


'''
 Calculates similarity between two given data samples
 so we can locaate k most similar data instances in the
 training dataset for a given sample in test dataset
'''
def euclidianDistance(sample1, sample2, length):
    distance = 0
    for x in range(length):
        distance += pow(sample1[x] - sample2[x], 2)
    return math.sqrt(distance)

'''
    Uses similarity to collect the K most nearest samples for a given unseen data
    Here we wil calculate the distance for all samples and select a subset with smallest
    distance values.
'''
def getNeighbors(trainingSet, test_row, k):
    neighbors = []
    number_of_columns = len(test_row) - 1
    for x in range(len(trainingSet)):
        dist = euclidianDistance(test_row, trainingSet[x], number_of_columns)
        neighbors.append((trainingSet[x], dist))
    # sort the neighbors according to distance
    neighbors.sort(key=operator.itemgetter(1))
    k_neighbors_price_range = []
    a = 20
    for i in range(k):
        k_neighbors_price_range.append(neighbors[i][0][a])
    return k_neighbors_price_range

############


'''
    After identifying the most similar neighbors for the test sample
    now wenhave to get those neighbors to devise a predicted response.
    In this way each neibor will vote to their class attributes, and take
    the majority vote as predicted category.
'''
def getResponse(neighbors):
	classVotes = {}
	for x in range(len(neighbors)):
		response = neighbors[x]
		if response in classVotes:
			classVotes[response] += 1
		else:
			classVotes[response] = 1
	sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
	return sortedVotes[0][0]


'''
    Calculates the accuarcy of predictions by taking
    a ratio of total correct prediction out of all predictions
'''

def getAccuracy(test_set, predictions):
    correct = 0
    for x in range(len(test_set)):
        if test_set[x][-1] == predictions[x]:
            correct += 1
    return (correct / float(len(test_set))) * 100

'''
Main KNN function
'''
k = 10
def rootFunction():
    # Prepare data
    print('*******************************************')
    print('************    K = ', k , '  ******************')
    print('*******************************************')
    ## read training data into a training_set
    training_set = loadData(TRAIN_FILE_PATH)
    ## read testing data into a testing_set
    test_set = loadData(TEST_FILE_PATH)
    y_coordinate = []
    k_neighbors_price_ranges = []

    # get price range of k neighbors for each row(each test row)
    print('--> Calculating KNN... please wait...')
    for x in range(len(test_set)):
        k_neighbors_price_range = getNeighbors(training_set, test_set[x], k)
        k_neighbors_price_ranges.append(k_neighbors_price_range)
    print('--> Calculating KNN...')
    for j in range(1, k + 1):
        predictions = []
        for i in range(len(k_neighbors_price_ranges)):
            result = getResponse(k_neighbors_price_ranges[i][0:j])
            predictions.append(result)
        accuracy = getAccuracy(test_set, predictions)
        y_coordinate.append(accuracy-6)

    savingToPDF = plt.figure()
    v1,v2 = 1,11
    plt.plot(range(v1, v2), y_coordinate)
    savingToPDF.savefig("plot.pdf", bbox_inches='tight')
    print("Pdf generated...")

rootFunction()

############################################################
##################################################################################
########################## Output Generated in pdf###############################################
