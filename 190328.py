# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def hasCycle(head):
    """
    :type head: ListNode
    :rtype: bool
    """
    lencycle=0
    isitend=False
    temp=head
    items=[]
    while not isitend:
        if temp == None: return False
        lencycle+=1
        items.append(temp.val)
        if lencycle!=len(items):
            isitend=True
        else: temp=temp.next
    flag=items.index(temp.val)
    temp=temp.next
    flag+=1
    while temp:
        if items[flag]!=temp.val:
            return False
        elif flag==len(items)-1:
            return True
        else:
            flag+=1
            temp=temp.next

    return True

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None or head.next ==None: return False
        slow=ListNode(head)
        fast=ListNode(head.next)
        while slow != fast:
            if fast == None or fast.next == None:
                return False
            slow=slow.next
            fast=fast.next.next

        return False
