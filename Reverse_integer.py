# Define a class called Solution
class Solution(object):
    # Define a function called reverse that takes an integer x as input and returns an integer
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # Check if x is negative or positive and store the sign
        if x < 0:
            sign = -1
            x = abs(x)
        else:
            sign = 1
        
        # Reverse the digits of x
        rev = 0
        while x != 0:
            rev = rev * 10 + x % 10
            x = x // 10
        
        # Check if reversed x is within the signed 32-bit integer range
        if rev > 2**31 - 1:
            return 0
        
        # Return the reversed integer with sign
        return sign * rev


# Create an instance of the Solution class
sol = Solution()

# Call the reverse method on the sol instance, passing 123 as the argument
# The output should be 321, which we print to the console
print(sol.reverse(123))
