from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to simplify the code
        dummy = ListNode(0)
        current = dummy

        # While both lists have nodes
        while list1 and list2:
            if list1.val <= list2.val:
                # Append the smaller node to the result list
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # If one list is longer than the other, append the remaining nodes
        if list1:
            current.next = list1
        elif list2:
            current.next = list2

        # Return the result list (excluding the dummy node)
        return dummy.next

# Convert the input lists to ListNode objects
l1 = [1, 2, 4, 6]
l2 = [3, 4, 5, 7]

list1 = ListNode(l1[0])
current = list1
for val in l1[1:]:
    current.next = ListNode(val)
    current = current.next

list2 = ListNode(l2[0])
current = list2
for val in l2[1:]:
    current.next = ListNode(val)
    current = current.next

# Merge the two lists
solution = Solution()
merged_list = solution.mergeTwoLists(list1, list2)

# Print the merged list
while merged_list:
    print(merged_list.val,end=" ")
    merged_list = merged_list.next