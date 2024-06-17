import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

# Kepp Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org")

# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
# price = f"{price_dollar.text},{price_cents.text}$"

# search_bar=driver.find_element(By.NAME, value="q")
# print(search_bar.tag_name)
# print(search_bar.get_attribute("placeholder"))

# button=driver.find_element(By.ID, value="submit")
# print(button.size)

# documentation_link=driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# print(documentation_link.text)

# bug_link=driver.find_element(By.XPATH,value='//*[@id="content"]/div/section/div[1]/div[3]/p[2]/a')
# print(bug_link.text)
final_dict = {}
list_of = driver.find_elements(By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li')
for entry, n in list_of:
    text_format = entry.text
    print(type(text_format))
    time = text_format.split(maxsplit=1)
    event = {"time": time[0],
             "name": time[1]}
    print(event)
    final_dict[n] = event
# driver.close()
print(final_dict)
driver.quit()
