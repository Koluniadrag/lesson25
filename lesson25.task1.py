class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.next = None

    def get_data(self):
        return self.data

    def set_data(self, new_data):
        self.data = new_data

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next


class UnorderedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()
        return count

    def search(self, item):
        current = self.head
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if found:
            if previous is None:
                self.head = current.get_next()
            else:
                previous.set_next(current.get_next())
        else:
            raise ValueError('Item not in list')

    def append(self, item):
        current = self.head
        if current is None:
            self.head = Node(item)
        else:
            while current.get_next() is not None:
                current = current.get_next()
            current.set_next(Node(item))

    def index(self, item):
        current = self.head
        index = 0
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
                index += 1
        if not found:
            raise ValueError('Item not in list')
        return index

    def pop(self, pos=None):
        if pos is None:
            pos = self.size() - 1

        if pos < 0 or pos >= self.size():
            raise IndexError('list index out of range')

        current = self.head
        previous = None
        index = 0
        while index != pos:
            previous = current
            current = current.get_next()
            index += 1

        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

        return current.get_data()

    def insert(self, pos, item):
        if pos < 0 or pos > self.size():
            raise IndexError('list index out of range')

        current = self.head
        previous = None
        index = 0
        while index != pos:
            previous = current
            current = current.get_next()
            index += 1

        temp = Node(item)
        temp.set_next(current)
        if previous is None:
            self.head = temp
        else:
            previous.set_next(temp)

    def slice(self, start, stop):
        if start < 0 or start >= self.size() or stop < 0 or stop > self.size() or start >= stop:
            raise ValueError('Invalid slice parameters')

        current = self.head


