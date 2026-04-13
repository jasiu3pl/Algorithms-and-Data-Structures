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
    # utworzenie pustej kolejki
    queue = PriorityQueue()
    # użycie w pętli enqueue do wpisana do niej elementów których priorytety będą brane z listy [7, 5, 1, 2, 5, 3, 4, 8, 9], a odpowiadające im wartości będą kolejnymi literami z napisu "GRYMOTYLA"
    prior_list = [7, 5, 1, 2, 5, 3, 4, 8, 9]
    letters = ["G", "R", "Y", "M", "O", "T", "Y", "L", "A"]
    for prior, letter in zip(prior_list, letters):
        elem = Element(letter, prior)
        queue.enqueue(elem)
    # wypisanie aktualnego stanu kolejki w postaci kopca
    queue.print_tree(0, 0)
    # wypisanie aktualnego stanu kolejki w postaci tablicy
    queue.print_tab()
    # użycie dequeue do odczytu  pierwszej  danej z kolejki, proszę ją zapamiętać
    greatest = queue.dequeue()
    # użycie  peek do odczytu i wypisania kolejnej  danej
    great_child = queue.peek()
    print(great_child)
    # wypisanie aktualnego stanu kolejki w postaci tablicy
    queue.print_tab()
    # wypisanie zapamiętanej, usuniętej pierwszej danej z kolejki
    print(greatest)
    # opróżnienie kolejki z wypisaniem usuwanych danych (użycie dequeue w pętli dopóki w kolejce będą dane)
    while not queue.is_empty():
        val = queue.dequeue()
        print(val)
        
    # wypisanie opróżnionej kolejki w postaci tablicy (powinno się wypisać { } )
    queue.print_tab()
    
    
if __name__ == "__main__":
    main()    
        
    