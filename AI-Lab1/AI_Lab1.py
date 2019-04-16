from UI import *


def DGBFS( expand, solution,goodness,root, type=0):
    if type!=2:
        l=list()
        l.append(root)
        func=lambda x:len(x)==0
    else:
        l=PriorityQueue()
        l.put((0,root))
        func=lambda x:x.empty()

    found=False
    sol=[]
    while not func(l) and not found:
        if type!=2:
            c=l.pop()
        else:
            c=l.get()[1]
        if solution(c):
            found=True
            sol=c
        else:
            aux=expand(c)
            if type==0:
                for i in aux:
                    l.insert(0,i)
            elif type==1:
                for i in aux:
                    l.append(i)
            elif type == 2:
                for i in aux:
                    l.put((goodness(aux),i))
            else:
                print(error)
    return found,sol
def exp_sudoku(root,n):
    l=[]
    croot=deepcopy(root)
    for i in range(len(root)):
        if root[i]==0:
            for j in range(1,n+1):
                croot[i]=j
                l.append(deepcopy(croot))
            return l
    return l
def sol_sudoku(ol,el):
    if el == [4,1,2,3,3,4]:
        print("hello")

    for i in el:
        if i ==0:
            return False
    olc=deepcopy(ol)
    elc=deepcopy(el)
    n=len(ol)

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
def gdns_sudoku(li):
    a = deepcopy(li)
    a=sorted(a)
    while a[0]==0:
        a.pop(0)
    return [len(list(group)) for key, group in groupby(a)]
    def sudoku1():
    flatten = lambda l: [item for sublist in l for item in sublist]
    li=[[3,0,0,2],[0,1,4,0],[1,2,0,4],[0,3,2,1]]
    s=0;
    for i in flatten(li):
        if i == 0:
            s+=1
    a,elc=DGBFS(lambda x: exp_sudoku(x,len(li)),lambda x: sol_sudoku(li,x),gdns_sudoku,root=[0]*s,type=2)
    n=len(li)
    olc=deepcopy(li)
    for i in range(n):
        for j in range(n):
            if olc[i][j]==0:
                olc[i][j]=elc.pop(0)
                if len(elc)==0:
                    break
        if len(elc)==0:
                    break
    return olc
'''
def main():
    print("Hello")
    print(sudoku1())
'''
def main():
    prb=Problem()
    ctrl=Controller(prb)
    ui=UI(ctrl)
    ui.mainMenu()

main()