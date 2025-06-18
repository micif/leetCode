class Solution(object):
    
    def map_to_pairs(self, s):
        pairs = []
        count = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
            else:
                pairs.append([int(s[i - 1]), count])
                count = 1
        pairs.append([int(s[-1]), count])
        return pairs

    def pairs_to_string(self, pairs):
        result = ""
        for digit, count in pairs:
            result += str(count) + str(digit)
        return result

    def countAndSay(self, n):
        result = "1"
        for _ in range(n - 1):
            pairs = self.map_to_pairs(result)      # כאן השתנה
            result = self.pairs_to_string(pairs)   # כאן השתנה
        return result
