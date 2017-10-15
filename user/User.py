from tools import getRandomStr


class User:
    def __init__(self, name, password, public, parent=""):
        self.name = name  # 账号名 string 不变
        self.parent = parent  # 邀请者 string 不变
        self.password = password  # 密码 string 可变
        self.addurl = getRandomStr.random_str(6)  # 用来添加好友的唯一码 string 可变
        self.friends = []  # 好友列表 [name] 可变
        self.rooms = []  # 房间列表 [id] 可变
        self.massageBox = []  # 消息队列 [massage] 可变
        self.public = public

        self.key = getRandomStr.random_str(128)  # 在线的cookie，每次登录都会改变，用来代替验证 string 可变

    def updateKey(self, oldKey):
        if oldKey == self.key:
            self.key = getRandomStr.random_str(128)

    def updatePassword(self, oldPassword, newPassword):
        if oldPassword == self.password:
            self.password = newPassword

    def updateAddURL(self, key):
        if key == self.key:
            self.addurl = getRandomStr.random_str(6)

    def pushMassage(self, massage):
        self.massageBox.append(massage)

    def popMassages(self, key):
        if key == self.key:
            tmpBox = self.massageBox[:]
            self.massageBox = []
            return tmpBox
