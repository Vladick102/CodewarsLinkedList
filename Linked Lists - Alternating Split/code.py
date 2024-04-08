class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def append(self, val):
        n = Node(val)
        head = self
        while head:
            if head.data is None:
                head.data = val
                break
            if head.next is None:
                head.next = n
                break
            head = head.next


class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second


def alternating_split(head):
    if head.data is None:
        return None
    if head.next.data is None or head.next.next is None:
        return Context(Node(head.data), Node(head.next.data))
    temp = head
    head1 = Node()
    head2 = Node()
    count = 0
    while temp:
        if count % 2 == 0:
            head1.append(temp.data)
        else:
            head2.append(temp.data)
        temp = temp.next
        count += 1
    return Context(head1, head2)
