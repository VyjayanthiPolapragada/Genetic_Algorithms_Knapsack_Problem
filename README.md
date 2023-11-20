# Genetic_Algorithms_Knapsack_Problem
Solving a single constraint binary (0-1) Knapsack problem using the concept of Genetic Algorithms

Single constraint: This type of problem is the standard knapsack problem where the limitation is only for one variable of the given items.

Binary (0-1): In this type of knapsack problem, there is only one item of each kind (or we can pick only one). 
So, we are available with only two options for each item, either pick it (1) or leave it (0)

Genetic Algorithms are computer algorithms that search for good solutions to a problem from among a large number of possible solutions.

Uploaded python files consists of different functions for different stages of Genetic Algorithm as stated below

1. Fitness_Selection.py : Used for defining functions which compute the fitness of population and select the fittest individuals to undergo crossover
2. Crossover_Mutation.py : Used for defining functions which implement single point corssover for the fittest individuals and mutate using bit-flip technique
3. Evaluate_Knapsack.py: Calculates the fitness of last generation and returns its parameters

Check main.py for main python script 

Libraries used: numpy, random (comes buit-in for jupyter notebook)

Optimum solution can be obtained for custom data set and randomly generated dataset as well. 

