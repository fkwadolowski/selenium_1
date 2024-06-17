from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(By.ID, "cookie")
game = True
timeout = time.time() + 1  # 5 minutes from now
while True:
    cookie.click()
    if time.time() > timeout:
        break
upgrades_gray = driver.find_elements(By.CLASS_NAME, "grayed")
upgrades_all = driver.find_elements(By.ID, "store")
all = []
gray = []
for up in upgrades_all:
    print(up.text)
    all.append(up.text)
for up in upgrades_gray:
    print(up.text)
    gray.append(up.text)
print("///////////////////////////////////////////////////////////////")
print(all)
#lista od konca sprawdzająca czy rekordy obu list są zgodne jak nie, dodaje go do nowej listy mozliwych do kupienie
# z których wybierana jest najdrozsza opcja