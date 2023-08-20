from selenium import webdriver

url = "https://cstimer.net/"
driver = webdriver.Edge()
driver.get(url)

# Aspetta che la pagina sia completamente caricata
driver.implicitly_wait(2)

# Trova lo scramble
scramble = driver.find_element_by_id("scrambleTxt").text
print(f"Scramble: {scramble}")

driver.quit()
