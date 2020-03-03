#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        return self.b(head)

    # 递归
    def a(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        nextNode = self.a(head.next)
        head.next.next = head
        head.next = None
        return nextNode

    # 循环
    def b(self, head: ListNode) -> ListNode:
        out_head = None
        while head:
            post = head.next
            head.next = out_head
            out_head = head
            head = post
        return out_head


# @lc code=end
