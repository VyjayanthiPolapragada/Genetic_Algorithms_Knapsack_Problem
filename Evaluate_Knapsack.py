#To evaluate the Knapsack

import numpy as np
import random as rd
from random import randint
from Fitness_Selection import compute_fitness, selection
from Crossover_Mutation import sing_crossover, mutation

def knapsack(weight, value, pop, pop_size, num_gene,max_limit):
 fitness_history = []
 paramtrs=[]
 num_parents = int(pop_size[0] / 2)
 num_offsprings = pop_size[0] - num_parents
 for i in range(num_gene):
    fitness = compute_fitness(weight, value, pop, max_limit)
    fitness_history.append(fitness)
    parents = selection(fitness,num_parents, pop)
    offsprings = sing_crossover(parents, num_offsprings)
    mutants = mutation(offsprings)
    pop[0:parents.shape[0], :] = parents
    pop[parents.shape[0]:, :] = mutants

    print("Last generation: \n{}\n".format(pop))
    fitness_last_gen = compute_fitness(weight, value, pop, max_limit)
    print("Fitness of the last generation: \n{}\n".format(fitness_last_gen))
    max_fitness = np.where(fitness_last_gen == np.max(fitness_last_gen))
    paramtrs.append(pop[max_fitness[0][0], :])
    return paramtrs, fitness_history