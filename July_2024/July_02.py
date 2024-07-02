# Linked list of strings forms a palindrome
def compute(head): 
    str1 = []
    while head is not None:
        str1.append(head.data)
        head = head.next
    
    str2 = ""
    for i in str1:
        str2 += i
    if str2 == str2[::-1]:
        return True
    return False

# Example usage
if __name__ == "__main__":
    # Creating a linked list: a -> b -> c -> b -> a
    node1 = Node('a')
    node2 = Node('b')
    node3 = Node('c')
    node4 = Node('b')
    node5 = Node('a')
    
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    # Check if the linked list forms a palindrome
    print(compute(node1))  # Output: True
