import unittest

class IsItANumberTask(unittest.TestCase):
    """
    Skriv ferdig metoden så sier om maybe_number er et tall eller ikke.

    """

    is_number = False
    def is_a_number(self, maybe_number):
        try:
            float(maybe_number)
        except:
            self.is_number = False
        else:
            self.is_number = True
        ## TODO SKRIV KODEN HER

    def test_true(self):
        self.is_a_number("1")

        self.assertTrue(self.is_number, True)

    def test_false(self):
        self.is_a_number("Tekst")
        self.assertTrue(self.is_number, False)
        
    def test_pi(self):
        self.is_a_number("3.14")
        self.assertTrue(self.is_number, True)

    def test_spaces(self):
        self.is_a_number("3    4")
        self.assertTrue(self.is_number, False)
    
    def test_untrimmed(self):
        self.is_a_number("3  ")
        self.assertTrue(self.is_number, True)
        

if __name__ == '__main__':
    unittest.main()