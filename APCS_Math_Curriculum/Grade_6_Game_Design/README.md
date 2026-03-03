# 小六 (Grade 6) 遊戲設計與數學觀念對照表

這個階段的核心是**「結構與優化」**。
目標：直接對接 APCS 實作題，挑戰圖論 (Graph)、動態規劃 (DP) 與複雜模擬。

## 循序漸進一覽表

| 順序 | 檔案 | 對應數學觀念 | 遊戲玩法 |
|------|------|--------------|----------|
| 1 | `demo_01_vector_movement.py` | 向量運算 (Vector) | 模擬太空船慣性漂移與重力吸引 |
| 2 | `demo_02_collision_circle.py` | 幾何距離 (Geometry) | 圓形碰撞檢測 (距離公式 < 半徑和) |
| 3 | `demo_03_matrix_transform.py` | 矩陣旋轉 (Matrix) | 俄羅斯方塊的旋轉邏輯 (轉 90 度公式) |
| 4 | `demo_04_shortest_path_dijkstra.py` | 最短路徑 (Dijkstra) | 導航系統模擬，有權重的地圖 (塞車路段) |
| 5 | `demo_05_dp_coin_change.py` | 動態規劃 (DP) | 湊錢問題：用最少硬幣湊出目標金額 |
| 6 | `demo_06_tree_traversal.py` | 樹的走訪 (DFS/BFS) | 檔案總管模擬，遍歷所有子資料夾 |
| 7 | `demo_07_graph_connection.py` | 圖論連通性 (Graph) | 電力公司：檢查所有城市是否都有電 (連通圖) |
| 8 | `demo_08_sorting_race.py` | 排序演算法比較 | 泡泡排序 vs 快速排序，看誰跑得快 |
| 9 | `demo_09_binary_search_tree.py` | 二元搜尋樹 (BST) | 數字大小自動分流，建立搜尋樹 |
| 10 | `demo_10_apcs_simulator.py` | 綜合模擬 (APCS) | 模擬 APCS 考題：機器人路徑規劃與資源收集 |

---

## 執行方式
使用 **Pygame Zero**。
`pgzrun demo_XX_name.py`
