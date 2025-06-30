class Solution(object):
    def divideString(self, s, k, fill):
        result = []
        current = []

        for char in s:
            current.append(char)
            if len(current) == k:
                result.append("".join(current))
                current = []

        if current:
            current += [fill] * (k - len(current))
            result.append("".join(current))

        return result
