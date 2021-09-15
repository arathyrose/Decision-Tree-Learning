# DECISION TREES

## How to run

- put your dataset in `dataset.csv` file
- edit your roll number in `make_all_ready.py`. For a plain decision tree learning algorithm, set `roll_no = ""`
- run `make_all_ready.py` using `python3`

### Running the main algorithm

- Rename the output obtained in the previous step to `input.txt`
- Run `main_algorithm.py` using `python3`
    As the program runs, the values of entropy and information gain obtained at each step is displayed.
- Obtain the split output in output1.txt and output2.txt
- For each output file obtained, unless the collective output of all the rows are the same, repeat the algorithm

### Contructing the tree from the main_algorithm

- The final line contains the choice decision made to split the dataset. Use this as a node in the decision tree.
- After splitting the dataset into two, while running the program again, the decision output obtained becomes the next node. (refer `theory.md` for better understanding)

## Directory Structure

| File Name         | Description                                                    |
| ----------------- | -------------------------------------------------------------- |
| Question.pdf      | Contains the list of datasets                                  |
| theory.md         | Contains the theory for decision trees (as discussed in class) |
| algorithm.md      | A brief description of the algorithm                           |
| a.png             | Contains a sample decision tree                                |
| question.md       | Contains a brief explanation for Q3                            |
| dataset.csv       | Contains a sample dataset corresponding to Q3                  |
| make_all_ready.py | Generates the input file for the main_algorithm                |
| main_algorithm.py | Performs the main algorithm                                    |

## Google colab link

This project is also available in google colab at ![here](https://colab.research.google.com/drive/1drcycPP76EYOjHivbnR1gz0tdJVed6BF#scrollTo=8RHR_jLfJx4S)

### Instructions to run

- Upload the `dataset.csv` file if available.
- Run all the cells.
- Edit cell  `dataset =` to your desired dataset.
- Check the section before, and rename the input files accordingly to run the next section of the code, and repeat.
