class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
#         x = []
#         for i in nums1[:m]:
#             for j in nums2:
#                 if j < i:
#                     x.append(j)
#                 else:
#                     x.append(i)
#         nums1 = x

        # Two pointers; one static (smaller) and another dynamic (bigger)
        
        # last element from arr1 > last from arr2
        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]: 
                nums1[m+n-1] = nums1[m-1] # put the biggest number in the last index
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]
        
        