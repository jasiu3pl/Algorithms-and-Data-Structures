from graf_mst import graf

class AdjecencyList:
    def __init__(self):
        self.graph_dict = {}
        
    def is_empty(self):
        return len(self.graph_dict) == 0
    
    def insert_vertex(self, vertex):
        if vertex in self.graph_dict:
            return
        self.graph_dict[vertex] = {} 
        
    def insert_edge(self, vertex1, vertex2, edge=None):
        self.graph_dict[vertex1][vertex2] = edge
        self.graph_dict[vertex2][vertex1] = edge
        
    def delete_edge(self, vertex1, vertex2):
        if vertex1 in self.graph_dict:
            if vertex2 in self.graph_dict[vertex1]:
                del self.graph_dict[vertex1][vertex2]
        return
    
    def delete_vertex(self, vertex):
        if vertex in self.graph_dict:
            for v in self.graph_dict:
                if vertex in self.graph_dict[v]:
                    del self.graph_dict[v][vertex]
            
            del self.graph_dict[vertex]
            
    def vertices(self):
        return list(self.graph_dict.keys())
    
    def neighbours(self, vertex_id):
        return list(self.graph_dict[vertex_id].items())
    
    def get_vertex(self, vertex_id):
        return vertex_id
    
    def get_edge(self, vertex1, vertex2):
        if vertex1 in self.graph_dict:
            if vertex2 in self.graph_dict[vertex1]:
                return self.graph_dict[vertex1][vertex2]
        
        return None
    
class UnionFind:
    def __init__(self, elements):
        self.elements = elements
        self.parent = {}
        self.size = {}
        
        for vertex in elements:
            self.parent[vertex] = vertex
            self.size[vertex] = 1
            
    def find(self, v):
        if self.parent[v] == v:
            return v
        self.parent[v] = self.find(self.parent[v])
        return self.parent[v]
    
    def union_sets(self, s1, s2):
        root1 = self.find(s1)
        root2 = self.find(s2)
        if root1 == root2:
            return
        
        size_root1 = self.size[root1]
        size_root2 = self.size[root2]
        if size_root1 < size_root2:
            self.parent[root1] = root2
            self.size[root2] += self.size[root1]
        else:
            self.parent[root2] = root1
            self.size[root1] += self.size[root2]
            
    def same_component(self, s1, s2):
        return self.find(s1) == self.find(s2)
    
def kruskal(edges, vertices):
    mst = AdjecencyList()
    for v in vertices:
        mst.insert_vertex(v)
    
    uf = UnionFind(vertices)
    sorted_edges = sorted(edges, key=lambda x: x[2])
    for v1, v2, weight in sorted_edges:
        if uf.same_component(v1, v2) == False:
            uf.union_sets(v1, v2)
            mst.insert_edge(v1, v2, weight)
            
    return mst

def printGraph(g):
    print("------GRAPH------")
    for v in g.vertices():
        print(v, end = " -> ")
        for (n, w) in g.neighbours(v):
            print(n, w, end=";")
        print()
    print("-------------------")
            
def main():
    cities = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    kruskal_graph = kruskal(graf, cities)
    printGraph(kruskal_graph)

if __name__ == "__main__":
    main()