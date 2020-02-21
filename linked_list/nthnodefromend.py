class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def nthnodefromend(self, position):
        mydict = {}
        count = 1
        if self.head is None:
            print("List is empty")
        else:
            cur = self.head
            while cur is not None:
                mydict[count] = cur.data
                cur = cur.next
                count = count + 1

            desired_node = count - position
            print(mydict[desired_node])

    # Using two pointer technique
    def nthnode(self, position):
        slow = self.head
        fast = self.head
        count = 0
        while count < position:
            fast = fast.next
            count = count + 1

        print(fast.data)
        while fast is not None:
            slow = slow.next
            fast = fast.next

        print(slow.data)

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next

            cur.next = Node(data)


llist = LinkedList()
llist.append(5)
llist.append(6)
llist.append(7)
llist.append(8)
llist.append(9)
llist.nthnodefromend(2)
llist.nthnode(2)