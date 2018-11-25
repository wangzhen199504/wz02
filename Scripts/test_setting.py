import os,sys
sys.path.append(os.getcwd())
import pytest
from Base.get_driver import get_driver
from Page.page_setting import PageSetting


class TestSetting():
    # 初始化方法
    def setup_class(self):
        self.driver=get_driver()
        # 实例化 PageSetting
        self.setting=PageSetting(self.driver)
    # 结束方法
    def teardown_class(self):
        self.driver.quit()
    # 测试方法
    @pytest.mark.parametrize("value,expect_result", [("l", "移动网络"), ("a", "壁纸"), ("w", "WLAN")])
    def test_setting(self,value,expect_result):
        # 点击搜索按钮
        self.setting.page_click_search_btn()
        # 输入搜索内容
        self.setting.page_input_search(value)
        # 断言
        try:
            # 获取当前搜索结果列表的文本
            list_text=self.setting.page_get_list_text()
            assert expect_result in list_text
            print("获取的列表文本为：",list_text)
            print("断言成功！")
        except:
            print("断言失败")
        # 点返回按钮
        self.setting.page_click_back()