class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.right = None
        self.left = None
        
class BST:
    def __init__(self):
        self.root = None
        
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
        if self.root is None:
            self.root = Node(key, value)
            return
        
        curr = self.root
        while curr:
            if curr.key == key:
                curr.value = value
                return
            
            elif key < curr.key:
                if curr.left is None:
                    curr.left = Node(key, value)
                    return
                elif curr.left is not None:
                    curr = curr.left
            
            elif key > curr.key:    
                if curr.right is None:
                    curr.right = Node(key, value)
                    return
                
                elif curr.right is not None:
                    curr = curr.right
                    
    def print_as_list(self):
        self._print_in_order(self.root)
        print()
        
    def _print_in_order(self, node):
        if node is not None:
            self._print_in_order(node.left)
            print(f"{node.key} {node.value},", end="")
            self._print_in_order(node.right)
            
    def height(self):
        if self.root is None:
            return 0
        return self._get_height(self.root) - 1
    
    def _get_height(self, node):
        if node is None:
            return 0
        else:
            left_height = self._get_height(node.left)
            right_height = self._get_height(node.right)
            return max(left_height, right_height) + 1
    
    def delete(self, key):
        self.root = self._delete_node(self.root, key)
    
    def _delete_node(self, node, key):
        # if node is None:
        #     return node
        
        # if key < node.key:
        #     node.left = self._delete_node(node.left, key)
        
        # elif key > node.key:
        #     node.right = self._delete_node(node.right, key)
            
        # else:
        pass
     
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
    tree = BST()
    keys = [50, 15, 62, 5, 20, 58, 91, 3, 8, 37, 60, 24]
    for i in range(0,12):
        tree.insert(keys[i], chr(65+i))
        
    tree.print_tree()
    tree.print_as_list()
    
if __name__ == "__main__":
    main()
        
        