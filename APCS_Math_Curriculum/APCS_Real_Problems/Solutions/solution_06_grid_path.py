# APCS 2017-10-28 實作題 Q4: 物品堆疊 (Stacking) - 修正對應
# 註：Demo 06 是「機器人路徑」，對應 APCS 題目其實比較像「物品堆疊」的 DP 或 Greedy 題型
# 或是「交錯字串」(c471)
# 但這裡我們實作「物品堆疊」(f608 類似題) 或最接近 Demo 06 的「最大路徑和」
#
# 題目 (類似 ZeroJudge d784 一筆畫問題，或 f315 低地距離)
# 這裡我們實作一個經典的 Grid DP: 「最大路徑和」
# 給定 N*M 矩陣，從左上走到右下，只能向右或向下，求路徑上數字總和最大值
# 這也是 APCS 常考的基礎 DP

def solve():
    try:
        # 讀取 R, C
        line = input().split()
        if not line: return
        R = int(line[0])
        C = int(line[1])
        
        grid = []
        for _ in range(R):
            grid.append(list(map(int, input().split())))
            
        # DP 表
        dp = [[0]*C for _ in range(R)]
        
        # 初始化起點
        dp[0][0] = grid[0][0]
        
        # 初始化第一列 (只能從左邊來)
        for c in range(1, C):
            dp[0][c] = dp[0][c-1] + grid[0][c]
            
        # 初始化第一行 (只能從上面來)
        for r in range(1, R):
            dp[r][0] = dp[r-1][0] + grid[r][0]
            
        # 填表
        for r in range(1, R):
            for c in range(1, C):
                # 從上面或左邊選大的
                dp[r][c] = max(dp[r-1][c], dp[r][c-1]) + grid[r][c]
                
        print(dp[R-1][C-1])
        
    except EOFError:
        pass

if __name__ == "__main__":
    solve()
