import numpy as np
import pandas as pd
import math
import statistics
import random

def selectWithGaussian(inputData,mu,sig,shuffle=False):
    def calculateSelectionProbs(function, labelSpace, normalization=True):
        # Generate selection probabilities for each label according to given function
        selectionProbs = [function(x) for x in labelSpace]
        if normalization:
            normFactor = 1 / max(selectionProbs)
            selectionProbs = [item * normFactor for item in selectionProbs]
        selectionCriteria = {labelSpace[i]: selectionProbs[i] for i in range(len(labelSpace))}
        return selectionCriteria


    def selectWithProbs(data, selectionCriteria):
        # Select items in dataset according to a dictionary of selection probabilities
        selectedData = []
        for sample in data:
            if random.uniform(0, 1) < float(selectionCriteria.get(sample)):
                selectedData.append(sample)
        return selectedData


    def shuffleNonMax(criteria):
        maxElement = max(criteria, key=criteria.get)
        maxValue = criteria.get(maxElement)
        del criteria[maxElement]
        keys = list(criteria.keys())
        values = list(criteria.values())
        random.shuffle(values)
        newDict = {keys[i]: values[i] for i in range(len(keys))}
        newDict[maxElement] = maxValue
        return newDict


    def gaussian(x, mu, sig):
        return np.exp(- np.power(x - mu, 2.) / (2 * np.power(sig, 2.))) / (sig * math.sqrt(2 * math.pi))

    # Select 'mu' according to most frequent label
    # sig determines the shape of the curve
    myGaussian = lambda x: gaussian(x, mu=mu, sig=sig)

    # Generate probability vector with myGaussian
    criteria = calculateSelectionProbs(myGaussian, list(set(inputData)))

    # Shuffle the probability vector without effecting the "peak"
    if shuffle : criteria_shuffled = shuffleNonMax(criteria)

    # Select a subset of the original dataset according to the probability vector
    sampledData = selectWithProbs(inputData, criteria)

    return sampledData
