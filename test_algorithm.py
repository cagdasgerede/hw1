import unittest
from algorithm import sum

class TestSum(unittest.TestCase):
  def test_sumSuccessful(self):
    self.assertEquals(60, sum([10, 20, 30]))

  def test_sumZero(self):
    self.assertEquals(0, sum([0, 0, 0]))

  def test_sumNegative(self):
    self.assertEquals(-20, sum([20, -40]))

  def test_sumEmptyArray(self):
    self.assertEquals(0, sum([]))

  def test_sumNoneArray(self):
    self.assertEquals(0, sum(None))

if __name__ == '__main__':
  unittest.main()

