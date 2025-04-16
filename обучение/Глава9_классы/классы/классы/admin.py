from user import User

class Privileges:
    def __init__(self):
        self.list_privileges = ['allow to add message', 'allow to del users', 'allow to ban users']

    def show_privileges(self):
        print(f"There are some admin's privileges: ")
        for privilege in self.list_privileges:
            print(f'\t{privilege.title()}')


class Admin(User):
    def __init__(self,first_name,last_name,location,nickname):
        super().__init__(first_name,last_name,location,nickname)
        self.privileges = Privileges()