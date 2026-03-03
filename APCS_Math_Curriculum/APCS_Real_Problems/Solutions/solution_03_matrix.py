# APCS 2017-03-04 實作題 Q2: 小群體 (Friend Groups) - 修正對應
# 註：原 Demo 03 是「矩陣翻轉」，對應 APCS 2017-03-04 Q2 (c291) 其實是小群體。
# 但 APCS 確實考過矩陣翻轉 (c295 矩陣翻轉 2017-03-04 Q2 其實是 c291 小群體，c295 是 2017-03-04 Q3 數字龍捲風... 等等，APCS 題號常變動)
# 這裡我們針對「矩陣翻轉」這個經典考題 (ZeroJudge b965) 撰寫解答。
#
# 題目 (b965): 給定 R x C 矩陣與 M 個操作 (0=旋轉, 1=翻轉)
# 0: 順時針旋轉 90 度
# 1: 上下翻轉

def rotate(matrix):
    """順時針旋轉 90 度"""
    R = len(matrix)
    C = len(matrix[0])
    # 新矩陣大小變 C x R
    new_m = [[0]*R for _ in range(C)]
    for r in range(R):
        for c in range(C):
            # 原本的 (r, c) 跑到 (c, R-1-r)
            new_m[c][R-1-r] = matrix[r][c]
    return new_m

def flip(matrix):
    """上下翻轉"""
    return matrix[::-1]

def solve():
    try:
        while True:
            line = list(map(int, input().split()))
            if not line: break
            R, C, M = line
            
            matrix = []
            for _ in range(R):
                matrix.append(list(map(int, input().split())))
            
            # 讀取操作指令 (反向讀取，因為題目可能是後進先出，或依題意順序)
            # b965 題目是依序執行
            ops = list(map(int, input().split()))
            
            # 執行操作 (從後面做回來？不，題目是依序)
            # 但有些題目要求從最後一個操作開始做，需看具體題敘。
            # b965: "請依照輸入的順序對矩陣進行操作" -> 正向
            # 但 ZeroJudge 測試測資有時需反向，這裡依標準正向寫法。
            # 修正：b965 實際上是「反向」執行的 (Stack 概念)，題目說 "第 k 個操作... 第 1 個操作"，通常輸入是 1...k，所以要 reverse。
            
            for op in ops[::-1]:
                if op == 0:
                    matrix = rotate(matrix)
                elif op == 1:
                    matrix = flip(matrix)
            
            # 輸出
            print(len(matrix), len(matrix[0]))
            for row in matrix:
                print(*row)
                
    except EOFError:
        pass

if __name__ == "__main__":
    solve()
