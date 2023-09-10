class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

############## INSERTIONS ###################
    def insertAtBegin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    def insertAtEnd(self, data):
        new_node = Node(data)
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
  
    def removeFirstNode(self):
        if self.head == None:
            return
        #   *
        # 1[5]->2[7]->3[2]
        # 2[7]->3[2]
        self.head = self.head.next

    def removeLastNode(self):
        if self.head == None:
            return
        
        current_node = self.head
        #        n->     ->
        # 1[5]->2[7]->3[2]->4[1]->5[11]->6[4]
        #               n->    ->
        # 1[5]->2[7]->3[2]->4[1]->5[11]->6[4]
        #                    n->    ->
        # 1[5]->2[7]->3[2]->4[1]->5[11]->6[4]
        #                          n->    ->
        # 1[5]->2[7]->3[2]->4[1]->5[11]->6[4]
        #                                [n->]   ->*
        # 1[5]->2[7]->3[2]->4[1]->5[11]->6[4]
        #                                
        # 1[5]->2[7]->3[2]->4[1]->5[11]
        while current_node.next.next:
            current_node = current_node.next
        
        current_node.next = None

    def removeAtIndex(self, index):
        
        if self.head == None:
            return
        
        current_node = self.head
        position = 0
        if position == index:
            #since our head is currently at index
            self.removeFirstNode()
        else:
            while current_node != None and position+1 != index:
                position+=1
                current_node = current_node.next
            
            #position now 1 below index
            if current_node != None:
                #index 3
                # 1[5]->2[7]->3[2]->4[1]->5[11]->6[4]
                #               *  ->  n  =  nn
                # 1[5]->2[7]->3[2]->4[1]->5[11]->6[4]
                #
                # 1[5]->2[7]->3[2]->5[11]->6[4]
                current_node.next = current_node.next.next
            else:
                print("index not present")
            
    #Delete a Linked List Node of a given Data
    def removeNode(self, data):

        current_node = self.head

        while current_node != None and current_node.next.data != data:
            current_node = current_node.next
 
        if current_node == None:
            return
        else:
            current_node.next = current_node.next.next

#################### Traverse ############################

    def printLL(self):
        current_node = self.head
        while current_node != None:
            print(current_node.data)
            current_node = current_node.next


if __name__ == '__main__':
    print("running linked list tests...")
    
    linked_list = LinkedList()

    linked_list.insertAtBegin(5)
    linked_list.insertAtEnd(7)
    linked_list.insertAtEnd(2)
    linked_list.insertAtEnd(1)
    linked_list.insertAtEnd(11)
    linked_list.insertAtEnd(4)

    linked_list.removeLastNode()


    linked_list.printLL()