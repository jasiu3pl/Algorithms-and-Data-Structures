from copy import deepcopy

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
                   
def transpose(matrix):
    res = Matrix((matrix.size()[1], matrix.size()[0]))
    for i in range(matrix.size()[1]):
        for j in range(matrix.size()[0]):
            res[i][j] = matrix[j][i]
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
        self.matrix[j][i] = edge
        
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
                
def prune(M, G_matrix, P_matrix):
    changed = True
    while changed:
        changed = False
        
        for i in range(M.size()[0]):
            for j in range(M.size()[1]):
                if M[i][j] == 1:
                    neighbours_i_in_P = [x[0] for x in(P_matrix.neighbours(i))]
                    neighbours_j_in_G = [y[0] for y in(G_matrix.neighbours(j))]
                    for neighbour_P in neighbours_i_in_P:
                        found = False
                        for neighbour_G in neighbours_j_in_G:
                            if M[neighbour_P][neighbour_G] == 1:
                                found = True
                                break
                        if not found:
                            M[i][j] = 0
                            changed = True
                            
def ullmann(used_columns, current_row, M, G_matrix, P_matrix, isomorphisms, no_calls):
    no_calls += 1
    
    if current_row == M.size()[0]:
        if P_matrix.matrix == M * transpose(M * G_matrix.matrix):
            isomorphisms.append(deepcopy(M))
        return no_calls

    for c in range(M.size()[1]):
        if not used_columns[c] and M[current_row][c] == 1:
            M_copy = deepcopy(M)
            used_columns[c] = True
            for i in range(M_copy.size()[1]):
                M_copy[current_row][i] = 0
                
            M_copy[current_row][c] = 1
            prune(M_copy, G_matrix, P_matrix)
            no_calls = ullmann(used_columns, current_row + 1, M_copy, G_matrix, P_matrix, isomorphisms, no_calls)
            used_columns[c] = False
            
    return no_calls

def main():
    graph_G = [ ('A','B',1), ('B','F',1), ('B','C',1), ('C','D',1), ('C','E',1), ('D','E',1)]
    graph_P = [ ('A','B',1), ('B','C',1), ('A','C',1)]
    
    unique_G = set()
    unique_P = set()
    
    for elem1, elem2, _ in graph_G:
        unique_G.add(elem1)
        unique_G.add(elem2)
            
    for elem1, elem2, _ in graph_P:
        unique_P.add(elem1)
        unique_P.add(elem2)
            
    unique_G_list = list(unique_G)
    unique_G_list.sort()
    
    unique_P_list = list(unique_P)
    unique_P_list.sort()
    
    Matrix_P = AdjecencyMatrix()
    Matrix_G = AdjecencyMatrix()
    
    for vertex in unique_G_list:
        Matrix_G.insert_vertex(vertex)
    for vertex in unique_P_list:
        Matrix_P.insert_vertex(vertex)
        
    for vertex1, vertex2, edge in graph_G:
        Matrix_G.insert_edge(vertex1, vertex2, edge)
    for vertex1, vertex2, edge in graph_P:
        Matrix_P.insert_edge(vertex1, vertex2, edge)
        
    M0 = Matrix((len(unique_P_list), len(unique_G_list)))
    for i in range(M0.size()[0]):
        for j in range(M0.size()[1]):
            degree_P = len(list(Matrix_P.neighbours(i)))
            degree_G = len(list(Matrix_G.neighbours(j)))
            
            if degree_P <= degree_G:
                M0[i][j] = 1
            else:
                M0[i][j] = 0
                
    isomorphisms = []
    used_columns = [False for _ in range(M0.size()[1])]
    no_calls = ullmann(used_columns, 0, M0, Matrix_G, Matrix_P, isomorphisms, 0)
    print(f"Izomorfizmy: {len(isomorphisms)}, Wywolania: {no_calls}")
    
if __name__ == "__main__":
    main()