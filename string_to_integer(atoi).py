class Solution(object):
    def myAtoi(self, s):
        # Step 1: Remove leading and trailing whitespace
        s = s.strip()
        
        # Step 2: Check if the number is negative or positive
        sign = 1
        if s and (s[0] == '-' or s[0] == '+'):
            sign = -1 if s[0] == '-' else 1
            s = s[1:]
        
        # Step 3: Read and convert digits
        num = 0
        for char in s:
            if not char.isdigit():  # If the character is not a digit, break the loop
                break
            num = num * 10 + int(char)  # Convert the character to integer and add it to the number
        
        # Step 4: Apply the sign and handle integer range
        num = sign * num  # Apply the sign to the number
        num = max(min(num, 2**31 - 1), -2**31)  # Clamp the number within the 32-bit signed integer range
        
        return num


s = '42'  # Example input string

solution = Solution()  # Create an instance of the Solution class
result = solution.myAtoi(s)  # Call the myAtoi function on the input string
print(result)  # Print the resulting converted integer
