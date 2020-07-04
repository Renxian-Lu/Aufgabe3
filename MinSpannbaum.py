from heapq import *
from _collections import defaultdict

# kante = []

def FindSet(x, p):

    if (x != p[x]):
        p[x] = FindSet(p[p[x]], p)
    else:
        return p[x]

def Kruskal(kante, n):
    p = list(range(n))
    cost = 0
    for u,v,w in sorted(kante, key=lambda x: x[2]):
        ru, rv = FindSet(u, p), FindSet(v, p)
        if (ru == rv):
            continue
        p[ru] = rv
        cost += w
    print(cost)