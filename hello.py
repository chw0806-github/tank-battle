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
        if guess < secret:
            print("太小了")
        elif guess > secret:
            print("太大了")
        else:
            score = max(0, (max_tries - tries + 1) * 10)
            print(f"猜对了！用了 {tries} 次，得分 {score}")
            return True

    print(f"机会用完了，答案是 {secret}")
    return False


def main():
    print("=" * 28)
    print("   欢迎来到猜数字游戏")
    print("=" * 28)

    wins = 0
    rounds = 0

    while True:
        rounds += 1
        if play_round():
            wins += 1

        again = input("\n再来一局？(y/n)：").strip().lower()
        if again not in ("y", "yes", "是"):
            break
        print()

    print(f"\n本局战绩：{wins}/{rounds} 胜")
    print("谢谢游玩！")


if __name__ == "__main__":
    main()
