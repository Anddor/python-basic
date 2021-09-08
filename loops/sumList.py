import unittest


"""
    Gitt en liste med tall, summer opp alle de positive elementene i listen.
    Hvis listen er tom skal svaret være 0.
"""
def positive_sum(liste):
    sum = 0
    for tall in liste:
        if tall > 0:
            sum = sum + tall
    return sum

class CountingList(unittest.TestCase):
    def test_basic_test_cases(self):
        self.assertEqual(positive_sum([1,2,3,4,5]),15)
        self.assertEqual(positive_sum([1,-2,3,4,5]),13)
        self.assertEqual(positive_sum([-1,2,3,4,-5]),9)
        
    def test_empty_case(self):
        self.assertEqual(positive_sum([]),0)      
        
    def test_negative_case(self):
        self.assertEqual(positive_sum([-1,-2,-3,-4,-5]),0)

if __name__ == '__main__':
    unittest.main()