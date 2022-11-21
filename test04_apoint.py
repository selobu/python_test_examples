# Import time module
import time
from math import sqrt 
from random import randint

def dist(a, b):
    return sqrt((a[0]-b[0])**2 +(a[1]-b[1])**2)
        
def solution(p):
    print('//-- checking length reducing size--//')
    Start = time.time()
    assert len(p) >= 2
    assert len(p) <= 2e4
    # deleting repeated points
    p= tuple(set(p))
    # unpack values
    unpacked = [x for l in p for x in l]
    # check pair
    assert len(unpacked) == 2*len(p)
    print(f'Required: {time.time()-Start}, newlen {len(p)}')
    
    print('//-- checking <1e7 --//')
    Start = time.time()
    unpacked = set(unpacked)
    unpacked = set(abs(i)  for i in unpacked)
    assert all([i <= 1e7 for i in unpacked])
    print(f'Required: {time.time()-Start}')
    
    print('//-- computing values--//')
    Start = time.time()
    curr_diff = []
    max_iter = len(p)
    curr_diff = ((min((dist(p[k1],p[k2]) for k2 in range(k1+1, max_iter)))) \
        for k1 in range(max_iter-1))
    curr_diff = min(curr_diff)
    print(f'Required: {time.time()-Start}') 
    return curr_diff

print('// Random generation//')
randomnumbers = [(randint(-10_000,10_000), randint(-10_000,10_000)) for i in range(2_000)]
print('//--- Computing ---//')
print(f'{solution(randomnumbers)} ms')