import unittest
import subprocess

class Whatever(unittest.TestCase):

	def test_69_1(self):
		self.assertEqual(69, 69, "420")

	def test_69_2(self):
		x = 69
		self.assertTrue(x == 69)

	def test_69_3(self):
		pass

if __name__ == '__main__':
	unittest.main()