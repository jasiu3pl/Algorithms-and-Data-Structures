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


def insertion_sort(tab):
    for i in range(1, len(tab)):
        j = i
        while j > 0 and tab[j] < tab[j-1]:
            tab[j-1], tab[j] = tab[j], tab[j-1]
            j -= 1
            
    return tab

def shell_sort_classic(tab):
    n = len(tab)
    h = n // 2
    
    while h > 0:
        for i in range(h, n):
            j = i
            while j >= h and tab[j] < tab[j-h]:
                tab[j-h], tab[j] = tab[j], tab[j-h]
                j -= h
     
        h = h // 2
    
    return tab

def shell_sort_modified(tab):
    n = len(tab)
    h = 1
    while (3 * h + 1) < (n // 3):
        h = 3 * h + 1
    
    while h > 0:
        for i in range(h, n):
            j = i
            while j >= h and tab[j] < tab[j-h]:
                tab[j-h], tab[j] = tab[j], tab[j-h]
                j -= h
     
        h = h // 3
    
    return tab

def main():
    test = int(input("Podaj, ktory test chcesz wykonac - 1 lub 2: "))
    match test:
        case 1:
            tab = [Element(value, key) for key,value in  [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')] ]
            tab_insertion = tab.copy()
            tab_shell_classic = tab.copy()
            tab_shell_modified = tab.copy()
            print("====== INSERTION SORT ======")
            print("Nieposortowana tablica:")
            print(tab_insertion)
            t_start = time.perf_counter()
            sorted_insertion = insertion_sort(tab_insertion)
            t_stop = time.perf_counter()
            print("Posortowana tablica:")
            print(sorted_insertion)
            print("STABILNE")
            print("Czas insertion sort:", "{:.7f}".format(t_stop - t_start))
            print("====== SHELL CLASSIC ======")
            print("Nieposortowana tablica:")
            print(tab_shell_classic)
            t_start = time.perf_counter()
            sorted_shell_classic = shell_sort_classic(tab_shell_classic)
            t_stop = time.perf_counter()
            print("Posortowana tablica:")
            print(sorted_shell_classic)
            print("NIESTABILNE")
            print("Czas metoda shella klasyczna:", "{:.7f}".format(t_stop - t_start))
            print("====== SHELL MODIFIED ======")
            print("Nieposortowana tablica:")
            print(tab_shell_modified)
            t_start = time.perf_counter()
            sorted_shell_modified = shell_sort_modified(tab_shell_modified)
            t_stop = time.perf_counter()
            print("Posortowana tablica:")
            print(sorted_shell_modified)
            print("STABILNE")
            print("Czas metoda shella zmodyfikowana:", "{:.7f}".format(t_stop - t_start))
        case 2:
            tab = [int(random.random() * 100) for _ in range(10000)]
            tab_insertion = tab.copy()
            tab_shell_classic = tab.copy()
            tab_shell_modified = tab.copy()
            tab_heap = tab.copy()
            print("====== INSERTION SORT ======")
            t_start = time.perf_counter()
            sorted_insertion = insertion_sort(tab_insertion)
            t_stop = time.perf_counter()
            print("Czas insertion sort:", "{:.7f}".format(t_stop - t_start))
            print("====== SHELL CLASSIC ======")
            t_start = time.perf_counter()
            sorted_shell_classic = shell_sort_classic(tab_shell_classic)
            t_stop = time.perf_counter()
            print("Czas metoda shella klasyczna:", "{:.7f}".format(t_stop - t_start))
            print("====== SHELL MODIFIED ======")
            t_start = time.perf_counter()
            sorted_shell_modified = shell_sort_modified(tab_shell_modified)
            t_stop = time.perf_counter()
            print("Czas metoda shella zmodyfikowana:", "{:.7f}".format(t_stop - t_start))
            print("====== HEAP SORT ======")
            t_start = time.perf_counter()
            heap = PriorityQueue(tab_heap)
            while not heap.is_empty():
                heap.dequeue()
            t_stop = time.perf_counter()
            print("Czas sortowania kopcowego:", "{:.7f}".format(t_stop - t_start))
            
    
    
    
if __name__ == "__main__":
    main()