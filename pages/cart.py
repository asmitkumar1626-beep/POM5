import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from utilities.base_page import Basepage
import csv
class Cart(Basepage):
    cart=(By.XPATH,"//button[@class='btn btn-inverse btn-block btn-lg dropdown-toggle']")
    view_cart=(By.XPATH,"//strong[normalize-space()='View Cart']")
    checkout=(By.XPATH,"//a[@class='btn btn-primary']")
    locator=(By.XPATH,"//h1[contains(text(),'Shopping Cart')]")


    def cart_cart(self):
        self.click(self.cart)
        self.wait.until(EC.presence_of_element_located(self.view_cart))
        self.click(self.view_cart)
        self.wait.until(EC.presence_of_element_located(self.locator))
        rows=self.driver.find_elements(By.XPATH,"//body[1]/div[2]/div[2]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr")
        header=[]
        for i in rows:
            gg=i.find_elements(By.TAG_NAME,"td")
            for j in gg:
                header.append(j.text)
                print(j.text,end="|")
            print()
        file=open("table_output.csv","w",newline="",encoding="utf-8")
        writer=csv.writer(file)
        writer.writerow(header)
        self.click(self.checkout)
        print("succesfully orderd")

