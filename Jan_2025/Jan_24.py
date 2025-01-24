class Solution:
    # Function to check if the linked list has a loop.
    def detectLoop(self, head):
        # Initialize two pointers, slow and fast
        slow = head
        fast = head

        # Traverse the linked list
        while fast is not None and fast.next is not None:
            slow = slow.next          # Move slow by one step
            fast = fast.next.next     # Move fast by two steps

            if slow == fast:          # If slow meets fast, there's a loop
                return True

        return False                  # If fast reaches the end, no loop
