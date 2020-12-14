import pytest
@pytest.fixture(scope = "module")
def myfixture():
    print("开始计算")
    yield
    print("结束运算")