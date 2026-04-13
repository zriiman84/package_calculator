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
        print(f"\n🚀 Test en el ambiente: {cls.ambiente}")
    
    #El motor de unittest detecta automáticamente los métodos que comienzan con "test_" y los ejecuta como pruebas unitarias
    def test_sumar(self):
        self.assertEqual(Calculadora.sumar(5, 5), 10)
        self.assertEqual(Calculadora.sumar(-1, 1), 0)
        print("✅ test_sumar pasó correctamente")

    def test_restar(self):
        self.assertEqual(Calculadora.restar(10, 5), 5)
        print("✅ test_restar pasó correctamente")

    def test_multiplicar(self):
        self.assertEqual(Calculadora.multiplicar(3, 4), 12)
        print("✅ test_multiplicar pasó correctamente")

    def test_dividir(self):
        self.assertEqual(Calculadora.dividir(10, 2), 5)
        # Probamos que lance error al dividir por cero
        with self.assertRaises(ValueError):
            Calculadora.dividir(10, 0)
        
        print("✅ test_dividir pasó correctamente")

    def test_exponenciar(self):
        self.assertEqual(Calculadora.exponenciar(2, 3), 8)
        print("✅ test_exponenciar pasó correctamente")

    def test_obtener_raiz(self):
        self.assertEqual(Calculadora.obtener_raiz(9, 2), 3)
        print("✅ test_obtener_raiz pasó correctamente")


if __name__ == '__main__':
    unittest.main()