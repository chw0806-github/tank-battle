# 猜数字小游戏

import random


def choose_difficulty():
    print("选择难度：")
    print("  1. 简单（1～10，5 次机会）")
    print("  2. 普通（1～50，7 次机会）")
    print("  3. 困难（1～100，8 次机会）")
    while True:
        choice = input("请输入 1/2/3：").strip()
        if choice == "1":
            return 1, 10, 5
        if choice == "2":
            return 1, 50, 7
        if choice == "3":
            return 1, 100, 8
        print("输入无效，请重新选择。")


def play_round():
    low, high, max_tries = choose_difficulty()
    secret = random.randint(low, high)
    tries = 0
    history = []

    print(f"\n我想了一个 {low}～{high} 的数字，你有 {max_tries} 次机会！")
    print("输入 h 可以要一次提示（会消耗 1 次机会）。\n")

    while tries < max_tries:
        remaining = max_tries - tries
        raw = input(f"[{remaining} 次剩余] 猜测或 h：").strip().lower()

        if raw == "h":
            tries += 1
            if secret % 2 == 0:
                print("提示：是偶数")
            else:
                print("提示：是奇数")
            if secret > (low + high) // 2:
                print("提示：比中间值大")
            else:
                print("提示：小于或等于中间值")
            continue

        if not raw.isdigit():
            print("请输入整数，或输入 h 获取提示。")
            continue

        guess = int(raw)
        if guess < low or guess > high:
            print(f"请输入 {low}～{high} 之间的数字。")
            continue

        tries += 1
        history.append(guess)
        gap = abs(guess - secret)
        if guess < secret:
            hint = "太小了"
        elif guess > secret:
            hint = "太大了"
        else:
            score = max(0, (max_tries - tries + 1) * 10)
            print(f"猜对了！用了 {tries} 次，得分 {score}")
            print(f"猜测记录：{history}")
            return True, score

        if gap <= 3:
            closeness = "非常接近"
        elif gap <= 10:
            closeness = "有点接近"
        else:
            closeness = "还差得远"
        print(f"{hint}（{closeness}）  已猜过：{history}")

    print(f"机会用完了，答案是 {secret}")
    print(f"猜测记录：{history}")
    return False, 0


def main():
    print("=" * 28)
    print("   欢迎来到猜数字游戏")
    print("=" * 28)

    wins = 0
    rounds = 0
    best_score = 0

    while True:
        rounds += 1
        won, score = play_round()
        if won:
            wins += 1
            if score > best_score:
                best_score = score

        again = input("\n再来一局？(y/n)：").strip().lower()
        if again not in ("y", "yes", "是"):
            break
        print()

    print(f"\n本局战绩：{wins}/{rounds} 胜，最高分 {best_score}")
    print("谢谢游玩！")


if __name__ == "__main__":
    main()
