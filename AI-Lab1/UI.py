from Controller import *
class UI(object):
    """description of class"""
    def __init__(self,controller):
        self.contrl=controller
    def mainMenu(self):
        option=0
        while True:
            print("1.DFS,2.GBFS:")
            option=input()
            if option=="1":
                self.printsol(1)
            elif option=="2":
                self.printsol(2)
            elif option=="0":
                break
            else:
                print("HE?")

        print("Good bye!");
    def printsol(self, opt):
        mystr=""
        self.contrl.type=int(opt)
        self.contrl.DGBFS()
        list=self.contrl.problem.finalState.initialElements
        for a in list:
            for b in a:
                mystr+=str(b)+" "
            mystr+="\n"
        print(mystr)

