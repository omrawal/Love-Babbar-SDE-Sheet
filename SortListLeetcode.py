# sortLinkedlist leetcode Mergesort
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def merge(self, head1, head2):
        if(head1 is None):
            return head2
        if(head2 is None):
            return head1
        if(head1.val <= head2.val):
            head = head1
            k1 = head1
            p1 = head1.next
            p2 = head2
        elif(head1.val > head2.val):
            head = head2
            k1 = head2
            p1 = head1
            p2 = head2.next

        # p2 = head2
        while(p1 != None and p2 != None):
            if(p1.val <= p2.val):
                k1.next = p1
                k1 = p1
                p1 = p1.next
            else:
                k1.next = p2
                k1 = p2
                p2 = p2.next
        while(p1 != None):
            k1.next = p1
            k1 = p1
            p1 = p1.next
        while(p2 != None):
            k1.next = p2
            k1 = p2
            p2 = p2.next
        return head

    def sortList(self, head: ListNode) -> ListNode:
        if(head is None or head.next is None):
            return head

        slow = head
        fast = head
        while(fast != None and fast.next != None):
            temp = slow
            slow = slow.next
            fast = fast.next.next
        head1 = head
        # splitting the second part by making temp.next to none
        temp.next = None
        head2 = slow
        l1 = self.sortList(head1)
        l2 = self.sortList(head2)
        return self.merge(l1, l2)
