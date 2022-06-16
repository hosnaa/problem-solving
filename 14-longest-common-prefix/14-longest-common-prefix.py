class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''
        shortest = min(strs, key=len)
        print(shortest)
        # remain_strs = strs - shortest
        for i, char in enumerate(shortest):
            for other in strs:
                if other[i] == char:
                    flag = True
                else:
                    return prefix
            if flag == True:
                prefix += char
                  # if other[i] != char: # by default for the other condition it passes
                  #    return shortest[:i]

        return prefix
                    
        