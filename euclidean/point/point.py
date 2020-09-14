class Point():
    def __init__(self, x, y, *args):
        self.__pos = (x,y) + tuple(args)
