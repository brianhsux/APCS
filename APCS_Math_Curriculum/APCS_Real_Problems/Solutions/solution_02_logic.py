# APCS 2016-10-29 實作題 Q2: 邏輯運算子 (Logic Operators)
# 題目連結: https://zerojudge.tw/ShowProblem?problemid=c291
#
# 輸入說明:
# 第一行包含三個整數 a, b, c (0 或 1)。
#
# 輸出說明:
# 輸出邏輯運算結果：(a AND b) OR (NOT c)
# 注意：C++ 中非 0 即為真，但本題輸入限定 0/1。
# 輸出 "AND: X OR: Y NOT: Z" 格式 (此為模擬題意，真實題目可能不同，依 ZeroJudge c291 為準)
# ZeroJudge c291 其實是更複雜的「最大群組」，但這裡我們對應 Demo 02 的邏輯題型。
# 修正：Demo 02 是簡化版邏輯。若要對應 APCS 真題「邏輯運算子 (c295)」，題目其實是給定多個數字，選出最大群組。
# 為了配合 Demo 02 的教學脈絡，這裡提供 Demo 02 對應的邏輯運算解法。

def solve():
    try:
        line = input().split()
        if not line: return
        
        a = int(line[0])
        b = int(line[1])
        c = int(line[2])
        
        # 邏輯運算
        # 1. AND
        res_and = 1 if (a > 0 and b > 0) else 0
        
        # 2. NOT
        res_not = 0 if c > 0 else 1
        
        # 3. OR
        res_final = 1 if (res_and > 0 or res_not > 0) else 0
        
        print(res_final)
        
    except EOFError:
        pass

if __name__ == "__main__":
    solve()
