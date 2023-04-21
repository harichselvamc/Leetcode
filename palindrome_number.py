# Define a class called Solution
class Solution(object):
    # Define a function called isPalindrome that takes an integer x as input
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Check if x is negative. If so, return False
        if x < 0:
            return False
        
        # Convert the integer to a string
        str_x = str(x)
        
        # Reverse the string
        reversed_str_x = str_x[::-1]
        
        # Compare the original string and the reversed string
        # If they are the same, return True. Otherwise, return False
        if str_x == reversed_str_x:
            return True
        else:
            return False

# Create an instance of the Solution class
palindrome_checker = Solution()

# Call the isPalindrome method on the palindrome_checker instance, passing 121 as the argument
result = palindrome_checker.isPalindrome(121)

# Print the result
print(result)
