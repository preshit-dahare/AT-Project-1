from Test_Utilities.login_module import Orangehrm

class TestInvalidText:

    def test_tc_login_02(self):
        """
        test case to test invalid credentials text

        :return:
        """

        _expected_text = "Invalid credentials"

        assert Orangehrm().error_text() == _expected_text