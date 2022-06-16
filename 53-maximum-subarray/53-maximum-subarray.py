class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        acc_sum = 0
        for i in range(len(nums)):
            acc_sum += nums[i]
            max_sum = max(max_sum, acc_sum)
            
            ## This abolishes the effect of the previous -ve; as if we skip these values
            ## and traverse starting from these positive
            ## For if the accumlated sum reached -ve then no need for all the values that caused this 
            ## However for the 3rd test case, even if the value is -ve
            ## The accumlated sum isn't that's why this works
            
            ## As no need for -ve accumlation we make it 0 which denotes neglecting traversing these previous values causing -ve and start traversing from the next
            if acc_sum < 0: acc_sum = 0
        return max_sum

## (1) No need to keep all, compare as you go and keep max only 
## (2) If total is -ve then it will impede my way, I can neglect them and traverse (start) from next by making their effect as 0