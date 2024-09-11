# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        poit=head
        # print(poit.val)
        while poit.next!=None:
            new_node=ListNode()
            new_node.val=gcd(poit.val,poit.next.val)
            new_node.next=poit.next
            poit.next=new_node
            poit=poit.next.next
        return head
        