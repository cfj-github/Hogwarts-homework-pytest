import pytest
from pythoncode.calculator import Calculator
import yaml

#定义计算器测试类
class TestCalculator():
    def setup_class(self):
        self.cal = Calculator()
        print("开始计算")
    def teardown_class(self):
        print("计算结束")

    #使用yaml文件实现用例数据参数化，读取数据
    def get_datas(self):
        with open("./data.yml") as f:
            datas = yaml.safe_load(f)
            print(datas)
            add_datas = datas["add_datas"]
            sub_datas = datas["sub_datas"]
            mul_datas = datas["mul_datas"]
            div_datas = datas["div_datas"]
            myids=datas["myid"]
            return [add_datas, sub_datas,mul_datas,div_datas,myids]

    #加减乘除运算
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize("a,b,expected",
        self.get_datas()[0],
        ids=self.get_datas()[4])
    def test_add(self,a,b,expected):
        assert self.cal.add(a,b) == expected

    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("a,b,expected",
                             self.get_datas()[1],
                             ids=self.get_datas()[4])
    def test_sub(self,a,b,expected):
        assert self.cal.sub(a,b) == expected

    @pytest.mark.run(order=3)
    @pytest.mark.parametrize("a,b,expected",
                             self.get_datas()[2],
                             ids=self.get_datas()[4])
    def test_mul(self,a,b,expected):
        assert self.cal.mul(a,b) == expected

    @pytest.mark.run(order=4)
    @pytest.mark.parametrize("a,b,expected",
                             self.get_datas()[3],
                             ids=self.get_datas()[4])
    def test_div(self,a,b,expected):
        assert self.cal.div(a,b) == expected
