from temperature import Temperature
import unittest

class TestTemperatureClass(unittest.TestCase):

    def testCase1(self):
        test = Temperature('84.2', 'Fahrenheit')
        self.assertEqual( test.compareTo('543.5', 'Rankine') , 'correct')
        
    def testCase2(self):
        test = Temperature('-45.14 ', 'Celsius')
        self.assertEqual( test.compareTo('227.51', 'Kelvin') , 'correct')
        
    def testCase3(self):
        test = Temperature('317.33', 'Kelvin')
        self.assertEqual( test.compareTo('110.5', 'Fahrenheit') , 'incorrect')
        
    def testCase4(self):
        test = Temperature('444.5', 'Rankine')
        self.assertEqual( test.compareTo('-30.9', 'Celsius') , 'incorrect')
        
    def testCase5(self):
        test = Temperature('6.5', 'Fahrenheit')
        self.assertEqual( test.compareTo('dog', 'Rankine') , 'incorrect')
        
    def testCase6(self):
        with self.assertRaises(ValueError):
            Temperature('dog', 'Celsius')

            
if __name__ == '__main__':
    unittest.main()
