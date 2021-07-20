import allure
import pytest

@allure.feature("计算器")
class Test_Calculator_Add(object):

    @allure.story("加法")
    @pytest.mark.run(order = 2)
    def test_add_001(self, initial_calculator_class, get_add_data):
        count = round(initial_calculator_class.add(get_add_data[0], get_add_data[1]), 8)
        assert count == get_add_data[2]

    @allure.story("除法")
    @pytest.mark.run(order = 1)
    def test_div_002(self, initial_calculator_class, get_div_data):
        try:
            count = round(initial_calculator_class.div(get_div_data[0], get_div_data[1]), 8)
        except ZeroDivisionError:
            assert get_div_data[1] == 0
            return
        assert count == get_div_data[2]
        return
