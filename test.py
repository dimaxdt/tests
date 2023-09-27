import unittest
from Calculator import calc

class Testing (unittest.TestCase):

  def test_add(self):
    self.assertEqual(calc.add(2,5),7)

  def test_sub(self):
    self.assertEqual(calc.sub(7,1),6)

  def test_mul(self):
    self.assertEqual(calc.mul(7,2),14)

  def test_div(self):
    self.assertEqual(calc.div(9,3),3)

  def test_fac(self):
    self.assertEqual(calc.fac(4),24)


if __name__ == "__main__":
  unittest.main()