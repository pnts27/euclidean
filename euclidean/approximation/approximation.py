from instance import Instance
from point import Point
from euclideanDistance import distance, setDistance as d, ds

class Approximation():
    def __init__(self, I: Instance):
        self.__I = I
        
        self.__approximationMidpoints = None
        self.__approximationRadius = -1
        
        self.approximate()

    def getApproximationMidpoints(self):
        return self.__approximationMidpoints

    def approximationMidpoints(self):
        for f in self.__approximationMidpoints:
            yield f

    def getApproximationRadis(self):
        return self.__approximationRadius

    def approximate(self):
        self.__optimalCandidateRadiuses = self.computeOptimalRadiusCandidates()
        self.__optimalCandidateRadiuses.sort()
        # TODO: Case when there is only one candidate radius
        self.findSmallestApproximationRadius()

    def computeOptimalRadiusCandidates(self):
        return list(set([d(c,f)
         for c in self.__I.clients()
         for f in self.__I-facilities()]))
         
    def findSmallestAppoximationRadius(self):
        # Binary search
        radiuses = self.__optimalCandidateRadiuses
        left = 0
        right = len(radiuses)-1

        while(left != right):
            current = (left+right) // 2
            r = radiuses[current]
            self.findSmallestCoverForRadius(r)
            
            if(self.__approximationRadius == r):
                right = current-1
            else:
                left = current+1

    def findSmallestCoverForRadius(self, r):
        maximalClientSubset = self.pickMaximalClientSubset(r)
        edgeInformation = self.computeEdgeInformation(maximalClientSubset, r)
        graph = self.computeGraph(maximalClientSubset, edgeInformation)
        clusterMidpoints = self.computeMinimumEdgeCover(graph)
        if len(clustermidpoins) <= self.__I.getNumberOfClusterCenters():
            self.__approximationMidpoints = [edgeInformation(e) for e in clusterMidpoints]
            self.__approximationRadius = r

    def pickMaximalClientSubset(self, r):
        clients = list(self.__I.clients())
        maximalSubset = []
        while len(clients) > 0:
            c = clients[0]
            maximalSubset += [c]
            clients = [cc for cc in clients if d(c, cc) <= r]
        return maximalSubset

    def edgeInformation(self, clients, r):
        facilities = list(self.__I.facilities())
        edgeInformation = {}
        for f in facilities:
            cf = [c in clients if d(c,f) <= r]
            if len(cf) == 1:
                edgeInformation[(cf[0], cf[0])] = f
            elif len(cf) == 2:
                edgeInformation[(cf[0], cf[1])] = f
        return edgeInformation

    def computeGraph(self, clients, edgeInformation):
        V = clients
        E = list(edgeInformation.keys())
        return (V, E)

    def computeMinimumEdgeCover(graph):
        #Todo: Find good algorithm
        pass
        
