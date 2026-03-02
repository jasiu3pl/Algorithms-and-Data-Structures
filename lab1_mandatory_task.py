class Matrix:
    def __init__(self, matrix, value=0):
        if isinstance(matrix, tuple):
            self.__matrix = [[value] * matrix[1] for _ in range(matrix[0])] 
        else:
            self.__matrix = matrix
            
    def size(self):
        return len(self.__matrix), len(self.__matrix[0])
            
    def __add__(self, b):
        res = Matrix(self.size())
        res.matrix = []
        for i in range(self.size()[0]):
            row = []
            for j in range(self.size()[1]):
                x = self.__matrix[i][j] + b.__matrix[i][j]
                row.append(x)
            res.matrix.append(row)
        return res
    
    def __mul__(self, b):
        if self.size()[1] != b.size()[0]:
            raise ValueError("Incompatible matrix sizes for multiplication")
        
        res = Matrix()
        res.matrix = []
        for i in range(self.size()[0]):
            for j in range(b.size()[1]):
                x = 0
                for k in range(self.size()[1]):
                    x += self.__matrix[i][k] * b.__matrix[k][j]
                
                res[i][j] = x
        return res
    
    def __eq__(self, b):
        if self.size() != b.size():
            return False
        
        for i in range(self.size()[0]):
            for j in range(self.size()[1]):
                if self.__matrix[i][j] != b.__matrix[i][j]:
                    return False
        return True
    
    def __getitem__(self, row):
        return self.__matrix[row]
    
    def __str__(self):
        for i in self.__matrix:
            print("|")
            for j in self.__matrix[i]:
                print(j)
            print("|\n")
            
            
def transpose(matrix):
    res = Matrix((matrix.size()[1]))
    
            