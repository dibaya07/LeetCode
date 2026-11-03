class Solution:
    def isPalindrome(self, s: str) -> bool:
        ignorables= string.punctuation
        value = s.translate(str.maketrans("","",ignorables+" ")).lower()
        value2 = value[::-1]
        for i in range(len(value)):
            if value[i] == value2[i]:
                pass
            else:
                return False
        return True