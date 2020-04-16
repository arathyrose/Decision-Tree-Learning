'''
Does the main algorithm
Takes the information stored in input.txt to produce the most optimal split based on entropy and maximised information gain
It also stores the split dataset into output1.txt and output2.txt
Input: input.txt
Output: output1.txt, output2.txt
'''
import math
import json


def log(no):
    if(no == 0):
        return - 1e+99
    return math.log(no, 2)


def information(n, y):
    print("I(y,n) = ",  - (n/(n + y))*log(n/(n + y)),
          ' + ',  - (y/(n + y))*log(y/(n + y)))
    print("I(y,n) = ",  - (n/(n + y)) *
          log(n/(n + y)) - (y/(n + y))*log(y/(n + y)))
    return - (n/(n + y))*log(n/(n + y)) - (y/(n + y))*log(y/(n + y))


def get_information(data):
    n = 0
    y = 0
    for i in data:
        if(i[3] == 'Y'):
            y += 1
        else:
            n += 1
    print("y = ", y)
    print("n = ", n)
    return information(n, y)


def mean(col):
    return sum(col)/len(col)


def partition(dataset, colno, val):
    nd1 = []
    nd2 = []
    for i in dataset:
        if(i[colno] < val):
            nd1.append(i)
        else:
            nd2.append(i)
    return nd1, nd2


def get_info_gain(dataset, colno):
    print()
    print("COLUMN", colno)
    print()
    col = [dataset[i][colno] for i in range(data_size)]
    pivot = mean(col)
    print("Condition: ", pivot)
    nd1, nd2 = partition(dataset, colno, pivot)
    print("Entropy calculations")
    print()
    print("Set1", len(nd1), nd1)
    print()
    gi1 = get_information(nd1)
    print()
    print("Set2", len(nd2), nd2)
    print()
    gi2 = get_information(nd2)
    print()
    entropy = (len(nd1)*gi1 + len(nd2)*gi2)/len(dataset)
    print("Entropy = ", len(nd1)*gi1/len(dataset), ' + ',
          len(nd2)*gi2/len(dataset), ' = ', entropy)
    info_gain = info_full - entropy
    print("Information gain = ", info_full, " - ", entropy, " = ", info_gain)
    print()
    return info_gain


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        dataset = json.load(f)
    data_size = len(dataset)
    print("DATASET:")
    print(dataset)
    print("Number of elements: ", data_size)
    print()
    print("COMPLETE DATASET")
    print()
    info_full = get_information(dataset)
    print()
    # partition the table values based on mean of the values
    print("Checking the best attribute:")
    ig = [get_info_gain(dataset, 0), get_info_gain(
        dataset, 1), get_info_gain(dataset, 2)]
    print(ig)
    print()
    column_to_split = ig.index(max(ig))
    print("Maximum at", column_to_split)
    print()
    col = [dataset[i][column_to_split] for i in range(data_size)]
    pivot = mean(col)
    print("Condition: ", pivot)
    nd1, nd2 = partition(dataset, column_to_split, pivot)
    json.dump(nd1, open("output1.txt", "w"))
    json.dump(nd2, open("output2.txt", "w"))
