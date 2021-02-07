# -*- coding: utf-8 -*-
"""
MAS Program

Created on Wed Feb 26 18:55:07 2020

@author: cotengineer
"""

import matplotlib.pyplot as plt
from random import randint
import numpy as np

#initialize search space record keeping
N = 30
log = np.zeros((N,N))

def rec(x):
    xx = x[0]
    yy = x[1]
    log[xx][yy] += 1
    return

#evaluate move    
def evalmove(x):

    if x[0] < N-1 and x[0] > 0 and x[1] > 0 and x[1] < N-1:
        n = log[x[0]][x[1]+1]
        e = log[x[0]+1][x[1]]
        s = log[x[0]][x[1]-1]
        w = log[x[0]-1][x[0]]
        
        d = {"north": n, "south": s, "east": e, "west": w}
        
        d = sorted(d.items(), key=lambda x:x[1])
        #print(d)
        return(str(d[0][0]))

for i in range(0,N):
    log[i][N-1] = 1000
    log[N-1][i] = 1000
    log[0][i] = 1000
    log[i][0] = 1000
    
def move(x,d):
    if d == 'north':
        x = [x[0],x[1]+1]
        rec(x)
    elif d == 'south':
        x = [x[0],x[1]-1]
        rec(x)
    elif d == 'east':
        x = [x[0]+1,x[1]]
        rec(x)
    elif d == 'west':
        x = [x[0]-1,x[1]]
        rec(x)
    return x
               
#place a target    
tx = randint(15,N-3)
ty = randint(15,N-3)
targ = [tx,ty]
#rec(targ)

#creare environment
envx = []
envy = []
rex = randint(10,20)
rey = randint(10,20)
for j in range(0,10):
    ex1 = rex+j
    envx.append(ex1)
    ey1 = rey
    envy.append(ey1)
    log[rex+j,rey] = 1000
    ex2 = rex
    envx.append(ex2)
    ey2 = rey+j
    envy.append(ey2)
    log[rex,rey+j] = 1000
    

#initialize agents
def ran(x):
    x = randint(1,6)
    return x

agents = []

while len(agents) < 4:
    hor = ran(0)
    ver = ran(0)
    if log[hor][ver] == 0.0:
        a = [hor,ver]
        agents.append(a)
        rec(a)  
    else:
        continue

a1 = agents[0]; a2 = agents[1]; a3 = agents[2]; a4 = agents[3]

#start search
search = 0

found = False

#Visualization and Search Function
while found == False:
    
    plt.scatter(targ[0],targ[1], s=400, marker = "*", c='red')
    plt.scatter(envx,envy, s=150, marker = "s", c='black')
    plt.scatter(a1[0],a1[1], s=250, marker = "o", c='blue')
    plt.scatter(a2[0],a2[1], s=250, marker = "^", c='orange')
    plt.scatter(a3[0],a3[1], s=250, marker = "d", c='yellow')
    plt.scatter(a4[0],a4[1], s=250, marker = "p", c='green')      
    plt.grid(color='red', linestyle='-.', linewidth=0.7)
    plt.xlim(-1, N)
    plt.ylim(-1, N)
    plt.xlabel('X',fontsize=18,color='k')
    plt.ylabel('Y',fontsize=18,color='k')
    plt.title('MAS Search',fontsize=18,color='r')
    plt.savefig("Agent"+str(search))    
    plt.show()    

    mo1 = evalmove(a1)
    a1 = move(a1,mo1)
    mo2 = evalmove(a2)
    a2 = move(a2,mo2)
    mo3 = evalmove(a3)
    a3 = move(a3,mo3)
    mo4 = evalmove(a4)
    a4 = move(a4,mo4)
    
    search += 1
    
    #stop condition
    if a1 == targ or a2 == targ or a3 == targ or a4 == targ:
        found = True
