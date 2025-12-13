from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from utilities.base_page import Basepage
class Register(Basepage):
    Myacnt=(By.XPATH,"//a[contains(text(),'My Account')]")
    register_con=(By.XPATH,"//a[normalize-space()='Continue']")
    firstname=(By.XPATH,"//input[@id='input-firstname']")
    lastname=(By.XPATH,"//input[@id='input-lastname']")
    email=(By.XPATH,"//input[@id='input-email']")
    number=(By.XPATH,"//input[@id='input-telephone']")
    password=(By.XPATH,"//input[@id='input-password']")
    confirm_password=(By.XPATH,"//input[@id='input-confirm']")
    subscribe_radio=(By.XPATH,"//label[normalize-space()='Yes']")
    privacy_checkbox=(By.XPATH,"//input[@name='agree']")
    CONTINUE=(By.XPATH,"//input[@value='Continue']")
    acnt_created=(By.XPATH,"//a[normalize-space()='Continue']")


    def myacnt(self):
        self.scroll(self.Myacnt)
        self.click(self.Myacnt)
        print("inside the my acnt section")
    def register(self):
        self.click(self.register_con)
        print("inside register page")
    def credentials_input(self):
        self.type(self.firstname,"asmit")
        self.type(self.lastname,"kumar")
        self.type(self.email,"asmitkumarrrrrrrrrr7750@gmail.com")
        self.type(self.number,"7873901626")
        self.type(self.password,"asmit@7750")
        self.type(self.confirm_password,"asmit@7750")
        print("filled credentials")
        self.click(self.subscribe_radio)
        self.click(self.privacy_checkbox)
        self.click(self.CONTINUE)
        self.click(self.acnt_created)
        print("acnt created ")



