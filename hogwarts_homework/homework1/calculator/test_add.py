import math
import pytest
from hogwarts_homework.homework1.calculator.calculator import calculator


class Test_Add(object):
    def setup(self):
        print("开始计算")
        self.cal = calculator()

    def teardown(self):
        print("计算结束")

    @pytest.mark.parametrize('a,b,expect', [
        (0.1, 0.1, 0.2), (0.1, 0.2, 0.3), (1, 2, 3), (0, 0, 0)
    ], ids=['float1', 'float2', 'int', 'zero'])
    def test_add_001(self,a , b , expect):
        difference = self.cal.add(a, b) - expect
        assert math.fabs(difference) < 0.0001