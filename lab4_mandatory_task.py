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
        first_free_index = None
        for i in range(self.size):
            idx = self._get_index(key, i)
            val = self.tab[idx]

            if val == self.deleted and first_free_index is None:
                first_free_index = idx
            
            if val is None:
                if first_free_index is not None:
                    self.tab[first_free_index] = Element(key, value)
                else:
                    self.tab[idx] = Element(key, value)
                return
            
            if isinstance(val, Element) and val.key == key:
                self.tab[idx] = Element(key, value)
                return
        
        if first_free_index is not None:
            self.tab[first_free_index] = Element(key, value)
            return
        
        raise ValueError("Brak miejsca")
    
    def remove(self, key):
        for i in range(self.size):
            idx = self._get_index(key, i)
            val = self.tab[idx]
         
            if val is None:
                raise ValueError("Brak danej")
        
            if val == self.deleted:
                continue
            
            if isinstance(val, Element) and val.key == key:
                self.tab[idx] = self.deleted
                return
        
        raise ValueError("Brak danej")
    
    def __str__(self):
        half_res = []
        for val in self.tab:
            if val is None or val is self.deleted:
                half_res.append("None")
            elif isinstance(val, Element):
                half_res.append(str(val))
        
        res = ", ".join(half_res)
        
        return "{" + res + "}"
    
    
def test_1(size, c1=1, c2=0):
    table = HashTable(size, c1, c2)
    klucze = [i for i in range(1,16)]
    klucze[5] = 18
    klucze[6] = 31
    for i in range(15):
        litera = chr(65 + i)
        try:
            table.insert(klucze[i], litera)
        except ValueError as e:
            print(f"ValueError dla klucza {i}: {e}\n")
            
    print(table,"\n")
    print(table.search(5), "\n")
    print(table.search(14), "\n")
    try:
        print(table.insert(5, chr(90)), "\n")
    except ValueError as e:
        print(f"ValueError: {e}\n")
    print(table.search(5), "\n")
    try:
        print(table.remove(5), "\n")
    except ValueError as e:
        print(f"ValueError: {e}\n")
    print(table, "\n")
    print(table.search(31), "\n")
    try:
        print(table.insert("test", chr(87)), "\n")
    except ValueError as e:
        print(f"ValueError: {e}\n")
    print(table, "\n")
    
# test_1(13,1,0)

def test_2(size, c1=1, c2=0):
    table = HashTable(size, c1, c2)
    for i in range(15):
        litera = chr(65 + i)
        klucz = 13 * (i + 1)
        try:
            table.insert(klucz, litera)
        except ValueError as e:
            print(f"ValueError dla klucza {i}: {e}\n")
    print(table)
    
def main():
    print("------FUNKCJA TESTUJACA NR1 PROBKOWANIE LINIOWE------\n")
    test_1(13,1,0)
    print("------FUNKCJA TESTUJACA NR2 PROBKOWANIE LINIOWE------\n")            
    test_2(13,1,0)
    print("------FUNKCJA TESTUJACA NR2 PROBKOWANIE KWADRATOWE------\n") 
    test_2(13,0,1)
    print("------FUNKCJA TESTUJACA NR1 PROBKOWANIE KWADRATOWE------\n")
    test_1(13,0,1)
                
if __name__ == "__main__":
    main()