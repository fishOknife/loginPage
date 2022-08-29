from selenium.webdriver.common.by import By
from baseMethod.basePage import BaseClass


# 登录页
class LoginClass(BaseClass):
    # 定位账号
    def find_username_element(self, ):
        return self.find_element(By.ID, "logUserName")

    # 定位密码
    def find_password_element(self):
        return self.find_element(By.ID, "logUserPw")

    # 定位按钮
    def find_submit_element(self):
        return self.find_element(By.ID, "loginSubmit")

    # 根据传入的参数确定定位目标
    def get_page_info(self, target):
        # print(target)
        if target == "alter":
            return self.get_alert_info()
        elif target == "title":
            return self.get_title_info()

