class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def remove_duplicates(head):
    if not head:
        return None
    if head.next is None:
        return head
    head1 = head
    while head:
        if not head.next:
            break
        if head.next.data == head.data:
            head.next = head.next.next
        else:
            head = head.next
    return head1
