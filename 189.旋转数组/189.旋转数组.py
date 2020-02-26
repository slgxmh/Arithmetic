#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 旋转数组
#


# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        k = k % length
        count = 0
        for start in range(length):
            # print('start=' + str(start))
            current = start
            prev = nums[start]
            while True:
                next = (current + k) % length
                temp = nums[next]
                nums[next] = prev
                prev = temp
                current = next
                count = count + 1
                # print('count=' + str(count))
                if start == current:
                    break
            if count == length:
                break


# @lc code=end
