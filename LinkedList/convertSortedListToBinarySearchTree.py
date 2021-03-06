# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def findMid(head):
            slow = head
            fast = head
            prev = None
            while fast!=None and fast.next!=None:
                prev = slow
                slow = slow.next
                fast = fast.next.next
            if prev: 
                prev.next = None
            return slow
        
        if not head:
            return None
        
        mid = findMid(head)
        node = TreeNode(mid.val)
        
        if head==mid:
            return node
        
        node.left = self.sortedListToBST(head)
        node.right = self.sortedListToBST(mid.next)
        return node