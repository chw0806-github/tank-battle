# 简单示例：猜数字

import random

secret = random.randint(1, 10)
print("我想了一个 1～10 的数字，来猜猜看！")

while True:
    guess = int(input("你的猜测："))
    if guess < secret:
        print("太小了")
    elif guess > secret:
        print("太大了")
    else:
        print("猜对了！")
        break
