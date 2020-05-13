class User:
    def __init__(self, info):
        self.info = info
        self.id = info.get('id', None)
        self.password = info.get('password', None)
        self.salt = info.get('salt', None)
        self.login = info.get('login', None)
        self.status = info.get('status', None)
        self.role = info.get('role', None)
        self.block_begin = info.get('block_begin', None)
        self.block_end = info.get('block_end', None)
        self.registration_date = info.get('registration_date', None)
        self.name1 = info.get('name1', None)
        self.name2 = info.get('name2', None)
        self.name3 = info.get('name3', None)
        self.id_personal_info = info.get('id_personal_info', None)
        self.company_name = info.get('company_name', None)
