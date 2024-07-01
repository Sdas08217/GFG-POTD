# Make Binary Tree From Linked List
def convert(head):
    arr = []
    while head:
        arr.append(head.data)
        head = head.next
    
    def fun(arr, i):
        if i >= len(arr):
            return None
        
        root = Tree(arr[i])
        root.left = fun(arr, 2 * i + 1)
        root.right = fun(arr, 2 * i + 2)
        
        return root
    
    return fun(arr, 0)

# Example usage:
input_list = [1, 2, 3, 4, 5]
linked_list_head = create_linked_list(input_list)
root = convert(linked_list_head)
output = level_order_traversal(root)
print(output)  # Output: [1, 2, 3, 4, 5]
