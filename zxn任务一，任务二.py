                                                            #任务一

#1、实现输入10个数字，并打印10个数的求和结果？
'''
i = 1
result = 0
while i <= 10:
    num = int(input(f"请输入第{i}个数字："))
    result += num
    i += 1
print(f"求和结果为：{result}")
'''

#2、从键盘依次输入10个数，最后打印最大的数、10个数的和、和平均数。
'''
i = 1
result = 0
list1 = []
while i <= 10:
    num = int(input(f"请输入第{i}个数字："))
    result += num
    list1.append(num)
    i += 1
list1.sort()
print("最大数为：", list1[-1])
print(f"求和结果为：{result}")
print(f"平均数为：{result / 10}")
'''

#3、使用random模块，如何产生 50~150之间的数？
'''
import random
# 随机整数
suiji = random.randint(50, 150)
print(suiji)
# 随机浮点数
suiji = random.uniform(50, 150)
print(suiji)
'''

#4、从键盘输入任意三边，判断是否能形成三角形，若可以，则判断形成什么三角形（结果判断：等腰，等边，直角，普通，不能形成三角形。）
'''
a = int(input("请输入边a的长度："))
b = int(input("请输入边b的长度："))
c = int(input("请输入边c的长度："))
bian = [a, b, c]
bian.sort()
[a, b, c] = bian
print(a, b, c)
if a + b > c and c - b < a:
    if a == b:
        print("等腰三角形")
    elif a**2 + b**2 == c**2:
        print("直角三角形")
    elif a == b == c:
        print("等边三角形")
    else:
        print("普通三角形")
else:
    print("不能构成三角形")

print(math.sqrt(2))
'''

#5、有以下两个数，使用+，-号实现两个数的调换。
# A=56
# B=78
# 实现效果：
# A=78
# B=56
'''
a=56
b=78
a=a+b
b=a-b
a=a-b
print("使用求和法得出结果：")
print("a变换后为：%d "%a)
print("b变换后为：%d"%b)
'''

#6、实现登陆系统的三次密码输入错误锁定功能（用户名：root,密码：admin）
'''
i = 1
while i <= 3:
    username = input("请输入用户名：")
    password = input("请输入密码：")
    if username == 'root' and password == 'admin':
        print("登录成功！！")
        break
    else:
        if i == 3:
            print("登录次数已达上限")
            break
        print("用户名或密码错误，请重新登录！")
        i += 1
        continue
'''

#7、编程实现下列图形的打印
'''
i = 1
while i <= 7:
    print('  ' * (7 - i) + '*   ' * i)
    i += 1
'''

#8、使用while循环实现99乘法表的打印。
'''
i, j = 1, 1
result = ' '
while j <= 9:
    while i <= j:
        result += f"{i} * {j} = {i * j}\t"
        i += 1
        if i > j:
            i = 1
            print(result)
            result = ' '
            break
    j += 1
'''

#9、编程实现99乘法表的倒叙打印
'''
i, j = 1, 9
result = ' '
while j >= 1:
    while i <= j:
        result += f"{i} * {j} = {i * j}\t"
        i += 1
        if i > j:
            i = 1
            print(result)
            result = ' '
            break
    j -= 1
'''

#10、一只青蛙掉在井里了，井高20米，青蛙白天网上爬3米，晚上下滑2米，问第几天能出来？请编程求出。
'''
h = 20
i = 0
while h > 0:
    h = h - 3
    i += 1
    if h <= 0:
        break
    h = h + 2
print(i)
'''

#11、判断下列变量命名是否合法
# 标识符	是否合法	标识符	是否合法
# char		    Cy%ty
# Oax_li		$123
# fLul		    3_3
# BYTE		    T_T
'''
print("判断上面变量命名是否合法，请在下面标识符：后输入;输入exit，退出判断！")
while True:
    s = input("标识符：")
    if s == "exit":
        print("欢迎下次使用")
        break
    if s[0].isalpha() or s[0] == "_":     #isalpha()函数：用于字符串处理，检查参数是否包含字母；若字符串中所有字符都是字母，则isalpha()方法返回“True”，否则，返回“False”。
        for i in  s[1:]:
            if not(i.isalnum() or i == "_"):     #isalnum()函数:检测一个字符是否为字母或者十进制数字
                print("%s变量命名不合法" %s)
                break
            else:
                print("%s变量命名合法" %s)
                break
    else:
            print("%s变量名不合法" %s)
'''



