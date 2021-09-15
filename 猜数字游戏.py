
'''
猜字游戏
需求：
1、猜的数字是系统产生的，不是自己定义的
2、键盘输入的   操作完填入：input（“提示”）
3、判断			操作完填入：if判断条件 elif 判断条件。。。。。。Else
4、循环			操作完填入：while 条件循环
如果你的num>ran打印猜大了    <  猜小了
初始金额为500 每猜一次扣除100  如果资金为0 退出系统
如果三次没有猜中那就退出
！！！如果猜的正确的那么增加10，随机数不能只随机一次
'''
import random # import 引模块、包。
ran=random.randint(0,80)
print("ran")
i=int(500)
print("猜数字(500)")
q=0
while True:
    i=i-100
    num = input("请输入一个数字")
    num=int(num)
    if num==ran:
        print("ok",i+10)
        break
    else:
        if num < ran:
            print("猜小了，你的金额还有",i)
            q=q+1
            if q >= 3:
                print("猜错三次游戏结束")
                break
            if i<=0:
                break
        elif num>ran:
                print("猜大了，你的金额还有",i)
                q=q+1
                if q>=3:
                    print("猜错三次游戏结束")
                    break
                if i <= 0:
                    break








