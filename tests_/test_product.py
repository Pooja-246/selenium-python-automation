from pages.b_productpage import ProductPage


def test_product(login):
    product=ProductPage(login)
    product.product()