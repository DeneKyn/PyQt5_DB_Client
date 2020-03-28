class User:
    def __init__(self, info):
        self.info = info
        self.id = info[0]
        self.login = info[1]
        self.status = info[2]
        self.role = info[3]
        self.block_begin = info[4]
        self.block_end = info[5]
        self.registration_date = info[6]
        self.name1 = info[7]
        self.name2 = info[8]
        self.name3 = info[9]
        self.id_personal_info = info[10]


