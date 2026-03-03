# APCS 2016-03-05 實作題 Q1: 成績指標 (Grade Indicators)
# 題目連結: https://zerojudge.tw/ShowProblem?problemid=c290
#
# 輸入說明:
# 第一行一個整數 N，表示學生人數。
# 第二行 N 個整數，表示學生成績。
#
# 輸出說明:
# 第一行：由小到大印出所有成績。
# 第二行：不及格的最高分 (Best Bad)，若無則印出 "best case"。
# 第三行：及格的最低分 (Worst Good)，若無則印出 "worst case"。

def solve():
    try:
        # 讀取 N (雖然 Python 可以直接讀第二行 split，但依題目要求讀 N)
        n = int(input())
        # 讀取成績並轉為整數列表
        scores = list(map(int, input().split()))
        
        # 1. 排序
        scores.sort()
        
        # 輸出排序後的成績 (用空格隔開)
        print(*scores)
        
        # 2. 找不及格最高分 (<60)
        best_bad = -1
        for s in scores:
            if s < 60:
                best_bad = s
            else:
                break # 因為排過序，一旦 >= 60 後面都不用看了
                
        if best_bad == -1:
            print("best case")
        else:
            print(best_bad)
            
        # 3. 找及格最低分 (>=60)
        worst_good = -1
        for s in scores:
            if s >= 60:
                worst_good = s
                break # 找到第一個及格的就是最小的
                
        if worst_good == -1:
            print("worst case")
        else:
            print(worst_good)
            
    except EOFError:
        pass

if __name__ == "__main__":
    solve()
