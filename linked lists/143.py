class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head: return []

        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        prev, current = None, slow.next
        while current:
            tempNext = current.next
            current.next = prev
            prev = current
            current = tempNext    
        slow.next = None
        
        head1, head2 = head, prev
        while head2:
            tempNext = head1.next
            head1.next = head2
            head1 = head2
            head2 = tempNext