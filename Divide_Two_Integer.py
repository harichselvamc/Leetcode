class Solution(object):
    def divide(self, dividend, divisor):
        # Handle division by zero case
        if divisor == 0:
            return float('inf')
        
        # Handle overflow cases
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        
        # Convert dividend and divisor to positive values
        positive_dividend = abs(dividend)
        positive_divisor = abs(divisor)
        
        quotient = 0
        while positive_dividend >= positive_divisor:
            # Find the largest multiple of the divisor that can be subtracted from the dividend
            temp = positive_divisor
            multiple = 1
            while positive_dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            
            # Subtract the multiple from the dividend and update the quotient
            positive_dividend -= temp
            quotient += multiple
        
        # Determine the sign of the quotient based on the signs of dividend and divisor
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            quotient = -quotient
        
        return quotient


solution = Solution()
dividend = 10
divisor = 3
result = solution.divide(dividend, divisor)
print(result)  # Output: 3

dividend = 7
divisor = -3
result = solution.divide(dividend, divisor)
print(result)  # Output: -2
