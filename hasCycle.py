#посылка 33698023
def hasCycle(head):
    node_set = []
    while head.next:
        if head in node_set:
            return True
        node_set.append(head)
        head = head.next
    return False


#O(1) память
def hasCycle(head):
    if head.next is None:
        return False
    if head.next.next is None:
        return False
    slow = head.next
    fast = head.next.next
    if slow == head == fast:
        return True
    while fast.next:
        slow = slow.next
        fast = fast.next.next
        if fast is None:
            return False
        if slow == fast:
            return True
    return False
