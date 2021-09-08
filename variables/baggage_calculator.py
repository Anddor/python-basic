import unittest
import math


"""
    Norwegian beskriver reglene for bagasje slik:
    * Hvert enkelt kolli må ikke veie mer enn 32 kg eller mindre enn 2 kg.
    * Du må betale overvekt for kolli som veier over 23 kg. Prisen for overvekt er 135 NOK  per kilo

    Skriv en kalkulator som beregner hvor mye man må betale for en gitt vekt.
    Input vil være et desimaltall mellom 2 og 32 kilo.
    Prisen er per begynte kilo rundet oppover.
"""
def bagasje_overvekt(vekt):
    if vekt > 23:
        print("Pris " + str(math.ceil(vekt - 23) * 135))
        return math.ceil(vekt - 23) * 135
    else:
        print("Pris " + "0")
        return 0

class BaggageCalc(unittest.TestCase):
    def test_underweight(self):
        self.assertEqual(bagasje_overvekt(5.5), 0)

    def test_overweight(self):
        self.assertEqual(bagasje_overvekt(30), 945)
    
    def test_rounded(self):
        self.assertEqual(bagasje_overvekt(23.5), 135)
        

if __name__ == '__main__':
    unittest.main()