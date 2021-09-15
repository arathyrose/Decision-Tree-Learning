'''
Extract information from the dataset in csv format
Change dataset.csv to contain your dataset
Change roll_no to your roll number
The output would be saved to given.txt
'''

import pandas as pd
import json

# Enter roll number here
roll_no = 2018101042
# if you wish to use the project without any swapping, uncomment the following line:
# roll_no = ""

# Read contents of file
data = pd.read_csv("dataset.csv")

# Make it to our format
data = data.to_dict()
kkk = list(data.keys())
data_size = len(data[kkk[0]])

main_array = []
for i in range(data_size):
    row = [0]*4
    for j in range(len(kkk)):
        row[j] = data[kkk[j]][i]
    main_array.append(row)

data = main_array

if roll_no != "":
    # Make swaps based on the roll_no
    second_last_digit = int((roll_no % 100)/10)
    last_digit = roll_no % 10

    flip1 = (last_digit+second_last_digit) % data_size+1-1
    flip2 = (second_last_digit) % data_size+1-1

    if(flip1 == flip2):
        flip1 = (second_last_digit) % data_size+1-1
        flip2 = (second_last_digit+1) % data_size+1-1

    print(flip1, flip2)
    print(data[flip1], data[flip2])

    t = data[flip1][3]
    data[flip1][3] = data[flip2][3]
    data[flip2][3] = t

    print(data[flip1], data[flip2])

# now data is ready
print("FINAL DATA: ", data)

# save this data to a file
with open("given.txt", "w") as f:
    json.dump(data, f)
