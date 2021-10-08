import pymysql

con = pymysql.connect(host="localhost", user="root", password="", database="company")
# 创建控制台
cursor = con.cursor()

import random

print("==============================================")
print("|------------中国工商银行账户管理系统------------|")
print("|------------1、开户              ------------|")
print("|------------2、存钱              ------------|")
print("|------------3、取钱              ------------|")
print("|------------4、转账              ------------|")
print("|------------5、查询              ------------|")
print("|------------6、退出              ------------|")
print("==============================================")
bank = {}
    # 'a': {'account': 1, 'password': '1234', 'country': '1', 'province': '1', 'street': '1', 'door': '1', 'money': 10000,
    #       'bank_name': '狼腾测试猿银行'},
    # 'b': {'account': 2, 'password': '1234', 'country': '1', 'province': '1', 'street': '1', 'door': '1', 'money': 100,
    #       'bank_name': '狼腾测试猿银行'}}
# 创建一个空的字典
# 开户逻辑
# aaa=input("111")
# bbb=input("222")
# print(bank[aaa][bbb])
bank_name = "狼腾测试猿银行"
# 执行
#                第一个对应第一个 不是名称对应名称
def bank_adduser(account, username, password, country, province, street, door, money):
    sql1 = "select count(*) from bank"
    cursor.execute(sql1)
    data = cursor.fetchall()
    if data[0][0] >= 100:
        return 3
    sql2 = "select * from bank where username = %s"
    param = username
    cursor.execute(sql2, param)
    data = cursor.fetchall()
    # 如变量在容器内执行下面的代码
    if len(data) != 0:
        return 2

    else:
        sql = "insert into bank value (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        param = [account, username, password, country, province, street, door, money, bank_name]
        cursor.execute(sql, param)
        con.commit()
        # bank[username] = {
        #     "account": account,  #
        #     "password": password,
        #     "country": country,
        #     "province": province,
        #     "street": street,
        #     "door": door,
        #     "money": 0,
        #     "bank_name": bank_name
        # }
        return 1


# 提交


def adduser():  # 定义了一个方法
    """

    :rtype: object
    """
    username = input("请输入您的用户名")
    password = input("请输入您的密码")
    print("请输入您的地址")
    country = input("\t\t请输入您的国家")
    province = input("\t\t请输入您的省份")
    street = input("\t\t请输入您的街道")
    door = input("\t\t请输入您的门牌号")
    money = 0
    account = random.randint(10000000, 99999999)
    stat = bank_adduser(account, username, password, country, province, street, door, money)
    # 调用方法   （元素，，，，，，，，，）
    if stat == 3:
        print("你去别的银行吧")
    elif stat == 2:
        print("开户失败，你别重复")
    elif stat == 1:
        info = '''
                    ------------个人信息------------
                    用户名:%s
                    账号：%s
                    密码：%s
                    国籍：%s
                    省份：%s
                    街道：%s
                    门牌号：%s
                    余额：%s
                    开户行名称：%s
                '''
        # 每个元素都可传入%
        print(info % (account, username, password, country, province, street, door, money, bank_name))


# {'frank': {'account': 88474479, 'password': '1234', 'country': '1', 'province': '1', 'street': '1', 'door': '1', 'money': 0, 'bank_name': '狼腾测试猿银行'}}
# 存钱
def addmoney():

    account = int(input("请输入您的账号"))
    sql ="select * from bank where account=%s"
    param=(account)
    cursor.execute(sql,param)
    con.commit()
    data=cursor.fetchall()
    if len(data) !=0:
        money1 = input("请输入想要储蓄的金额：")
        sql = "update bank set money=money+%s  where account=%s "
        param=(money1,account)
        cursor.execute(sql,param)
        con.commit()
        print("储存成功")
    else:
        return 0

    return 1


    # account = list(bank.keys())
    # for i in range(len(account)):
    #     if account == bank[account[i]]['account']:
    #         money = bank[account[i]]['money']
    #         print("您的余额：", money)
    #         money1 = int(input("请输入想要储蓄的金额："))
    #         money = money + money1
    #         bank[account[i]]['money'] = money
    #         info = '''
    #                     ------------个人信息------------
    #                     用户名:%s
    #                     账号：%s
    #                     余额：%s
    #                     开户行名称：%s
    #                 '''
    #         # 每个元素都可传入%
    #         print(info % (account[i], account, money, bank_name))
    #         sql3 = "insert into bank value (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    #         param = [account, account, money, bank_name]
    #         cursor.execute(sql3, param)
    #         con.commit()

#取钱
def remoney():
    account = int(input("请输入您的账号"))
    password = int(input("请输入您的密码"))
    sql ="select * from bank where account=%s or password=%s"
    param=(account,password)
    cursor.execute(sql,param)
    con.commit()
    data=cursor.fetchall()
    if len(data) !=0:
        money1 = input("请输入想要取的金额：")
        money1=int(money1)
        sql = "select money from bank where account=%s or password=%s"
        param = (account, password)
        cursor.execute(sql, param)
        con.commit()
        money = cursor.fetchall()
        money=money[0][0]
        if money1<=money:
            sql = "update bank set money=money-%s  where account=%s "
            param=(money1,account)
            cursor.execute(sql,param)
            con.commit()
            print("取成功")
        else:
            print("余额不足")
    else:
        return 0



