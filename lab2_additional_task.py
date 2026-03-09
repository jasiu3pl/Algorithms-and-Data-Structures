class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
class DoublyLinkedList:
    def __init__(self, tail):
        self.head = None
        self.tail = None
        
    def is_empty(self):
        return self.head is None
    
    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count
    
    def get(self):
        if self.is_empty():
            raise ValueError("List is empty")
        
        return self.head.data
        
    def destroy(self):
        self.head = None
        
    def add(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        else:
            self.tail = new_node
        self.head = new_node
    
    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:    
            
    
    def remove(self):
        if self.is_empty():
            raise ValueError("List is empty")
        
        self.head = self.head.next
        
    def remove_end(self):
        if self.is_empty():
            raise ValueError("List is empty")
        
        if self.head.next is None:
            self.head = None
        
        else:
            current = self.head
            while current.next.next:
                current = current.next
            
            current.next = None
        
    def __str__(self):
        res=""
        current = self.head
        while current:
            res += f"-> {current.data} \n"
            current = current.next
        return res
        
    
def main():
    dane_uczelnie = [('AGH', 'Kraków', 1919),
    ('UJ', 'Kraków', 1364),
    ('PW', 'Warszawa', 1915),
    ('UW', 'Warszawa', 1915),
    ('UP', 'Poznań', 1919),
    ('PG', 'Gdańsk', 1945)]
    
    #ex1
    uczelnie = LinkedList()
    for uczelnia in dane_uczelnie[:3]:
        uczelnie.append(uczelnia)
    
    #ex2
    for uczelnia in dane_uczelnie[3:]:
        uczelnie.add(uczelnia)
    
    #ex3
    print(uczelnie)
    
    #ex4
    print(uczelnie.length())
    
    #ex5
    uczelnie.remove()
    print(uczelnie.get(),'\n')
    
    #ex6
    uczelnie.remove_end()
    print(uczelnie)
    
    #ex7
    uczelnie.destroy()
    print(uczelnie.is_empty())
    
    #ex8
    try:
        uczelnie.remove()
    except ValueError as e:
        print(f"ValueError: {e}\n")
    
    #ex9
    try:
        uczelnie.remove_end()
    except ValueError as e:
        print(f"ValueError: {e}\n")
    
    #ex10
    uczelnie.append(dane_uczelnie[0])
    print(uczelnie)
    
    #ex11
    uczelnie.remove_end()
    print(uczelnie)
    
    #ex12
    print(uczelnie.is_empty())
    
    
if __name__ == "__main__":
    main()
        


        
        