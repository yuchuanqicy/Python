class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        if part not in s:
            return  s
        index=s.index(part)
        removed_string = s[:index] + s[(index + len(part)):]
        return self.removeOccurrences(removed_string,part)
s=Solution()
ss=s.removeOccurrences("daabcbaabcbc","abc")
print(ss)