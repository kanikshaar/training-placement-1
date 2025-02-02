# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):

        length = self.dl(head)

        if length == n:
            return head.next
        index_to_remove = length - n
        self.deep(head, 1, index_to_remove)
        
        return head
    
    def deep(self, root, count, index_to_remove):
        if count == index_to_remove:
            root.next = root.next.next
            return
        self.deep(root.next, count + 1, index_to_remove)
    
    def dl(self, root):
        if not root:
            return 0
        return 1 + self.dl(root.next)
