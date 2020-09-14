from euclidean import Point, Instance, Approximation

def client_locs():
    cs = []
    for i in range(10):
        for j in range(10):
            for k in range(10):
                cs += [Point(i,j,k)] 
    return cs
           
def facility_locs():
    fs = []
    for i in range(2, 9):
        for j in range(2, 9):
            for k in range(3,8):
                fs += [Point(i+1/3, j+1/5, k-(i+j)/(i+j+k))]
    return fs

if __name__ == "__main__":
    c = client_locs()
    f = facility_locs()
    k = 4

    I = Instance(c,f,k)
    A = Approximation(I)

    print("Approximation radius: ", A.getApproximationRadius())
    print("Approximation midpoints: ")
    print(str(A.getApproximationMidpoints()))
