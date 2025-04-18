from utilities.lib import SeleniumWrapper
class ProductPage:
    _lnk_product=("xpath","//a[text()='Mobiles']")
    _btn_mobile=("xpath","(//span[text()='Apple'])[2]")
    _btn_product=("xpath","//span[text()='Apple 20W USB-C Power Adapter (for iPhone, iPad & AirPods)']")
    _btn_cart=("xpath","(//button[@name='submit.addToCart'])[1]")
    def __init__(self,driver):
        self.driver=driver
    def product(self):
        sw=SeleniumWrapper(self.driver)
        sw.click_element(ProductPage._lnk_product)
        sw.click_element(ProductPage._btn_mobile)
        sw.click_element(ProductPage._btn_product)
        sw.click_element(ProductPage._btn_cart)




