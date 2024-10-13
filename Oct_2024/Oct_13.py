# Delete Alternate Nodes
class Solution:
    def deleteAlt(self, cur):
        while cur and cur.next:
            cur.next = cur.next.next
            cur = cur.next
        return cur

  # Example usage of deleteAlt
if __name__ == "__main__":
    # Create a linked list 1 -> 2 -> 3 -> 4 -> 5 -> None
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    # Print the original list
    print("Original list:")
    head.printList()

    # Create Solution object and delete alternate nodes
    solution = Solution()
    solution.deleteAlt(head)

    # Print the modified list
    print("Modified list after deleting alternate nodes:")
    head.printList()
