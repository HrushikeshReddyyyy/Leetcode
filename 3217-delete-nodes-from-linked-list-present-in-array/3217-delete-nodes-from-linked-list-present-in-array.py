class Solution:
    def modifiedList(self, nums: list[int], head: ListNode | None) -> ListNode | None:
        numsSet = set(nums)
        curr = head
        
        while curr and curr.next:
            if curr.next.val in numsSet:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return head if head and head.val not in numsSet else head.next
