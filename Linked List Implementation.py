class Node():
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList():
    def __init__(self, head):
        self.head = head
        self.tail = None

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


    def lookup(self, index):
        temp = self.head
        i = 0

        while index != i:
            temp = temp.next
            i += 1
        
        return temp.data if temp else None


    def append(self, data):
        temp = self.head
        
        if not temp.next:
            self.tail = temp

        new_node = Node(data)
        self.tail.next = new_node
        self.tail = self.tail.next
        
        return self.tail.data


    def insert_head(self, data):
        new_node = Node(data)

        temp = self.head
        new_node.next = temp
        self.head = new_node

        return self.head.data

    
    def insert(self, index, data):
        new_node = Node(data)
        pre = self.head

        for i in range(index - 1):
            pre = pre.next
        
        after = pre.next
        pre.next = new_node
        new_node.next = after

    def pop(self):
        pre = self.head
        temp = self.head.next

        while temp.next:
            temp = temp.next
            pre = pre.next

        pre.next = None
        self.tail = pre
        del temp




head = Node(0)
# node1 = Node(1)
# node2 = Node(2)
# node3 = Node(3)

# head.next = node1
# node1.next = node2
# node2.next = node3

my_linked_list = LinkedList(head)
print(my_linked_list.append(1))
print(my_linked_list.append(2))
print(my_linked_list.append(3))

print(my_linked_list.insert_head(10))
print(my_linked_list.insert(2, 9))

print(my_linked_list.count_nodes())
print(my_linked_list.show_nodes())

print(my_linked_list.pop())
print(my_linked_list.show_nodes())

print(my_linked_list.append(4))
print(my_linked_list.show_nodes())

print(my_linked_list.lookup(6))

# print(my_linked_list.insert(4))
# print(my_linked_list.show_nodes())
        