from ArrayStack import ArrayStack

class LinkedStack:

    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._size = 0
        self._data = []

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, e):
        self._head = self._Node(e, self._head)
        self._data.append(self._head)
        self._size += 1

    def top(self):
        if self.is_empty():
            return "Stack is empty"
        else:
            return self._head._element

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        else:
            answer =  self._head._element
            self._head = self._head._next
            self._size -= 1
            self._data.remove(answer)
            return answer

    def __str__(self):
        if self.is_empty():
            return "Stack is empty"
        else:
            return str(self._data)

    def sortMerge(self, list1, list2):
        sort = ArrayStack()
        first = list1._head
        second = list2._head

        while first != None and second != None:

            while first._element <= second._element:
                sort.push(first._element)
                first._next = first

            while second._element <= first.element:
                sort.push(second._element)
                second._next = second

        while first != None:
            sort.push(first._element)
            first._next = first

        while second != None:
            sort.push(second._element)
            second._next = second

        sortedLinked = LinkedStack()
        for i in sort:
            sortedLinked.push(i)

        return sortedLinked

x = LinkedStack()
y = LinkedStack()
for i in range(5):
    x.push(i)
print x
