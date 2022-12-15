import unittest

from base import Base
from fecha import Fecha
from persona import Persona


class MyTest(unittest.TestCase):

    def setUp(self):
        self.fecha1 = Fecha(2000, 2, 28)
        self.fecha2 = Fecha(1999, 3, 1)
        self.fecha3 = Fecha(2003, 1, 1)
        self.fecha4 = Fecha(1998, 7, 1)
        self.fecha5 = Fecha(2002, 12, 31)
        self.persona1 = Persona('diaz', 'juan', self.fecha1)
        self.persona2 = Persona('garcia', 'jose', self.fecha2)
        self.persona3 = Persona('gomez', 'jorge', self.fecha3)
        self.persona4 = Persona('flores', 'ana', self.fecha4)
        self.persona5 = Persona('campos', 'silvia', self.fecha5)

    def test_sorted(self):
        base = Base()
        base.add(self.persona1)
        base.add(self.persona2)
        base.add(self.persona3)
        base.add(self.persona4)
        base.add(self.persona5)
        # Ordena la lista de personas por fecha de nacimiento
        base.sorted()

        base_control = Base()
        base_control.add(self.persona4)
        base_control.add(self.persona2)
        base_control.add(self.persona1)
        base_control.add(self.persona5)
        base_control.add(self.persona3)

        self.assertListEqual(base.data, base_control.data)

    def test_compare_to_1(self):
        self.assertEqual(self.fecha2.compare_to(self.fecha1), -1)

    def test_compare_to_2(self):
        self.assertEqual(self.fecha3.compare_to(self.fecha3), 0)

    def test_compare_to_3(self):
        self.assertEqual(self.fecha5.compare_to(self.fecha4), 1)


if __name__ == '__main__':
    unittest.main()
