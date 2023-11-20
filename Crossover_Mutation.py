#Perform Crossover and Mutation

#libraries 
import numpy as np
import random as rd
from random import randint

#Functions

def sing_crossover(parents, num_offsprings):
    offsprings = np.empty((num_offsprings, parents.shape[1]))
    c_point = int(parents.shape[1]/2)   #crossover point (single)
    c_rate = 0.9                       #crossover rate (for optimum solution)
    i=0
    while (parents.shape[0] < num_offsprings):
        p1_ind = i%parents.shape[0]
        p2_ind = (i+1)%parents.shape[0]
        x = rd.random()
        if x > c_rate:
            continue
        p1_ind = i%parents.shape[0]
        p2_ind = (i+1)%parents.shape[0]
        offsprings[i,0:c_point] = parents[p1_ind,0:c_point]
        offsprings[i,c_point:] = parents[p2_ind,c_point:]
        i=+1
    return offsprings


def mutation(offsprings):
    mutants = np.empty((offsprings.shape))
    m_rate = 0.4
    for i in range(mutants.shape[0]):
        random_value = rd.random()
        mutants[i,:] = offsprings[i,:]
        if random_value > m_rate:
            continue
        rd_value = randint(0,offsprings.shape[1]-1)
        if mutants[i,rd_value] == 0 :
            mutants[i,rd_value] = 1
        else :
            mutants[i,rd_value] = 0
    return mutants