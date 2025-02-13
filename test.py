import unittest
from health_utils import calculate_bmi, calculate_bmr

class TestHealthUtils(unittest.TestCase):

    def test_calculate_bmi(self):
        """Test BMI calculation."""
        self.assertAlmostEqual(calculate_bmi(1.75, 70), 22.86, places=2)
        self.assertAlmostEqual(calculate_bmi(1.60, 50), 19.53, places=2)
        self.assertRaises(ValueError, calculate_bmi, 0, 70)  # Height can't be 0
        self.assertRaises(ValueError, calculate_bmi, 1.75, -70)  # Weight can't be negative

    def test_calculate_bmr(self):
        """Test BMR calculation."""
        # Male example (30 years, 1.75 meters tall, 70 kg)
        self.assertAlmostEqual(calculate_bmr(1.75, 70, 30, 'male'), 1695.36, places=2)
        # Female example (30 years, 1.75 meters tall, 70 kg)
        self.assertAlmostEqual(calculate_bmr(1.75, 70, 30, 'female'), 1505.1, places=2)  # Corrected expected value
        
        # Edge case: invalid gender
        self.assertRaises(ValueError, calculate_bmr, 1.75, 70, 30, 'other')

        # Edge case: invalid height, weight, or age
        self.assertRaises(ValueError, calculate_bmr, 0, 70, 30, 'male')
        self.assertRaises(ValueError, calculate_bmr, 1.75, 0, 30, 'male')
        self.assertRaises(ValueError, calculate_bmr, 1.75, 70, 0, 'male')

if __name__ == '__main__':
    unittest.main()
