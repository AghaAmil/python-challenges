class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def listMaking(self, user_input):
        # Remove any leading/trailing whitespace and the enclosing square brackets.
        # This assumes the input always starts with '[' and ends with ']'.
        remove_brackets = user_input.strip()[1:-1]

        # Split the string by commas to get individual number strings.
        split_numbers = remove_brackets.split(',')

        list_of_nums = [int(num.strip()) for num in split_numbers]

        return list_of_nums


user_input = input('Enter the list of numbers (e.g., [1, 2, 3, 4, 5, 6, 7]): ')
target = int(input('Enter the target sum: '))

input_array = Solution().listMaking(user_input)

result = Solution().twoSum(input_array, target)

print(result)
