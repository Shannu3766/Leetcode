# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        point_1=head
        if point_1 is None or point_1.next is None:
            return head
        point_2=head.next
        while True:
            # print(point_1.val,point_2.val)
            if point_2 is not None:
                point_1.val,point_2.val=point_2.val,point_1.val
                point_1=point_2.next
            else:
                break
            if point_1 is not None:
                point_2=point_1.next
            else:
                break
        return head
        