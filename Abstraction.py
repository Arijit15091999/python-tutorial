from abc import abstractmethod, ABC

class User(ABC):
    @abstractmethod
    def login(self):
        pass

    @abstractmethod
    def logout(self):
        pass

    @abstractmethod
    def auth(self):
        pass

class Buyer(User):
    def __init__(self):
        super().__init__()
    def greeting(self):
        print("Hello")

    def login(self):
        print("login")

    def logout(self):
        print("logout")

    def auth(self):
        print("auth")