#12、继续完成上午的猜数字游戏的需求功能。
# 1.	添加计数打印功能
# 2.	添加次数金币功能和锁定系统功能。
'''
import random
capital = 500
count = 0
input_num = input("请输入一个0-20的整数：")
def suiji():
    guess1 = random.randint(0, 20)
    # 显示随机数
    # print(guess1)
    return guess1
def isnum(num):
    while True:
        flag = num.isdigit()
        if flag:
            num = int(num)
            return num
        else:
            print("注意：请输入0-20的整数！！！")
def compare(num, cap, coun):
    guess = suiji()
    while True:
        if num < guess:
            cap -= 100
            coun += 1
            if coun == 3:
                print(f"您已经猜错{coun}次了，游戏结束！")
                break
            if cap <= 0:
                print("您的资金已经为0,游戏结束")
                break
            print(f"您输入的数字偏小了,当前资金剩余{cap},您已经猜错{coun}次了,还有{3 - coun}次机会,请重新输入：")
            num = isnum(input("请输入一个0-20的整数："))
            continue
        elif num > guess:
            cap -= 100
            coun += 1
            if coun == 3:
                print(f"您已经猜错{coun}次了，游戏结束！")
                break
            if cap <= 0:
                print("您的资金已经为0,游戏结束")
                break
            print(f"您输入的数字偏大了,当前资金剩余{cap},您已经猜错{coun}次了,还有{3 - coun}次机会,请重新输入：")
            num = isnum(input("请输入一个0-20的整数："))
            continue
        else:
            coun = 0
            cap += 10
            print(f"恭喜你猜对了！！,当前资金为{cap}")
            guess = suiji()
            num = isnum(input("请输入一个0-20的整数："))
            continue

input_num = isnum(input_num)
compare(input_num, capital, count)
'''


#13、用循环来实现20以内的数的阶乘。（1! +2!+3!+…..+20!）
'''
import math
i = 1
result = 0
while i <= 20:
    result += math.factorial(i)
    i += 1
print(result)
#不使用math函数
i = 1
j = 1
result = 0
res = 1
while i <= 20:
    while j <= i:
        res *= j
        j += 1
    result += res
    i += 1
print(result)
'''



                                                             #任务二

#1、有一个列表，[“北京”,”上海”,”广东”]
# 1)	将中国所有省会城市添加到上述列表中
list=["北京","上海","广东"]
for i in range (31):
  name = input("请输入其他省份城市")
  list.append(name)
print(list)
# 2)	广东成为第二大发达城市，将广东排在上海前面
list = ["北京","上海","广东"]
list[1] = '广东'
list[2] = '上海'
print(list)
# 3)	[36710.36,35427.10,29863.23,29667.39,27665.36,27650.45,27620.38,25369.20]这是中国GDP排名前8的城市的GDP数值，请统计前8城市的GDP总和，平均GDP。
list=[36710.36,35427.10,29863.23,29667.39,27665.36,27650.45,27620.38,25369.20]
n=0
for i in range (7):
  n=n+list[i]
print(n)

#2、有以下一个列表，求其中是5的倍数的和
'''
a = [1,5,21,30,15,9,30,24]
a = [1, 5, 21, 30, 15, 9, 30, 24]
result = 0
for i in range(len(a)):
    if a[i] % 5 == 0:
        result += a[i]
    else:
        continue

print(result)

dict1 = {
    'first': 1,
    'second': 2,
    'third': 3,
}
for m, n in dict1.items():
    print(m, n)
'''




#3、有下列列表，请编程实现列表的数据翻转（京东金融的测试开发笔试题）
# List = [1,2,3,4,5,6,7,8,9]
# 实现效果：list = [9,8,7,6,5,4,3,2,1]
'''
List=[1,2,3,4,5,6,7,8,9,]
list=List[::-1]  #从倒数最后一个数字往前进行降值输出
print(list)
'''


# 4、请编程统计列表中的每个数字出现的次数(百度初级测试开发笔试题)
# List = [1,4,7,5,8,2,1,3,4,5,9,7,6,1,10]
'''
List = [1,4,7,5,8,2,1,3,4,5,9,7,6,1,10]
a = set(List)
for n in a:
    print(f"数字{n}出现了{List.count(n)}次！！！")
'''









