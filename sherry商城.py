#
#      shreey的商城：
#      1、准备商品
#      2、空的购物车
#      3、钱包初始化金钱
#      4、最后打印购物小票
# 1.业务:
#      看到商品：
#          商品存在
#              看金钱够：
#                   成功加入购物车
#                   余额减去对应价格
#              不够
#                 穷鬼，去买其他商品
#          商品不存在
#              输入非法
#          输入q或Q退出并结算，打印小票
# 任务：尽量多的添加商品
# 任务：10个辣条优惠券(0.3),20机械革命优惠券（0.9）
#      在进入商城是，随机抽取优惠券，在最后结算使用优惠券。
#
# 1.商品
shop = [
    #角标   0        ,     1
    ["机械革命"   ,   15000],#0 print(shop[0][1])=15000
    ["HUAWEI watch", 1200],#1 print(shop[1][1])=1200
    ["MAC PC",       13000],#2 print(shop[2][1])=13000
    ["Iphone 54 plus",45000],#3 print(shop[3][1])=45000
    ["辣条"           ,2.5],#4 print(shop[4][1])=45000
    ["老干妈"          ,13],#5 print(shop[5][1])=45000
    ["水杯"           ,20],#6 print(shop[6][1])=45000
]
#print(shop[0][0])
#2.初始化你的金额
moeny=int(input("请输入你的金额"))#str

#3.准备一个空的购物车
mycart=[]
#进入商城领取优惠券
import random
cheap=["辣条优惠券3折","机械革命优惠券9折"]
a=random.randint(0,1)
b=a
a=cheap[a]
print("您已领取成功优惠券",a)

#4.购买
while True: #永远循环
    for index,value in enumerate(shop):#枚举，把角标和角标对应的内容进行整体打印
        print(index,value)#打印所有的商品
    chose=input("请输入你想要的商品")#int 如果你一开始就是数字，那么下面的if就没有意义
    if chose.isdigit():#isdigit-判断是否为数字
        chose =int(chose)
        if chose>len(shop)-1:#你输入的角标，如果大于商品的长度就执行代码
            print("你所输入的商品不存在")
            break
        else:
            mycart.append(shop[chose])#加入购物车
            if moeny< shop[chose][1] :#你原有存款和商品价格对比
                print("你的余额不足，欢迎下次光临！")
            elif b==0 and chose==4:
                moeny = moeny=moeny-shop[chose][1]*0.3
                moeny=round(moeny,2)
                print("您的余额还剩:",moeny,"元")
            elif b==1 and chose==0:
                moeny = moeny = moeny - shop[chose][1] * 0.9
                moeny = round(moeny, 2)
                print("您的余额还剩:", moeny, "元")
            else:
                moeny=moeny-shop[chose][1]#存款减去商品价格
                print("恭喜你购买成功，已经加入购物车")
    elif chose == "q" or chose == "Q":
        print("欢迎下次光临，下面的是您的小票")
        for index,value in enumerate(mycart):
            print(index," ",value)
        print("您的余额还剩:",moeny,"元")
        break
    else:
        print("输入非法")
