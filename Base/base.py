from selenium.webdriver.support.wait import WebDriverWait


class Base():
    def __init__(self,driver):
        self.driver01=driver
    # 查找元素
    def base_find_element(self,loc,timeout=30,poll=0.5):
        """
        为什么使用find_element()方法去封装：
            1. 元素定位方法底层用的全是 find_element()方法
            2. 封装动态数据(ID,CLASS_NAME,XPATH)
        参数：
            loc：为参数，数据类型为元组；*loc为解包
        """
        # 获取元素
        element=self.driver01.find_element(*loc)

        element=WebDriverWait(self.driver01,timeout,poll_frequency=poll).until(lambda x:x.find_element(*loc))
        # 返回元素
        return element
    # 查找一组元素封装
    def base_find_elements(self,loc,timeout=30,poll=0.5):
        element=WebDriverWait(self.driver01,timeout,poll_frequency=poll).until(lambda x:x.find_elements(*loc))
        # 返回元素
        return element
    # 点击元素
    def base_click_element(self,loc):
        # 获取元素
        el=self.base_find_element(loc)
        # 元素进行点击
        el.click()
    # 输入元素
    def base_input_element(self,loc,value):
        # 获取元素
        el=self.base_find_element(loc)
        # 清除操作
        el.clear()
        # 元素输入操作
        el.send_keys(value)