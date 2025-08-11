# 🎰 Python Casino Game

A fun, terminal-based betting simulation game built in Python.  
Play against three computer-controlled opponents and see if you can keep your coins longer than they can!

---

## 📜 About the Game

This is a **4-player casino game**:
- **1 Human Player** (You)
- **3 Computer Players** (C1, C2, C3)

Every player starts with **500 coins**.  
Each round:
1. Place a bet (1–99 coins, or fewer if you have less).
2. Choose where to bet:
   - `R` = Red (payout x2)
   - `B` = Black (payout x2)
   - Numbers `1–8` (payout x8, alternating red/black colors)
3. Computer players place bets automatically.
4. The game randomly selects a **winning cell**.
5. Players who bet on it win coins according to the payout rate.
6. Repeat until any player’s coins reach **0**.

The player with the most coins at the end is the winner.

---

## 🖥 Example Gameplay

```text
[Players' coin] MY: 500 / C1: 500 / C2: 500 / C3: 500 /
How many coins do you bet?: (1-99) 30
On what do you bet?: (R, B, 1-8) R
MY bet 30 coin(s) to R.
C1 bet 43 coin(s) to 2.
C2 bet 12 coin(s) to B.
C3 bet 55 coin(s) to 6.
Winning number is R.
MY won. Gained 60 coins.
[Players' coin] MY: 530 / C1: 457 / C2: 488 / C3: 445 /
