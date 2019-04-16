from Population import *
from imports import *

class Algorithm(object):
    """description of class"""
    def __init__(self, _problem, _population):
        self.problem = _problem
        self.population = _population
        self.population.func=self.problem.function
    def readParameters(file_name):
        0==0
    def iteration(self):
        self.population.evaluate()
        self.population.selection(self.problem)
    def run(self):
        for i in range(NO_ITER):
            self.iteration()
    def statistics(self):
        bestfitnesses=[]
        for i in range(TEST_RUNS):
            self.population=Population(no=TEST_POP)
            for j in range(TEST_ITER):
                self.iteration()
            bestfitnesses.append(self.population.v[0].fittness(self.problem))
        bf=np.array(bestfitnesses)
        mu = bf.mean()
        sigma = bf.std()

        textstr = '\n'.join((
    r'$\mu=%.2f$' % (mu, ),
    r'$\sigma=%.2f$' % (sigma, )))

        f, axarr = plt.subplots(1,2,figsize=(10,5))


        axarr[0].set_title("Results of "+str(TEST_RUNS)+" runs with a population of "+str(TEST_POP))
        axarr[0].plot(np.array(range(len(bestfitnesses))),bf,c='r', label="Fitness")
        axarr[0].set_xlabel("Run")
        axarr[0].set_ylabel("Fitness")
        axarr[0].legend(loc='upper right')
        props = dict(boxstyle='round', facecolor='w', alpha=0.5)
        axarr[0].text(0.05, 0.95, textstr, transform=axarr[0].transAxes, fontsize=14,verticalalignment='top', bbox=props)

        self.population=Population()

        fitnesses=[]
        for i in range(NO_ITER):
            self.iteration()
            fitnesses.append(self.population.v[0].fittness(self.problem))
        
        axarr[1].set_title("Variation of fitness in one run")
        axarr[1].plot(np.array(range(len(fitnesses))),np.array(fitnesses),c='r', label="Fitness")
        axarr[1].set_xlabel("Iteration")
        axarr[1].set_ylabel("Fitness")
        axarr[1].legend(loc='upper right')
        #fig.show()




    def plot(self):
        

        fig=plt.figure()
        ax=fig.add_subplot(111)
        ax.plot(np.array(range(len(fitnesses))),np.array(fitnesses),c='r', label="Fitness")
        ax.set_xlabel("Iteration")
        ax.set_ylabel("Fitness")
        ax.legend(loc='upper right')
        fig.show()
