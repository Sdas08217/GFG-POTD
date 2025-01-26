class Solution:
    # Function to remove a loop in the linked list.
    def removeLoop(self, head):
        # Detect if there's a loop using Floyd's Cycle Detection Algorithm.
        def detectCycle(head):
            slow, fast = head, head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
                if slow == fast:
                    return slow
            return None
        # Find the starting node of the loop.
        def findLoopStart(head, meeting_point):
            ptr1, ptr2 = head, meeting_point
            while ptr1 != ptr2:
                ptr1 = ptr1.next
                ptr2 = ptr2.next
            return ptr1
        # Remove the loop from the linked list.
        def breakLoop(loop_start):
            temp = loop_start
            while temp.next != loop_start:
                temp = temp.next
            temp.next = None  # Break the loop.
        # Main logic
        if not head or not head.next:
            return  # No loop possible in empty or single-node linked list.
        meeting_point = detectCycle(head)
        if meeting_point:
            loop_start = findLoopStart(head, meeting_point)
            breakLoop(loop_start)
        return
