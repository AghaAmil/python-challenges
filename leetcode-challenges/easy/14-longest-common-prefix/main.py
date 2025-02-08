class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        # If the list is empty, return an empty string
        if not strs:
            return ""

        # Start with the first string as the prefix
        prefix = strs[0]

        # Iterate over the remaining strings
        for s in strs[1:]:
            # Reduce the prefix until it is a prefix of s
            while not s.startswith(prefix):
                # Remove the last character from prefix
                prefix = prefix[:-1]
                # If prefix becomes empty, there is no common prefix
                if not prefix:
                    return ""

        # After processing all strings, prefix contains the longest common prefix
        return prefix

    def listMaking(self, strs):
        remove_brackets = strs[1:-1]

        remove_quotes = ""

        for char in remove_brackets:
            if char != '"':
                remove_quotes += char

        list_of_strs = remove_quotes.split(',')

        return list_of_strs


user_input = input('Enter the list of strings (e.g. ["flower","flow","flight"]): ')

list_of_strs = Solution().listMaking(user_input)

print(f'"{Solution().longestCommonPrefix(list_of_strs)}"')
