
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


class Solution:
    def reverseList(self, head):
        # Code here

        prev=None
        curr=head
        while curr is not None:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
            
        # i=head    
        # while i.next!=None:
        #     if i.next!=None:
        #         print(f"{i.data}->",end="")
        #     else:
        #         print(i.data,end="")
        head = prev
        return head
    
    def printlist(self,node):
        
        while node is not None:
            print(f"{node.data}",end="")
            if node.next is not None:
                print(" -> ",end="")
            node=node.next
        print()