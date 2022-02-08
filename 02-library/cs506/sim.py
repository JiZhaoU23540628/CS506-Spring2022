import numpy as np
def euclidean_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += (x[i] - y[i])**2
    return res**(1/2)

def manhattan_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += abs(x[i]-y[i])
    return res

def jaccard_dist(x, y):
    x =np.asarray(x)
    y =np.asarray(y)
    up = np.double(np.bitwise)_and((x!=y), np.bitwise_or(x != 0, y !=0)).sum())
    down = np.double(np.bitwise_or(x != 0, y != 0).sum())
    dis = (up/down)
    return dis
   

def cosine_sim(x, y):
    dis = 1- np.dot(x,y)/np.linalg.norm(x)*np.linalg.norm(y))
    return dis

# Feel free to add more
