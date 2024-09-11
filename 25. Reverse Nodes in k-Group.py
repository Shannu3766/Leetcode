# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        point_1=head
        i=1
        lis_1=[]
        final=point_1
        lis=[]
        while point_1 is not None:
            lis.append(point_1.val)
            if i%k==0:
                lis_1=lis_1+lis[::-1]
                lis=[]
            point_1=point_1.next
            i+=1
        lis_1=lis_1+lis
        point_1=head
        for i in lis_1:
            point_1.val=i
            point_1=point_1.next
        # print(lis_1+lis)
        return head
        