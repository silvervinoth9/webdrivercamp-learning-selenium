from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def open_and_print_url(url):
    driver = webdriver.Chrome()
    driver.get(url)
    print(f"Current URL: {driver.current_url}")
    driver.quit()


def open_wait_and_print_url(url):
    driver = webdriver.Chrome()
    driver.get(url)
    wait = WebDriverWait(driver, 20)
    wait.until(ec.presence_of_element_located((By.ID, "gh-ac")))
    print(f"Current URL: {driver.current_url}")
    driver.quit()


def search_items(search_query):
    driver = webdriver.Chrome()
    driver.get("https://www.ebay.com/")
    wait = WebDriverWait(driver, 10)
    wait.until(ec.presence_of_element_located((By.ID, "gh-ac")))
    search_field = driver.find_element(By.ID, "gh-ac")
    search_field.send_keys(search_query)
    search_field.send_keys(Keys.RETURN)
    print(f"Current URL: {driver.current_url}")
    driver.quit()


def verify_search_results(search_query, expected_text):
    driver = webdriver.Chrome()
    driver.get("https://www.ebay.com")
    wait = WebDriverWait(driver, 10)
    wait.until(ec.presence_of_element_located((By.ID, "gh-ac")))
    search_field = driver.find_element(By.ID, "gh-ac")
    search_field.send_keys(search_query)
    search_field.send_keys(Keys.RETURN)
    wait.until(ec.presence_of_element_located((By.CLASS_NAME, "s-item")))
    results_header = driver.find_element(By.CLASS_NAME, "srp-controls__count-heading")
    assert expected_text in results_header.text
    print(f"Current URL: {driver.current_url}")
    driver.quit()


open_and_print_url("https://www.ebay.com")
open_wait_and_print_url("https://www.ebay.com")
search_items("women watch")
verify_search_results("women watch", "results for women watch")
