from imports import *
from Particle import *
from Problem import *
class Swarm(object):
    """description of class"""
    def __init__(self, problem, _noParticles=POP_SIZE):
        self.noParticles=_noParticles
        self.v=[]
        for i in range(self.noParticles):
            x=Particle()
            x.evaluate(problem)
            self.v.append(x)
    def getBestNeighbour(self, particle):
        neighbours =[]

        for i in range(NBH_SIZE):
            x=self.v[random.randint(0,len(self.v)-1)]
            while (x in neighbours):
               x=self.v[random.randint(0,len(self.v)-1)]
            neighbours.append(x)

        bestN=Particle()

        for p in neighbours:
            if bestN.fitness>p.fitness:
                bestN.update(p)


        return bestN
    def geBestParticles(self, problem):
        self.v.sort(key= lambda x: x.fitness(problem))

        return self.v.copy()


