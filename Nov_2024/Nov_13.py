# Intersection Point in Y Shaped Linked Lists.
def intersetPoint(head1, head2):
    # Initialize two pointers to start of both lists
    ptr1 = head1
    ptr2 = head2
    # Traverse until they meet or both reach the end (None)
    while ptr1 != ptr2:
        # Move to the next node in the list, or switch to the other list's head
        ptr1 = ptr1.next if ptr1 else head2
        ptr2 = ptr2.next if ptr2 else head1
    # Either they meet at the intersection or at None (no intersection)
    return ptr1.data if ptr1 else -1

