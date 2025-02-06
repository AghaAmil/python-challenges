class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: str
        :rtype: bool
        """
        reverse_x = x[::-1]

        if reverse_x == x:
            return True
        else:
            return False


class Solution2(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        reverse_x = 0

        while x != 0:
            digit = x % 10
            reverse_x = reverse_x * 10 + digit
            x = x // 10

        if reverse_x == x:
            return True
        else:
            return False


input_num = input('Enter a number: ')

print(Solution().isPalindrome(input_num))
print(Solution2().isPalindrome(int(input_num)))
