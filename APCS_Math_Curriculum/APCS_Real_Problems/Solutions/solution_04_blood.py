# APCS 2016-03-05 實作題 Q4: 血緣關係 (Blood Distance)
# 題目連結: https://zerojudge.tw/ShowProblem?problemid=c292
#
# 輸入說明:
# 第一行 N (節點數 0~N-1)
# 接下來 N-1 行，每行兩個整數 A B，表示 A 是 B 的父節點 (樹狀結構)
#
# 輸出說明:
# 輸出樹中「最遠的兩個節點」之間的距離 (樹直徑 Tree Diameter)
#
# 解法:
# 1. 建圖 (Adjacency List)
# 2. 找到根節點 (入度為 0) -> 其實求直徑不需要根，隨便一點做 BFS 找最遠，再從最遠做 BFS 即可。
# 3. 標準求樹直徑做法：
#    - 從任意點 x 出發，BFS 找到最遠點 u
#    - 從 u 出發，BFS 找到最遠點 v
#    - dist(u, v) 即為直徑

import sys
# 增加遞迴深度 (若用 DFS)
sys.setrecursionlimit(100000)

def bfs(start, n, adj):
    # 回傳 (最遠節點, 距離)
    dist = [-1] * n
    dist[start] = 0
    queue = [start]
    
    max_d = 0
    farthest_node = start
    
    while queue:
        u = queue.pop(0)
        if dist[u] > max_d:
            max_d = dist[u]
            farthest_node = u
            
        for v in adj[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                queue.append(v)
                
    return farthest_node, max_d

def solve():
    try:
        line = sys.stdin.readline()
        if not line: return
        n = int(line.strip())
        
        # 題目給的是有向邊 (父->子)，但求距離視為無向
        adj = [[] for _ in range(n)]
        
        # 讀取 N-1 條邊
        # 注意：APCS 測試資料有時很大，input() 會慢，建議 sys.stdin
        for _ in range(n - 1):
            line = sys.stdin.readline().split()
            if not line: break
            u, v = int(line[0]), int(line[1])
            adj[u].append(v)
            adj[v].append(u) # 無向邊方便 BFS
            
        # 第一次 BFS: 找端點 u
        u, _ = bfs(0, n, adj)
        
        # 第二次 BFS: 從 u 找 v
        v, diameter = bfs(u, n, adj)
        
        print(diameter)
        
    except ValueError:
        pass

if __name__ == "__main__":
    solve()
