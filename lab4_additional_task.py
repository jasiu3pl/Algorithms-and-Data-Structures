import random

class Element:
    def __init__(self, key, value, levels):
        self.key = key
        self.value = value
        self.tab = [None for _ in range(levels)]
        
class SkipList:
    def __init__(self, max_level):
        self.max_level = max_level
        self.head = Element(None, None, max_level)
        
    def _randomLevel(self, p=0.5):
        lvl = 1   
        while random.random() < p and lvl < self.max_level:
                lvl = lvl + 1
        return lvl
    
    def displayList_(self):
        node = self.head.tab[0]
        keys = [ ]
        while node is not None:
            keys.append(node.key)
            node = node.tab[0]

        for lvl in range(self.max_level - 1, -1, -1):
            print(f"{lvl}  ", end=" ")
            node = self.head.tab[lvl]
            idx = 0
            while node is not None:
                while node.key > keys[idx]:
                    print(end=5*" ")
                    idx += 1
                idx += 1
                print(f"{node.key:2d}:{node.value:2s}", end="")
                node = node.tab[lvl]
            print()
    
    def search(self, key):
        node = self.head
        for lvl in range(self.max_level - 1, -1, -1):
            while node.tab[lvl] is not None and node.tab[lvl].key < key:
                node = node.tab[lvl]
                
        node = node.tab[0]
        
        if node is not None and node.key == key:
            return node.value
        else:
            return None
        
    def insert(self, key, value):
        update = [None for _ in range(self.max_level)]
        node = self.head
        for lvl in range(self.max_level -1, -1, -1):
            while node.tab[lvl] is not None and node.tab[lvl].key < key:
                node = node.tab[lvl]
            
            update[lvl] = node
        
        node = node.tab[0] 
        
        if node is not None and node.key == key:
            node.value = value
            return
        else:
            new_level = self._randomLevel(0.5)
            new_node = Element(key, value, new_level)
            for i in range(new_level):
                new_node.tab[i] = update[i].tab[i]
                update[i].tab[i] = new_node
                
    def remove(self, key):
        update = [None for _ in range(self.max_level)]
        node = self.head
        for lvl in range(self.max_level -1, -1, -1):
            while node.tab[lvl] is not None and node.tab[lvl].key < key:
                node = node.tab[lvl]
            
            update[lvl] = node
        
        node = node.tab[0] 
        if node is not None and node.key == key:
            for i in range(0, self.max_level):
                if update[i].tab[i] == node:
                    update[i].tab[i] = node.tab[i]
            return
                
                          
    def __str__(self):
        node = self.head.tab[0]
        res = []
        while node is not None:
            res.append(f"{node.key}:{node.value}")
            node = node.tab[0]
         
        return "[" + ", ".join(res) + "]"          

def main():
    random.seed(42)

    print("------TEST 1: Wstawianie 1-15------")
    sl = SkipList(5)
    
    for i in range(1, 16):
        sl.insert(i, chr(64 + i))

    sl.displayList_()
    print(sl.search(2), "\n")
    sl.insert(2, 'Z')
    print(sl.search(2), "\n")
    sl.remove(5)
    sl.remove(6)
    sl.remove(7)
    print(sl, "\n")
    sl.insert(6, 'W')
    print(sl, "\n")

    print("------TEST 2: Wstawianie 15-1------")
    sl2 = SkipList(5)
    for i in range(15, 0, -1):
        sl2.insert(i, chr(64 + i))
    
    sl2.displayList_()
    print(sl2.search(2), "\n")
    sl2.insert(2, 'Z')
    print(sl2.search(2), "\n")
    sl2.remove(5)
    sl2.remove(6)
    sl2.remove(7)
    print(sl2, "\n")
    sl2.insert(6, 'W')
    print(sl2, "\n")

if __name__ == '__main__':
    main()
     
            