from scipy.spatial import distance as d

def distance(x,y):
    return d.euclidean(x.getCoordinates(),y.getCoordinates())
