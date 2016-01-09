from collections import deque
from panda import Panda
from social_network import PandaSocialNetwork
import unittest

class TestSocialNetwork(unittest.TestCase):
    def setUp(self):
        self.sn = PandaSocialNetwork()
        self.pan1 = Panda("Peter", "peter@pandamail.com", "male")
        self.pan2 = Panda("Sanja", "sanja@pandamail.com", "female")
        self.pan3 = Panda("Rada", "rada@pandamail.com", "female")
        self.pan4 = Panda("Pafel", "pafel@pandamail.com", "male")
        self.sn.add_panda(self.pan1)

    def test_has_panda(self):
        self.assertFalse(self.sn.has_panda(self.pan2))
        self.assertTrue(self.sn.has_panda(self.pan1))

    def test_connection_level(self):
        self.sn.make_friends(self.pan1, self.pan2)
        self.sn.make_friends(self.pan1, self.pan3)
        self.sn.make_friends(self.pan4, self.pan2)
        self.sn.make_friends(self.pan2, self.pan3)
        self.assertEqual(self.sn.connection_level(self.pan1, self.pan4), 2)

    def test_add_panda(self):
        self.sn.add_panda(self.pan2)
        self.assertTrue(self.sn.has_panda(self.pan2))
        self.assertFalse(self.sn.has_panda(self.pan3))

    def test_print_network(self):
        self.assertEqual(self.sn.print_network(), {"Peter":[]})

    def test_are_make_friends(self):
        self.sn.make_friends(self.pan1, self.pan3)
        self.assertTrue(self.sn.are_friends(self.pan1, self.pan3))

    def test_are_connected(self):
        self.sn.make_friends(self.pan2, self.pan3)
        self.assertFalse(self.sn.are_connected(self.pan1, self.pan3))
        self.assertTrue(self.sn.are_connected(self.pan2, self.pan3))

    def test_friends_of(self):
        self.sn.make_friends(self.pan1, self.pan4)
        self.assertEqual(self.sn.friends_of(self.pan1), ["Pafel"])

    def test_how_many_gender_in_network(self):
        self.sn.make_friends(self.pan1, self.pan4)
        self.sn.make_friends(self.pan1, self.pan2)
        self.sn.make_friends(self.pan2, self.pan3)
        self.assertEqual(self.sn.how_many_gender_in_network(2, self.pan2,"male"), 1)
        self.assertEqual(self.sn.how_many_gender_in_network(1, self.pan3,"male"), 0)
    
        

if __name__ == "__main__":
    unittest.main()
