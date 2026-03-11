# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head , k, lvl):
        if lvl==0 or not head:
            return head
        curr = head
        prev = None
        cnt =0
        while cnt<k and curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            cnt +=1
 
        head.next = self.reverse(curr,k,lvl-1)

        return prev


    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp = head
        cnt = 0
        while temp:
            temp = temp.next
            cnt +=1
        lvl = cnt // k
        return self.reverse(head, k,lvl)
