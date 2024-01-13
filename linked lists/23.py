class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        return self.sort(lists, 0, len(lists))
        
    def merge(self, l1, l2):
        if not l1 or not l2:
            return l1 or l2
        if l1.val < l2.val:
            l1.next = self.merge(l1.next, l2)
            return l1
        else:
            l2.next = self.merge(l1, l2.next)
            return l2
    
    def sort(self, lists, i, j):
        if i >= j:
            return None
        if i + 1 == j:
            return lists[i]
        mid = (i + j) // 2
        l = self.sort(lists, i, mid)
        r = self.sort(lists, mid, j)
        return self.merge(l, r)