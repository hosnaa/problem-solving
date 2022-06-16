class Solution:
    def isPalindrome(self, x: int) -> bool:
        import math
        x_str = str(x)        
        # for i in range(math.floor(len(x_str)/2)):
        #     if x_str[i] != x_str[-(i+1)]:
        #         return False
        # return True
        if x_str != x_str[::-1]: # start:stop:step => step: -1 means go backward one by one
            return False
        else: return True
        
        
