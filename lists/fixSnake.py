import unittest


"""
Slangen er i feil rekkefølge! 

Funksjonen får inn en liste med tre elementer, ["hale", "kropp", "hode"],
fiks slangen slik den er i riktig rekkefølge: ["hode", "kropp", "hale"]

"""
def fixSnake(snake):
    # TODO fiks slange
    return snake[::-1]

class FixSnake(unittest.TestCase):
    def test(self):
        self.assertEqual(fixSnake(["hale", "kropp", "hode"]), ["hode", "kropp", "hale"])
    
    def other_value(self):
        self.assertEqual(fixSnake([3, 2, 1]), [1, 2, 3])
        

if __name__ == '__main__':
    unittest.main()