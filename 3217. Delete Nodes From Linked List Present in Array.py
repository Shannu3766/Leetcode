# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        point_1=head
        nums=list(set(nums))
        max_val=max(nums)
        num_pos=[False]*(max(nums)+1)
        for i in nums:
            num_pos[i]=True
        print(nums)
        while point_1.next is not None:
            if point_1.next.val<max_val+1 and num_pos[point_1.next.val]==True:
                point_1.next=point_1.next.next
            else:
                point_1=point_1.next
        if head.val<max_val+1 and num_pos[head.val]:
            head=head.next
        return head