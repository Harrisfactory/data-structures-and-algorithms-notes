class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


############## INSERTIONS ###################
    def insertAtBegin(self, data):
        new_node = node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    def insertAtEnd(self, data):
        new_node = node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        #now at end, so insert here
        current_node.next = new_node
    
    #indexing starts from 0.
    def insertAtIndex(self, data, index):
        new_node = Node(data)
        current_node = self.head
        position = 0
        if position == index:
            self.insertAtbegin(data)
        else:
            while current_node != None and position+1 != index:
                position+=1
                current_node = current_node.next
            
            if current_node != None:
                new_node.next = current_node.next
                current_node.next = new_node
            else:
                print("index not present")

    def updateAtIndex(self, val, index):
        current_node = self.head
        #node position, which will be compared to the index
        position = 0
        if position == index:
            current_node.data = val
        else:
            while current_node != None and position != index:
                position+=1
                current_node = current_node.next
            
            if current_node != None:
                current_node.data = val
            else:
                print("index not present")

############## Deletions ##############################
  
    