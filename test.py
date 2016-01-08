import unittest
from panda import Panda
from social_network import PandaSocialNetwork

class TestSovialNetwork(unittest.TestCase):
    def setUp(self):
        self.ivo = Panda("Ivo", "ivo@pandamail.com", "male")
        self.network = PandaSocialNetwork()

    def test_has_and_add_panda_in_network(self):
        self.network.add_panda(self.ivo)

        self.assertTrue(self.network.has_panda(self.ivo))

if __name__ == '__main__':
    unittest.main()
