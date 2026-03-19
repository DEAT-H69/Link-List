class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display_table(self, cols):
        current = self.head
        row_data = []
        count = 0
        while current:
            row_data.append(str(current.data))
            count += 1
            if count % cols == 0:  # new row after 'cols' numbers
                print("\t".join(row_data))
                row_data = []
            current = current.next
        if row_data:  # print remaining if any
            print("\t".join(row_data))

# Create linked list
ll = LinkedList()

for i in range(50, 0, -1): 
    ll.append(12 * i)

ll.display_table(12)