class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        letter_count = {}

        for char in magazine:
            letter_count[char] = letter_count.get(char, 0) + 1

        for char in ransomNote:
            if char not in letter_count or letter_count[char] == 0:
                return False
            letter_count[char] -= 1

        return True
