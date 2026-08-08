# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # current = head
        # size = 0
        # hashmap = {}

        # while current is not None:
        #     size += 1
        #     current = current.next

        # original_size = size

        # while head is not None:
        #     hashmap[size] = head.val
        #     head = head.next
        #     size -= 1
        
        # if n in hashmap:
        #     del hashmap[n]

        # dummy = ListNode(0)
        # new_node = dummy

        # for i in range(original_size, 0, -1):
        #     if i in hashmap:
        #         new_node.next = ListNode(hashmap[i])
        #         new_node = new_node.next

        # return dummy.next

        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy

        for _ in range(n+1):
            fast = fast.next
        
        while fast is not None:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return dummy.next


        