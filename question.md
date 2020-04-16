# ASSIGNMENT 4: MDL

## Guidelines

1. Construct a decision tree for the problem corresponding to ((roll numbers)%10+ 1).

2. For the chosen decision tree, flip entries[1-indexed] (make Yes as No and Vice Versa) for
         -  (LastDigitofRollNum+SecondLastDigitofRollNum)%NoOfEntriesInDataset+1
         -  (SecondLastDigitofRollNum)%NoOfEntriesInDataset+1
   - If both of the above are equal flip:
         -  (SecondLastDigitofRollNum)%NoOfEntriesInDataset+1
         -  (SecondLastDigitofRollNum+1)%NoOfEntriesInDataset+1
3. Follow the textbook for decision tree algorithm [Greedy version]
4. Decision tree needs to be calculated manually without help of any library. On account of missing steps,you will be appropriately penalized.
5. Refer to submission format at the end of the PDF.

## Guideline information

1. Problem = (2018101042 % 10)+1 = 3
2. Flip entries of (2+4)%9+1 and (4)%9+1 = 7 and 5

## Problem statement: Bull’s eye

After watching a movie, your TA is highly interested in determining if the sniper shot is going to make a kill or not. He is bad at physics but good at ML. Hence to confirm his hypothesis, he asks you to come up witha decision tree which fits the below data very well.

## Dataset SK

| Horizontal Angle(degree) | Distance(m) | Wind Speed(mph) | Kill |
| ------------------------ | ----------- | --------------- | ---- |
| 1.5                      | 450         | 220             | N    |
| 4.5                      | 520         | -120            | Y    |
| 3                        | 490         | 120             | Y    |
| 5.5                      | 530         | 117             | N    |
| 3.2                      | 470         | -170            | N    |
| 5.2                      | 505         | -90             | Y    |
| 1.85                     | 465         | 120             | Y    |
| 4.8                      | 517         | 147             | Y    |
| 1.7                      | 430         | -100            | Y    |

## Submission format

You will need to submit a zip of folder(RollNumber) containing two files:

### 1. A file(Rollnumber.txt)

1. Database Number(1-10)
2. Put conditions for every path to leaf node separated by ’and’.  Use′strexample′for strings[quotes].  Use == to check equality, comparison operators(<,>,≤,≥) remain the same.  Fields need to be mentioned as f[0],f[1],f[2],..., based on their position in table.  At the end, separated by acomma, put the expected label(don’t need quotes here).  

For example :f[0]<10 and f[1]==’Sunny’,Yes.

Example script for above tree:

```less
2
f[2]<5 and f[0]==’Rndm’ andf[1]<= 1, False
f[2]<5 and f[0]==’Rndm’ andf[1]>1, True
f[2]<5 and f[0]!=’Rndm’ andf[1]>2, True
f[2]<5 and f[0]!=’Rndm’ andf[1]<= 2, False
f[2]>= 5 andf[1] == 2, True
f[2]>= 5 andf[1]! = 2, False
```

### 2. A brief report explaining how you reached your solution[step-wise decisions and entropy at each step].(RollNumber.pdf)

- Make sure you report Entropy after each step.
- Please show all steps involved. On account of missing steps,you will be appropriately penalized
