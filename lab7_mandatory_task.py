import time
import random
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
            
def selection_sort_swap(tab):
    for i in range(0, len(tab)):
        m = min(tab[i:])
        idx_m = tab.index(m, i)
        tab[i], tab[idx_m] = tab[idx_m], tab[i]
    return tab
        
def selection_sort_shift(tab):
    for i in range(0, len(tab)):
        m = min(tab[i:])
        idx_m = tab.index(m, i)
        deleted_elem = tab.pop(idx_m)
        tab.insert(i, deleted_elem)
    return tab
            
            
def main():
    test = int(input("Podaj, ktory test chcesz wykonac - 1 lub 2: "))
    match test:
        case 1:
            tab = [Element(value, key) for key,value in  [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')]]
            heap = PriorityQueue(tab)
            heap.print_tree(0, 0)
            heap.print_tab()
            while not heap.is_empty():
                heap.dequeue()
            print("Posortowana tablica:")
            print(heap.tab)
            print("NIESTABILNE\n")
            
            tab = [Element(value, key) for key,value in  [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')]]
            print(tab)
            swap = selection_sort_swap(tab)
            print("Posortowana tablica:")
            print(swap)
            print("NIEsSTABILNE\n")
            
            tab = [Element(value, key) for key,value in  [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')]]
            print(tab)
            shift = selection_sort_shift(tab)
            print("Posortowana tablica:")
            print(shift)
            print("STABILNE\n")
        case 2:
            tab = [int(random.random() * 100) for _ in range(10000)]
            tab_heap = tab.copy()
            tab_swap = tab.copy()
            tab_shift = tab.copy()
            t_start = time.perf_counter()
            heap = PriorityQueue(tab_heap)
            while not heap.is_empty():
                heap.dequeue()
            t_stop = time.perf_counter()
            print("Czas sortowania kopcowego:", "{:.7f}".format(t_stop - t_start))
            
            t_start = time.perf_counter()
            selection_sort_swap(tab_swap) 
            t_stop = time.perf_counter()
            print("Czas sortowania selection_sort_swap:", "{:.7f}".format(t_stop - t_start))
    
            t_start = time.perf_counter()
            selection_sort_shift(tab_shift) 
            t_stop = time.perf_counter()
            print("Czas sortowania selection_sort_shift:", "{:.7f}".format(t_stop - t_start))
    
if __name__ == "__main__":
    main()