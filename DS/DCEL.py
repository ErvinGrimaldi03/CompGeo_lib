from Point import Point

class Vertex:
    def __init__(self, pt:Point):
        self.x =pt.x
        self.y = pt.y
        self.edge = None


class HalfEdge:
    def __init__(self):
        self.vertex = None
        self.twin = None
        self.face = None
        self.next = None
        self.prev = None


class Face:
    def __init__(self):
        self.edge = None


class Dcel:
    def __init__(self):
        self.vertices = []
        self.faces = []
        self.halfEdges = []

    def read_dcel(self, verteces, edges, faces):
        pass
