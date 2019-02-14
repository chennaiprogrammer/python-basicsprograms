


import unittest
import calc

class Test_calc(unittest.TestCase):

    def test_add(self):

        self.data=calc.add(1,3)
        self.assertEqual(self.data,4,msg='result should be 4')

    def test_sub(self):

        self.data=calc.sub(7,2)
        self.assertEqual(self.data,5,msg='result should be 5')

    def test_div(self):

        self.data=calc.div(10,2)
        self.data1=calc.div(10,5)
        self.assertEqual(self.data,5,msg='result sholud be 2')
        self.assertEqual(self.data1,2,msg='result should be 0')

        with self.assertRaises(ValueError):
            calc.div(10,0)


if __name__ == '__main__':
    unittest.main()