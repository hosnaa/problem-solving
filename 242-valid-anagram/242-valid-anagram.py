class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list_s = list(s)
        for j in t:
            if j not in list_s:
                return False
            # _ = list_s.pop(list_s.index(j)) # what's difference between pop() and remove()
            list_s.remove(j)

        if list_s:
            return False
        return True
        