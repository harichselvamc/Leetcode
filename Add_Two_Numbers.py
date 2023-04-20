# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        # Initialize carry variable to 0
        carry = 0
        # Initialize a new linked list with dummy node
        l3 = ListNode(0)
        # Pointer to current node in l3
        p = l3
        # Loop through the two input linked lists and the carry variable
        while l1 or l2 or carry == 1:
            # Initialize sum variable to 0
            sum = 0
            # Add value of l1 node to sum if l1 is not None
            if l1:
                sum += l1.val
                l1 = l1.next
            # Add value of l2 node to sum if l2 is not None
            if l2:
                sum += l2.val
                l2 = l2.next
            # Add value of carry to sum
            sum += carry
            # Calculate new carry value
            carry = sum // 10
            # Create a new node in l3 with value equal to sum % 10
            node = ListNode(sum % 10)
            # Set the next pointer of current node to the new node
            p.next = node
            # Move the pointer to the new node
            p = p.next
        # Return the linked list starting from the second node (dummy node)
        return l3.next


# Define the input linked lists
l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))

# Create an instance of the Solution class
s = Solution()

# Run the addTwoNumbers method and get the result
result = s.addTwoNumbers(l1, l2)

# Print the result
output = []
while result:
    output.append(result.val)
    result = result.next
print(output)  # should print [7, 0, 8]


