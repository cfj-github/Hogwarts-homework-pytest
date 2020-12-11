import pytest
from pythoncode.calculator import Calculator

class TestCalc():
    def setup_class(self):
        self.cal = Calculator()
        print("开始计算")
    def tear_down(self):
        print("计算结束")

    @pytest.mark.parametrize("a,b,expect",[
        (3,5,8),(-1,-2,-3),(100,300,400)
    ],ids=["int","minus","bigint"])
    def test_add(self,a,b,expect):
        assert expect == self.cal.add(a,b)

    @pytest.mark.parametrize("a,b,expect", [
        (5, 2, 3), (-1, -2, 1), (350, 200, 150)
    ], ids=["int", "minus", "bigint"])
    def test_sub(self,a,b,expect):
        assert expect == self.cal.sub(a,b)

    @pytest.mark.parametrize("a,b,expect", [
        (3, 5, 15), (-1, -2, 2), (150, 200, 30000)
    ], ids=["int", "minus", "bigint"])
    def test_mul(self,a,b,expect):
        assert expect == self.cal.mul(a,b)

    @pytest.mark.parametrize("a,b,expect", [
        (15, 5, 3), (-2, -1, 2), (600, 200, 3)
    ], ids=["int", "minus", "bigint"])
    def test_div(self,a,b,expect):
        assert expect == self.cal.div(a,b)
