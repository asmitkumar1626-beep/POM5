from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from utilities.base_page import Basepage
class Dash(Basepage):
    HOME=(By.XPATH,"//i[@class='fa fa-home']")
    MAC=(By.XPATH,"//a[normalize-space()='MacBook']")
    MAC_LIKE=(By.XPATH,"//div[@id='product-product']//div[@class='btn-group']//button[1]")
    ADD_MAC=(By.XPATH,"//button[@id='button-cart']")
    Home=(By.XPATH,"//i[@class='fa fa-home']")
    mp3_player=(By.XPATH,"//a[normalize-space()='MP3 Players']")
    show_mp3=(By.XPATH,"//a[normalize-space()='Show AllMP3 Players']")
    IPOD=(By.XPATH,"//a[normalize-space()='iPod Touch']")
    ADD_IPOD=(By.XPATH,"//button[@id='button-cart']")



    def add(self):
        self.jsclick(self.HOME)
        print("in homepage")
        self.jsclick(self.MAC)
        print("in mac page")
        self.click(self.MAC_LIKE)
        print("liked mac")
        self.click(self.ADD_MAC)
        print("added mac to cart")
        actions=ActionChains(self.driver)
        ele=self.wait.until(EC.element_to_be_clickable(self.mp3_player))
        actions.move_to_element(ele).click().perform()
        print("inside mp3 sections")
        self.jsclick(self.show_mp3)
        print("inside all mp3")
        self.scroll(self.IPOD)
        self.click(self.IPOD)
        self.click(self.ADD_IPOD)
        print("added ipod")


