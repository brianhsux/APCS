# APCS 實作題 - 純 Python 解答 (Solutions)

這個資料夾收錄了對應 `APCS_Real_Problems` 視覺化 Demo 的**標準 Python 解答**。
這些程式碼是可以直接提交到 ZeroJudge 或 APCS 考試系統的格式（讀取 `stdin`，輸出到 `stdout`）。

## 📝 檔案對照表

| 視覺化 Demo | 標準解答 | 對應 APCS 題型 | 說明 |
|-------------|----------|----------------|------|
| `apcs_01_grade.py` | `solution_01_grade.py` | 成績指標 (c290) | 排序與條件判斷 |
| `apcs_02_logic_operators.py` | `solution_02_logic.py` | 邏輯運算 (c291) | 布林運算模擬 |
| `apcs_03_matrix_rotation.py` | `solution_03_matrix.py` | 矩陣翻轉 (b965) | 二維陣列操作 (旋轉/翻轉) |
| `apcs_04_blood_distance.py` | `solution_04_blood.py` | 血緣關係 (c292) | 樹直徑 / BFS / DFS |
| `apcs_05_stack_game.py` | `solution_05_spiral.py` | 數字龍捲風 (c296) | *註：Demo 05 是 Stack，解答提供螺旋矩陣 (更常考)* |
| `apcs_06_robot_path.py` | `solution_06_grid_path.py` | 格子路徑 DP | 動態規劃求最大路徑和 |

## 🚀 如何練習

1.  **閱讀題目**：打開 `.py` 檔，最上方註解有題目描述與輸入輸出格式。
2.  **執行測試**：
    ```bash
    python3 solution_01_grade.py
    ```
    然後手動輸入測資（或複製貼上）。
3.  **比較差異**：
    - **視覺化版 (Demo)**：側重於「看懂流程」，有動畫、有圖形。
    - **解答版 (Solution)**：側重於「通過考試」，講究 I/O 格式、效率與正確性。

## ⚠️ 注意事項

- APCS 考試通常支援 Python，但建議熟悉 `sys.stdin` 讀取方式以加快速度。
- 遞迴題目 (如 Q4) 在 Python 中需注意 `sys.setrecursionlimit`。
