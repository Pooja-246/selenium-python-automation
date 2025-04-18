from utilities.lib import SeleniumWrapper
class CartPage:
    _lnk_cart=("id","nav-cart-count")
    _lnk_buy=("xpath","//input[@name='proceedToRetailCheckout']")
    _btn_payment=("xpath","//input[@aria-labelledby='checkout-primary-continue-button-id-announce']")
    def __init__(self,driver):
        self.driver=driver
    def cart(self):
        sw=SeleniumWrapper(self.driver)
        sw.click_element(CartPage._lnk_cart)
        sw.click_element(CartPage._lnk_buy)
        sw.click_element(CartPage._btn_payment)




