class Solution:
    def mergeTwoLists(self, list1, list2):
        a = ListNode()   
        new= a

        while list1 and list2:
            if list1.val < list2.val:
                new.next = list1
                list1 = list1.next
            else:
                new.next = list2
                list2 = list2.next
            new = new.next
        new.next = list1 if list1 else list2
        return a.next