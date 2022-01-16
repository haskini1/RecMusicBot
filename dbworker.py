from vedis import Vedis
import config

def get_current_state(user_id):
    with Vedis(config.db_file) as db:
        try:
            return db[user_id].decode()
        except KeyError:  # если не найден человек в базе
            return config.States.S_START.value # значение по умолчанию - начало диалога


def set_state(user_id, value):
    with Vedis(config.db_file) as db:
        try:
            db[user_id] = value
            return True
        except:
            # орбаботка ситуации
            return False

