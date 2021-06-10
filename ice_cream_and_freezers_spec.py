import unittest
from ice_cream import IceCream
from freezer import Freezer

class TestIceCream(unittest.TestCase):
    def setUp(self):
        self.test_icecream = IceCream("Vanilla")

    def test_flavor(self):
        self.assertTrue(self.test_icecream.get_flavor, "Vanilla")

    def test_set_done_status(self):
        self.test_icecream.set_done_status("Butter")
        self.assertTrue(self.test_icecream.get_done_status, "Butter")

class TestFreezer(unittest.TestCase):
    def setUp(self):
        self.test_freezer = Freezer()
        self.test_freezer.store_ice_cream("Peanut Butter")
        self.test_freezer.store_ice_cream("Vanilla")

    def test_freezer_exists(self):
        self.assertTrue(type(self.test_freezer), object)

    def test_freezer_remove_first(self):
        removed_ice_cream = self.test_freezer.remove_first_ice_cream()
        self.assertTrue(removed_ice_cream.flavor, "Vanilla")
        self.assertTrue(len(self.test_freezer.storage), 1)

    def test_remove_by_doneness(self):
        # We should test that it's returning what we're asking
        # We should test that it has actually removed an item from freezer storage
        removed_ice_cream = self.test_freezer.remove_done_ice_cream("Peanut Butter", "watery")
        self.assertTrue(removed_ice_cream.flavor, "Peanut Butter")
        self.assertTrue(len(self.test_freezer.storage), 1)

    def test_freezer_aging(self):
        pass
        

if __name__ == '__main__':
    unittest.main()
