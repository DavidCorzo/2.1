import gc
from memory_profiler import profile


class Node: 
    def __init__(self,val):
        self.value = val 
        self.left_child = None
        self.right_child = None 
    
    def insert(self,data):
        if (self.value == data):
            return False # No se pueden valores duplicados
        elif self.value > data:
            if (self.left_child):
                return self.left_child.insert(data)
            else:
                self.left_child = Node(data)
                return True 
        else: 
            if (self.right_child):
                return self.right_child.insert(data)
            else:
                self.right_child = Node(data)
                return True 
    
    def find(self, key):
        if (self.value == key):
            return True 
        elif self.value > key: 
            if (self.left_child):
                return self.left_child.find(key)
            else:
                return False 
        else:
            if (self.right_child):
                return self.right_child.find(key)
            else:
                return False 

    def traverse(self):
        print(self.value)
        if (self.left_child):
            return self.left_child.traverse()
        if (self.right_child):
            return self.right_child.traverse()

    def find_min(self):
        if (self.left_child):
            return self.left_child.find_min()
        else:
            return self.value # Retorna el valor que tenga en ese momento 
        
    def find_max(self):
        if (self.right_child):
            return self.left_child.find_max()
        else:
            return self.value # Retorna el valor que tenga en ese momento 
        

class Tree:
    def __init__(self):
        self.root = None 

    def insert(self, data):
        if (self.root):
            return self.root.insert(data) 
        else:
            self.root = Node(data)
            return True 

    def find(self, key):
        if (self.root):
            return self.root.find(key)
        else: 
            return False # No existe
    
    def traverse(self):
        if (self.root):
            self.root.traverse()
        else:
            return False 
    
    def find_min(self):
        if (self.root):
            return self.root.find_min()
        else:
            return False 
    
    def find_max(self):
        if (self.root):
            return self.root.find_max()
        else:
            return False 

@profile 
def main():
    bst = Tree()
    # print(bst.traverse()) 
    # print(bts.insert(10)) # True
    # print(bts.insert(15)) # True 
    # print(bts.find(15)) # True
    # print(bts.find(1)) # False
    bst.insert(5)
    bst.insert(15)
    bst.insert(20)
    bst.insert(21)
    bst.insert(18)
    bst.insert(30)
    bst.insert(120)
    bst.insert(-15)
    bst.insert(-100)
    # bst.traverse() 
    print("Min val: ",bst.find_min())
    print("Max val: ",bst.find_max())

    for obj in gc.get_objects():
        if isinstance(obj,Tree):
            print("Tree:", obj)
    for obj in gc.get_objects():
        if isinstance(obj, Node):
            print("Node: ", obj.value, obj)
            print("Right child: ", obj.right_child)



if __name__ == "__main__":
    main()
