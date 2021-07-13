# Reversing a linked list Recursive and Iterative

# Iterative O(N) time


def reverseList(self, head):
    if(head == None):
        return head
    else:
        dummy = None
        while(head != None):
            next = head.next
            head.next = dummy
            dummy = head
            head = next
        return dummy


# recursive O(N) Time
def reverseList(self, head):
    # recursive
    if(head == None or head.next == None):
        return head
    newhead = self.reverseList(head.next)
    head.next.next = head
    head.next = None
    return newhead
