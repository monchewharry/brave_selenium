from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from subprocess import check_output
def get_driverpath():
    stdout = check_output(['which','chromedriver']).decode('utf-8')
    return stdout

driver_path = get_driverpath().strip('\n') #'/opt/homebrew/bin/chromedriver'
brave_path = "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"

option = webdriver.ChromeOptions()
option.binary_location = brave_path
option.add_experimental_option("excludeSwitches", ["enable-automation"])

# Create new Instance of Chrome
browser = webdriver.Chrome(executable_path=driver_path, chrome_options=option)

browser.get("https://www.google.com/")
print(browser.title)
# Find searchbar using element name
search_bar = browser.find_element(by= By.NAME, value='q')#browser.find_element_by_name("q") 
search_bar.clear()
search_bar.send_keys("btc")
search_bar.send_keys(Keys.RETURN)
print(browser.current_url)
browser.quit()