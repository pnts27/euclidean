from euclidean import Point, Instance, Approximation

def client_locs():
    cs = []
    for i in range(100):
        for j in range(100):
           cs += [Point(i,j)] 
    return cs
           
def facility_locs():
    fs = [Point(0,0), Point(99,99), Point(0,99), Point(99,0), Point(49.5,49.5)]
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
    print(A.getApproximationGraph().edges())
