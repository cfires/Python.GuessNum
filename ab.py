# -*- coding:utf-8 -*-
import random
secret = random.randint(1, 100)
guess = 0
tries = 0
print("这是一个猜数字游戏!")
print("数字是1到99,你有六次机会!")
while guess != secret and tries < 6:
    guess = input(u"请输入数字:")
    if guess < secret:
        print("数字太小...!")
    elif guess > secret:
        print("数字太大...")
    elif guess == secret:
        print("恭喜你猜对了!")
    tries += 1
    if tries == 6:
        print("你6次机会用完了...")
        print("正确的数字是"), secret
        break
