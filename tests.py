import unittest
from check_pwd import check_pwd


# Sariah Bunnell
# October 26 2020
# Passwords are 8 - 20 characters
# 1+ lowercase, 1+ uppercase
# 1+ digit, 1+ symbol [~`!@#$%^&*()_+-=]


class TestDrivenDevelopment(unittest.TestCase):
    # first value = empty string
    def test_empty(self):
        str_val = ""
        self.assertFalse(check_pwd(str_val))

    # second - test that length >= 8
    def test_full(self):
        str_val = "m1lk*Bone"
        self.assertTrue(check_pwd(str_val))


    # third - test that length <= 20
    def test_length(self):
        str_val = "m1lk*Bonezzzzzzzzzzzz"
        self.assertFalse(check_pwd(str_val))

    # fourth - test 1+ lowercase letter
    def test_upper(self):
        str_val = "M1LK*BONE"
        self.assertFalse(check_pwd(str_val))


if __name__ == '__main__':
    unittest.main()

