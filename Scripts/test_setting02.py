import sys,os
sys.path.append(os.getcwd())
from Page.page_in import PageIn
class TestSetting02():
    def setup_class(self):
        # 实例化统一入口类
        self.setting=PageIn().page_get_setting()
    def teardown_class(self):
        self.setting.driver01.quit()
    def test_setting02(self,value="wlan"):
        sett=self.setting
        # 点击搜索按钮
        sett.page_click_search_btn()
        # 输入内容
        sett.page_input_search(value)
        #点击返回
        sett.page_click_back()