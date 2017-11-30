

class Admin:
    # admin = "1"
    # passwd = "1"
    def __init__(self,allUsers,admin):
        self.allUsers = allUsers
        self.admin1 = admin                          #将登陆账户初作为类属性储存

    def login(self):

        if not self.allUsers.get(self.admin1):                           #检测用户是否在数据库中，如果没有，会自动跳到创建用户界面
                print("没有此用户，请按照以下步骤创建新账户")
                return False
        user = self.allUsers.get(self.admin1)
        password = input("请输入你的密码：")
        if not user.card.passwd:
            print("密码输入错误")
            return False
        return True




    def welcomeView(self):
        print("*****************************************************************")
        print("*                                                               *")
        print("*                                                               *")
        print("*                        欢迎登陆破烂银行                       *")
        print("*                                                               *")
        print("*                                                               *")
        print("*****************************************************************")


    def startView(self):
        print("*****************************************************************")
        print("*        开户(1)                            查询(2)             *")
        print("*        取款(3)                            存款(4)             *")
        print("*        转账(5)                            改密(6)             *")
        print("*        锁定(7)                            解锁(8)             *")
        print("*        补卡(9)                            销户(0)             *")
        print("*                         退出(t)                               *")
        print("*****************************************************************")
    # def adminOption(self):
    #     Admin = input("请输入管理员账户： ")
    #     if Admin != self.admin:
    #         print("此账户不存在，请重新输入")
    #         return -1
    #     Passwd = input("请输入管理员密码： ")
    #     if Passwd != self.passwd:
    #         print("密码输入错误!")
    #         return -1
    #     #账号密码输入正确以后才能执行后面的代码
    #     print("操作成功，欢迎您的到来，请稍后...")
    #     # time.sleep(3)
    #     return 0