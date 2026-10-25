# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def revNode(prev, curr):
            if curr == None:
                return prev
            nxt = curr.next
            curr.next = prev
            return revNode(curr, nxt)
            
        return revNode(None,head)