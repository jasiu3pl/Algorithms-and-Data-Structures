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
    def __init__(self, tab = None):
        if tab is None: 
            self.tab = []
            self.heap_size = 0 
        else:
            self.tab = tab 
            self.heap_size = len(tab)
            start_idx = self.parent(self.heap_size - 1)
            for i in range(start_idx, -1, -1):
                self.heap_fix(i)
        
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
        self.tab[0], self.tab[self.heap_size - 1] = self.tab[self.heap_size - 1], self.tab[0]
        self.heap_size -= 1
        self.heap_fix(0)
        return self.tab[self.heap_size]
    
    def heap_fix(self, idx):
        while True:
            l = self.left(idx)
            r = self.right(idx)
            greatest = idx
            if l < self.heap_size:
                if self.tab[l] > self.tab[greatest]:
                    greatest = l
                    
            if r < self.heap_size:
                if self.tab[r] > self.tab[greatest]:
                    greatest = r
                    
            if greatest == idx:
                break
            else:
                self.tab[greatest], self.tab[idx] = self.tab[idx], self.tab[greatest]
                idx = greatest
                    
    def print_tab(self):
        print ('{', end=' ')
        print(*self.tab[:self.heap_size], sep=', ', end = ' ')
        print( '}')
        
    def print_tree(self, idx, lvl):
        if idx<self.heap_size:           
            self.print_tree(self.right(idx), lvl+1)
            print(2*lvl*'  ', self.tab[idx] if self.tab[idx] else None)           
            self.print_tree(self.left(idx), lvl+1)
            
            
def main():
    # Niech dana będzie lista krotek:
    # [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')]
    # Stwórz na jej podstawie listę (tablicę), której elementy są obiektami utworzonej na poprzednich zajęciach klasy.
    # Przykładowo może to być instrukcja:
    # [ Elem(key, value) for key,value in  [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')]]
    tab = [Element(key, value) for key,value in  [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')]]
    # Przekaż tak utworzoną tablicę jako parametr konstruktora przy tworzeniu kopca.
    heap = PriorityQueue(tab)
    # Wypisz utworzony kopiec jako tablicę i jako drzewo 2D, a następnie, po rozebraniu kopca, wypisz posortowaną tablicę (tą którą kopiec dostał jako argument przy jego tworzeniu).
    heap.print_tree(0, 0)
    heap.print_tab()
    # Zaobserwuj i wypisz, czy sortowanie jest stabilne, tzn. czy kolejność elementów o tym samym priorytecie zostanie zachowana (w porównaniu z ich kolejnością w liście z danymi). Wypisane powinno zostać jedno słowo:
    while not heap.is_empty():
        heap.dequeue()
    print("Posortowana tablica:")
    print(heap.tab)
    print("NIESTABILNE")
    # STABILNE lub NIESTABILNE
    
    
    
if __name__ == "__main__":
    main()