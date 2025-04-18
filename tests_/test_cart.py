from pages.d_cartpage import CartPage
def test_cart(login):
    cart=CartPage(login)
    cart.cart()