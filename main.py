#Main 

import numpy as np
import random as rd
from random import randint
from Evaluate_Knapsack import knapsack
num_items = input("Enter the number of items in the knapsack")
knapsack_limit = input("Enter the maximum limit for the knapsack")
Max_KP = int(knapsack_limit)
item_num = np.arange(1,int(num_items)+1)
print("Choose whether the input is random or not")
print("\nEnter Random for random inputs or enter NotRandom ")
n=input("Enter")

if n == "Random":
                     up_limit=input("Enter the upper limit of weight")
                     low_limit=input("Enter the lower limit of weight")
                     val_ulimit=input("Enter the upper limit for values")
                     val_lowlimit=input("Enter the lower limit for values")
                     weight=np.random.randint(int(low_limit),int(up_limit), size=int(num_items))
                     value = np.random.randint(int(val_lowlimit), int(val_ulimit), size=int(num_items))
else:
         weight=[]
         value=[]
         for i in range(int(num_items)):
             w=input("Enter weight of "+str(i+1)+"element")
             weight.append(int(w))
             val=input("Enter the corresponding value")
             value.append(int(val))

print("The entered list is as follows")
print("Item No.   Weight   Value")
for i in range(item_num.shape[0]):
    print("{0}          {1}          {2}\n".format(item_num[i], weight[i], value[i]))
solutions_pop=input("Enter the population size")
sol_per_pop = int(solutions_pop)
pop_size = (sol_per_pop, item_num.shape[0])

print("Population size = {}".format(pop_size))

initial_pop = np.random.randint(2, size = pop_size)
initial_pop = initial_pop.astype(int)
num_generations=input("Enter the number of generations")
num_gene=int(num_generations)

print("Initial population: \n{}".format(initial_pop))

parameters, fitness_history = knapsack(weight, value, initial_pop, pop_size, num_gene,Max_KP)
print("The optimized parameters for the given inputs are: \n{}".format(parameters))
item_selected = item_num * parameters
print("\nThe following displays the items selected to have a maximum value without exceeding Knapsack limit:")
total_value=0
for i in range(item_selected.shape[1]):
  if item_selected[0][i] != 0:
     total_value = total_value+value[i]
     print("{}\n".format(item_selected[0][i]))
print("The maximum value obtained is",total_value)