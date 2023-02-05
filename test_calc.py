# тест для калькулятора хрониться в директории "tests"
import pytest

from app.calc import Calculator  # импортируем калькулятор "calc" из директории "app"

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_adding_success(self):
        assert self.calc.adding(self, 1, 1)== 2

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(self, 1, 0)

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_success_subtraction(self):
        assert self.calc.subtraction(self, 6, 1) >= 5

    def test_success_percent(self):
        assert self.calc.percent(self, 10, 5) == 200

    def test_success_division(self):
        assert self.calc.division(self, 10, 5) <= 2

    def teardown(self):
        print('Выполнение метода Teardown')