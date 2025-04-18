from pages.c_addresspage import AddressPage
from pytest import mark
header="full_name,phone_num,pincode,hno,cross,landmark,town,state"
data=[
    ("Pooja M G","9742518117","560028","no 283","7th cross","narasimha swamy temple","Bangalore","KARNATAKA")
]
@mark.parametrize(header,data)
def test_address(login,full_name,phone_num,pincode,hno,cross,landmark,town,state):
    address=AddressPage(login)
    address.address(full_name,phone_num,pincode,hno,cross,landmark,town,state)