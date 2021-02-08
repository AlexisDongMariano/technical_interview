class Node():
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList():
    def __init__(self, head):
        self.head = head

    def count_nodes(self):
        count = 0
        temp = self.head

        if not temp:
            return None
        
        while temp:
            count += 1
            temp = temp.next
        
        return count

    def show_nodes(self):
        nodes = []

        temp = self.head

        while temp:
            nodes.append(temp.data)
            temp = temp.next
        
        return nodes

    def insert(self, data, index=0):
        new = Node(data)

        temp = self.head
        new.next = temp
        self.head = new




head = Node(0)
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

head.next = node1
node1.next = node2
node2.next = node3

my_linked_list = LinkedList(head)

print(my_linked_list.count_nodes())
print(my_linked_list.show_nodes())

print(my_linked_list.insert(4))
print(my_linked_list.show_nodes())
        