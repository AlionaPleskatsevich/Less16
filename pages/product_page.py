from pages.base_page import BasePage


class ProductPage(BasePage):
    URL = 'https://automationexercise.com/products'

    def __init__(self, page):
        super().__init__(page)
        self.search_input = page.locator('#search_product')
        self.search_button = page.locator('#submit_search')
        self.products = page.locator('.product-image-wrapper')
        self.searched_products_title = page.locator('.title.text-center')
        self.product_information = page.locator('.product-information')
        self.product_names = page.locator('.product-information h2')
        self.searched_products = page.get_by_role("heading", name="Searched Products")
        self.search_product_name = page.get_by_text("Lace Top For Women").first
        self.first_product = page.get_by_role("link", name="View Product").first
        self.all_products = page.get_by_role("heading", name="All Products")

    def open_product(self):
        self.open(self.URL)

    def search_product(self, product):
        self.search_input.click()
        self.search_input.fill(product)
        self.search_button.click()

    def open_first_product(self):
        self.first_product.click()
