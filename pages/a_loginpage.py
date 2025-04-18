from utilities.lib import SeleniumWrapper

class LoginPage:
    _lnk_login=("id","nav-link-accountList-nav-line-1")
    _txt_email=("id","ap_email_login")
    _btn_cont=("xpath","//input[@aria-labelledby='continue-announce']")
    _txt_password=("id","ap_password")
    _btn_login=("id","signInSubmit")
    def __init__(self,driver):
        self.driver=driver
    def login(self,email,password):
        sw=SeleniumWrapper(self.driver)
        sw.click_element(LoginPage._lnk_login)
        sw.enter_text(LoginPage._txt_email,value=email)
        sw.click_element(LoginPage._btn_cont)
        sw.enter_text(LoginPage._txt_password,value=password)
        sw.click_element(LoginPage._btn_login)


