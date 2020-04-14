class Vertex:
    def __init__(self,name: str):
        self.name = name 


class Graph:
    def __init__(self):
        self.vertices = {}
        self.edges = []
        self.edge_indices = {} 

    def add_vertex(self,vertex):
        '''Tengo que añadis una nueva columna y una nueva fila al incrementar el número de vértices'''
        if vertex.name in self.vertices:
            return False
        else:
            self.vertices[vertex.name] = vertex 
            for row in self.edges:
                row.append(0)
            self.edges.append([0] * (len(self.edges)+1))
            self.edge_indices[vertex.name] = len(self.edge_indices)
            return True
    
    def add_edge(self,u,v,weight=1):
        '''Podemos implementar con peso o sin peso de una sola vez'''
        if u in self.vertices and v in self.vertices:
            self.edges[self.edge_indices[u]][self.edge_indices[v]] = weight
            self.edges[self.edge_indices[v]][self.edge_indices[u]] = weight
            return True 
        else:
            return False
    
    def print_graph(self):
        for v,i in sorted(self.edge_indices.items()):
            print(v + ' ', end='')
            for j in range(len(self.edges)):
                print(self.edges[i][j], end='')
            print(' ')

def main():
    G = Graph()
    for i in range(ord('A'),ord('F')):
        G.add_vertex(Vertex(chr(i)))
    
    edges = ['AB','BC','BD','CD','DE']
    for edge in edges:
        G.add_edge(edge[0],edge[1])
    
    # print(G.edge_indices)
    G.print_graph()
    

if __name__ == "__main__":
    main()
