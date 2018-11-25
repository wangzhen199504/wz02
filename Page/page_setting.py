from Base.base import Base
import Page
class PageSetting(Base):
    # 点击搜索按钮
    def page_click_search_btn(self):
        self.base_click_element(Page.search_btn)
    # 搜索框内输入内容
    def page_input_search(self,value):
        self.base_input_element(Page.input_text,value)
    # 点击返回
    def page_click_back(self):
        self.base_click_element(Page.back_btn)

    # 断言方法  移动网络
    # def page_is_ok(self):
    #     try:
    #         self.base_find_element(ydwl)
    #         # 找到移动网络 返回True 说明断言成功
    #         return True
    #     except:
    #         # 找到移动网络 返回True 说明断言失败
    #         return False

    # 获取一组元素文本方法
    def page_get_list_text(self):
        # 返回结果为 ['wlan','wlan直连']
        return [i.text for i in self.base_find_elements(Page.id_list)]