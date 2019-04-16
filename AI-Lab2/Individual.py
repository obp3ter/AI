from imports import *

class Individual(object):
    """description of class"""

    def __init__(self,_x = [0.0]*IND_SIZE,func = lambda x:(x[0])):
        self.size = IND_SIZE
        self.x=_x
        self.fitness=float("Inf")

    def fittness(self,problem):
        if self.fitness != float("Inf"):
            return self.fitness
        return problem.function(*self.x)
    def mutate(self, probability= MUTATE_PROB ):
        if probability > random.random():
            p = random.randint(0, self.size-1)
            self.x[p] = random.random()*(VMAX[p]-VMIN[p])+VMIN[p]
    def crossover(self, parent2,probability= PARENT_PROB):
        childl=[]
        for x in range(self.size):
            childl.append(probability*(self.x[x]-parent2.x[x])+parent2.x[x])
        return Individual(childl)
    

