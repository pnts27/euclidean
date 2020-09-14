import networkx as nx

from euclidean.instance import Instance
from euclidean.point import Point
from euclidean.euclideanMetric import distance as d

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

    def getApproximationRadius(self):
        return self.__approximationRadius

    def approximate(self):
        self.__optimalCandidateRadiuses = self.computeOptimalRadiusCandidates()
        self.__optimalCandidateRadiuses.sort()
        # TODO: Case when there is only one candidate radius
        self.findSmallestApproximationRadius()

    def computeOptimalRadiusCandidates(self):
        return list(set([d(c,f)
         for c in self.__I.clients()
         for f in self.__I.facilities()]))
         
    def findSmallestApproximationRadius(self):
        # Binary search
        radiuses = self.__optimalCandidateRadiuses
        # Binary search
        # left = 0
        # right = len(radiuses)-1

        # while left < right:
        #     current = (left+right) // 2
        #     r = radiuses[current]
        #     self.findSmallestCoverForRadius(r)
        #     if self.__approximationRadius == r:
        #         right = current-1
        #     else:
        #         left = current+1

        # Linear search:
        for r in radiuses:
            self.findSmallestCoverForRadius(r)
            if self.__approximationRadius == r:
                return
        
            
    def findSmallestCoverForRadius(self, r):
        maximalClientSubset = self.pickMaximalClientSubset(r)
        edgeInformation = self.computeEdgeInformation(maximalClientSubset, r)
        if self.verifyACoveringExists(maximalClientSubset, edgeInformation):
            graph = self.computeGraph(edgeInformation)
            clusterMidpoints = self.computeMinimumEdgeCover(graph)
            if len(clusterMidpoints) <= self.__I.getNumberOfClusterCenters():
                clusterMidpoints = self.sortClusterMidpoints(clusterMidpoints)
                self.__approximationMidpoints = [edgeInformation[e] for e in clusterMidpoints]
                self.__approximationRadius = r
                
    def pickMaximalClientSubset(self, r):
        clients = list(self.__I.clients())
        maximalSubset = []
        while len(clients) > 0:
            c = clients[0]
            maximalSubset += [c]
            clients = [cc for cc in clients if d(c, cc) > r]
        return maximalSubset

    def computeEdgeInformation(self, clients, r):
        facilities = list(self.__I.facilities())
        edgeInformation = {}
        for f in facilities:
            cf = [c for c in clients if d(c,f) <= r]
            if len(cf) == 1:
                edgeInformation[(cf[0], cf[0])] = f
            elif len(cf) == 2:
                cf.sort(key=lambda x: id(x))
                edgeInformation[(cf[0], cf[1])] = f
        return edgeInformation

    def verifyACoveringExists(self, clients, edgeInformation):
        keys = list(edgeInformation.keys())
        includedClients = []
        for (a,b) in keys:
            includedClients += [a,b]
        return set(clients) == set(includedClients)

    def computeGraph(self, edgeInformation):
        E = list(edgeInformation.keys())
        G = nx.Graph()
        G.add_edges_from(E)
        return G

    def computeMinimumEdgeCover(self, G):
        return nx.algorithms.covering.min_edge_cover(G)

    def sortClusterMidpoints(self, clusterMidpoints):
        temp = [list(cm) for cm in clusterMidpoints]
        for cm in temp:
            cm.sort(key=lambda x: id(x))
        return [tuple(cm) for cm in temp]
            
