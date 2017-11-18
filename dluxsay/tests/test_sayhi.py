'''
Unit test for SayHiClass on src

To run:
python -m unittest dluxsay.tests.test_sayhi
OR
python -m unittest discover

@author: luzC
'''
import unittest
from  dluxsay.say_hi import SayHiClass


class SayHiTestCase(unittest.TestCase):

    def setUp(self):
        print ("Unit test case setup")
        super(SayHiTestCase, self).setUp()
        self.say = SayHiClass()

    def test_hi(self):
        # Accept empty
        self.say.hi()
        # Accept a value
        self.say.hi('Luz')
        # Accept a number
        self.say.hi(666)

    def test_f_sum(self):
        output = self.say.sum([1,2,3,4])
        self.assertEqual(10, output, 'Something went wrong with the operation')

    def test_invalid_sum(self):
        self.assertRaises(ValueError, self.say.sum, [1,'otro',''])

    def test_empty_sum(self):
        self.assertRaises(TypeError, self.say.sum)

if __name__ == '__main__':
    unittest.main()

