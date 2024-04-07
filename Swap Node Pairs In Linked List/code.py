def swap_pairs(head):
    if head is None or head.next is None:
        return head

    lst = head.next.next
    new_head = head.next
    new_head.next = head
    head.next = swap_pairs(lst)
    return new_head
