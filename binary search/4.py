class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1 = len(nums1)
        len2 = len(nums2)
        
        if len1 > len2:
            return self.findMedianSortedArrays(nums2, nums1)
        
        n = len1 + len2
        left = (len1 + len2 + 1) // 2
        low = 0
        high = len1
        
        while low <= high:
            mid1 = (low + high) // 2
            mid2 = left - mid1
            
            left1 = float('-inf')
            left2 = float('-inf')
            right1 = float('inf')
            right2 = float('inf')
            
            if mid1 < len1:
                right1 = nums1[mid1]
            if mid2 < len2:
                right2 = nums2[mid2]
            if mid1 - 1 >= 0:
                left1 = nums1[mid1 - 1]
            if mid2 - 1 >= 0:
                left2 = nums2[mid2 - 1]
            
            if left1 <= right2 and left2 <= right1:
                if n % 2 == 1:
                    return max(left1, left2)
                else:
                    return (max(left1, left2) + min(right1, right2)) / 2.0
            elif left1 > right2:
                high = mid1 - 1
            else:
                low = mid1 + 1
        
        return 0