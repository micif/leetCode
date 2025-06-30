class Solution(object):
    def divideString(self, s, k, fill):
        result=[]
        str=""
        for a in s:
            if(len(str)<k):
                str+=a
            else:
                result.append(str)
                str=a
        while(len(str)<k):
            str+=fill
        result.append(str)
        return result
            
        