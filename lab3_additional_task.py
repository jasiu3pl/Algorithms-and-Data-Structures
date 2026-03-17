SIZE = 5
class Node:
    def __init__(self):
        self.elements = [None for _ in range(SIZE)]
        self.count = 0
        self.next = None
        
    def insert_local(self, index, value):
        for i in range(self.count, index, -1):
           self.elements[i] = self.elements[i - 1]
        self.elements[index] = value
        self.count += 1 
                
    def delete_local(self, index):
        for i in range(index, self.count - 1):
            self.elements[i] = self.elements[i + 1]
        self.elements[self.count - 1] = None
        self.count -= 1
        
class UnrolledLinkedList:
    def __init__(self):
        self.head = None
        self.total_size = 0
        
    def _find_node_and_index(self, index):
        current = self.head
        while current:
            if index < current.count or current.next is None:
                return current, index
            else:
                index -= current.count
                current = current.next
        return None, None
        
    def get(self,index):
        if index < 0 or index >= self.total_size:
            return None
        
        node, local_index = self._find_node_and_index(index)
        if node:
            return node.elements[local_index]
        return None
          
    def insert(self, index, value):
        if self.head is None:
            self.head = Node()
        
        if index > self.total_size:
            index = self.total_size
            
        node, local_index = self._find_node_and_index(index)
        if node.count < SIZE:
            node.insert_local(local_index, value)
        else:
            new_node = Node()
            new_node.next = node.next
            node.next = new_node
            half = SIZE // 2
            
            for i in range(half,SIZE):
                elem = node.elements[i]
                new_node.insert_local(new_node.count, elem)
                node.elements[i] = None
                
            node.count = half
            if local_index <= node.count:
                node.insert_local(local_index, value)
            else:
                new_node.insert_local(local_index - node.count, value)
            
        self.total_size += 1
        
    def delete(self, index):
        if (index < 0) or (index >= self.total_size) or (self.head is None):
            return
        
        node, local_index = self._find_node_and_index(index)
        node.delete_local(local_index)
        self.total_size -= 1
        half = SIZE // 2
        if node.count < half and node.next is not None:
            next_node = node.next
            if node.count + next_node.count <= SIZE:
                for i in range(next_node.count):
                    node.insert_local(node.count, next_node.elements[i])
                node.next = next_node.next
            else:
                missing = half - node.count
                for _ in range(missing):
                    elem = next_node.elements[0]
                    next_node.delete_local(0)
                    node.insert_local(node.count, elem)
        
        if self.head and self.head.count == 0:
            self.head = self.head.next
        
    def display(self):
        current = self.head
        res = []
        while current:
            elems = []
            for i in range(current.count):
                elems.append(str(current.elements[i]))
            res.append(f'[{elems}]')
            current = current.next
        if res:
            print(" -> ".join(res))
        else:
            print('List of nodes is empty')
            
def main():

    lista = UnrolledLinkedList()

    for i in range(1, 10):
        lista.insert(100, i)

    lista.display()

    print(lista.get(4))

    lista.insert(1, 10)
    lista.insert(8, 11)

    lista.display()

    lista.delete(1)
    lista.delete(1)

    lista.display()
    
    
if __name__ == "__main__":
    main()
        