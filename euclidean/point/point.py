class Point():
    def __init__(self, x, y, *args):
        self.__pos = (x,y) + tuple(args)

    def getCoordinates(self):
        return self.__pos

    def coordiantes(self):
        for coord in self.__pos:
            yield coord

    def __repr__(self):
        return str(self.__pos)
