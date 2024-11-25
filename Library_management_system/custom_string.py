class CustomString:
    def __init__(self):
        self.good_ = '\033[32m'
        self.warning_ = '\033[31m'
        self.id_book_ = '\033[1m'
        self.separate_ = '\033[33m'
        self.welcome_ = '\033[43m'
        self.info_ = '\033[35m'
        self.info_result_ = '\033[46m'
        self.default_ = '\033[0m'

    def good(self, string: str):
        return self.good_ + string + self.default_

    def warning(self, string: str):
        return self.warning_ + string + self.default_

    def id_book(self, string: str):
        return self.id_book_ + string + self.default_

    def separate(self, string: str):
        return self.separate_ + string + self.default_

    def welcome(self, string: str):
        return self.welcome_ + string + self.default_

    def info(self, string: str):
        return self.info_ + string + self.default_

    def info_result(self, string: str):
        return self.info_result_ + string + self.default_
