import pymysql
import pymysql.cursors
import hashlib
import os
import re
from datetime import datetime
from Models.BackUp import BackUp
from Models.User import User
from Models.UserStatus import UserStatus


def is_user_ban(block_end):
    if type(block_end) == datetime:
        diff = int((block_end - datetime.now()).total_seconds())
        print(diff)
        if diff > 0:
            return True
    return False


class DBHelper:
    def __init__(self):
        self.connect = pymysql.connect(
            host='192.168.83.130',
            user='student',
            password='student',
            db= 'OnlineStoreDB',
            charset='utf8mb4'
        )
        self.cursor = self.connect.cursor()

    def update_user_type(self, login, user_type):
        self.cursor.execute(f"UPDATE users SET "
                            f"role = '{user_type}' "
                            f"WHERE login = '{login}' ")
        self.cursor.fetchone()
        self.connect.commit()

    def unlock_user(self, login):
        self.cursor.execute(f"UPDATE users SET "
                            f"block_begin = NULL, block_end= NULL, status='{UserStatus.Active.value}' "
                            f"WHERE login = '{login}'")
        self.cursor.fetchone()
        self.connect.commit()

    def block_user_forever(self, login):
        self.cursor.execute(f"UPDATE users SET "
                            f"block_begin = NOW(), block_end='2038-01-01', status='{UserStatus.Blocked.value}' "
                            f"WHERE login = '{login}'")
        self.cursor.fetchone()
        self.connect.commit()


    def block_user_temporary(self, login, seconds):
        self.cursor.execute(f"UPDATE users SET "
                            f"block_begin = NOW(), block_end = NOW() + INTERVAL {seconds} SECOND ,"
                            f" status='{UserStatus.Blocked.value}' "
                            f"WHERE login = '{login}'")
        self.cursor.fetchone()
        self.connect.commit()
        self.create_unlock_event(login, seconds)

    def create_unlock_event(self, login, seconds):
        self.cursor.execute(f"DROP EVENT IF EXISTS unlock_event_{login}")
        self.connect.commit()
        self.cursor.execute(f"CREATE EVENT unlock_event_{login} "
                            f"ON SCHEDULE "
                            f"AT NOW() + INTERVAL {seconds} SECOND "
                            f"DO "
                            f"UPDATE users SET "
                            f"block_begin = NULL, block_end= NULL, status='{UserStatus.Active.value}'  "
                            f" WHERE login = '{login}' ")
        self.connect.commit()

    def insert_lock_row(self, table, key, value):
        self.cursor.execute(f"LOCK TABLE {table} WRITE ")
        self.cursor.execute(f"INSERT IGNORE INTO {table}({key}) VALUES ('{value}') ")
        self.cursor.execute("UNLOCK TABLE ")
        self.cursor.fetchone()

    def backup_user(self):
        self.cursor.execute("SELECT * FROM users_backup ORDER BY change_date DESC limit 1")
        result = self.cursor.fetchone()

        if result is not None:
            backup = BackUp(result)
            if not is_user_ban(backup.block_end):
                backup.block_end = None
                backup.block_begin = None
                backup.status = UserStatus.Active.value

            self.cursor.execute(f"DELETE FROM users_backup WHERE id = {backup.id}")
            self.connect.commit()

            if backup.operation_type == "Update":
                self.backup_user_on_update(backup)
            elif backup.operation_type == "Delete":
                self.backup_user_on_delete(backup)
        else:
            raise ValueError('No more backups')

    def backup_user_on_delete(self, backup):
        sql_query = f"INSERT INTO users(id, login, password, salt, status, role, block_begin, block_end, " \
                    f"registration_date, id_name1, id_name2, id_name3, id_personal_info) " \
                    f"VALUES ({backup.user_id}, '{backup.login}', '{backup.password}', '{backup.salt}', " \
                    f"'{backup.status}', '{backup.role}', '{backup.block_begin}', '{backup.block_begin}', " \
                    f"'{backup.register_date}', {backup.id_name1}, {backup.id_name2}, {backup.id_name3}, " \
                    f"{backup.id_personal_info}) ".replace("'None'", "NULL")
        self.cursor.execute("LOCK TABLE users WRITE, users_backup READ ")
        self.cursor.execute(sql_query)
        self.cursor.execute("UNLOCK TABLE ")
        self.connect.commit()

    def backup_user_on_update(self, backup):
        sql_query = f"UPDATE users SET " \
                   f"password = '{backup.password}', salt = '{backup.salt}', role = '{backup.role}', " \
                   f"status = '{backup.status}', block_begin = '{backup.block_begin}', " \
                   f"block_end = '{backup.block_end}', id_name1 = {backup.id_name1}, " \
                   f"id_name2 = {backup.id_name2}, id_name3 = {backup.id_name3}, " \
                   f"id_personal_info = {backup.id_personal_info} " \
                   f"WHERE id = '{backup.user_id}'".replace("'None'", "NULL")

        self.cursor.execute("LOCK TABLE users WRITE, users_backup WRITE ")
        self.cursor.execute(sql_query)
        self.cursor.execute("UNLOCK TABLE ")
        self.connect.commit()

        self.cursor.execute(f"DELETE FROM users_backup"
                            f" WHERE user_id = {backup.user_id}"
                            f" ORDER BY change_date DESC limit 1")
        self.connect.commit()

    def create_user(self, login, password, role, name1, name2, name3):
        salt = os.urandom(32).hex()
        hash_pass = hashlib.sha512(password.encode('utf-8') + salt.encode('utf-8')).hexdigest()

        self.insert_lock_row('names1', 'name1', name1)
        self.insert_lock_row('names2', 'name2', name2)
        self.insert_lock_row('names3', 'name3', name3)

        self.cursor.execute(
            f"INSERT INTO users(login, password, salt, role, status, registration_date, id_name1, id_name2, id_name3) \
            VALUES ('{login}', '{hash_pass}', '{salt}', '{role}', '{UserStatus.Active.value}', NOW(), \
            (SELECT id FROM names1 WHERE name1='{name1}'), \
            (SELECT id FROM names2 WHERE name2='{name2}'), \
            (SELECT id FROM names3 WHERE name3='{name3}'));"
            )

        self.cursor.fetchone()
        self.connect.commit()

    def delete_user(self, login):
        self.cursor.execute(f"DELETE FROM users WHERE login='{login}'")
        self.cursor.fetchone()
        self.connect.commit()

    def get_search_users(self, status='', user_type='', name1='', name2='', name3=''):
        self.connect.commit()
        sql_query = f"SELECT users.id, login, status, role, block_begin, block_end, registration_date, \
                            name1, name2, name3, id_personal_info FROM users \
                            INNER JOIN names1 ON users.id_name1 = names1.id \
                            INNER JOIN names2 ON users.id_name2 = names2.id \
                            INNER JOIN names3 ON users.id_name3 = names3.id \
                            WHERE \
                            name1 like '%{name1}%' AND \
                            name2 like '%{name2}%' AND \
                            name3 like '%{name3}%' "
        if user_type:
            sql_query += f"AND role = '{user_type}' "
        if status:
            sql_query += f"AND status = '{status}' "

        users = []
        self.cursor.execute(sql_query)
        kek = self.cursor.fetchall()

        for user in kek:
            users.append(User(user))
        return users

    def login_user(self, login, password):
        self.connect.commit()
        self.cursor.execute(f"SELECT salt FROM users WHERE login = '{login}'")
        salt = self.cursor.fetchone()

        if salt is not None:
            pass_hash = hashlib.sha512(password.encode('utf-8') + salt[0].encode('utf-8')).hexdigest()
            self.cursor.execute(f"SELECT id FROM users WHERE login = '{login}' AND password = '{pass_hash}'")
            id_user = self.cursor.fetchone()

            if id_user is not None:
                self.cursor.execute(f"SELECT users.id, login, status, role, block_begin, block_end,"
                                    f" registration_date, name1, name2, name3, id_personal_info FROM users "
                                    f"INNER JOIN names1 ON users.id_name1 = names1.id "
                                    f"INNER JOIN names2 ON users.id_name2 = names2.id "
                                    f"INNER JOIN names3 ON users.id_name3 = names3.id "
                                    f"WHERE users.id = {id_user[0]} AND users.status = '{UserStatus.Active.value}' ")
                user = self.cursor.fetchone()

                self.connect.commit()

                if user is not None:
                    u = User(user)
                    self.cursor.execute(f"INSERT INTO auth_log(login, login_date, status, role) "
                                        f" VALUES ('{u.login}', NOW(), '{u.status}', '{u.role}')")
                    return u

                else:
                    raise ValueError('User is blocked')
            else:
                raise ValueError('Login or password are incorrect')
        else:
            raise ValueError('Login or password are incorrect')

