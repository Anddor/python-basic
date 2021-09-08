import unittest
import math

class CockroachTask(unittest.TestCase):
    """
    Vi skal beregne hvor rask en kakkerlakk er!

    Vi får inn hastigheten i kilometer i timen, og skal regne ut cm i sekundet.

    Kilometer i timen er et flytall, f.eks 1.08,
    mens svaret skal være et heltall rundet av nedover, i dette tilfellet 30.

    """
    cm_i_sekundet = 0

    def calculate(self, kilometer_i_timen):
        self.cm_i_sekundet = math.floor(kilometer_i_timen * 27.77778)
  

    def test(self):
        self.calculate(1.08)
        self.assertEquals(self.cm_i_sekundet, 30)

    def test_round(self):
        self.calculate(1)
        self.assertEqual(self.cm_i_sekundet, 27)

    def test_big(self):
        self.calculate(5)
        self.assertEqual(self.cm_i_sekundet, 138)
        

if __name__ == '__main__':
    unittest.main()