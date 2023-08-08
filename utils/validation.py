import re

class Validator():
    def __init__(self):
        pass
    def isCorrectionName(self, name):
        if not isinstance(name, str):
            return None
        if len(name)< 2:
            return None
        return True
    def isValidName(self, name):
        pattern = r'^[а-яА-Я]+$'
        return re.match(pattern, name) is not None
    def isValidPassword(self, password):
        if not isinstance(password, str):
            return False
        if len(password) < 8:
            return False
        if not any(c.isdigit() for c in password):
            return False
        return True