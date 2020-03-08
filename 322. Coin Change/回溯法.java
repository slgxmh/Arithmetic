/*
 * @lc app=leetcode.cn id=322 lang=java
 *
 * [322] 零钱兑换
 */

// @lc code=start
public class Solution {
  public int coinChange(int[] coins, int amount) {
    // 调用初始条件
    return coinChange(0, coins, amount);
  }

  // 回溯法三要素：退出条件，回溯过程，递归参数
  // 参数为当前用的硬币索引，硬币数组，当前已经产生的数值
  private int coinChange(int idxCoin, int[] coins, int amount) {
    // 回溯退出
    if (amount == 0)   return 0;
    // 回溯执行的条件，仍然有硬币可用或仍有余额
    if (idxCoin < coins.length && amount > 0) {
      // 当前值用几个当前硬币表示（向下取整）
      int maxVal = amount / coins[idxCoin];
      int minCost = Integer.MAX_VALUE;
      // 回溯核心内容，每取一个当前硬币，探索其他情况，x为当前用了几个该面值硬币
      for (int x = 0; x <= maxVal; x++) {
        // 仍有余额，即为 amount - coins[idxCoin] >= 0
        if (amount >= x * coins[idxCoin]) {
          // 用下一个硬币试试
          int res = coinChange(idxCoin + 1, coins, amount - x * coins[idxCoin]);
          // 回溯成功，下一种情况也有解
          if (res != -1)
            // 与目前的最优解比比看
            minCost = Math.min(minCost, res + x);
        }
      }
      // 最小代价没有更新，说明所有方案无效
      return (minCost == Integer.MAX_VALUE)? -1: minCost;
    }
    // 没有执行上一个返回那就是一次也没有运行，直接失败
    return -1;
  }
}

// Time Limit Exceeded
// @lc code=end

