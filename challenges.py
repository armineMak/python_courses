# godaddy
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.current_url

driver.get("https://www.godaddy.com/")
page_title = driver.find_element(By.XPATH,
                                '//*[@id="id-14b0084c-abc6-4f66-a27c-8a0790a6da7f"]/div/div/div/div/div[2]/div').text
print(pageTitle)
expected_value_of_title = driver.find_element(By.XPATH,
                                '//*[@id="id-14b0084c-abc6-4f66-a27c-8a0790a6da7f"]/div/div/div/div/div[2]/div').text
assert page_title == expected_value_of_title
print(driver.current_url)

title_present = driver.page_source
if page_title in title_present:
    print("The page title name is: ", page_title)
else:
    print("Did not find page title.")

driver.quit()
