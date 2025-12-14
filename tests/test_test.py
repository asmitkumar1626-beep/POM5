

from pages.cart import Cart
from pages.dash import Dash
from pages.register import Register
from utilities.driver_setup import get_driver

def test_complete_order_flow(driver):
    driver.get("https://tutorialsninja.com/demo/")

    register=Register(driver)
    register.myacnt()
    register.register()
    register.credentials_input()

    dash=Dash(driver)
    dash.add()

    cart=Cart(driver)
    cart.cart_cart()