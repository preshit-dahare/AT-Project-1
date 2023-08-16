from Test_Utilities.login_module import Orangehrm

class TestLoginTitle:

    def test_tc_login_01(self):
        """
        test case to test title of our page

        :return:
        """

        _expected_title = "OrangeHRM"

        assert Orangehrm().title_of_page() == _expected_title