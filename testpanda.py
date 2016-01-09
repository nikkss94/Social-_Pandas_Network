from panda import Panda
import unittest

class TestPanda(unittest.TestCase):
    def setUp(self):
        self.vladko = Panda('Vladko', 'vladko@pandamail.com', 'male')

    def test_is_male(self):
        self.assertEqual(self.vladko.isMale(), True)

    def test_is_female(self):
        self.assertEqual(self.vladko.isFemale(), False)

    def test_str(self):
        self.assertEqual(self.vladko.__str__(), "User Vladko with e-mail vladko@pandamail.com of male gender")

    def test_repr(self):
        self.assertEqual(self.vladko.__repr__(), "User Vladko with e-mail vladko@pandamail.com of male gender")

    def test_name(self):
        self.assertEqual(self.vladko.name(), "Vladko")

    def test_email(self):
        self.assertEqual(self.vladko.email(), "vladko@pandamail.com")

    def test_gender(self):
        self.assertEqual(self.vladko.gender(), "male")

    def test_is_valid_address(self):
        self.assertTrue(self.vladko.isValidAddress() == True)


if __name__ == "__main__":
    unittest.main()
