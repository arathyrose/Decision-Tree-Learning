import pandas as pd
import json


# Read contents of file
data = pd.read_csv("dataset_SK.csv")

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

# Make swaps based on the roll_no
roll_no = 2018101042
second_last_digit = int((roll_no % 100)/10)
last_digit = roll_no % 10

flip1 = (last_digit+second_last_digit) % data_size+1
flip2 = (second_last_digit) % data_size+1

if(flip1 == flip2):
    flip1 = (second_last_digit) % data_size+1
    flip2 = (second_last_digit+1) % data_size+1

t = data[flip1][3]
data[flip1][3] = data[flip2][3]
data[flip2][3] = t

# now data is ready
print("FINAL DATA: ", data)

# save this data to a file
with open("out1.txt", "w") as f:
    json.dump(f, data)
