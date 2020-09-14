from euclidean import Point, Instance, Approximation

def client_locs():
    cs = []
    for i in range(10):
        for j in range(10):
           cs += [Point(i,j)] 
    return cs
           
def facility_locs():
    fs = [Point(0,0)]
    return fs

if __name__ == "__main__":
    c = client_locs()
    f = facility_locs()
    k = 1

    I = Instance(c,f,k)
    A = Approximation(I)

    print("Approximation radius: ", A.getApproximationRadius())
    print("Approximation midpoints: ")
    print(str(A.getApproximationMidpoints()))
