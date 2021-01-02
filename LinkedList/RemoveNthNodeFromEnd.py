# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head, n: int): (head is of type ListNode and return type is also of type ListNode)

        # Two pass solution
        curr = head
        count = 0
        while curr!=None:
            count+=1
            curr = curr.next
        node = head
        k = count-n
        if count==1 and n==1:
            return None
        count = 0
        prev = None
        while node!=None:
            count+=1
            prev = node
            node = node.next
            if count==k:
                prev.next = node.next
        return head.next if k==0 else head

        #One pass solution
        dummy = ListNode(0)
        dummy.next = head
        node = dummy
        prev = dummy
        for i in range(n+1):
            node = node.next
        while node!=None:
            node = node.next
            prev = prev.next
        prev.next = prev.next.next
        return dummy.next 
            
                