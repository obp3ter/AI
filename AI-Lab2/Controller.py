from Swarm import *
from Problem import *
from imports import *


class Controller(object):
    """description of class"""
    def __init__(self,pop=Swarm(problem=Problem()),_prob=Problem()):
        self.population=pop
        self.problem=_prob
    def iteration(self,w=W):
        for p in self.population.v:
            bestN=self.population.getBestNeighbour(p)
            newVel=[w*v for v in p.velocity]
            newVel=[newVel[i]+C1/C3*random.random()*(bestN.position[i]-p.position[i]) for i in range(IND_SIZE)]
            newVel=[newVel[i]+C2/C3*random.random()*(p.bestPosition[i]-p.position[i]) for i in range(IND_SIZE)]
            p.velocity=newVel

            newPos=[p.position[i]+p.velocity[i] for i in range(IND_SIZE)]
            
            if newPos[0]<VMIN[0]:
                newPos[0]=VMIN[0]
            if newPos[1]<VMIN[1]:
                newPos[1]=VMIN[1]
            if newPos[0]>VMAX[0]:
                newPos[0]=VMAX[0]
            if newPos[1]>VMAX[1]:
                newPos[1]=VMAX[1]



            p.position=newPos
            p.evaluate(self.problem)


    def runAlg(self, w=W):
        self.plotCS()

        for i in range(NO_ITER):
            w/=(i+1)
            self.iteration()
        self.plotCS()
        return self.population.v[0]
    def plotCS(self):
        x=[]
        y=[]

        for p in self.population.v:
            x.append(p.position[0])
            y.append(p.position[1])

        x=np.array(x)
        y=np.array(y)

        plt.scatter(x,y, alpha=0.5)
        plt.show(block=False)
        plt.pause(1)
        plt.close()

