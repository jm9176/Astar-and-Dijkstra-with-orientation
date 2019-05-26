# Node class for the position in the grid
class Node(object):

    def __init__(self, x, y, o):
        self._x = x
        self._y = y
        self._o = o
        
    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def o(self):
        return self._o

    @property
    def tuple(self):
        return tuple((self._x, self._y, self._o))
            
    def __eq__(self, other):
        return self._x == other.x and self._y == other.y and self._o == other.o

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return 'Node({}, {}, {})'.format (self._x, self._y, self._o)

    def __repr__(self):
        return str(self)

    def __hash__(self):
        return hash((self._x, self._y, self._o))
