#making the nodes
class Node:
    def __init__ (self, data):
        self.data = data
        self.next = None
#initializing the linked list       
class LinkedList:
    def __init__ (self):
        self.head = None
      #function for appending data
    def append (self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
          #stating the last node
        lastnode = self.head
        while lastnode.next:
            lastnode = lastnode.next
            
        lastnode.next = new_node
            #print list function
    def print_list(self):
      #stating the current node
        current = self.head
        while current:
            if current.next:
                print(current.data, end=" -- ")
            else:
                print(current.data)
            current = current.next

#creating the linked list
linked_list = LinkedList()

#stating all of the names 
linked_list.append("Marcos")
linked_list.append("Aidan")
linked_list.append("Shahood")
linked_list.append("Ryan")
linked_list.append("Muntag")
linked_list.append("Leo")
linked_list.append("Mason")
linked_list.append("Nate")
linked_list.append("Gavin")
linked_list.append("Chris") 
linked_list.append("Jaiden")

#print the linked list
linked_list.print_list()
