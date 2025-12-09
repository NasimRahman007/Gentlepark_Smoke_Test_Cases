import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import pytest
from selenium.webdriver.common.keys import Keys


options_chrome = Options()
options_chrome.add_experimental_option(name="detach",value=True)
service_obj = Service()
driver = webdriver.Chrome(service=service_obj, options=options_chrome)

driver.implicitly_wait(10)

driver.get("https://gentle-park.hellonotionhive.com/")
driver.maximize_window()


wait_1 = WebDriverWait(driver, 15)
accept_all_btn = wait_1.until(expected_conditions.visibility_of_element_located((By.XPATH, "//div/button[normalize-space()='Accept All']")))
accept_all_btn.click()


driver.find_element(By.LINK_TEXT, "SIGN IN").click()
time.sleep(2)

driver.find_element(By.NAME, "email").send_keys("nasim@notionhive.com")
driver.find_element(By.NAME, "password").send_keys("Quantem007#")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
time.sleep(2)

driver.find_element(By.LINK_TEXT, "Shop").click()

wait_2 = WebDriverWait(driver, 15)
category_link = wait_2.until(expected_conditions.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Category']")))
category_link.click()

wait_3 = WebDriverWait(driver, 15)
subcategory_link = wait_3.until(expected_conditions.visibility_of_element_located((By.XPATH, "(//span[@class='text-nowrap typo-12mc text-dark uppercase'][normalize-space()='Polo Shirt Half'])[1]")))
subcategory_link.click()


wait_4 = WebDriverWait(driver, 15)
load_more_btn = (By.CSS_SELECTOR,"button[class='cursor-pointer bg-[#FFFFFF] !border !border-[#020617] px-[60px] py-4 text-dark typo-12sb transition-all duration-300 hover:bg-dark hover:text-white w-full sm:w-fit']")

while True:
    try:
        # wait until the button is clickable
        button = wait_4.until(expected_conditions.element_to_be_clickable(load_more_btn))
        button.click()
        print("Clicked 'Load More' button")
    except (TimeoutException, NoSuchElementException):
        print("No more 'Load More' button found. All products loaded.")
        break
time.sleep(3)

wait_17 = WebDriverWait(driver, 35)
desired_product = wait_17.until(expected_conditions.visibility_of_element_located((By.XPATH, '//img[@alt="Steel Blue Zip Polo Shirt"]')))
desired_product.click()
time.sleep(2)

wait_5 = WebDriverWait(driver, 15)
product_size = wait_5.until(expected_conditions.element_to_be_clickable((By.XPATH, "//button[normalize-space()='XXL']")))
product_size.click()
time.sleep(1)


wait_6 = WebDriverWait(driver, 15)
product_quantity = wait_6.until(expected_conditions.element_to_be_clickable((By.XPATH, "(//button)[11]")))
product_quantity.click()
time.sleep(1)

driver.find_element(By.XPATH, "//button[normalize-space()='Add To Cart']").click()
time.sleep(2)

wait_7 = WebDriverWait(driver, 15)
continue_to_checkout_btn = wait_7.until(expected_conditions.visibility_of_element_located((By.XPATH, "//button[normalize-space()='continue to checkout']")))
continue_to_checkout_btn.click()



# wait_8 = WebDriverWait(driver, 35)
# shipping_information_edit_btn = wait_8.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='button'][normalize-space()='Edit']")))
# shipping_information_edit_btn.click()





wait_9 = WebDriverWait(driver, 15)
continue_to_delivery_options_btn = wait_9.until(expected_conditions.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Continue to Delivery Options']")))
continue_to_delivery_options_btn.click()

# wait_18 = WebDriverWait(driver, 15)
# delivery_option = wait_18.until(expected_conditions.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Continue to Delivery Options']")))
# delivery_option.click()

# wait_10 = WebDriverWait(driver, 15)
# update_delivery_method_btn = wait_10.until(expected_conditions.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Update Delivery Method']")))
# update_delivery_method_btn.click()

wait_11 = WebDriverWait(driver, 15)
payment_method_edit_btn= wait_11.until(expected_conditions.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Continue to Payment']")))
payment_method_edit_btn.click()

wait_12 = WebDriverWait(driver, 15)
payment_method = wait_12.until(expected_conditions.visibility_of_element_located((By.XPATH, "//label[@for='cash_on_delivery']")))
payment_method.click()

wait_13 = WebDriverWait(driver, 15)
total_amount_on_checkout_page = wait_13.until(expected_conditions.visibility_of_element_located((By.XPATH, "//body/main/div/div/main/div/div/aside/div/div/div/p[2]"))).text
print("Total amount on checkout page:", total_amount_on_checkout_page)


wait_14 = WebDriverWait(driver, 15)
order_placement= wait_14.until(expected_conditions.element_to_be_clickable((By.XPATH, "//div[@class='hidden lg:block']//button[normalize-space()='Place order']")))
order_placement.click()
time.sleep(5)

wait_15 = WebDriverWait(driver, 15)
# wait until the toast is not visible anymore
wait_15.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "li[data-sonner-toast]")))
go_to_order_history_btn = wait_15.until(expected_conditions.element_to_be_clickable((By.XPATH, "//button[text()='Go to My Orders']")))
go_to_order_history_btn.click()


wait_16 = WebDriverWait(driver, 15)
total_amount_on_order_history_page = wait_16.until(expected_conditions.element_to_be_clickable((By.XPATH, "(//span[contains(@class,'typo-14sbc text-dark')])[1]"))).text
print("Total amount on order history page:", total_amount_on_order_history_page)

assert total_amount_on_checkout_page == total_amount_on_order_history_page,"Total amount on checkout page matches with the total amount on order history page."
print("Total amount on checkout page matches with the total amount on order history page.")