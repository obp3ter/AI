from State import *
class Problem(object):
    """description of class"""
    def __init__(self):
        _initialState=State(self.readFromFile())
        self.initialState=_initialState
        self.finalState=State([[]])
        self.currentState=_initialState
        


    def expand(self,state):
        l=[]
        croot=deepcopy(state.elements)
        for i in range(len(state.elements)):
            if state.elements[i]==0:
                for j in range(1,state.size+1):
                    croot[i]=j
                    temp=State(state.initialElements)
                    temp.setList(deepcopy(croot))
                    l.append(temp)
                return l
        return l
    def heuristic(self,li):
        a = [e.elements for e in li]
        a=sorted(a)
        while a[0]==0:
            a.pop(0)
        return [len(list(group)) for key, group in groupby(a)]
    def solution(self):
        for i in self.currentState.elements:
            if i ==0:
                return False
        olc=deepcopy(self.initialState.initialElements)
        elc=deepcopy(self.currentState.elements)
        n=self.currentState.size

        for i in range(n):
            for j in range(n):
                if olc[i][j]==0:
                    olc[i][j]=elc.pop(0)
                    if len(elc)==0:
                        break
            if len(elc)==0:
                        break

        #check h,v

        for i in range(n):
            elementsinh=[]
            elementsinv=[]
            for j in range(n):
                if olc[i][j] not in elementsinh:
                    elementsinh.append(olc[i][j])
                else:
                    return False
                if olc[j][i] not in elementsinv:
                    elementsinv.append(olc[j][i])
                else:
                    return False
        for i in range(int(sqrt(n))):
            for j in range(int(sqrt(n))):
                elementsinc=[]
                for k in range(int(sqrt(n))):
                    for u in range(int(sqrt(n))):
                        if olc[i*int(sqrt(n))+k][j*int(sqrt(n))+u] not in elementsinc:
                            elementsinc.append(olc[i*int(sqrt(n))+k][j*int(sqrt(n))+u])
                        else:
                            return False

            

        return True
    def finish(self,state):
        olc=deepcopy(self.initialState.initialElements)
        elc=deepcopy(state.elements)
        for i in range(self.initialState.size):
            for j in range(self.initialState.size):
                if olc[i][j]==0:
                    olc[i][j]=elc.pop(0)
                    if len(elc)==0:
                        break
            if len(elc)==0:
                        break
        self.finalState=State(olc)
    def readFromFile(self):
        f = open("problem.txt", "r")
        s=f.readline()
        l=[]
        while s!='':
            
            l.append([int(i) for i in s.split(" ")])
            s=f.readline()

        return l

        


