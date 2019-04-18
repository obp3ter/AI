from imports import *

class Particle(object):
    """description of class"""
    def __init__(self, _position=[-5.0]*IND_SIZE,_velocity=[0.0]*IND_SIZE,_fitness=float("Inf"),bestPos=[0.0]*IND_SIZE,bestFtns=float("Inf")):
        if _position[0]==-5.0:
            _position= [ (random.random()*(VMAX[x]-VMIN[x])+VMIN[x]) for x in range(IND_SIZE) ]
        
        self.position=_position
        self.velocity=_velocity
        self.fitness=_fitness
        self.bestPosition=bestPos
        self.bestFitness=bestFtns

    def evaluate(self, problem):
        self.fitness=self.fittness(problem)
        if self.bestFitness > self.fitness:
            self.bestFitness = self.fitness
            self.bestPosition= self.position

    def update(self, particle):
        self.position=particle.position
        self.velocity=particle.velocity
        self.fitness=particle.fitness
        self.bestPosition=particle.bestPosition
        self.bestFitness=particle.bestFitness
    def fittness(self,problem):
        if self.fitness != float("Inf"):
            return self.fitness
        return problem.function(*self.position)

