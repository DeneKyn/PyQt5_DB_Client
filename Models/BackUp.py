class BackUp:
    def __init__(self, info):
        self.info = info
        self.id = info[0]
        self.operation_type = info[1]
        self.user_id = info[2]
        self.change_date = info[3]
        self.login = info[4]
        self.password = info[5]
        self.salt = info[6]
        self.role = info[7]
        self.status = info[8]
        self.block_begin = info[9]
        self.block_end = info[10]
        self.register_date = info[11]
        self.id_name1 = info[12]
        self.id_name2 = info[13]
        self.id_name3 = info[14]
        self.id_personal_info = info[15] if info[15] is not None else 'NULL'
