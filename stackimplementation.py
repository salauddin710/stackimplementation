from queue import Empty
class linkedStack:
    class Node:
        __slots__ = 'element','next'
        def __init__(self,element, next):
            self.element = element
            self.next = next
    def __init__(self):
        self.head = None
        self.size = 0
    def __len__(self):
        return self.size
    def is_empty(self):
        return self.size == 0
    def push(self, e):
        self.head = self.Node(e, self.head)
        self.size = self.size + 1
        return self.head.element
    def pop(self):
        if self.is_empty():
            raise Empty('stack is empty')
        value = self.head.element
        self.head = self.head.next
        self.size = self.size - 1
        return value
    def top(self):
        if self.is_empty():
            raise Empty("stack is EEEmpty")
        return self.head.element
    def diplay(self):
        tm = self.head
        while tm:
            print(tm.element, end="===>")
            tm = tm.next
        print()


ls = linkedStack()
ls.push(10)
ls.push(20)
ls.push(50)
ls.push(40)
ls.push(80)
ls.diplay()
print("poped : ", ls.pop())
ls.diplay()
print("pushed : ", ls.push(90))
ls.diplay()
print("top : ", ls.top())
print("pooped : ", ls.pop())
ls.diplay()