#To compute fitness and selection

#libraries 
import numpy as np
import random as rd
from random import randint

#functions
def compute_fitness(w, v, pop, max):
    fitness = np.empty(pop.shape[0])     #w=weight, v= value
    for i in range(pop.shape[0]):
        sum_val = np.sum(pop[i] * v)
        sum_weight = np.sum(pop[i] * w)
        if sum_weight <= max:
            fitness[i] = sum_val
        else :
            fitness[i] = 0
    return fitness.astype(int)


def selection(fitness, num_parents, pop):
    fitness = list(fitness)
    parents = np.empty((num_parents, pop.shape[1]))
    for i in range(num_parents):
        max_fitness = np.where(fitness == np.max(fitness))   #finding the individual for max fitness in current population
        parents[i,:] = pop[max_fitness[0][0], :]
        fitness[max_fitness[0][0]] = -999999                 #setting the value to lowest num so that individual is not repeated
    return parents