from collections.abc import Iterable

class Instance():
    def __init__(self,
                 clients: Iterable, # Points
                 facilities: Iterable, # Points
                 k: int):
        self.__c = set(clients)
        self.__f = set(facilities)
        self.__k = k

    def clients(self):
        for c in self.__c:
            yield c

    def facilities(self):
        for f in self.__f:
            yield f

    def getNumberOfClusterCenters(self):
        return self.__k
