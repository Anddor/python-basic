import unittest

class AssignmentTask(unittest.TestCase):
    """
    I denne oppgaven blir ikke variabelen som skal ha navnet på skolen opprettet riktig. Finner du feilen?

    """

    navn = "Elvebakken"
    navn += " VGS"

    def test(self):
        self.assertEqual(AssignmentTask.navn, "Elvebakken VGS")
        

if __name__ == '__main__':
    unittest.main()