class Solution:
    
    #Function to rotate a linked list.
    def rotate(self, head, k):
        # code here
        if k == 0:
            return head
        curr = head
        l = 1
        while curr.next is not None:
            curr = curr.next
            l += 1
        k %= l
        if k == 0:
            return head
        curr.next = head
        curr = head
        for _ in range(1, k):
            curr = curr.next
        head = curr.next
        curr.next = None
        return head
