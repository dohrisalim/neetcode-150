class Solution:
    def countSubstrings(self, s: str) -> int:
        sub = []
        for indi, i in enumerate(s):
            for indj, j in enumerate(s[indi:], start=indi):
                if i == j and s[indi:indj+1] == s[indi:indj+1][::-1]:
                    sub.append(s[indi:indj+1])
        
        return len(sub)