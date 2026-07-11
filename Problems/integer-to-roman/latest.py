class Solution(object):
    def intToRoman(self, num):
        # Create tuples of decimal values and their corresponding Roman numerals
        roman_tuples = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]
        
        # Initialize the result
        result = ''
        
        # Iterate through the tuples
        for value, roman in roman_tuples:
            while num >= value:
                result += roman
                num -= value
        
        return result