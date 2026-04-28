import polska

class Vertex:
    def __init__(self, key):
        self.key = key
        
    def __eq__(self, other):
        if isinstance(other, Vertex):
            return self.key == other.key
        return self.key == other
    
    def __hash__(self):
        return hash(self.key)
    
    def __repr__(self):
        return self.key

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

class Matrix:
    def __init__(self, matrix, value=0):
        if isinstance(matrix, tuple):
            self.__matrix = [[value] * matrix[1] for _ in range(matrix[0])] 
        else:
            self.__matrix = matrix
            
    def size(self):
        return len(self.__matrix), len(self.__matrix[0])
    
    def __getitem__(self, row):
        return self.__matrix[row]
            
    def __add__(self, b):
        res = Matrix(self.size())
        for i in range(self.size()[0]):
            for j in range(self.size()[1]):
                res[i][j] = self.__matrix[i][j] + b.__matrix[i][j]
        return res
    
    def __mul__(self, b):
        if self.size()[1] != b.size()[0]:
            raise ValueError("Incompatible matrix sizes for multiplication")
        
        res = Matrix((self.size()[0], b.size()[1]))
        for i in range(self.size()[0]):
            for j in range(b.size()[1]):
                for k in range(self.size()[1]):
                    res[i][j] += self.__matrix[i][k] * b.__matrix[k][j]
        return res
    
    def __eq__(self, b):
        if self.size() != b.size():
            return False
        
        for i in range(self.size()[0]):
            for j in range(self.size()[1]):
                if self.__matrix[i][j] != b.__matrix[i][j]:
                    return False
        return True
    
    def __str__(self):
        res = ""
        for row in self.__matrix:
            res += "|"
            for elem in row:
                res += f" {elem} "
            res += "|\n"
        return res
    
class AdjecencyMatrix:
    def __init__(self):
        self.nodes = []
        self.matrix = Matrix((0, 0))
        
    def insert_vertex(self, vertex):
        if vertex in self.nodes:
            return
        self.nodes.append(vertex)
        n = len(self.nodes)
        new_matrix = Matrix((n, n))
        for i in range(n - 1):
            for j in range(n - 1):
                new_matrix[i][j] = self.matrix[i][j]
                
        self.matrix = new_matrix
        
    def insert_edge(self, vertex1, vertex2, edge=1):
        i = self.nodes.index(vertex1)
        j = self.nodes.index(vertex2)
        self.matrix[i][j] = edge
        
    def delete_edge(self, vertex1, vertex2):
        i = self.nodes.index(vertex1)
        j = self.nodes.index(vertex2)
        self.matrix[i][j] = 0
        
    def delete_vertex(self, vertex):
        n = len(self.nodes)
        idx = self.nodes.index(vertex)
        self.nodes.pop(idx)
        new_matrix = Matrix((n-1, n-1))
        
        new_i = 0
        for i in range(n):
            if i == idx:
                continue
            
            new_j = 0
            for j in range(n):
                if j == idx:
                    continue
                
                new_matrix[new_i][new_j] = self.matrix[i][j]
                
                new_j += 1
            new_i += 1
        
        self.matrix = new_matrix
        
    def vertices(self):
        return [i for i in range(0, len(self.nodes))]
    
    def get_vertex(self, vertex_id):
        return self.nodes[vertex_id]
    
    def neighbours(self, vertex_id):
        for idx, value in enumerate(self.matrix[vertex_id]):
            if value > 0:
                yield (idx, value)
                
def color_graph(graph, start_vertex, method='BFS'):
    to_visit = [start_vertex]
    visited = {start_vertex}
    colors = {}
    used_colors = []
    
    while to_visit:
        match method:
            case 'BFS':
                current  = to_visit.pop(0)
            case 'DFS':
                current = to_visit.pop()
            case _:
                print("Podaj jedna z dwoch metod BFS/DFS")
                return
        
        used_colors = []
        for neighbour, _ in graph.neighbours(current):
            if neighbour in colors:
                used_colors.append(colors[neighbour])
                
        smallest = 0
        while smallest in used_colors:
            smallest += 1
            
        colors[current] = smallest
        
        for neighbour, _ in graph.neighbours(current):   
            if neighbour not in visited:
                visited.add(neighbour)
                to_visit.append(neighbour)
                
    return [(graph.get_vertex(v).key, c) for v, c in colors.items()]
                
        
        
                
def main():
    graph_bfs = AdjecencyList()
    graph_dfs = AdjecencyMatrix()
    
    for x, y, litera in polska.polska:
        graph_bfs.insert_vertex(Vertex(litera))
        
    for v1, v2 in polska.graf:
        graph_bfs.insert_edge(Vertex(v1), Vertex(v2))
        
    for x, y, litera in polska.polska:
        graph_dfs.insert_vertex(Vertex(litera))
        
    for v1, v2 in polska.graf:
        graph_dfs.insert_edge(Vertex(v1), Vertex(v2))
    
    res_bfs = color_graph(graph_bfs, Vertex('Z'), method='BFS')
    res_dfs = color_graph(graph_dfs, graph_dfs.nodes.index(Vertex('Z')), method='DFS')
    
    polska.draw_map(graph_bfs, res_bfs)
    polska.draw_map(graph_dfs, res_dfs)
    
    
if __name__ == "__main__":
    main()
            
                