class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest


def move_node(source, dest):
    node = source.data
    source = source.next
    res = Node(node)
    res.next = dest
    return Context(source, res)
