import requests


class UserRegister:
    def __init__(self, name, last_name, email, password, repeat_password):
        self.name = name
        self.lastName = last_name
        self.email = email
        self.password = password
        self.repeatPassword = repeat_password


class UserLogin:
    def __init__(self, email, password, remember):
        self.email = email
        self.password = password
        self.remember = remember


class TestQautoApi:

    def setup_class(self):
        self.session = requests.session()

        user_to_register = UserRegister("Yana", "Shevchenko", "yana@test.com", "YanaShevchenko", "YanaShevchenko")
        self.session.post(url='https://qauto2.forstudy.space/api/auth/signup',
                          json=user_to_register.__dict__)

    def test_user_to_login(self):
        user_to_login = UserLogin("yan", "YanaShevchenko", False)

        result = self.session.post(url="https://qauto2.forstudy.space/api/auth/signin",
                                   json=user_to_login.__dict__)

    def teardown_class(self):
        self.session.delete("https://qauto2.forstudy.space/api/users")
