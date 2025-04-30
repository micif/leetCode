class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        
        res = len(strs[0])  
        for word in strs[1:]:
            count = 0
            for i in range(min(len(word), len(strs[0]))):
                if word[i] == strs[0][i]:
                    count += 1
                else:
                    break
            res = min(res, count)
            if res == 0:
                return ""
        
        return strs[0][:res]
  


        