class Solution:
    def romanToInt(self, s: str) -> int:
        ao = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        count = 0
        last_value = 0
        for item in range(len(s)):
            if item == 0:
                count += ao[s[item]]
                last_value = ao[s[item]]
            else:
                if last_value < ao[s[item]]:
                    count += ao[s[item]] - 2 * last_value
                else:
                    count += ao[s[item]]
                    last_value = ao[s[item]]
                if item == len(s) - 1:
                    last_value = 0
        print(count)
        return count
