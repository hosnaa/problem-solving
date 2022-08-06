class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag = [m for m in magazine]
        for i in ransomNote:
            if i in mag:
                mag.pop(mag.index(i))
            else:
                return False
        return True
