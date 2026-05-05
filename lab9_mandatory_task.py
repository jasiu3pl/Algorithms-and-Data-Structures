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
        
def get_path_flow(graph, start_node, end_node, parent):
    if end_node not in parent:
        return 0
    
    min_flow = float('inf')
    current = end_node
    
    while current != start_node:
        p = parent[current]
        edge = graph.get_edge(p, current)
        
        if edge.residual_capacity < min_flow:
            min_flow = edge.residual_capacity
            
        current = p
    
    return min_flow

def augment_path(graph, start_node, end_node, parent, min_flow):
    current = end_node
    while current != start_node:
        p = parent[current]
        
        forward_edge = graph.get_edge(p, current)
        backward_edge = graph.get_edge(current, p)
        
        forward_edge.residual_capacity -= min_flow
        backward_edge.residual_capacity += min_flow
        
        if not forward_edge.is_residual:
            forward_edge.flow += min_flow
        else:
            backward_edge.flow -= min_flow
            
        current = p
        
def printGraph(g):
    print("------GRAPH------")
    for v in g.vertices():
        print(v, end = " -> ")
        for (n, w) in g.neighbours(v):
            print(n, w, end=";")
        print()
    print("-------------------")
    
def edmonds_karp(graph, start_node, end_node):
    while True:
        parent = bfs(graph, start_node, end_node)
        if end_node not in parent:
            break
        
        min_flow = get_path_flow(graph, start_node, end_node, parent)
        
        augment_path(graph, start_node, end_node, parent, min_flow)
        
    total_flow = 0
    
    for v in graph.vertices():
        edge = graph.get_edge(v, end_node)
        
        if edge is not None and not edge.is_residual:
            total_flow += edge.flow
    
    return total_flow

def main():
    #przypadek 1
    graf_0_data = [ ('s','u',2), ('u','t',1), ('u','v',3), ('s','v',1), ('v','t',2) ]
    g0 = build_graph(graf_0_data)
    max_flow_0 = edmonds_karp(g0, 's', 't')
    
    print(f"Znaleziony przepływ dla g0: {max_flow_0}")
    printGraph(g0)
    wyplyw_z_u = 0
    for _, edge in g0.neighbours('u'):
        if not edge.is_residual:
            wyplyw_z_u += edge.flow
        
    print(f"Rzeczywisty przepływ g0: {wyplyw_z_u}")
    
    #przypadek 2
    graf_1_data = [ ('s', 'a', 16), ('s', 'c', 13), ('a', 'c', 10), ('a', 'b', 12), ('b', 'c', 9), ('b', 't', 20), ('c', 'd', 14), ('d', 'b', 7), ('d', 't', 4) ]
    g1 = build_graph(graf_1_data)
    max_flow_1 = edmonds_karp(g1, 's', 't')
    
    print(f"Znaleziony przepływ dla g1: {max_flow_1}")
    printGraph(g1)
    wyplyw_z_u = 0
    for _, edge in g1.neighbours('a'):
        if not edge.is_residual:
            wyplyw_z_u += edge.flow
        
    print(f"Rzeczywisty przepływ g1: {wyplyw_z_u}")
    
    #przypadek 3
    graf_2_data = [ ('s', 'a', 3), ('s', 'c', 3), ('a', 'b', 4), ('b', 's', 3), ('b', 'c', 1), ('b', 'd', 2), ('c', 'e', 6), ('c', 'd', 2), ('d', 't', 1), ('e', 't', 9)]
    g2 = build_graph(graf_2_data)
    max_flow_2 = edmonds_karp(g2, 's', 't')
    
    print(f"Znaleziony przepływ dla g2: {max_flow_2}")
    printGraph(g2)
    wyplyw_z_u = 0
    for _, edge in g2.neighbours('a'):
        if not edge.is_residual:
            wyplyw_z_u += edge.flow
        
    print(f"Rzeczywisty przepływ g2: {wyplyw_z_u}")
    
    #przypadek 4
    graf_3_data = [('s', 'a', 3), ('s', 'd', 2), ('a', 'b', 4), ('b', 'c', 5), ('c', 't', 6), ('a', 'f', 3),  ('f', 't', 3), ('d', 'e', 2), ('e','f',2)]
    g3 = build_graph(graf_3_data)
    max_flow_3 = edmonds_karp(g3, 's', 't')
    
    print(f"Znaleziony przepływ dla g3: {max_flow_3}")
    printGraph(g3)
    wyplyw_z_u = 0
    for _, edge in g3.neighbours('a'):
        if not edge.is_residual:
            wyplyw_z_u += edge.flow
        
    print(f"Rzeczywisty przepływ g3: {wyplyw_z_u}")

if __name__ == "__main__":
    main()
        