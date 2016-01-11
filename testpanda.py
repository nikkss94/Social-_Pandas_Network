from panda import Panda
import unittest

class TestPanda(unittest.TestCase):
    def setUp(self):
        self.vladko = Panda('Vladko', 'vladko@pandamail.com', 'male')

    def test_is_male(self):
        self.assertEqual(self.vladko.isMale(), True)

    def test_is_female(self):
        self.assertEqual(self.vladko.isFemale(), False)

    def test_id(self):
        self.assertEqual(self.vladko.get_id(), 2)
        self.pavel = Panda('Pavel', 'pavel@pandamail.com', 'male')
        self.assertEqual(self.pavel.get_id(), 3)
        self.peter = Panda('Pavel', 'pavel2@pandamail.com', 'male')
        self.assertEqual(self.peter.get_id(), 4)

    def test_str(self):
        self.assertEqual(self.vladko.__str__(), "Vladko")

    def test_repr(self):
        self.assertEqual(self.vladko.__repr__(), "Vladko")

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
