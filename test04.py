# coding:utf-8
# Encontrar la distancia euclidiana mínima para una serie de puntos
# en el plano cartesiano sqrt((x1-x2)**2+(y1-y2)**2) punto (x1,y1) (x2,y2)
# 
# entrada: p = [[x,y],[a,b],...,[w,u]]
#
# limites:
# len(p) <= 2e4
# p[i] dos elementos
# abs(p[i][j]) < 1e7
# presicion < 1e-6
# tiempo de ejecución como límite 5 sec
# 
from math import dist
from time import time
    
def resolve(p):
    assert len(p) < 2e4
    res = [x for l in p for x in l] 
    assert len(res) == 2*len(p)
    assert sum([r>1e7 for r in res])+sum([r<-1e7 for r in res]) == 0
    return min((min([ dist(p[j],p[k]) for j in range(k+1,len(p))]) for k in range(len(p)-1)))
    
#########################################################
###############           test Zone             #########

from random import randint
p = [[randint(-1e7,1e7), randint(-1e7,1e7)] for i in range(5000)]
start = time()
test1 = resolve(p)
dt = time()-start
if dt > 30:
    print(f'No cumple el tiempo: {dt}')
else:
    print(f't1 {dt}')


p[-1]=[1,* p[-1]]
start = time()
try:
    test1 = resolve(p)
except:
    print('catch succeeded')
dt = time()-start
if dt > 30:
    print(f'No cumple el tiempo: {dt}')
else:
    print(f't2 {dt}')

p = [[randint(-1e7,1e7), randint(-1e7,1e7)] for i in range(19_999)]
p[-1][1] = 1e8
start = time()
try:
    test1 = resolve(p)
except:
    print('catched')
dt = time()-start
if dt > 30:
    print(f'No cumple el tiempo: {dt}')
else:
    print(f't3 {dt}')