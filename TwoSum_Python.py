class Solution: # Define a class called Solution
    def twoSum(self, nums, target): # Define a method called twoSum that takes in a list of integers nums and a target integer target
        n = len(nums) # Find the length of the list nums and assign it to the variable n
        order = [] # Create an empty list called order to store the indices of the two numbers that add up to the target
        for i in range(n): # Loop through the list nums from the first index to the last index
            for j in range(i + 1, n): # Loop through the list nums from the index after the current index to the last index
                if nums[i] + nums[j] == target: # If the sum of the numbers at the current index and the next index equals the target
                    order.append(i) # Add the current index to the order list
                    order.append(j) # Add the next index to the order list
                    return order # Return the order list
        return [] # If no pair of numbers add up to the target, return an empty list

solution = Solution() # Create an instance of the Solution class called solution
solution.twoSum([3,2,4], 6) # Call the twoSum method on the list [3, 2, 4] and target integer 6
