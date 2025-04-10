# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        h1 = ListNode()
        p = h1
        while list1 and list2:
            if list1.val <= list2.val:
                h1.next = ListNode(list1.val)
                list1 = list1.next
            else:
                h1.next = ListNode(list2.val)
                list2 = list2.next
            h1 = h1.next
        while list1:
            h1.next = ListNode(list1.val)
            h1 = h1.next
            list1 = list1.next
        while list2:
            h1.next = ListNode(list2.val)
            h1 = h1.next
            list2 = list2.next
        return p.next