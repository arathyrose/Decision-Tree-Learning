# What is greedy approach in Decision tree algorithm

“Greedy Approach is based on the concept of Heuristic Problem Solving by making an optimal local choice at each node. By making these local optimal choices, we reach the approximate optimal solution globally.”

The algorithm can be summarized as :

1. At each stage (node), pick out the best feature as the test condition.
2. Now split the node into the possible outcomes (internal nodes).
3. Repeat the above steps until all the test conditions have been exhausted into leaf nodes.

When you start to implement the algorithm, the first question is: ‘How to pick the starting test condition?’

- Entropy: Entropy in Decision Tree stands for homogeneity. If the data is completely homogenous, the entropy is 0, else if the data is divided (50-50%) entropy is 1.
- Information Gain: Information Gain is the decrease/increase in Entropy value when the node is split.

An attribute should have the highest information gain to be selected for splitting. Based on the computed values of Entropy and Information Gain, we choose the best attribute at any particular step.
