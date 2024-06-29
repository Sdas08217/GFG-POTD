# Identical Linked Lists
def areIdentical(head1, head2):
    
    trav1 = head1
    trav2 = head2
    
    flag = 0
    while(trav1 != None and trav2 != None):
        
        if(trav1.data != trav2.data):
            flag = 1
            break
        else:
            trav1 = trav1.next
            trav2 = trav2.next
        
    if flag == 1 or trav1!= None or trav2 != None:
        return False
    else:
        return True
