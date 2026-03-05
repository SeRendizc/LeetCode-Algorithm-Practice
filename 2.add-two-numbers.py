#
# @lc app=leetcode.cn id=2 lang=python3
# @lcpr version=30204
#
# [2] 两数相加
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode], carry = 0) -> Optional[ListNode]:
        if l1 is None and l2 is None and carry == 0:
            return None
        if l1:
            carry += l1.val
            l1 = l1.next
        if l2:
            carry += l2.val
            l2 = l2.next
        return ListNode(carry % 10, self.addTwoNumbers(l1, l2, carry // 10))
        
        # dummy = cur = ListNode()
        # carry = 0
        # while l1 or l2 or carry:
        #     if l1:
        #         carry += l1.val
        #         l1 = l1.next
        #     if l2:
        #         carry += l2.val
        #         l2 = l2.next
        #     cur.next = ListNode(carry % 10)
        #     carry //= 10
        #     cur = cur.next
        # return dummy.next
        
        # dummy = ListNode(0)
        # cur = dummy
        # carry = 0
        # while l1 or l2 or carry:
        #     val1 = l1.val if l1 else 0
        #     val2 = l2.val if l2 else 0
        #     total = val1 + val2 + carry
        #     carry = total // 10
        #     cur.next = ListNode(total % 10)
        #     cur = cur.next
        #     if l1: l1 = l1.next
        #     if l2: l2 = l2.next
        # return dummy.next

# @lc code=end



#
# @lcpr case=start
# [2,4,3]\n[5,6,4]\n
# @lcpr case=end

# @lcpr case=start
# [0]\n[0]\n
# @lcpr case=end

# @lcpr case=start
# [9,9,9,9,9,9,9]\n[9,9,9,9]\n
# @lcpr case=end

#

