from imports import *
from Algorithm import *
from Problem import *
from Population import *
from Swarm import *
from Controller import *







# -*- coding: utf-8 -*-
"""
Sa se determine minimul functiei f(x)= x_1**2+...+x_n**2

"""

from random import randint, random
from operator import add
from math import cos, pi


def individual(length, vmin, vmax):
    '''
    Create a member of the population - an individual

    length: the number of genes (components)
    vmin: the minimum possible value 
    vmax: the maximum possible value 
    '''
    return [ (random()*(vmax-vmin)+vmin) for x in range(length) ]
    
def population(count, length, vmin, vmax):
    """
    Create a number of individuals (i.e. a population).

    count: the number of individuals in the population
    length: the number of values per individual
    vmin: the minimum possible value 
    vmax: the maximum possible value 
    """
    return [ individual(length, vmin, vmax) for x in range(count) ]

def fitness(individual):
    """
    Determine the fitness of an individual. Lower is better.(min problem)
    For this problem we have the Rastrigin function
    
    individual: the individual to evaluate
    """
    x=individual[0]
    y=individual[1]
    return (sin(x+y) + (x-y)**2 - 1.5*x + 2.5*y + 1.0)
    
def mutate(individual, pM, vmin, vmax): 
    '''
    Performs a mutation on an individual with the probability of pM.
    If the event will take place, at a random position a new value will be
    generated in the interval [vmin, vmax]

    individual:the individual to be mutated
    pM: the probability the mutation to occure
    vmin: the minimum possible value 
    vmax: the maximum possible value
    '''
    if pM > random():
            p = randint(0, len(individual)-1)
            individual[p] = random()**(VMAX[p]-VMIN[p])+VMIN[p]
    return individual
    
def crossover(parent1, parent2):
    '''
    crossover between 2 parents
    '''
    child=[]
    alpha=random()
    for x in range(len(parent1)):
        child.append(alpha*(parent1[x]-parent2[x])+parent2[x])
    return child

def iteration(pop, pM, vmin, vmax):
    '''
    an iteration

    pop: the current population
    pM: the probability the mutation to occure
    vmin: the minimum possible value 
    vmax: the maximum possible value
    '''
    i1=randint(0,len(pop)-1)
    i2=randint(0,len(pop)-1)
    if (i1!=i2):
        c=crossover(pop[i1],pop[i2])
        c=mutate(c, pM, vmin, vmax)
        f1=fitness(pop[i1])
        f2=fitness(pop[i2])
        '''
        the repeated evaluation of the parents can be avoided
        if  next to the values stored in the individuals we 
        keep also their fitnesses 
        '''
        fc=fitness(c)
        if(f1>f2) and (f1>fc):
            pop[i1]=c
        if(f2>f1) and (f2>fc):
            pop[i2]=c
    return pop

def main2(noIteratii=10000):
    #PARAMETERS:
    
    #population size
    dimPopulation = 100
    #individual size
    dimIndividual = 2
    #the boundries of the search interval
    vmin = -5.12
    vmax = 5.12
    #the mutation probability
    pM=0.01
    
    P = population(dimPopulation, dimIndividual, vmin, vmax)
    for i in range(noIteratii):
        P = iteration(P, pM, vmin, vmax)

    #print the best individual
    graded = [ (fitness(x), x) for x in P]
    graded =  sorted(graded)
    result=graded[0]
    fitnessOptim=result[0]
    individualOptim=result[1]
    print('Result: The detected minimum point after %d iterations is f(%3.2f %3.2f) = %3.2f'% \
          (noIteratii,individualOptim[0],individualOptim[1], fitnessOptim) )

def main1():
    
    #random.seed(datetime.now())
    prob = Problem()
    pop = Population()
    alg=Algorithm(prob, pop)
    alg.run()
    res = alg.population.v[0]

    fitnessOptim=res.fittness(prob)
    individualOptim=res.x
    print('Result: The detectet minimum point is (%3.2f %3.2f) \n with function\'s value %3.2f'% \
          (individualOptim[0],individualOptim[1], fitnessOptim) )


def main2():
    prob = Problem()
    pop = Population()
    alg=Algorithm(prob, pop)
    alg.statistics()
    plt.show()

def main3():
    prob= Problem()
    pop = Swarm(prob)
    ctrl=Controller()
    res=ctrl.runAlg()
    fitnessOptim=res.fitness
    individualOptim=res.position
    print('Result: The detectet minimum point is (%3.2f %3.2f) \n with function\'s value %3.2f'% \
          (individualOptim[0],individualOptim[1], fitnessOptim) )

def main4():
    # Set-up hyperparameters
    options = {'c1': C1, 'c2': C2, 'w':W}
    # Call instance of PSO
    optimizer = ps.single.GlobalBestPSO(n_particles=POP_SIZE, dimensions=IND_SIZE, options=options)
    # Perform optimization
    fitnessOptim, individualOptim = optimizer.optimize(lambda x: np.apply_along_axis(lambda a: Problem().function(a[0],a[1]) ,1 ,x), iters=NO_ITER)
    
    print('Result: The detectet minimum point is (%3.2f %3.2f) \n with function\'s value %3.2f'% \
              (individualOptim[0],individualOptim[1], fitnessOptim) )

main2()