from euclidean import Point, Instance, Approximation

def client_locs():
    cs = []
    for i in range(10):
        for j in range(10):
           cs += [Point(i,j)] 
    return cs
           
def facility_locs():
    fs = []
    for i in range(2, 9):
        for j in range(2, 9):
            fs += [Point(i+1/3, j+1/5)]
    return fs

if __name__ == "__main__":
    c = client_locs()
    f = facility_locs()
    k = 7

    I = Instance(c,f,k)
    A = Approximation(I)

    print(A.approximationRadius())
    print(A.getApproximationMidpoints())
