class Solution:
    def addTwoLists(self, num1, num2):
        # code here
        prev1 = None
        cur = num2
        while cur.data == 0:
            cur = cur.next
            if cur == None:
                break
        while cur != None:
            temp = cur.next
            cur.next = prev1
            prev1 = cur
            cur = temp
        prev2 = None
        cur = num1
        while cur.data == 0:
            cur = cur.next
            if cur == None:
                break
        while cur != None:
            temp = cur.next
            cur.next = prev2
            prev2 = cur
            cur = temp
        res = Node(-1)
        cur = res
        carry = 0
        while carry or prev1 or prev2:
            
            n1 = prev1.data if prev1 is not None else 0
            n2 = prev2.data if prev2 is not None else 0
            m_sum = carry + n1 + n2
            
            
            carry = m_sum//10
                
            cur.next = Node(m_sum%10)
            cur = cur.next
            prev1 = None if prev1 is None else prev1.next
            prev2 = None if prev2 is None else prev2.next
            
         
        res = res.next
        
        prev = None
        cur = res 
        while cur != None:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        if prev == None:
            return Node(0)
        return prev 
