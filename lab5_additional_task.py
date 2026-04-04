class AVLNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.right = None
        self.left = None
        self.height = 1
        
class AVLTree:
    def __init__(self):
        self.root = None
        
    def get_height(self, node):
        if node is None:
            return 0
        return node.height
    
    def get_balance(self, node):
        if node is None:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)
    
    def right_rotate(self, y):
        x = y.left
        T2 = x.right
        
        x.right = y
        y.left = T2
        
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1
        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1
        
        return x
    
    def left_rotate(self, x):
        y = x.right
        T2 = y.left
        
        y.left = x
        x.right = T2
        
        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1
        
        return y
    
    def search(self, key):
        curr = self.root
        while curr:
            if curr.key == key:
                return curr.value
            
            elif curr.key < key:
                curr = curr.right
                
            elif curr.key > key:
                curr = curr.left
                
        return None
    
    def insert(self, key, value):
        self.root = self._insert(self.root, key, value)
        
    def _insert(self, node, key, value):
        if node is None:
            return AVLNode(key, value)
        
        if key < node.key:
            node.left = self._insert(node.left, key, value)     
        elif key > node.key:
            node.right = self._insert(node.right, key, value)   
        else:
            node.value = value
            return node
        
        node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1
        
        balance_factor = self.get_balance(node)
        
        if balance_factor > 1 and self.get_balance(node.left) >= 0:
            return self.right_rotate(node)
        elif balance_factor > 1 and self.get_balance(node.left) < 0:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)
        elif balance_factor < -1 and self.get_balance(node.right) <= 0:
            return self.left_rotate(node)
        elif balance_factor < -1 and self.get_balance(node.right) > 0:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)
        
        return node
        
    def delete(self, key):
        self.root = self._delete_node(self.root, key)
    
    def _delete_node(self, node, key):
        if node is None:
            return node
        
        if key < node.key:
            node.left = self._delete_node(node.left, key)
        
        elif key > node.key:
            node.right = self._delete_node(node.right, key)
            
        else:
            if node.left is None:
                return node.right
            
            elif node.right is None:
                return node.left
            
            else:
                temp = node.right
                while temp.left:
                    temp = temp.left
                    
                node.key, node.value = temp.key, temp.value
                node.right = self._delete_node(node.right, temp.key)
        
        node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1
        
        balance_factor = self.get_balance(node)
        
        if balance_factor > 1 and self.get_balance(node.left) >= 0:
            return self.right_rotate(node)
        elif balance_factor > 1 and self.get_balance(node.left) < 0:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)
        elif balance_factor < -1 and self.get_balance(node.right) <= 0:
            return self.left_rotate(node)
        elif balance_factor < -1 and self.get_balance(node.right) > 0:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)
        
        return node
    
    def print_as_list(self):
        self._print_in_order(self.root)
        print()
        
    def _print_in_order(self, node):
        if node is not None:
            self._print_in_order(node.left)
            print(f"{node.key}:{node.value} ", end="")
            self._print_in_order(node.right)
            
    def print_tree(self):
        print("==============")
        self.__print_tree(self.root, 0)
        print("==============")

    def __print_tree(self, node, lvl):
        if node!=None:
            self.__print_tree(node.right, lvl+5)

            print()
            print(lvl*" ", node.key, node.value)
     
            self.__print_tree(node.left, lvl+5)
            

def main():
    avl_tree = AVLTree()
    data = {50:'A', 15:'B', 62:'C', 5:'D', 2:'E', 1:'F', 11:'G', 100:'H', 7:'I', 6:'J', 55:'K', 52:'L', 51:'M', 57:'N', 8:'O', 9:'P', 10:'R', 99:'S', 12:'T'}
    for key, val in data.items():
        avl_tree.insert(key, val)
    # wyświetl drzewo 2D
    avl_tree.print_tree()
    # wyświetl zawartość drzewa jako listę od najmniejszego do największego klucza w formie klucz:wartość
    avl_tree.print_as_list()
    # wyszukaj element o kluczu 10 i wypisz wartość
    print(avl_tree.search(10))
    # usuń element o kluczu 50
    avl_tree.delete(50)
    # usuń element o kluczu 52
    avl_tree.delete(52)
    # usuń element o kluczu 11
    avl_tree.delete(11)
    # usuń element o kluczu 57
    avl_tree.delete(57)
    # usuń element o kluczu 1
    avl_tree.delete(1)
    # usuń element o kluczu 12
    avl_tree.delete(12)
    # dodaj element o kluczu 3:AA
    avl_tree.insert(3, "AA")
    # dodaj element o kluczu 4:BB
    avl_tree.insert(4, "BB")
    # usuń element o kluczu 7
    avl_tree.delete(7)
    # usuń element o kluczu 8
    avl_tree.delete(8)
    # wyświetl drzewo 2D
    avl_tree.print_tree()
    # wyświetl zawartość drzewa jako listę od najmniejszego do największego klucza w formie klucz:wartość
    avl_tree.print_as_list()      
        
if __name__ == "__main__":
    main()    