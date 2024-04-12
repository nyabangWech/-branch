class Node:
 def init_(self,data):
        self.data =data
        self.left =self.right= None
    
def findMax(root):
       if(root==None):
         return float('_inf') 
       res = root.data
       res = findMax(root.left)
       rres = findMax(root.right)
       if (lres > res):
         lres = res
       if (rres > res):
        rres = res
        return res
    
       if __name__ == '__main__':
         root = Node(3)
       root.left = Node(8)
       root.right = Node(5)
       root.left.right = Node(10)
       root.left.right.left = Node(5)
       root.left.right.right = Node(3)
       root.right.right = Node(11)
       root.right.right.left = Node(4)
       print(
         findMax(root))
       