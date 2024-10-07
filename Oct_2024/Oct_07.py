# XOR Linked List
def insert(head, data):
    node = Node(data)
    if head == None: head = node
    else:
        node.npx = head
        head = node
    return head
    
def getList(head):
    lis = []
    while head:
        lis.append(head.data)
        head = head.npx
    return lis

# Example usage
head = None
head = insert(head, 10)
head = insert(head, 20)
head = insert(head, 30)

print(getList(head))  # Output: [30, 20, 10]
