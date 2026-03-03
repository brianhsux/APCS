# 小五 (Grade 5) 遊戲設計與數學觀念對照表

這個階段的核心是**「效率與演算法」**。
目標：處理更複雜的數據結構（質數、加密），並開始接觸「遞迴」與「動態規劃」的雛形。

## 循序漸進一覽表

| 順序 | 檔案 | 對應數學觀念 | 遊戲玩法 |
|------|------|--------------|----------|
| 1 | `demo_01_prime_shield.py` | 質數 (Prime) | 只有質數盾牌能擋住攻擊，合數會碎掉 |
| 2 | `demo_02_gcd_puzzle.py` | 最大公因數 (GCD) | 切蛋糕/拼地磚，找出最大正方形邊長 |
| 3 | `demo_03_caesar_cipher.py` | 模運算與加密 (Mod) | 凱薩密碼解謎，將字母位移來傳送秘密訊息 |
| 4 | `demo_04_recursion_tree.py` | 遞迴 (Recursion) | 畫出一棵碎形樹 (Fractal Tree) |
| 5 | `demo_05_fibonacci_rabbit.py` | 數列與遞迴 | 兔子生兔子模擬，費氏數列視覺化 |
| 6 | `demo_06_binary_encoding.py` | 二進位 (Binary) | 開關燈泡代表 0/1，計算對應的十進位數字 |
| 7 | `demo_07_stack_tower.py` | 堆疊 (Stack) | 河內塔遊戲 (Hanoi)，後進先出的概念 |
| 8 | `demo_08_queue_customer.py` | 佇列 (Queue) | 飲料店排隊模擬，先進先出 (FIFO) |
| 9 | `demo_09_path_finding_bfs.py` | 廣度優先搜尋 (BFS) | 像水波一樣擴散，找出迷宮最短路徑 |
| 10 | `demo_10_dungeon_gen.py` | 隨機地圖生成 (ProcGen) | 結合亂數與遞迴，自動產生不重複的地牢 |

---

## 執行方式
使用 **Pygame Zero**。
`pgzrun demo_XX_name.py`
