def stringify(node):
    """
    Convert linked list to string
    """
    l = []
    while node:
        l.append(str(node.data))
        node = node.next
    return " -> ".join(l + ["None"])
