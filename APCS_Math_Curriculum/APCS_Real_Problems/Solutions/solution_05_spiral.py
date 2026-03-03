# APCS 2017-03-04 實作題 Q3: 數字龍捲風 (Number Spiral)
# 題目連結: https://zerojudge.tw/ShowProblem?problemid=c296
#
# 輸入說明:
# 第一行 N (寬度), D (方向 0:左 1:上 2:右 3:下)
# 接下來 N 行 N 列的矩陣
#
# 輸出說明:
# 從中心點開始，依螺旋順序輸出的數字串
#
# 規律:
# 步數序列: 1, 1, 2, 2, 3, 3, 4, 4 ... (每兩次方向變換後，步數+1)
# 方向循環: 左 -> 上 -> 右 -> 下 -> 左 ...

def solve():
    try:
        line = input().split()
        if not line: return
        N = int(line[0])
        D = int(line[1])
        
        grid = []
        for _ in range(N):
            grid.append(list(map(int, input().split())))
            
        # 中心點
        r, c = N // 2, N // 2
        print(grid[r][c], end="") # 先印中心
        
        # 方向向量 (左, 上, 右, 下)
        # 注意題目定義: 0左, 1上, 2右, 3下
        # r變化: 0, -1, 0, 1
        # c變化: -1, 0, 1, 0
        dr = [0, -1, 0, 1]
        dc = [-1, 0, 1, 0]
        
        step_len = 1
        step_count = 0 # 走了幾次 step_len
        
        # 總共要走 N*N - 1 步
        total_steps = 0
        
        while total_steps < N*N - 1:
            for _ in range(step_len):
                r += dr[D]
                c += dc[D]
                
                # 邊界檢查 (雖然理論上螺旋不會出界，直到結束)
                if 0 <= r < N and 0 <= c < N:
                    print(f"{grid[r][c]}", end="")
                    total_steps += 1
                    if total_steps >= N*N - 1: break
            
            D = (D + 1) % 4 # 轉向
            step_count += 1
            if step_count == 2: # 每兩次轉向，步長+1
                step_len += 1
                step_count = 0
                
        print() # 換行
        
    except EOFError:
        pass

if __name__ == "__main__":
    solve()
