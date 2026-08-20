class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class singly_linked_list:
    def __init__(self):
        self.head = None

    def add_by_index(self, index, data):
        new_node = node(data)
        if self.head == None:
            self.head = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            last = self.head
            counter = 0
            while counter != index - 1:
                last = last.next
                counter += 1
            new_node.next = last.next
            last.next = new_node

    def print_node(self, index):
        last = self.head
        counter = 1
        while counter != index:
            last = last.next
            counter += 1
        print(last.data)

    def delete_by_index(self, index):
        if index == 1:
            self.head = self.head.next
        else:
            last = self.head
            counter = 1
            while counter != index - 1:
                last = last.next
                counter += 1
            last.next = last.next.next

ll = singly_linked_list()
q = int(input())
for i in range(q):
    input_p = list(map(int, input().split()))
    if input_p[0] == 1:
        ll.add_by_index(input_p[1], input_p[2])
    elif input_p[0] == 2:
        ll.print_node(input_p[1])
    else:
        ll.delete_by_index(input_p[1])
