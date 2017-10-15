class Massage0:
    def __init__(self, masterType, subType, time, info):
        self.version = "0"  # 版本号
        self.time = time  # 时间戳
        self.masterType = masterType  # 主类型
        self.subType = subType  # 副类型
        self.info = info  # 消息本体
        self.check = ""  # 验证体
