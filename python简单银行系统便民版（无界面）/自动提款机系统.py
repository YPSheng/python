from admin import Admin
from atm import Atm
import pickle
import time
import os
# import admin


def main():
    filepath = os.path.join(os.getcwd(), "allusers.txt")

    f = open(filepath, "rb")

    allUsers = pickle.load(f)

    admin1 = int(input("请输入你的卡号："))
    admin = Admin(allUsers,admin1)               #将登陆账户传入到用户类中储存

    atm = Atm(allUsers,admin1)                    #将登陆账户传入到atm类中储存
    if admin.login():

        admin.welcomeView()

        print("*********************************************************")
        # print(allUsers)
        print("请选择一下功能选项：")
        time.sleep(2)

        while True:
            admin.startView()
            option = input("请输入你要办理的业务号：")
            if option == '1':
                atm.createUser()
            elif option == '2':
                atm.selectInfor()
            elif option == '3':
                atm.get_Money()
            elif option == '4':
                atm.save_Money()
            elif option == '5':
                atm.transfer_Accounts()
            elif option == '6':
                atm.change_Password()
            elif option == '7':
                atm.card_Lock()
            elif option == '8':
                atm.card_ReLock()
            elif option == '9':
                atm.fill_Card()
            elif option == '0':
                atm.del_User()
            elif option == 't':
                f = open(filepath,"wb")
                pickle.dump(allUsers,f)
                f.close()
                break
            # time.sleep(2)
    else:
        atm.createUser()
        while True:
            admin.startView()
            option = input("请输入你要办理的业务号：")
            if option == '1':
                atm.createUser()
            elif option == '2':
                atm.selectInfor()
            elif option == '3':
                atm.get_Money()
            elif option == '4':
                atm.save_Money()
            elif option == '5':
                atm.transfer_Accounts()
            elif option == '6':
                atm.change_Password()
            elif option == '7':
                atm.card_Lock()
            elif option == '8':
                atm.card_ReLock()
            elif option == '9':
                atm.fill_Card()
            elif option == '0':
                atm.del_User()
            elif option == 't':
                f = open(filepath, "wb")
                pickle.dump(allUsers, f)
                # f.write(allUsers.encode("utf-8"))
                f.close()
                # return -1
                break

if __name__ == "__main__":

    main()



