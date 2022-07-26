def contains_cycle(first_node):
    # Start both pointers at beginning
    slow_point = first_node
    fast_point = first_node

    # Increment pointers until end of list
    while slow_point.next is not None and fast_point.next is not None:
        slow_point = slow_point.next
        fast_point = fast_point.next.next

        # if pointers meet
        if fast_point is slow_point:
            return True

    return False
