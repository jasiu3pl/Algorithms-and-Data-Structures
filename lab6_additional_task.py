class BNode:
    def __init__(self):
        self.keys = []
        self.children = []
    
    def _is_leaf(self):
        return self.children == []
    
class BTree:
    def __init__(self, max_children):
        self.max_children = max_children
        self.max_keys = max_children - 1
        self.root = BNode()
        
    def _insert_to_node(self, node,  key, right_child = None):
        i = 0
        while i < len(node.keys) and node.keys[i] < key:
            i += 1
            
        node.keys.insert(i, key)
        
        if right_child:
            node.children.insert(i + 1, right_child)
        
        if len(node.keys) > self.max_keys:
            mid = len(node.keys) // 2
            mid_key = node.keys[mid]
            new_node = BNode()
            new_node.keys = node.keys[mid + 1:]
            node.keys = node.keys[:mid]
            
            if not node._is_leaf():
                new_node.children = node.children[mid + 1:]
                node.children = node.children[:mid + 1]
                
            return mid_key, new_node
            
        return None
        
    def insert(self, key):
        result = self._insert_recursive(self.root, key)
        
        if result:
            mid_key, new_node = result
            
            new_node2 = BNode()
            new_node2.keys = [mid_key]
            new_node2.children = [self.root, new_node]
            self.root = new_node2
            
    def _insert_recursive(self, node, key):
        i = 0
        while i < len(node.keys) and node.keys[i] < key:
            i += 1
            
        if node._is_leaf():
            return self._insert_to_node(node, key)
        else:
            result = self._insert_recursive(node.children[i], key)
            if result:
                mid_key, new_child = result
                return self._insert_to_node(node, mid_key, new_child)
            else:
                return None
            
    def print_tree(self):
        print("==============")
        self._print_tree(self.root, 0)
        print("==============")
    
    def _print_tree(self, node, lvl):
        if node!=None:
            for i in range(len(node.keys)+1):
                if not node._is_leaf(): 	                	
                    self._print_tree(node.children[i], lvl+1)
                if i<len(node.keys):
                    print(lvl*'  ', node.keys[i])
                    

def main():
    # utwórz puste drzewo o maksymalnej liczbie potomków równej 4
    b_tree = BTree(4)
    # dodaj do niego elementy (będące jednocześnie kluczami) po kolei z listy: [5, 17, 2, 14, 7, 4, 12, 1, 16, 8, 11, 9, 6, 13, 0, 3, 18 , 15, 10, 19]
    keys = [5, 17, 2, 14, 7, 4, 12, 1, 16, 8, 11, 9, 6, 13, 0, 3, 18 , 15, 10, 19]
    for key in keys:
        b_tree.insert(key)
    # wyświetl drzewo
    b_tree.print_tree()
    # utwórz drugie puste drzewo, dodaj do niego 20 kolejnych liczb od 0 do 19 (będą to te same liczby co w liście ale dodane w kolejności rosnącej)
    b_tree2 = BTree(4)
    keys = [5, 17, 2, 14, 7, 4, 12, 1, 16, 8, 11, 9, 6, 13, 0, 3, 18 , 15, 10, 19]
    keys.sort()
    for key in keys:
        b_tree2.insert(key)
    # wyświetl stworzone drzewo (zauważ jak różni się od poprzedniego)
    b_tree2.print_tree()
    # dodaj do drugiego drzewa kolejne liczby od 20 do 199, wyświetl drzewo (zauważ jak wzrosła jego wysokość)
    keys_larger = [i for i in range(20,200)]
    for key in keys_larger:
        b_tree2.insert(key)
    b_tree2.print_tree()
    # utwórz trzecie puste drzewo o maksymalnej liczbie potomków równej 6, dodaj do niego te same liczby co do drugiego drzewa (od 0 do 199) i wyświetl go (zauważ jak zmalała jego wysokość)
    b_tree3 = BTree(6)
    keys = [i for i in range(0,200)]
    for key in keys:
        b_tree3.insert(key)
    b_tree3.print_tree()
    
    
if __name__ == "__main__":
    main()     
                   
        
            