from instance import Instance
from point import Point
from euclideanDistance import distance as d

class Approximation():
    def __init__(self, I: Instance):
        self.__I = I
        self.approximate()

    def getApproximationMidpoints():
        return self.__approximationMidpoints

    def approximationMidpoints():
        for f in self.__approximationMidpoints:
            yield f

    def getApproximationRadis():
        return self.__approximationRadius

    def approximate(self):
        pass
