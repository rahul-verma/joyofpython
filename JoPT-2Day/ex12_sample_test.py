from jopt.basetest import BaseTest
from ddt import ddt, data

@ddt
class SettingsTest(BaseTest):

    def test_valid_login(self):
        user_name = self.config["wp_user"]
        password = self.config["wp_pwd"]
        self.login_with_valid_creds(user_name, password)
        self.logout()

    @data(
        ('anything', 'any_pass', 'Invalid username'),
        ('user', 'wrong_pass', r'The password you entered for the username {} is incorrect')
    )
    def test_invalid_login(self, data):
        user_name, password, message = data
        try:
            message = message.format(user_name)
        except Exception:
            pass
        self.login_with_invalid_creds(user_name, password, message)
