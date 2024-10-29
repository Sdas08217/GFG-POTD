# Quick Sort on Linked List

def quickSort(head):
    #return head after sorting
    def sort(h, t):
        if not h or h == t or h.next == t:
            return h
            
        v = h.data
        dummy = Node(0)
        dummy.next = h
        
        prev, w = dummy, h
        
        while w != t:
            nw = w.next
            if w.data < v:
                prev.next = w.next
                w.next = dummy.next
                dummy.next = w
            else:
                prev = prev.next
                
            w = nw
        
        h.next = sort(h.next, t)
        return sort(dummy.next, h)
    return sort(head, None)

# Example usage
values = [4, 2, 5, 3, 1]
head = create_linked_list(values)
print("Original list:")
print_linked_list(head)

sorted_head = quickSort(head)
print("Sorted list:")
print_linked_list(sorted_head)
