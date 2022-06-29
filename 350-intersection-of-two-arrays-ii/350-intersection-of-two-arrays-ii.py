class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersect = []
    
        """
        Sort + Pointers solution (sort then move pointers according to whether it's smaller or what)
        """
        intersect = []
        # nums1, nums2 = sorted(nums1), sorted(nums2)
        # i = j = 0 # i and j are pointers

        # while True:
        #     try:
        #         if nums1[i] < nums2[j]:
        #             i += 1
        #         elif nums2[j] < nums1[i]:
        #             j += 1
        #         else:
        #             intersect.append(nums1[i])
        #             i += 1
        #             j += 1
        #     except (IndexError): 
        #         break
        # print(intersect)

        """
        Counter (then check the element and take the smallest count)
        """

        c1, c2 = Counter(nums1), Counter(nums2) # Counter => return dictionary-like obj for number and its count
        for num in c1:
            if num in c2:
                intersect.extend([num]*min(c1[num], c2[num]))

        return intersect
                
            
                    
        