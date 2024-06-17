from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(By.ID, "cookie")  # 5 sec from now
for x in range(5):
    list_of_uprades = []
    avaliable = {}
    timeout = time.time() + 5
    while True:
        cookie.click()
        if time.time() > timeout:
            upgrades_all = driver.find_elements(By.CSS_SELECTOR, "#store div")
            for up in upgrades_all:
                list_of_uprades.append(up)
                if up.get_attribute("class") == "grayed":
                    print(f"{up.get_attribute("id")}-ble")
                else:
                    try:
                        text = up.text
                        text_strip = text.split("-", maxsplit=1)
                        name = text_strip[0]
                        price = text_strip[1].split("\n")
                        avaliable[name] = int(price[0])
                        print(f"{name}= {int(price[0])}")
                    except:
                        print("no more avaliable")
            best_upgrade = max(avaliable, key=avaliable.get)
            print(best_upgrade)
            money = driver.find_element(By.ID, "money")
            while True:
                try:
                    upgrades_all[len(avaliable)-1].click()
                except:
                    print("no more points")
                    break
            break

# for up in upgrades_gray:
#     print(up.text)
#     gray.append(up.text)


# lista od konca sprawdzająca czy rekordy obu list są zgodne jak nie, dodaje go do nowej listy mozliwych do kupienie
# z których wybierana jest najdrozsza opcja
