class Solution:
    def firstUniqChar(self, s: str) -> int:
        ## This works only as in valid parantheses
        # str_dict = {}
        # # we have to loop over the whole string
        # for i, char in enumerate(s):
        #     if char in str_dict: # for fast look_up make dictionary
        #         char = str_dict.pop(char)
        #     else:
        #         str_dict[char] = i
        # if str_dict:
        #     _, unique = list(str_dict.items())[0]
        #     return unique
        # else:
        #     return -1
        
        str_dict = {}
        for i, char in enumerate(s):
            if char in str_dict: # for fast look_up make dictionary
                # if we just pop; this entails that they have to be even in number as parantheses 
                str_dict[char] = 'repeated' 
            else:
                str_dict[char] = i
        # if str_dict:
        for key, value in list(str_dict.items()):
            if value != 'repeated': # if we use false; 0 is expected as false
                return value
        # else:
        return -1
        