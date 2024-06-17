from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# number_of_articles=driver.find_element(By.XPATH,value='//*[@id="articlecount"]/a[1]')
# number_of_articles.click()

# click_by_text_in_hyperlink=driver.find_element(By.LINK_TEXT, value="Content portals")
# click_by_text_in_hyperlink.click()

# write_input=driver.find_element(By.CLASS_NAME,"cdx-text-input__input")
# write_input.send_keys("Python")
# write_input.send_keys(Keys.ENTER)


# Challange
driver = webdriver.Chrome(options=chrome_options)
credentials = ["Filip", "Filippo", "fortnite@gmail.com"]
driver.get("http://secure-retreat-92358.herokuapp.com/")
name_input = driver.find_elements(By.TAG_NAME, "input")
i=0
for name in name_input:
    name.send_keys(credentials[i])
    i+=1
button = driver.find_element(By.CLASS_NAME, "btn-block")
button.click()
