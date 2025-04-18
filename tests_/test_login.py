from pages.a_loginpage import LoginPage
from pytest import mark
header="email,password"
data=[
        ("poojamg246@gmail.com","Pooja@123")
]
@mark.parametrize(header,data)
def test_login(set_tear,email,password):
    login=LoginPage(set_tear)
    login.login("poojamg246@gmail.com","Pooja@123")
