from imports import *
from Individual import *

class Population(object):
    """description of class"""
    def __init__(self, func = lambda x:(x[0]),no=POP_SIZE):
        self.noIndividuals=no
        self.v=[]
        for i in range(self.noIndividuals):
            self.v.append(Individual())
    def evaluate(self):
        i=0
        it=0
        while i < self.noIndividuals and it < SIM_CH :
            c=self.v[i].crossover(self.v[i+1])
            c.mutate()
            self.v.append(c)
            i+=2
            it+=1


    def selection(self,problem):
        self.v.sort(key=lambda x: x.fittness(problem))
        for i in range((len(self.v)-POP_SIZE)):
            self.v.pop()
