def loop_size(node):
    slow = node
    fast = node

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            slow = node

            while fast != slow:
                slow = slow.next
                fast = fast.next

            counter = 1
            fast = fast.next

            while fast != slow:
                fast = fast.next
                counter += 1
            return counter
