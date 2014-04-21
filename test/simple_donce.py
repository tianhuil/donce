from donce import SimpleDonce
import unittest

class DonceTest(unittest.TestCase):
  def create_donce1(self):
    return SimpleDonce("test_name1")

  def create_donce2(self):
    return SimpleDonce("test_name2")

  def setUp(self):
    self.simple_donce1 = self.create_donce1()
    self.simple_donce2 = self.create_donce2()
    self.simple_donce1._delete()
    self.simple_donce2._delete()

  def testSimpleDonce(self):
    # check that "a" is added to donce1 but not donce2
    self.simple_donce1.add("a")
    self.assertTrue("a" in self.simple_donce1)
    self.assertFalse("a" in self.simple_donce2)

    # check that "a" is persisted in donce1 but not donce2
    self.assertTrue("a" in self.create_donce1())
    self.assertFalse("a" in self.create_donce2())

    # check that "b" is added to donce1, without affecting "a"
    self.assertFalse("b" in self.simple_donce1)
    self.simple_donce1.add("b")
    self.assertTrue("b" in self.simple_donce1)
    self.assertTrue("a" in self.simple_donce1)

  def tearDown(self):
    self.simple_donce1._delete()
    self.simple_donce2._delete()


if __name__ == '__main__':
  unittest.main()
