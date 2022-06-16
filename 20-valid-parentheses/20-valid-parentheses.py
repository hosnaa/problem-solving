class Solution:
    def isValid(self, s: str) -> bool:
        
#         char_map = {'(':')', '[':']', '{':'}'}
#         closure = []
#         i = 0
#         if len(s) == 1: return False
#         while(i < len(s)):
#             ## get the appropriate closure for the opening parant
                        
#             if s[i] in char_map.keys():
#                 fit = char_map[s[i]]
#                 try: 
#                     if s[i+1] == fit:
#                         i = i+2
#                     else:
#                         closure.append(char_map[s[i]])
#                         i = i+1
#                 except:
#                     return False
#             else:
#                 if s[i] == closure[-1]:
#                     print(s[i], closure[-1])
#                     closure.pop(-1)
#                     i = i+1
#                 else: 
#                     return False            
        
#         return True
        lookup_parent = {'(':')', '[':']', '{':'}'}
        close = []
        for char in s:
            if char in lookup_parent: # O(1) => hash
                close.append(lookup_parent[char])
            else: 
                if len(close) and char == close[-1]: # you won't proceed here unless length > 
                    close.pop(-1)
                else:
                    return False
        return True if close == [] else False
            
        