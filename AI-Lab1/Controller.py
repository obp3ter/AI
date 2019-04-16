from Problem import *
class Controller(object):
    """description of class"""

    def __init__(self, _problem,_type=0):
        self.problem=_problem
        self.type=_type
    def orderStates(states):
        print("???")

    def DGBFS(self):
        if self.type!=2:
            l=list()
            l.append(self.problem.initialState)
            func=lambda x:len(x)==0
        else:
            l=PriorityQueue()
            l.put((0,self.problem.initialState))
            func=lambda x:x.empty()

        found=False
        sol=[]
        while not func(l) and not found:
            if self.type!=2:
                self.problem.currentState=l.pop()
            else:
                self.problem.currentState=l.get()[1]
            if self.problem.solution():
                found=True
                self.problem.finish(self.problem.currentState)
            else:
                aux=self.problem.expand(self.problem.currentState)
                if self.type==0:
                    for i in aux:
                        l.insert(0,i)
                elif self.type==1:
                    for i in aux:
                        l.append(i)
                elif self.type == 2:
                    for i in aux:
                        l.put((self.problem.heuristic(aux),i))
                else:
                    print(error)
        
