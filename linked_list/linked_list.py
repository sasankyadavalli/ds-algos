class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at Tail
    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next

            cur.next = Node(data)

    # Insert at Head
    def insert_at_head(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        else:
            cur = self.head
            self.head = Node(data)
            self.head.next = cur

    # Insert at any index
    # Need to improvise the solution
    def insert_at(self, data, index):
        new_node = Node(data)
        cur = self.head
        prev = None
        count = 1
        while cur is not None:
            # Insert at head
            if index == 1:
                cur = self.head
                self.head = new_node
                self.head.next = cur
                return

            if count == index:
                prev.next = new_node
                new_node.next = cur
                return

            prev = cur
            cur = cur.next
            count += 1

        if index == count:
            prev.next = new_node

        else:
            print("Out of bound error")

    # Delete Node
    def delete_node(self, data):
        cur = self.head
        prev = None
        if cur is None:
            print("List is empty")
        elif data == cur.data:
            self.head = cur.next
        else:
            while cur is not None:
                if data == cur.data:
                    prev.next = cur.next

                prev = cur
                cur = cur.next

    # Reverse the List
    def reverse(self):
        cur = self.head
        prev = None
        while cur is not None:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        self.head = prev


    # Length of linked list
    def length_list(self):
        cur = self.head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next

        print("The length of the linked list is {}".format(count))

    # Traversing the linked list and printing
    def print_nodes(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next


llist = LinkedList()
llist.append(5)
llist.append(6)
llist.append(7)
llist.append(8)
llist.append(9)
llist.insert_at(4,6)
#llist.insert_at_head(0)
llist.insert_at(3, 5)
# llist.insert_at(1,1)
# llist.insert_at(11,6)
llist.insert_at(12, 7)
#llist.insert_at(12,23)
# llist.length_list()
llist.delete_node(9)
llist.delete_node(5)
llist.print_nodes()
print("==============================================")
llist.reverse()
llist.print_nodes()
