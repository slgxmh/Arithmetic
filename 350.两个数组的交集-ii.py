#
# @lc app=leetcode.cn id=350 lang=python3
#
# [350] 两个数组的交集 II
#


# @lc code=start
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        map = {}
        for item in nums1:
            if item in map:
                v = map[item]
                map[item] = v + 1
            else:
                map[item] = 1
        out = []
        for item in nums2:
            if item in map and map[item] != 0:
                out.append(item)
                v = map[item]
                map[item] = v - 1
        return out


# @lc code=end