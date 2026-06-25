class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        test = ListNode(0, head)

        right = test
        left = test

        for i in range(n):
            right = right.next

        while right.next is not None:
            left = left.next
            right = right.next

        left.next = left.next.next

        return test.next