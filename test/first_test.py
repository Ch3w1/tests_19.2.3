import pytest
from app.calculator import Calculator

class TestCalcul:
    def setup(self):
        self.calcul = Calculator

    def test_multiply_calculate_correctly(self):
        assert self.calcul.multiply(self, 3, 3) == 9

    def test_division_calculate_correctly(self):
        assert self.calcul.division(self, 6, 2) == 3

    def test_subtraction_calculate_correctly(self):
        assert self.calcul.subtraction(self, 2, 2) == 0

    def test_adding_calculate_correctly(self):
        assert self.calcul.adding(self, 4, 2) == 6
