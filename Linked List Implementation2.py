class LinkedList():
    def __init__(self, data):
            self.head = self.Node(data)
            self.tail = self.head
            self.length = 1


    class Node():
        def __init__(self, value):
            self.value = value
            self.next = None
    

    def __len__(self):
        return self.length

    def nodes(self):
        temp = self.head
        while temp:
            print(temp.value, end=' ')
            temp = temp.next
        print()

    def append(self, value):
        new_node = self.Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
        return self.length
    
    def prepend(self, value):
        new_node = self.Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        new_node.next = self.head
        self.head = new_node
        self.length += 1
        return self.length
        

myLinkedList = LinkedList(1)
myLinkedList.append(2)
myLinkedList.append(3)
myLinkedList.prepend(0)
myLinkedList.nodes()

print('tail:', myLinkedList.tail.value)
print('len:', len(myLinkedList))
    
