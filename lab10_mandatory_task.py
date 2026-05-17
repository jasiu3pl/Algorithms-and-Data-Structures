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
    
def prim(graph):
    distance = {}
    intree = {}
    parent = {}
    for v in graph.vertices():
        distance[v] = float('inf')
        intree[v] = False
        parent[v] = None
    
    start_vertex = graph.vertices()[0]
    distance[start_vertex] = 0
    mst = AdjecencyList()
    
    while False in intree.values():
        smallest_dist = float('inf')
        current_vertex = None
        for v in graph.vertices():
            if intree[v] == False:
                if distance[v] < smallest_dist:
                    smallest_dist = distance[v]
                    current_vertex = v
        
        intree[current_vertex] = True
        mst.insert_vertex(current_vertex)
        if parent[current_vertex] != None:
            mst.insert_edge(parent[current_vertex], current_vertex, distance[current_vertex])
            
        for neighbour, weight in graph.neighbours(current_vertex):
            if intree[neighbour] == False:
                if distance[neighbour] > weight:
                    distance[neighbour] = weight
                    parent[neighbour] = current_vertex
    
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
    graph_test = AdjecencyList()
    for vertex1, vertex2, weight in graf:
        graph_test.insert_vertex(vertex1)
        graph_test.insert_vertex(vertex2)
        graph_test.insert_edge(vertex1, vertex2, weight)
        
    graph_test_mst = prim(graph_test)
    printGraph(graph_test_mst)
    
    
if __name__ == "__main__":
    main()