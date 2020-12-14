import pytest
class Test_Demo():

    @pytest.mark.demo
    def test_Demo(self):
        print("我的第一个用例")

    @pytest.mark.demo
    @pytest.mark.smoke
    def test_two(self):
        print("我的第二个用例")