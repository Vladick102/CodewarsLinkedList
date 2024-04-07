def sorted_insert(head, data):

    head1 = head
    node = Node(data)

    if head is None:
        return node

    if head.data > data:
        node.next = head
        return node

    while True:
        if head.next is None or head.next.data > data:
            node.next = head.next
            head.next = node
            return head1

        head = head.next
