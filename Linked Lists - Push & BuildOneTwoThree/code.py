def push(head, data):
    n = Node(data)
    n.next = head
    return n


def build_one_two_three():
    return push(push(push(None, 3), 2), 1)
