import random
print("==============================================")
print("|------------中国工商银行账户管理系统------------|")
print("|------------1、开户              ------------|")
print("|------------2、取钱              ------------|")
print("|------------3、存钱              ------------|")
print("|------------4、转账              ------------|")
print("|------------5、查询              ------------|")
print("|------------6、退出              ------------|")
print("==============================================")
bank={}#创建一个空的字典
bank_name="银行"
def bank_adduser(account,username,password,country,province,street,door):
    if  len(bank) >100:
        return 3
    if account in bank:#  如变量在容器内执行下面的代码
        return 2
    bank[account]={
        "username":username,#
        "password":password,
        "country":country,
        "province":province,
        "street":street,
        "door":door,
        "money":0,
        "bank_name":bank_name
    }
    return 1
def adduser():#定义了一个方法
    username=input("请输入您的用户名")
    password = input("请输入您的密码")
    print("请输入您的地址")
    country=input("\t\t请输入您的国家")
    province=input("\t\t请输入您的省份")
    street=input("\t\t请输入您的街道")
    door=input("\t\t请输入您的门牌号")
    account=random.randint(10000000,99999999)
    stast=bank_adduser(account,username,password,country,province,street,door)
    #        调用方法   （元素，，，，，，，，，）
    if stast ==3 :
        print("你去别的银行吧")
    elif stast== 2:
        print("开户失败，你别重复")
    elif stast== 1:
        info = '''  
                    ------------个人信息------------
                    用户名:%s
                    账号：%s
                    密码：*****
                    国籍：%s
                    省份：%s
                    街道：%s
                    门牌号：%s
                    余额：%s
                    开户行名称：%s
                    --------------------------------
                '''
        # 每个元素都可传入%
        print(info % (username, account, country, province, street, door, bank[account]["money"], bank_name))
#查询
def select():
    acc=input("请输入账号：")
    acc=int(acc)
    if acc in bank:
        upass = input("请输入密码")
        if upass == bank[acc]["password"]:
            info = '''
                                                ------------个人信息------------
                                                账号：%s
                                                用户名:%s
                                                密码：*****
                                                地址：%s%s%s%s
                                                余额：%s
                                                开户行名称：%s
                                                --------------------------------
                                            '''
            print(info % (acc,
                          bank[acc]['username'],
                          bank[acc]['country'],
                          bank[acc]['province'],
                          bank[acc]['street'],
                          bank[acc]['door'],
                          bank[acc]["money"],
                          bank[acc]['bank_name']))

        else:
            print("密码错误")
    else:
        print("账号不存在！")


#存钱
def put():
    uaccount=input("请输入账号：")
    uaccount=int(uaccount)
    if uaccount in bank:
        upassword=input("请输入密码：")
        if upassword == bank[uaccount]["password"]:
            money = int(input("请输入存入的金额："))
            bank[uaccount]["money"]+=money
            print("您的余额为：",bank[uaccount]["money"])
        else :
            print("密码错误！")
    else :
        print("false")
#取钱
def take():
    name=input("请输入账号：")
    name=int(name)
    if name in bank :
        npass=input("请输入密码：")
        if npass == bank[name]["password"]:
           mon=input("请输入取出的金额：")
           mon=int(mon)
           bank[name]["money"]=int(bank[name]["money"])
           if  bank[name]["money"] >= mon:
                bank[name]["money"]=bank[name]["money"]-mon
                print("取出成功，您的余额为：",bank[name]["money"])
           else :
                return Return(3)

        else :
            return Return(2)

    else:
        return Return(1)
#转账

def transfer():
    while 1 :
        in_account = input("请输入转入的账号：")
        out_account = input("请输入转出的账号：")
        in_account = int(in_account)
        out_account = int(out_account)
        if out_account == in_account :
            print("不能自己给自己转账！")
        else :
            if in_account in bank and out_account in bank:
                out_password = input("请输入转出账号的密码：")
                if out_password == bank[out_account["password"]]:
                    out_money = input("请输入转出的金额：")
                    out_money = int(out_money)
                    bank[out_account]["money"] = int(bank[out_account]["money"])
                    bank[in_account]["money"] = int(bank[in_account]["money"])
                    if bank[out_account]["money"] >= out_money:
                        bank[out_account]["money"] = bank[out_account]["money"] - out_money
                        bank[in_account]["money"] = bank[in_account]["money"] + out_money
                        print("转出的金额为：",out_money)
                        print("输入账户的余额为：")
                        print(bank[in_account]["money"])
                        print("输出账户的余额为：")
                        print(bank[out_account]["money"])
                        break
                    else:
                        return Return(3)

                else:
                    return Return(2)

            else:
                return Return(1)

#返回值
def Return(num):
    if num == 1:
        print("您输入的账号不对：")
    elif num == 2:
        print("您输入的密码不对：")
    elif num == 3:
        print("您的钱不够：")
    else:
        print("")




while True:
    begin = input("请选择业务")
    if begin =="1":#您输入的业务等于1执行开户操作
        adduser()
    elif begin == "2":
        put()
    elif begin == "3":
        take()
    elif begin == "4":
        transfer()
    elif begin == "5":
        select()
    else:
        print("Byebye")
        break