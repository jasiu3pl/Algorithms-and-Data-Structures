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

def main():
    m1 = Matrix([[1, 0, 2], [-1, 3, 1]])
    m3 = Matrix([[3, 1], [2, 1], [1, 0]])

    print(transpose(m1))
    print(m1 + Matrix(m1.size(), 1))
    print(m1 * m3)
    
if __name__ == "__main__":   
    main()
    
            