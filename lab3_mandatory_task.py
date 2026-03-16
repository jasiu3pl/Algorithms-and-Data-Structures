class CircularQueue:
    def __init__(self):
        self.size = 5
        self.tab = [None for _ in range(self.size)]
        self.read_index = 0
        self.write_index = 0
    
    def is_empty(self):
        return self.read_index == self.write_index
    
    def peek(self):
        if self.is_empty():
            raise None
        
        return self.tab[self.read_index]
    
    def dequeue(self):
        if self.is_empty():
            raise None
        
        temp_value = self.tab[self.read_index]
        self.tab[self.read_index] = None
        self.read_index = (self.read_index + 1) % self.size
        return temp_value
    
    def enqueue(self, data):
        self.tab[self.write_index] = data
        self.write_index = (self.write_index + 1) % self.size
        
        if self.write_index == self.read_index:
            old_size = self.size
            new_tab = self.tab + [None for _ in range(self.size)]
            for i in range(self.read_index, old_size):
                new_tab[i + old_size] = self.tab[i]
                new_tab[i] = None
            
            self.tab = new_tab
            self.size = 2*old_size
            self.read_index += old_size
            
    def print_tab(self):
        for i in range(self.tab):
            print(self.tab[i])
            
    def __str__(self):
        if self.is_empty():
            return "[]"
        res = []
        idx = self.read_index
        while idx != self.write_index:
            res.append(self.tab[idx])
            idx = (idx + 1) % self.size
        
        return str(res) 

def main():
    kolejka = CircularQueue()

    for i in range(1, 5):
        kolejka.enqueue(i)

    pierwsza_dana = kolejka.dequeue()
    print(pierwsza_dana)

    druga_dana = kolejka.peek()
    print(druga_dana)

    print(kolejka)

    for i in range(5, 9):
        kolejka.enqueue(i)

    print(kolejka.tab) 

    while not kolejka.is_empty():
        print(kolejka.dequeue())

    print(kolejka)
    
if __name__ == "__main__":
    main()     
        
        
        
    
    