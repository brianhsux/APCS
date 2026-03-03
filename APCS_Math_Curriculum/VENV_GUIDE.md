# APCS 專案虛擬環境使用教學（macOS）

這份教學是給老師與學生使用，說明如何在 `APCS` 專案中，用 **虛擬環境 (virtualenv/venv)** 安裝與管理像 `pgzero` 這類套件，而不影響電腦上的其他專案。

> 專案路徑假設為：`/Users/brianhsu/Documents/APCS`

---

## 1. 虛擬環境是什麼？為什麼要用？

- **虛擬環境**就是一個「專案自己的 Python 空間」，裡面有獨立的套件清單。
- 這樣做有幾個好處：
  - 不會跟別的專案的套件版本打架。
  - 學生安裝/移除套件不會弄壞系統 Python。
  - 搬專案到別台電腦時，只要在虛擬環境裡重新安裝需求即可。

在這個 APCS 專案裡，我們會在專案根目錄（`APCS`）下放一個 `.venv` 資料夾，裡面就是虛擬環境。

---

## 2. 第一次建立虛擬環境

在終端機執行以下步驟（只要做一次）：

```bash
cd "/Users/brianhsu/Documents/APCS"   # 進入專案根目錄
python3 -m venv .venv                  # 建立名為 .venv 的虛擬環境
```

完成後，專案底下會多一個 `.venv` 資料夾：

```bash
ls -a
# 你會看到類似：
# .  ..  .git  .venv  APCS_Math_Curriculum
```

> 注意：這一步 **只要做一次**，之後不需要重複建立。

---

## 3. 每次使用前：啟動虛擬環境（activate）

之後，只要你要在這個專案裡安裝套件或執行 Demo，**先啟動虛擬環境**：

```bash
cd "/Users/brianhsu/Documents/APCS"
source .venv/bin/activate
```

啟動成功後，終端機前面會多一個類似這樣的前綴：

```bash
(.venv) brianhsu@MacBook APCS %
```

代表現在所有的 `python`、`pip`、`pgzrun` 指令，都會使用這個虛擬環境裡的 Python 和套件。

---

## 4. 在虛擬環境中安裝套件（例如 Pygame Zero）

啟動虛擬環境之後，就可以安裝教學需要的套件，例如 `pgzero`：

```bash
(.venv) python3 -m pip install pgzero
```

安裝完成後，`pgzrun` 指令就會在這個虛擬環境裡可用。

你可以簡單檢查一下：

```bash
(.venv) pgzrun --version
```

如果沒有出錯，表示安裝成功，可以開始跑我們的遊戲 Demo。

---

## 5. 執行 APCS_Math_Curriculum 底下的遊戲 Demo

### 5.1 進入對應年級資料夾

以九年級 I/O 練習為例：

```bash
(.venv) cd "APCS_Math_Curriculum/Grade_9_Game_Design"
(.venv) pgzrun demo_01_io_practice.py
```

以三年級的座標練習為例：

```bash
(.venv) cd "APCS_Math_Curriculum/Grade_3_Game_Design"
(.venv) pgzrun demo_01_basic_move.py
```

所有我們設計的 Demo（Grade 3〜Grade 9），都是用 **Pygame Zero** 寫的，所以一律用：

```bash
pgzrun 檔名.py
```

---

## 6. 用 Mu Editor 時如何搭配虛擬環境？（選用）

如果你用 **Mu Editor** 上課，Mu 內建自己的 Python 與 Pygame Zero，不一定需要手動啟動虛擬環境：

1. 打開 Mu。
2. 在上方選單選擇 **Mode → Pygame Zero**。
3. 開啟某個 `demo_xx_xxx.py` 檔案。
4. 按 **Play** 就可以直接執行。

這個情境下，Mu 使用的是它內建的環境，不會用到 `.venv`。

如果你希望 Mu 也使用專案的虛擬環境，則需要在 Mu 的設定裡指定 Python 路徑（這比較進階，可以先不用）。

---

## 7. 結束虛擬環境（deactivate）

當你今天的教學結束，不想再留在專案虛擬環境時，可以輸入：

```bash
(.venv) deactivate
```

這會讓終端機回到系統預設的 Python：

```bash
brianhsu@MacBook APCS %
```

之後如果要再繼續上 APCS 課，只要回到第 3 步，重新 `source .venv/bin/activate` 即可。

---

## 8. 給學生的簡化版口訣

1. 進專案：
   ```bash
   cd "/Users/brianhsu/Documents/APCS"
   ```
2. 啟動環境：
   ```bash
   source .venv/bin/activate
   ```
3. 跑遊戲（以三年級 demo 為例）：
   ```bash
   cd "APCS_Math_Curriculum/Grade_3_Game_Design"
   pgzrun demo_01_basic_move.py
   ```
4. 下課回家：
   ```bash
   deactivate
   ```

照這份教學檔，一步一步做，就可以穩定地在同一台電腦上維護 APCS 整套課程與所有 Demo。 
