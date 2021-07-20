import math
import pytest
from hogwarts_homework.homework1.calculator.calculator import calculator


class Test_Div(object):
    def setup(self):
        print("开始计算")
        self.cal = calculator()

    def teardown(self):
        print("结束计算")

    @pytest.mark.parametrize('a, b, expect', [
        [0.2, 0.2, 1], [0.2, 0.3, 0.6666666], [4, 2, 2], [2, 3, 0.666666], [2, 0, 0]
    ], ids = ['float1', 'float2', 'int1', 'int2', 'zero'])
    def test_div_001(self, a, b, expect):
        if b == 0:
            try:
                self.cal.div(a, b)
            except ZeroDivisionError:
                print("touch ZeroDivisionError")
            else:
                assert 1 == 2
            return
        difference = expect - self.cal.div(a, b)
        assert math.fabs(difference) < 0.0001