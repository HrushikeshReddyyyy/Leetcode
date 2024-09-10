# Custom GCD function (Euclid's algorithm)
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertGreatestCommonDivisors(self, head):
        curr = head
        while curr and curr.next:
            # Calculate GCD using the custom gcd function
            gcd_value = gcd(curr.val, curr.next.val)
            # Create a new node with the GCD value
            new_node = ListNode(gcd_value)
            # Insert this new node between curr and curr.next
            new_node.next = curr.next
            curr.next = new_node
            # Move to the node after the newly inserted node
            curr = new_node.next
        return head
