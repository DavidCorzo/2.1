class Vertex:
    def __init__(self,name: str):
        self.name = name 
        self.neighbors = list()

    def add_neighbor(self,v):
        if v not in self.neighbors:
            self.neighbors.append(v)
            self.neighbors.sort()
    
class Graph:
    def __init__(self):
        self.vertices = {}
    
    def add_vertex(self,vertex):
        if vertex.name in self.vertices:
            return False
        else:
            self.vertices[vertex.name] = vertex 
            return True 
    
    def add_edge(self,u,v): # Comprobar que existen ambos y conectarlos
        if u in self.vertices and v in self.vertices:
            self.vertices[u].add_neighbor(v) 
            self.vertices[v].add_neighbor(u)
            return True 
        else:
            return False 

    def print_graph(self):
        for vertex in sorted(self.vertices.keys()):
            print(vertex, '=>', self.vertices[vertex].neighbors)

def main():
    G = Graph()
    a = Vertex('A')
    G.add_vertex(a)
    G.add_vertex(Vertex('B'))
    
    for i in range(ord('C'),ord('F')):
        G.add_vertex(Vertex(chr(i)))
    
    edges = ['AB','BC','BD','CD','DE']
    for edge in edges:
        G.add_edge(edge[0],edge[1])
    
    G.print_graph()

if __name__ == "__main__":
    main()
