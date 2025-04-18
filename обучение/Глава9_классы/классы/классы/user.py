class User:
    def __init__(self,first_name,last_name,location,nickname):
        self.first = first_name
        self.last = last_name
        self.location = location
        self.nickname = nickname
        self.login_attempts = 0

    def describe_user(self):
        print(f"\n{self.first.title()} {self.last.title()}'s nickname is {self.nickname}")
        print(f"His location is {self.location.title()}")

    def greet_user(self):
        print(f"Hello, {self.nickname}!")

    def increment_login_attempts(self):
        self.login_attempts += 1
        return self.login_attempts

    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f'Login attempts reset: {self.login_attempts}')