class Solution:
    def romanToInt(self, s: str) -> int:
        roman_num = {'I':1, 'V':5, 'X': 10, 'L':50, 'C':100, 'D':500, 'M':1000}
        ##### This is while using a flag to skip #####
        # roman_int = 0
        # skip_next = False
        # for i in range(len(s)):
        #     if skip_next == False:
        #         if i != len(s)-1 and roman_num[s[i]] < roman_num[s[i+1]]:
        #             roman_int += roman_num[s[i+1]] - roman_num[s[i]]
        #             skip_next = True
        #         else:
        #             roman_int += roman_num[s[i]]
        #             skip_next = False
        #     else:
        #         skip_next = False
        #         continue
        # return roman_int
    
        ##### This concerns with the effect that will happen on the current number ######
        roman_int = 0
        for i in range(len(s)):
            if i != len(s)-1 and roman_num[s[i]] < roman_num[s[i+1]]:
                roman_int += -roman_num[s[i]]
            else: 
                roman_int += roman_num[s[i]]
        return roman_int
                