from imports import *
class State(object):
    """description of class"""
    def __init__(self, _initialElements):
        self.initialElements=_initialElements
        flatten = lambda l: [item for sublist in l for item in sublist]
        self.size=len(_initialElements)
        s=0;
        for i in flatten( _initialElements):
            if i == 0:
                s+=1


        self.elements=[0]*s

    def setList(self, list):
        self.elements=list
    def __lt__(self, other):
        return self.elements<other.elements