import polska

class Vertex:
    def __init__(self, key):
        self.key = key
        
    def __eq__(self, other):
        return self.key == other.key
    
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
        pass