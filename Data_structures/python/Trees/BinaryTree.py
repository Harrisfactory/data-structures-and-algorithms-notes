######
####contains:
###Data
###pointer to left child
###pointer to right child
#####
######
####uses:
###Inserting an element[]
###Removing an element[]
###Searching for an element[]
###Traversing the tree[]
######
####other uses:
###Finding the height of a tree[]
###Find the level of a node of the tree[]
###Finding the size of the tree[]
######
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


######
####Tree Traversal
###Preorder
###Inorder
###Postorder
######

######
####Uses for preOrder
###when we're searching for an element within a binary search tree.
######
def preOrder(root):
    if root == None:
        return
    #process data
    print(root.data)
    preOrder(root.left)
    preOrder(root.right)
######
####Uses for inOrder
###print out all the values in a tree in sorted order
######
def inOrder(root):
    if root == None:
        return
    inOrder(root.left)
    #process data
    print(root.data)
    inOrder(root.right)

######
####Uses for postOrder
###
#####
def postOrder(root):
    if root == None:
        return
    postOrder(root.left)
    postOrder(root.right)
    #process data
    print(root.data)

######
####USES FOR LEVEL ORDER
###
######
#BST FOR TREES
def levelOrder(root):

    #create empty queue 
    #for level orer traversal
    queue = []

    #enqueue root to initialize height
    queue.append(root)

    h = 0

    while len(queue) > 0:
       

        #print the front of the queue 
        #and remove it from queue
        print(queue[0].data)
        node = queue.pop(0)

        #optional to find height
        #if node.left is not None or node.right is not None:
        #    h+=1

        #Enqueue left child
        if node.left is not None:
            queue.append(node.left)

        #Enqueue right child
        if node.right is not None:
            queue.append(node.right)
    #print("height is " + str(h))





######
####Driver code
######

#                   (3)
#                   /   \
#                 (4)    (7)
#                 / \    /  \
#               (5) (6) (8) (9)
root = Node(3)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(6)

root.right = Node(7)
root.right.left = Node(8)
root.right.right = Node(9)


print("printing preOrder, should be [3,4,5,6,7,8,9]")
preOrder(root)
print("printing inOrder, should be [5,4,6,3,8,7,9]")
inOrder(root)
print("printing postOrder, should be [5,6,4,8,9,7,3]")
postOrder(root)
print("printing levelOrder (BFS), should be [3,4,7,5,6,8,9]")
levelOrder(root)



