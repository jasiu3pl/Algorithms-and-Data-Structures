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
    
    def chio_det(self):
        if self.size()[0] != self.size()[1]:
            raise ValueError("Matrix must be square for determinant calculation")
        
        if self.size() == (1, 1):
            return self[0][0]
        
        if self.size() == (2, 2):
            return self[0][0] * self[1][1] - self[0][1] * self[1][0]
        
        else:
            sign = 1
            if self[0][0] == 0:
                row_changed = False
                for i in range(1, self.size()[0]):
                    if self[i][0] != 0:
                        self.__matrix[0], self.__matrix[i] = self.__matrix[i], self.__matrix[0]
                        sign = -1
                        row_changed = True
                        break
                    
                if not row_changed:
                    return 0 
            
            smaller_matrix = Matrix((self.size()[0] - 1, self.size()[1] - 1))
            for i in range(smaller_matrix.size()[0]):
                for j in range(smaller_matrix.size()[1]):
                    smaller_matrix[i][j] = self[0][0] * self[i + 1][j + 1] - self[0][j + 1] * self[i + 1][0]
            return sign * (1 / (self[0][0] ** (self.size()[0] - 2)) * smaller_matrix.chio_det())
        
def main():
    m1 = Matrix([[5, 1, 1, 2, 3], [4, 2, 1, 7, 3], [2, 1, 2, 4, 7], [9, 1, 0, 7, 0], [1, 4, 7, 2, 2]])
    m2 = Matrix([[0, 1, 1, 2, 3], [4, 2, 1, 7, 3], [2, 1, 2, 4, 7], [9, 1, 0, 7, 0], [1, 4, 7, 2, 2]])
    m3 = Matrix([[0, 0, 0, 0, 0], [4, 2, 1, 7, 3], [2, 1, 2, 4, 7], [9, 1, 0, 7, 0], [1, 4, 7, 2, 2]])
    m4 = Matrix([[0, 1, 1, 2, 3], [0, 2, 1, 7, 3], [0, 1, 2, 4, 7], [0, 1, 0, 7, 0], [0, 4, 7, 2, 2]])
    print(m1.chio_det())
    print(m2.chio_det())
    print(m3.chio_det())
    print(m4.chio_det())
    
if __name__ == "__main__":
    main()
        
        
        
