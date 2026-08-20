class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class singly_linked_list:
    def __init__(self):
        self.head = None

    def create_singly_linked_list(self, mas):
        for i in range(len(mas)):
            new_node = node(mas[i])
            if self.head == None:
                self.head = new_node
                last = self.head
            else:
                last.next = new_node
                last = last.next
        return

    def search_max(self):
        last = self.head
        temp_max = -1
        index_max = -1
        counter = 0
        while last.next != None:
            if last.data >= temp_max:
                index_max = counter
                temp_max = last.data
            counter += 1
            last = last.next
        if last.data >= temp_max:
            index_max = counter
        return index_max

    def create_list(self, index_max):
        last = self.head
        counter = 0
        result_list = []
        while last.next != None:
            if counter != index_max:
                result_list.append(last.data)
            counter +=1
            last = last.next
        if counter != index_max:
            result_list.append(last.data)
        print(*result_list)
        return

n = int(input())
start_list = list(map(int, input().split()))
ll = singly_linked_list()
ll.create_singly_linked_list(start_list)
index_max = ll.search_max()
ll.create_list(index_max)
