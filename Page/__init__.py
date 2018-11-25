from selenium.webdriver.common.by import By
"""
    以下为setting页面配置数据
"""
# 搜索按钮
search_btn=By.ID,"com.android.settings:id/search"
# 搜索文本框
input_text=By.ID,"android:id/search_src_text"
# 返回按钮
back_btn=By.CLASS_NAME,"android.widget.ImageButton"
# 一组元素 属性
id_list=By.ID,"com.android.settings:id/title"
"""
    以下为短信页面配置数据
"""