import unittest
import src.prob

class ProbTest(unittest.TestCase):
    def test_prob_001(self):
        """Test case for Problem 001"""
        self.assertEqual(src.prob.P001().aop(), 233168)

    def test_prob_002(self):
        """Test case for Problem 002"""
        self.assertEqual(src.prob.P002().aop(), 4613732)

    def test_prob_003(self):
        """Test case for Problem 003"""
        self.assertEqual(src.prob.P003().aop(), 6857)

    def test_prob_004(self):
        """Test case for Problem 004"""
        self.assertEqual(src.prob.P004().aop(), 906609)

    def test_prob_005(self):
        """Test case for Problem 005"""
        self.assertEqual(src.prob.P005().aop(), 232792560)

    def test_prob_006(self):
        """Test case for Problem 006"""
        self.assertEqual(src.prob.P006().aop(), 25164150)

    def test_prob_007(self):
        """Test case for Problem 007"""
        self.assertEqual(src.prob.P007().aop(), 104743)


if __name__ == "__main__":
    unittest.main()