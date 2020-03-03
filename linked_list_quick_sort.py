class LinkedListNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
    def update(self, new_node):
        self.next = new_node
        return new_node

        
def ll_sort(start, end):
    if start is end:
        return start, end
    start, prev_target, target, end = ll_partition(start, end)
    if start is not target:
        new_start_1, new_end_1 = ll_sort(start, prev_target)
    else:
        new_start_1 = start
    if target.next is not None:
        new_start_2, new_end_2 = ll_sort(target.next, end)
        target.next = new_start_2
    else:
        new_end_2 = target
    return new_start_1, new_end_2


def ll_partition(start, end):
    original_next = end.next
    end.next = None
    target = start
    i = start.next
    target.next = None
    small = small_head = LinkedListNode("NOT_USED")
    large = large_head = LinkedListNode("NOT_USED")
    while i is not None:
        real_next = i.next
        i.next = None
        if i.data <= target.data:
            small = small.update(i)
        else:
            large = large.update(i)
        if i is end:
            break
        i = real_next
    small.next = target
    target.next = large_head.next
    if target.next is not None:
        large.next = original_next
        return small_head.next, small, target, large
    else:
        target.next = original_next
        return small_head.next, small, target, target.next
