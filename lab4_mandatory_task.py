class Element:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        
    def __str__(self):
        return f'{self.key} : {self.value}'
    
class HashTable:
    def __init__(self, size, c1 = 1, c2 = 0):
        self.size = size
        self.tab = [None for _ in range(size)]
        self.c1 = c1
        self.c2 = c2
        self.deleted = "REMOVED"
        
    def _hash_function(self, key):
        counter = 0
        if isinstance(key, str):
            for i in key:
                counter += ord(i)
        else:
            counter = key
                
        return counter % self.size
        
    
    def _get_index(self, key, i):
        hash_val = self._hash_function(key)
        return (hash_val + self.c1 * i + self.c2 * (i**2)) % self.size
    
    def search(self, key):
        for i in range(self.size):
            idx = self._get_index(key, i)
            val = self.tab[idx]
         
            if val is None:
                return None
            
            if isinstance(val, Element) and val.key == key:
                return val.value
        
        return None
    
    def insert(self, key, value):
        for i in range(self.size):
            idx = self._get_index(key, i)
            val = self.tab[idx]
         
            if val is None or val == self.deleted:
                self.tab[idx] = Element(key, value)
                return
            
            if isinstance(val, Element) and val.key == key:
                val.value = value
                return
        
        return None
        
        