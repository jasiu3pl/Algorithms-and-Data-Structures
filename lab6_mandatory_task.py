class Element:
    def __init__(self, dane, priorytet):
        self.__dane = dane
        self.__priorytet = priorytet
        
    def __lt__(self, other):
        return self.__priorytet < other.__priorytet
    
    def __gt__(self, other):
        return self.__priorytet > other.__priorytet
    
    def __repr__(self):
        return f"{self.__priorytet} : {self.__dane}"
    
class PriorityQueue:
    def __init__(self):
        self.tab = []
        self.heap_size = 0
        
    def is_empty(self):
        return self.heap_size == 0
    
    def right(self, idx):
        return 2 * idx + 2
    
    def left(self, idx):
        return 2 * idx + 1
    
    def parent(self, idx):
        return (idx - 1) // 2
    
    def peek(self):
        if self.is_empty():
            return None
        return self.tab[0]
    
    def enqueue(self, element):
        if self.heap_size == len(self.tab):
            self.tab.append(element)
            self.heap_size += 1
        elif self.heap_size < len(self.tab):
            self.tab[self.heap_size] = element
            self.heap_size += 1
            
        idx = self.heap_size - 1
        while idx > 0 and self.tab[idx] > self.tab[self.parent(idx)]:
            self.tab[self.parent(idx)], self.tab[idx]  = self.tab[idx], self.tab[self.parent(idx)]
            idx = self.parent(idx)
            
    def dequeue(self):
        if self.is_empty():
            return None
        greatest_priority = self.tab[0]
        self.heap_size -= 1
        self.tab[0] = self.tab[self.heap_size]
        self.heap_fix(0)
        return greatest_priority
    
    def heap_fix(self, idx):
        while True:
            l = self.left(idx)
            r = self.right(idx)
            greatest = idx
            if self.tab[l] < self.tab[self.heap_size]:
                if l > greatest:
                    greatest = l
            if self.tab[r] < self.tab[self.heap_size]:
                if r > greatest:
                    greatest = r
            elif greatest == idx:
                break
            else:
                self.tab[greatest], self.tab[idx] = self.tab[idx], self.tab[greatest]
                    
                
        
        
            
        
    