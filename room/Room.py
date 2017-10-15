from tools import getRandomStr


class Room:
    number = 0

    def __init__(self, creator, name=""):
        self.ID = Room.number  # Room的ID int 不变
        Room.number += 1
        self.creator = creator  # 创建者 user.name 不变
        self.name = name  # 房间名 string 可变
        self.addURList = [(getRandomStr.random_str(12)), creator]  # 进房间邀请号 [(URL user.name)] 可变

        self.userList = [creator]  # 用户列表 [user.name] 可变

        self.massageBox = []  # 消息队列 [massage] 可变

        self.aes = getRandomStr.random_str(512)  # 对称秘钥 string 可变
        self.public = ""  # 非对称加密的公钥 string 不变
        self.private = ""  # 非对称加密的秘钥 string 不变
