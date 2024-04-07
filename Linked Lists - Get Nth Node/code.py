def get_nth(node, index):
    for _ in range(index):
        if isinstance(node, Node):
            node = node.next
        else:
            raise AttributeError
    if index > -1 and node:
        return node
    else:
        raise AttributeError
