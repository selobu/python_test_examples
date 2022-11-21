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
from math import sqrt
from time import time
def resolve(p):
    assert len(p) < 2e4
    r1=[]
    for k in range(len(p)-1):
        for j in range(k+1,len(p)):
            p1=p[k]
            p2=p[j]
            assert len(p1)==2 and len(p2) == 2
            assert abs(p1[0])<=1e7 and abs(p1[1]) <= 1e7
            assert abs(p2[0])<=1e7 and abs(p2[1]) <= 1e7
            r1.append(sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2))
    return min(r1)

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