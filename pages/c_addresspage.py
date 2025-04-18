from utilities.lib import SeleniumWrapper

class AddressPage:
    _lnk_address=("id","glow-ingress-block")
    _lnk_add=("xpath","//a[text()='Add an address or pick-up point ']")
    _lnk_Add=("id","ya-myab-plus-address-icon")
    _txt_fullname=("id","address-ui-widgets-enterAddressFullName")
    _txt_phone_number=("id","address-ui-widgets-enterAddressPhoneNumber")
    _txt_pincode=("id","address-ui-widgets-enterAddressPostalCode")
    _txt_no=("id","address-ui-widgets-enterAddressLine1")
    _txt_street=("id","address-ui-widgets-enterAddressLine2")
    _txt_landmark=("id","address-ui-widgets-landmark")
    _txt_town=("id","address-ui-widgets-enterAddressCity")
    _btn_state=("xpath","//select[@name='address-ui-widgets-enterAddressStateOrRegion']")
    _btn_add_address=("xpath","(//input[@class='a-button-input'])[3]")
    def __init__(self,driver):
        self.driver=driver
    def address(self,full_name,phone_num,pincode,hno,cross,landmark,town,state):
        sw=SeleniumWrapper(self.driver)
        sw.click_element(AddressPage._lnk_address)
        sw.click_element(AddressPage._lnk_add)
        sw.click_element(AddressPage._lnk_Add)
        sw.enter_text(AddressPage._txt_fullname,value=full_name)
        sw.enter_text(AddressPage._txt_phone_number,value=phone_num)
        sw.enter_text(AddressPage._txt_pincode,value=pincode)
        sw.enter_text(AddressPage._txt_no,value=hno)
        sw.enter_text(AddressPage._txt_street,value=cross)
        sw.enter_text(AddressPage._txt_landmark,value=landmark)
        sw.enter_text(AddressPage._txt_town,value=town)
        sw.select_item(AddressPage._btn_state,item=state)
        sw.click_element(AddressPage._btn_add_address)




