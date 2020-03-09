/*
 * @lc app=leetcode.cn id=322 lang=java
 *
 * [322] 零钱兑换
 */

// @lc code=start
public class Solution {
  public int coinChange(int[] coins, int amount) {
    // 初始条件检查
    if (amount < 1) return 0;
    // 动态规划入口
    return coinChange(coins, amount, new int[amount]);
  }

  /** 
  * 自上而下的动态规划方法
  * coins:硬币面额
  * rem:余额
  * count:存储中间计算结果，空间换时间
  */
  private int coinChange(int[] coins, int rem, int[] count) {
    // 结束条件：此路径不通
    if (rem < 0) return -1;
    // 结束条件：余额为0，成功结束
    if (rem == 0) return 0;
    // 之前已经计算过这种情况，直接返回结果，避免重复计算
    if (count[rem - 1] != 0) return count[rem - 1];
    int min = Integer.MAX_VALUE;
    // 遍历当前递归子树的每一种情况
    for (int coin : coins) {
      // 用一下coin这个面值的硬币会怎样？res是这个方法的最优情况
      int res = coinChange(coins, rem - coin, count);
      // res<0 即为 res=-1,此法失败，res>min不是最优情况，舍去
      if (res >= 0 && res < min)
        min = 1 + res;
    }
    // count[rem - 1]存储着给定金额amount的解
    // 若为Integer.MAX_VALUE则该情况无解
    count[rem - 1] = (min == Integer.MAX_VALUE) ? -1 : min;
    return count[rem - 1];
  }
}

// Time Limit Exceeded
// @lc code=end

