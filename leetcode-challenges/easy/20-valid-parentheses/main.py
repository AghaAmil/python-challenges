class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        result = []

        for char in s:
            if not result:
                result.append(char)
            else:
                if self.charMatching(result[-1], char):
                    result = result[:-1]
                else:
                    result.append(char)

        if result:
            return False
        else:
            return True

    def charMatching(self, char1, char2):
        if char1 == '(' and char2 == ')' or char1 == '[' and char2 == ']' or char1 == '{' and char2 == '}':
            return True

        return False

    def userInput(self):
        while True:
            input_str = input('Enter String Input: ')

            for char in input_str:
                if char not in ['(', '{', '[', ')', '}', ']']:
                    print("Invalid input Entered, just '(', ')', '{', '}', '[' and ']' characters are accepted")
                else:
                    return input_str


user_input = Solution().userInput()
print(Solution().isValid(user_input))
