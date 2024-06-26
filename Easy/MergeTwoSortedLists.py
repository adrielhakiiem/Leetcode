# Define new class
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode() # Declare dummy as a ListNode
        current = dummy # Assign dummy to a variable 
        
        # Stage 1: Compare value of each nodes in both lists 
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1 # move to the next node of the dummy (new) list 
                list1 = list1.next # move to the next node of list1 
            else:
                current.next = list2
                list2 = list2.next 
            current = current.next
        
        # Stage 2: If there are remainders
        if list1:
            current.next = list1 # Insert all the remaining ones directly 
        elif list2:
            current.next = list2 
        
        return dummy.next
