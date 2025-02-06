class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        sum = 0
        previous_value = 0

        roman_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        s = reversed(s)

        for char in s:
            value = roman_map[char]

            if value >= previous_value:
                sum += value
            else:
                sum -= value

            previous_value = value

        return sum


user_input = input('Enter the Roman numerals: ')

print(Solution().romanToInt(user_input))
