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

    def create_head(self, new_node):
        self.head = new_node
        self.tail = self.head

    def nodes(self):
        temp = self.head
        while temp:
            print(temp.value, end=' ')
            temp = temp.next
        print()

    def append(self, value):
        new_node = self.Node(value)
        if self.head is None:
            self.create_head(new_node)
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1
        return self.length
    
    def prepend(self, value):
        new_node = self.Node(value)
        if self.head is None:
            self.create_head(new_node)
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
    
