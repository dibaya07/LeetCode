class Solution:
    def reverseString(self, s: list[str]) -> None:
        string_len=len(s)
        for idx in range(len(s)):
            value = s[string_len - idx - 2]
            s.pop(string_len - idx - 2)
            s.append(value)
        