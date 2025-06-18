class Solution(object):
    
    def countAndSay(self,n):
        result = "1"
        for _ in range(n - 1):
            prev = result
            result = ""
            count = 1
            for i in range(1, len(prev)):
                if prev[i] == prev[i - 1]:
                    count += 1
                else:
                    result += str(count) + prev[i - 1]
                    count = 1
            result += str(count) + prev[-1]
        return result