# 取钱
# def  bank_addcunqian(account, password, username, money):
#     account = int(input("请输入您的账号"))
#     c
#     sql = "select * from bank where account=%s or password=%s"
#     param = (account,password)
#     cursor.execute(sql, param)
#     con.commit()
#     data = cursor.fetchall()
#     if len(data) != 0:
#         money=input("输入想要取出的金额")
#         param = (money, account)
#         cursor.execute(sql, param)
#         con.commit()
#         print("取钱成功")
#     else:
#         print(1)


# if money <= money:
#         money = money - money
#     else:
#         print("余额不足")
#     if account in bank.values():
#         if password in bank.values():
#             if username in bank.values():
#                 money = money - money
#             else:
#                 return 3
#         else:
#             return 2
#     else:
#         bank[username] = {
#             "account": account,  #
#             "password": password,
#             "money": money,
#         }
#          return 1


# def remoney():
#     account = int(input("请输入您的账号："))
#     password = input("请输入您的密码：")
#     username = list(bank.keys())
#     for i in range(len(username)):
#         if account == bank[username[i]]['account']:
#             if password == bank[username[i]]['password']:
#                 money = bank[username[i]]['money']
#                 print("您的余额：", money)
#                 money1 = int(input("请输入想要取出的金额："))
#                 if money1 <= money:
#                     money = money - money1
#                     bank[username[i]]['money'] = money
#                     info = '''
#                                     ------------个人信息------------
#                                     用户名:%s
#                                     账号：%s
#                                     余额：%s
#                                     开户行名称：%s
#                                 '''
#                     # 每个元素都可传入%
#                     print(info % (username[i], account, money, bank_name))
#                 else:
#                     print(("余额不足"))
#             else:
#                 print("密码错误")
#         else:
#             print("账号不存在")
#             return 1
#转账
def addzhuanru():
    account = int(input("请输入您的账号"))
    password =int(input("输入您的密码"))
    accountout = int(input("请输入您的转出账号"))
    sql ="select * from bank where account=%s"
    param=account
    cursor.execute(sql,param)
    data=cursor.fetchall()
    if len(data) !=0:
        sql = "select password from bank where account=%s"
        param = account
        cursor.execute(sql, param)
        data = cursor.fetchall()
        if data[0][0]==password:
            sql = "select * from bank where account=%s"
            param = accountout
            cursor.execute(sql, param)
            data = cursor.fetchall()
            if len(data)!=0:
                money=input("请输入要转账的金额")
                money=int(money)
                sql ="update bank set money=money-%s  where account=%s "
                param=(money,accountout)
                cursor.execute(sql,param)
                con.commit()
            else:
                return fanhui(3)
        else:
            return fanhui(2)
    else:
        return fanhui(1)


# def addzhuanru():
#     while 1:
#         accoutin = input("请输入转入的账号")
#         accoutout = input("请输入转出的账号")
#         accoutin = int(accoutin)
#         accoutout = int(accoutout)
#         if accoutout == accoutin:
#             print("转账失败")
#         else:
#             if accoutout in bank and accoutin in bank:
#                 passwordout = input("请输入转出账号密码")
#                 if passwordout == bank[passwordout]["password"]:
#                     moneyout = int(input("请输入转账金额"))
#                     if bank[accoutout]["money"] >= moneyout:
#                         print("输入账户余额")
#                         print(bank[accoutin]["money"])
#                         break
#                     else:
#                         return fanhui(3)
#                 else:
#                     return fanhui(2)
#             else:
#                 return fanhui(1)


# 返回
def fanhui(num):
    if num == 1:
        print("账号不对")
    elif num == 2:
        print("您输入密码不对")
    elif num == 3:
        print("money不够")
    else:
        print("")


# 查询
def chaxun():
    account = int(input("请输入您的账号"))
    password = int(input("请输入您的密码"))
    sql ="select account from bank where account=%s"
    param1=[account]
    data =cursor.execute(sql,param1)
    if data > 0:
        sql = "select password from bank where password=%s and account = %s"
        param2 = [password,param1]
        data = cursor.execute(sql, param2)
        if data > 0:
            sql2 = "select * from bank where account = %s"
            fin = [account]
            cursor.execute(sql2,fin)
            data = cursor.fetchone()
            info = '''
                                ------------个人信息 - -----------
                                用户名: %s
                                账号： %s
                                密码： ******
                                余额： %s
                                开户行名称： %s
                        '''
            print(info % (data[1],data[0],data[7],data[8]))
        else:
            print("密码错误")
    else:
        print("账号不存在")




# def chaxun():
#     account = int(input("请输入账号"))
#     if account in bank:
#         password = int(input("请输入账号密码"))
#         if password == bank[account]["password"]:
#             info = '''
#                     ------------个人信息 - -----------
#                     用户名: %s
#                     账号： %s
#                     密码： ** ** *
#                     余额： %s
#                     开户行名称： %s
#                         '''
#             print(info % (account,
#                           bank[account]["username"],
#                           bank[account]["password"],
#                           bank[account]["money"],
#                           bank[account]["bank_name"]
#                           ))
#         else:
#             print("密码错误")
#     else:
#         print("账号不存在")


def goodbye():
    print("再见")
    cursor.close()
    con.close()


while True:
    begin = input("请选择业务")
    if begin == "1":  # 您输入的业务等于1执行开户操作
        adduser()
    elif begin == "2":
        addmoney()
    elif begin == "3":
        remoney()
    elif begin == "4":
        addzhuanru()
    elif begin == "5":
        chaxun()
    else:
        goodbye()
        break
