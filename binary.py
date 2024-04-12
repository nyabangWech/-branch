class Node:
   def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def inOrderTraversal(node):
    if node is None:
        return
    inOrderTraversal(node.left)
    print(node.data,end=",")
    inOrderTraversal(node.right)

root = Node('R')
nodeA = Node('A')
nodeB = Node('B')
nodeC = Node('c')
nodeD = Node('D')
nodeE = Node('E')
nodeF = Node('F')
nodeG = Node('G')

root.left = nodeA
root.right = nodeB

nodeA.left = nodeC
nodeA.right = nodeD

nodeB.left = nodeE
nodeB.right = nodeF

nodeF.left = nodeG

inOrderTraversal(root)

