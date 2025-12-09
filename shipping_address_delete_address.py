import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import pytest
from selenium.webdriver.common.keys import Keys


# delete_existing_address():
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

wait_2 = WebDriverWait(driver, 15)
address_book_link = wait_2.until(expected_conditions.visibility_of_element_located((By.XPATH, "//a[normalize-space()='Address Book']")))
address_book_link.click()

wait_3 = WebDriverWait(driver, 15)
delete_button = wait_3.until(expected_conditions.visibility_of_element_located((By.XPATH, "(//button[@class='typo-14sbc h-fit hover-btn text-dark w-fit shrink-0 hover:text-app-red'][normalize-space()='Delete'])[2]")))
delete_button.click()
driver.find_element(By.XPATH, "(//button[@class='typo-14sbc flex justify-center items-center w-fit p-5 select-none text-white bg-dark/90 hover:bg-dark/90 disabled:text-[#7E8088] disabled:bg-[#E1E2E3] border border-transparent transition-colors duration-300 h-10'])[1]").click()

driver.refresh()
print("Address deleted successfully.")