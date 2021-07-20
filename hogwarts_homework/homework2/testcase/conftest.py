import pytest
import yaml

from homework2.calculator import calculator

def get_test_data():
    with open("./test_data.yaml") as f:
        test_data = yaml.safe_load(f)
        return test_data


#初始化计算器累，生成一个实例
@pytest.fixture(scope = "class")
def initial_calculator_class():
    print("\n测试开始")
    cal = calculator.calculator()
    yield cal
    print("\n测试结束")


#获取测试add方法的测试数据
@pytest.fixture(params = get_test_data()['test_div_data'],
                ids = get_test_data()['test_div_ids'])
def get_div_data(request):
    return request.param


#获取测试div方法的测试数据
@pytest.fixture(params = get_test_data()['test_add_data'],
                ids = get_test_data()['test_add_ids'])
def get_add_data(request):
    return request.param