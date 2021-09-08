import unittest


"""
    For å hjelpe å sovne, er det et gammelt triks å telle sauer.
    Men må telle dem en og en.
    Gitt et antall sauer, gi tilbake en liste med alle tallene oppover, til og med det tallet, men uten null.

"""
def telle_sauer(antall):
    ListSau = []
    for tall in range(antall):
        ListSau.append(tall + 1)
    print(ListSau)
    return ListSau

class CountingList(unittest.TestCase):
    def test(self):
        self.assertEquals(telle_sauer(4), [1, 2, 3, 4])

    def test_single(self):
        self.assertEquals(telle_sauer(1), [1])

        

if __name__ == '__main__':
    unittest.main()