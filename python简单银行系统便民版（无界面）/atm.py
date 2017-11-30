from admin import Admin
import random
from User import User
from Card import Card
import time
# from admin import Admin
class Atm:
    def __init__(self,allUsers,admin):
        self.allUsers = allUsers                  #卡号账户
        self.admin1 = admin


    def createUser(self):                              #创建用户
        name = input("请输入你的姓名: ")
        Id = input("请输入你的身份证号: ")
        Tel = input("请输入你的电话号码: ")

        prestoreMoney = int(input("请输入预存款金额："))
        if prestoreMoney < 0:
            print("预存款金额有误！开户失败....")
            return -1
        while True:
            onePasswd = input("请设置您的六位数密码： ")
            if len(onePasswd) != 6:
                print("密码格式错误，请输入六位数密码，请重新输入：")
                # return -1
                continue
            break
        #开户所需信息齐全

        while True:
            cardId = random.randrange(100000,999999)
            if not self.allUsers.get(cardId):
                break
        card = Card(cardId,onePasswd,prestoreMoney)
        user = User(name,Id,Tel,card)
        #转存到字典
        self.allUsers[cardId] = user

        print("开户成功!!请牢记你的卡号{}".format(cardId))
    def selectInfor(self):                                 #查询信息

        user = self.allUsers.get(self.admin1)

        #判断是否锁定
        if user.card.cardLock:
            print("改卡已经锁定！！请在解锁后在进行其他操作...")
            time.sleep(2)
            return -1


        time.sleep(2)
        print("账户为：{} 余额为：{}元".format(user.card.cardId,user.card.money))
        time.sleep(1)


    def get_Money(self):                                #取款

        user = self.allUsers.get(self.admin1)
                                             #判断卡是否锁定
        if user.card.cardLock:
            print("改卡已经锁定！！请在解锁后在进行其他操作...")
            return -1

        if not check_Password(user):
            return


        get_money = eval(input("请输入你要取款的金额： "))
        if get_money > user.card.money:
            print("您的余额不足，不能取款，余额为{}元".format(user.card.money))
        else:
            user.card.money -= get_money
            print("您本次取款{}元，余额为{}元".format(get_money,user.card.money))
        time.sleep(2)


    def save_Money(self):                              #存款

        user = self.allUsers.get(self.admin1)

        if user.card.cardLock:
            print("改卡已经锁定！！请在解锁后在进行其他操作...")
            return -1

        if not check_Password(user):
            return

        save_Money = eval(input("请输入存款金额： "))
        print("请放入钞票",end="钞票放入成功")
        user.card.money += save_Money
        print("本次存款{}元，账户余额为：{}元".format(save_Money,user.card.money))
        time.sleep(2)


    def transfer_Accounts(self):                     #转账
        trans_Card = int(input("请输入转账卡号： "))
        user1 = self.allUsers.get(trans_Card)
        if not user1:
            print("你输入的账户不存在")
            return -1




        trans_Money = eval(input("请输入转账金额： "))


        user = self.allUsers.get(self.admin1)


        if trans_Money > user.card.money:
            print("你的账户余额不足，转账失败，账户余额为:{}元".format(user.card.money))
            return -1


        user.card.money -= trans_Money
        user1.card.money += trans_Money
        print("您给用户{}转账{}元成功，您的当前余额为：{}元".format(user1.card.cardId,trans_Money,user.card.money))
        time.sleep(2)


    def change_Password(self):                         #修改密码

        user = self.allUsers.get(self.admin1)

        newpasswd = input("请输入你的新密码： ")
        user.card.passwd = newpasswd
        print("账号{}密码修改成功，请牢记您的新密码".format(self.admin1))
        time.sleep(2)


    def card_Lock(self):                        #锁定

        user = self.allUsers.get(self.admin1)

        if  user.card.cardLock:
            print("你的卡已锁定，不需要再次锁定")
            return -1

        tempIdCard = input("请输入你的身份证号：")
        if tempIdCard != user.Id:
            print("身份证号错误，锁定失败")
            return -1


        user.card.cardLock = True
        print("该卡已锁定")
        time.sleep(1)
        # return -1

    def card_ReLock(self):                       #解锁

        user = self.allUsers.get(self.admin1)

        if not user.card.cardLock:
            print("你的卡没有锁定，不需要解锁")
            return -1

        if not check_Password(user):
            return


        tempIdCard = input("请输入你的身份证号：")
        if tempIdCard != user.Id:
            print("身份证号错误，解锁失败")
            return -1

        user.card.cardLock = False
        print("成功解锁")
        time.sleep(2)

    def fill_Card(self):                        #补卡

        user = self.allUsers.get(self.admin1)

        isOK = input("您确定要补卡？ ： ")
        if isOK in ("no"):
            return -1


        if not check_Password(user):
            return

        while True:
            cardId = random.randrange(100000, 999999)
            if not self.allUsers.get(cardId):
                #     continue
                break
        self.allUsers[cardId] = user
        del self.allUsers[self.admin1]
        print("补卡成功，新卡号为：{}".format(cardId))
        time.sleep(2)


    def del_User(self):                             #销户

        isOK = input("您确定要注销本账户： ")
        if isOK in ("no"):
            return -1

        user = self.allUsers.get(self.admin1)

        if not check_Password(user):
            return

        del self.allUsers[self.admin1]
        print("用户注销成功")
        time.sleep(2)


def check_Password(user):               #检测密码

    passwd = input("请输入你的密码：")
    if passwd != user.card.passwd:
        for i in range(1, 3):
            num = 1
            passwd = input("密码错误,请再次输入你的密码： ")
            if passwd == user.card.passwd:
                print("密码输入正确")
                num = 2

                break
        if num == 1:
            user.card.cardLock = True
            print("密码输入错误超过3次，此卡已锁，请解锁后再继续操作")
            time.sleep(1)
            return
    return True

