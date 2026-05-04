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

class Edge:
    def __init__(self, capacity, is_residual):
        self.is_residual = is_residual
        if is_residual:
            self.capacity = 0
            self.residual_capacity = 0
            self.flow = 0 
        else:
            self.capacity = capacity
            self.residual_capacity = capacity
            self.flow = 0
            
    def __repr__(self):
        return f"{self.capacity} {self.flow} {self.residual_capacity} {self.is_residual}"
    
def build_graph(edges_list):
    graph = AdjecencyList()
    
    for start, end, cap in edges_list:
        graph.insert_vertex(start)
        graph.insert_vertex(end)
        
        edge = Edge(cap, False)
        graph.insert_edge(start, end, edge)
        
        edge_residual = Edge(cap, True)
        graph.insert_edge(end, start, edge_residual)
        
    return graph

def bfs(graph, start_node, end_node):
    visited = set()
    parent = {}
    queue = [start_node]
    visited.add(start_node)
    
    while queue:
        current = queue.pop(0)
        if current == end_node:
            break
        
        for neighbour, edge in graph.neighbours(current):
            if (neighbour not in visited) and (edge.residual_capacity > 0):
                queue.append(neighbour)
                visited.add(neighbour)
                parent[neighbour] = current
                
    return parent
        
    
        