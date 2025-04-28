import re

class Solution(object):
    def clean_string(self, input_string):
        # הופכים את המחרוזת לאותיות קטנות ומסירים כל תו שאינו אות
        return re.sub(r'[^a-z0-9]', '', input_string.lower())

    def isPalindrome(self, s):
        # קריאה לפונקציה clean_string
        cleaned_str = self.clean_string(s)
        
        # בדיקה אם המחרוזת היא פלאנדום
        for l, r in zip(cleaned_str, reversed(cleaned_str)):
            if l != r:
                return False
        return True
