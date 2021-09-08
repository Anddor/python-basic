import unittest


"""
    Vi går tilbake til Norwegian sin bagasje-definisjon: 
    
    * Hvert enkelt kolli må ikke veie mer enn 32 kg eller mindre enn 2 kg.
    
    Lag koden som gir tilbake Boolean om bagasjen er gyldig gitt vekten `vekt`
    Hint: Bruk if
    
"""
def gyldig_bagasje(vekt):
    return (vekt > 2) and (vekt < 32)

class BaggageValidator(unittest.TestCase):
    def test_underweight(self):
        self.assertEqual(gyldig_bagasje(1.5), False)

    def test_overweight(self):
        self.assertEqual(gyldig_bagasje(35), False)
    
    def test_rounded(self):
        self.assertEqual(gyldig_bagasje(32.5), False)
    
    def test_valid(self):
        self.assertEqual(gyldig_bagasje(10), True)
    
    def test_negative(self):
        self.assertEqual(gyldig_bagasje(-10), False)
        

if __name__ == '__main__':
    unittest.main()