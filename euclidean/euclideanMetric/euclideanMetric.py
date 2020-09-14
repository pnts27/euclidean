from scipy.spatial import distance as d

def distance(x,y):
    return d.euclidean(x,y)

def setDistance(x, Y):
    return min([distance(x,y) for y in Y])
