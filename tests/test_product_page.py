from playwright.sync_api import expect
from pages.product_page import ProductPage


def test_open_products_page(page):
    product_page = ProductPage(page)
    product_page.open_product()
    assert "products" in product_page.get_url()


def test_search_product(page):
    product_page = ProductPage(page)
    product_page.open_product()
    product_page.search_product("Men Tshirt")
    expect(product_page.searched_products_title).to_have_text("Searched Products")


def test_search_result_contains_product(page):
    product_page = ProductPage(page)
    product_page.open_product()
    product_page.search_product("Lace Top For Women")
    expect(product_page.searched_products).to_have_text("Searched Products")
    expect(product_page.search_product_name).to_contain_text("Lace Top For Women")


def test_open_first_product(page):
    product_page = ProductPage(page)
    product_page.open_product()
    expect(product_page.all_products).to_have_text("All Products")
    product_page.open_first_product()
    expect(page).to_have_url("https://automationexercise.com/product_details/1")
