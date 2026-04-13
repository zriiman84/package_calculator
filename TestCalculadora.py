import unittest
import os 
# Importamos la clase desde la carpeta del paquete
from package_calculator.Calculadora import Calculadora

class TestCalculadora(unittest.TestCase):

    #El motor de unittest ejecuta este método una sola vez al inicio, antes de que corra cualquier test de esta clase.
    @classmethod
    def setUpClass(cls):
        # El segundo parámetro es un valor por defecto si la variable no existe
        cls.ambiente = os.getenv('APP_ENV', 'Local Development')
        print(f"\n🚀 Ejecutando tests en el ambiente: {cls.ambiente}")
    
    #El motor de unittest detecta automáticamente los métodos que comienzan con "test_" y los ejecuta como pruebas unitarias
    def test_sumar(self):
        self.assertEqual(Calculadora.sumar(5, 5), 10)
        self.assertEqual(Calculadora.sumar(-1, 1), 0)

    def test_restar(self):
        self.assertEqual(Calculadora.restar(10, 5), 5)

    def test_multiplicar(self):
        self.assertEqual(Calculadora.multiplicar(3, 4), 12)

    def test_dividir(self):
        self.assertEqual(Calculadora.dividir(10, 2), 5)
        # Probamos que lance error al dividir por cero
        with self.assertRaises(ValueError):
            Calculadora.dividir(10, 0)

    def test_exponenciar(self):
        self.assertEqual(Calculadora.exponenciar(2, 3), 8)

    def test_obtener_raiz(self):
        self.assertEqual(Calculadora.obtener_raiz(9, 2), 3)


if __name__ == '__main__':
    unittest.main()