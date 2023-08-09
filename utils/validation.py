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
    def isValidImgface(self, Imgface):
        pattern = r'^[a-zA-Z_]+$'
        return re.match(pattern, Imgface) is not None
    def isValidName(self, name):
        pattern = r'^[а-яА-Я]+$'
        return re.match(pattern, name) is not None
    def isValidPassword(self, password):
        if len(password) < 4:
            return False
        return True